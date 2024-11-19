import com.github.javaparser.JavaParser;
import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.VariableDeclarator;
import com.github.javaparser.ast.expr.MethodCallExpr;
import com.github.javaparser.ast.stmt.Statement;
import com.github.javaparser.ast.visitor.GenericListVisitorAdapter;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

public class MethodStatementCollector {

    private Set<String> visitedMethods = new HashSet<>();

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java MethodStatementCollector <rootDir> <outputFile>");
            return;
        }

        String rootDir = args[0];
        String outputFile = args[1];

        MethodStatementCollector collector = new MethodStatementCollector();

        try {
            // List to store all collected statements
            List<String> allStatements = new ArrayList<>();

            // Find and parse all Java files in the directory
            List<Path> javaFiles = collector.findJavaFiles(Paths.get(rootDir));

            if (javaFiles.isEmpty()) {
                System.out.println("No Java files found in the directory.");
                return;
            }

            for (Path javaFile : javaFiles) {
                CompilationUnit cu = collector.parseClassFile(javaFile);
                if (cu == null) {
                    System.out.println("Failed to parse file: " + javaFile);
                    continue;
                }

                // Collect statements from all methods in the class
                cu.findAll(MethodDeclaration.class).forEach(method -> {
                    List<String> statements = collector.collectStatementsWithDeclarations(cu, method);
                    collector.writeStatementsToFile(statements, outputFile, method.getNameAsString(),
                            cu.getPackageDeclaration().map(pkg -> pkg.getNameAsString()).orElse("N/A"),
                            cu.findFirst(com.github.javaparser.ast.body.ClassOrInterfaceDeclaration.class)
                                    .map(cls -> cls.getNameAsString())
                                    .orElse("N/A"),
                            rootDir);
                });
            }
        } catch (Exception e) {
            System.err.println("Error processing files: " + e.getMessage());
        }
    }

    // Method to find all Java files in a directory
    public List<Path> findJavaFiles(Path rootDir) throws IOException {
        try (var paths = Files.walk(rootDir)) {
            return paths.filter(path -> path.toString().endsWith(".java"))
                    .collect(Collectors.toList());
        }
    }

    // Method to parse a Java file
    public CompilationUnit parseClassFile(Path javaFile) {
        try {
            String content = Files.readString(javaFile);
            return StaticJavaParser.parse(content);
        } catch (IOException e) {
            System.err.println("Error reading file " + javaFile + ": " + e.getMessage());
            return null;
        }
    }

    // Collect statements and declarations from a method
    public List<String> collectStatementsWithDeclarations(CompilationUnit cu, MethodDeclaration method) {
        List<Statement> statements = method.accept(new MethodCallCollector(cu, visitedMethods), null);

        // Find variable declarations inside the method
        List<String> statementStrings = statements.stream()
                .map(Statement::toString)
                .map(this::removeComments)
                .collect(Collectors.toList());

        // Collect variables used in the method and check for declarations in the class
        Set<String> variableNames = findVariableNames(statementStrings);
        List<String> classDeclarations = findClassVariableDeclarationsWithModifiers(cu, variableNames);

        // Combine class-level declarations with the method's statements
        statementStrings.addAll(0, classDeclarations); // Add class-level declarations to the top
        return statementStrings;
    }

    private String removeComments(String statement) {
        return statement.replaceAll("//.*", "").replaceAll("/\\*.*?\\*/", "").trim();
    }

    public void writeStatementsToFile(List<String> statements, String outputFile, String methodName,
                                      String packageName, String className, String rootDir) {
        File file = new File(outputFile);
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(file, true))) {
            // Start the JSON object
            writer.write("\"" + className + ":" + methodName + "\": {");
            writer.newLine();

            // Write file_path, class_name, and method_name keys
            writer.write("  \"project\": \"" + escapeJson(rootDir) + "\",");
            writer.newLine();
            writer.write("  \"package\": \"" + escapeJson(packageName) + "\",");
            writer.newLine();
            writer.write("  \"class_name\": \"" + escapeJson(className) + "\",");
            writer.newLine();
            writer.write("  \"method_name\": \"" + escapeJson(methodName) + "\",");
            writer.newLine();

            // Write the statements array
            writer.write("  \"statements\": [");
            writer.newLine();
            for (int i = 0; i < statements.size(); i++) {
                writer.write("    \"" + escapeJson(statements.get(i)) + "\"");
                if (i < statements.size() - 1) {
                    writer.write(",");
                }
                writer.newLine();
            }
            writer.write("  ]");
            writer.newLine();

            // End the JSON object
            writer.write("},");
            writer.newLine();
        } catch (IOException e) {
            System.err.println("Error writing to JSON file: " + e.getMessage());
        }
    }

    private String escapeJson(String input) {
        return input.replace("\\", "\\\\")
                .replace("\"", "\\\"")
                .replace("\n", "\\n")
                .replace("\r", "\\r")
                .replace("\t", "\\t");
    }

    private Set<String> findVariableNames(List<String> statements) {
        Set<String> variableNames = new HashSet<>();
        statements.forEach(statement -> {
            String[] tokens = statement.split("[\\s\\(\\)\\.;,]");
            Arrays.stream(tokens).filter(token -> !token.isEmpty() && Character.isLowerCase(token.charAt(0)))
                    .forEach(variableNames::add);
        });
        return variableNames;
    }

    private List<String> findClassVariableDeclarationsWithModifiers(CompilationUnit cu, Set<String> variableNames) {
        List<String> declarations = new ArrayList<>();
        cu.findAll(FieldDeclaration.class).forEach(field -> {
            for (VariableDeclarator variable : field.getVariables()) {
                if (variableNames.contains(variable.getNameAsString())) {
                    String modifiers = field.getModifiers().stream()
                            .map(modifier -> modifier.getKeyword().asString())
                            .collect(Collectors.joining(" "));

                    String declaration = String.format("%s %s %s;", modifiers, variable.getType().asString(), variable.getNameAsString());
                    declarations.add(declaration);
                }
            }
        });
        return declarations;
    }
}

class MethodCallCollector extends GenericListVisitorAdapter<Statement, Void> {
    private final CompilationUnit cu;
    private final Set<String> visitedMethods;

    public MethodCallCollector(CompilationUnit cu, Set<String> visitedMethods) {
        this.cu = cu;
        this.visitedMethods = visitedMethods;
    }

    @Override
    public List<Statement> visit(MethodDeclaration method, Void arg) {
        List<Statement> statements = super.visit(method, arg);

        String methodSignature = method.getNameAsString();
        if (visitedMethods.contains(methodSignature)) return statements;
        visitedMethods.add(methodSignature);

        method.getBody().ifPresent(body -> statements.addAll(body.getStatements()));

        method.findAll(MethodCallExpr.class).forEach(methodCall -> {
            String calledMethodName = methodCall.getNameAsString();
            cu.findAll(MethodDeclaration.class).stream()
                    .filter(m -> m.getNameAsString().equals(calledMethodName))
                    .findFirst()
                    .ifPresent(calledMethod -> statements.addAll(calledMethod.accept(this, arg)));
        });

        return statements;
    }
}
