import com.github.javaparser.JavaParser;
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
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

public class MethodStatementCollector {

    private Set<String> visitedMethods = new HashSet<>();

    public static void main(String[] args) {
        if (args.length != 5) {
            System.out.println("Usage: java MethodStatementCollector <methodName> <className> <package> <rootDir> <outputFile>");
            return;
        }

        String methodName = args[0];
        String className = args[1];
        String packageName = args[2];
        String rootDir = args[3];
        String outputFile = args[4];

        MethodStatementCollector collector = new MethodStatementCollector();

        try {
            // Find and parse the class file in all subdirectories
            CompilationUnit cu = collector.findAndParseClassFile(Paths.get(rootDir), className + ".java");
            if (cu == null) {
                System.out.println("Class not found in package or subdirectories.");
                return;
            }

            // Collect statements and write to output file
            List<String> statements = cu.findAll(MethodDeclaration.class).stream()
                    .filter(method -> method.getNameAsString().equals(methodName))
                    .flatMap(method -> collector.collectStatementsWithDeclarations(cu, method).stream())
                    .collect(Collectors.toList());

            collector.writeStatementsToFile(statements, outputFile);
        } catch (Exception e) {
            System.err.println("Error parsing file or collecting statements: " + e.getMessage());
        }
    }

    public CompilationUnit findAndParseClassFile(Path rootDir, String classFileName) {
        File classFile = findClassFileRecursive(rootDir.toFile(), classFileName);
        if (classFile != null) {
            try {
                JavaParser parser = new JavaParser();
                return parser.parse(classFile).getResult().orElse(null);
            } catch (Exception e) {
                System.err.println("Error parsing class file: " + e.getMessage());
            }
        }
        return null;
    }

    private File findClassFileRecursive(File dir, String classFileName) {
        if (dir == null || !dir.exists() || !dir.isDirectory()) {
            return null;
        }

        for (File file : Objects.requireNonNull(dir.listFiles())) {
            if (file.isDirectory()) {
                // Recurse into subdirectories
                File found = findClassFileRecursive(file, classFileName);
                if (found != null) {
                    return found;
                }
            } else if (file.isFile() && file.getName().equals(classFileName)) {
                // System.out.println("Class file found: " + file.getAbsolutePath());
                return file;
            }
        }
        return null;
    }

    public List<String> collectStatementsWithDeclarations(CompilationUnit cu, MethodDeclaration method) {
        // Collect method statements and variable declarations in scope
        List<Statement> statements = method.accept(new MethodCallCollector(cu, visitedMethods), null);

        // Find variable declarations inside the method
        List<String> statementStrings = statements.stream()
                .map(Statement::toString)
                .map(this::removeComments)
                .collect(Collectors.toList());

        // Collect variables used in method and check for declarations in the class
        Set<String> variableNames = findVariableNames(statementStrings);
        List<String> classDeclarations = findClassVariableDeclarationsWithModifiers(cu, variableNames);

        // Combine class-level declarations with the method's statements
        statementStrings.addAll(0, classDeclarations);  // Add class-level declarations to the top
        return statementStrings;
    }

    private String removeComments(String statement) {
        return statement.replaceAll("//.*", "").replaceAll("/\\*.*?\\*/", "").trim();
    }

    private void writeStatementsToFile(List<String> statements, String outputFile) {
        File file = new File(outputFile);
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(file))) {
            for (String statement : statements) {
                writer.write(statement);
                writer.newLine();
            }
            // System.out.println("Statements written to: " + outputFile);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
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
                    // Collect modifiers (e.g., public, static) and format as a full declaration
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
