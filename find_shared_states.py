import json
from pathlib import Path

def in_original_orders(file_path, identifier):
    return True

def find_static_fields(ast):
    """Finds all static fields in the given AST."""
    static_fields = set()
    
    for file_data in ast['folder']['file']:
        file_ast = file_data['ast']
        file_path = file_data['path']

        type_declarations = file_ast.get('CompilationUnit', {})
        if isinstance(type_declarations, dict):
            type_declarations = type_declarations.get('TypeDeclaration', [])
            
            if not isinstance(type_declarations, list):
                type_declarations = [type_declarations]
            
            for type_declaration in type_declarations:
                if isinstance(type_declaration, dict):  # Ensure it's a dictionary
                    field_declarations = type_declaration.get('FieldDeclaration', [])
                    
                    # Ensure field_declarations is a list
                    if not isinstance(field_declarations, list):
                        field_declarations = [field_declarations]

                    for field in field_declarations:
                        if isinstance(field, dict):  # Ensure we only process dicts
                            modifiers = field.get('Modifier', [])
                            if isinstance(modifiers, list) and 'static' in modifiers:
                                variable_name = field.get('VariableDeclarationFragment', None)
                                if not isinstance(variable_name,list):
                                    variable_name = [variable_name]
                                    for v in variable_name:
                                        static_fields.add((file_path, v))
    
    
    return static_fields

def is_test_method(file_path):
    """Checks if the file path contains 'test' or 'tests' (case-insensitive)."""
    return 'test' in file_path.lower().split('/') or 'tests' in file_path.lower().split('/')

def find_test_methods_and_dependencies(ast, static_fields, identifier):
    """Finds test methods and checks if they reference any static fields."""
    dependencies = {}

    test_count = 0
    class_count = 0

    for file_data in ast['folder']['file']:
        file_ast = file_data['ast']
        file_path = file_data['path']

        if not in_original_orders(file_path, identifier) : continue
        if not is_test_method(file_path):
            continue
        class_count = class_count + 1
        if isinstance(file_ast, dict):
            type_declarations = file_ast.get('CompilationUnit', {})
            
            if isinstance(type_declarations, dict): 
                type_declarations = type_declarations.get('TypeDeclaration', [])
                # Ensure type_declarations is a list
                if not isinstance(type_declarations, list):
                    type_declarations = [type_declarations]
                
                for type_declaration in type_declarations:
                    if isinstance(type_declaration, dict):  # Ensure it's a dictionary
                        method_declarations = type_declaration.get('MethodDeclaration', [])
                        
                        if not isinstance(method_declarations, list):
                            method_declarations = [method_declarations]  # Ensure it's a list

                        for method in method_declarations:
                            if is_test_method(file_path=file_path) : 
                                test_count = test_count + 1
                                
                            if isinstance(method, dict):  # Ensure method is a dictionary
                                method_name = method.get('SimpleName', None)

                                key = f"{file_path}: {method_name}"
                                dependencies[key] = []

                                for field_path, field_name in static_fields:
                                    if file_path in field_path:
                                        dependencies[key].append(f"{field_path}: {field_name}")
    global total_test_count
    total_test_count = test_count
    global total_class_count
    total_class_count = class_count
    return dependencies

def write_dependencies_to_file(dependencies, identifier):
    """Write the detected dependencies to a file."""
    Path('io/found_tests').mkdir(parents=True, exist_ok=True)
    Path('io/dependencies').mkdir(parents=True, exist_ok=True)
    with open('io/dependencies/'+identifier, 'a+') as f:
        if not dependencies:
            f.write("No test methods found.\n")
        else:
            with open('io/found_tests/'+identifier, 'a+') as ff:
                for test_method, shared_states in dependencies.items():
                    f.write(f"Test: {test_method}\n")
                    if shared_states:
                        f.write("Shared States:\n")
                        ff.write(f"{test_method.replace('.java','').replace(' ','').replace('/','.').replace(':','.')}\n")
                        for state in shared_states:
                            f.write(f"  - {state}\n")
                    f.write("\n")
    # print(f"Tests written to {'io/found_tests/'+identifier}")

def print_results(identifier):
    expected_set = set()
    output_set = set()

    with open('io/expected_tests/'+identifier, 'r') as e:
        while True:
            line = e.readline().strip()
            if not line:
                break
            expected_set.add(line)

    with open('io/found_tests/'+identifier, 'r') as o:
        while True:
            line = o.readline().strip()
            if not line:
                break
            output_set.add(line)

    expected_list = list(expected_set)
    output_list = list(output_set)
    
    matches = []
    for expected in expected_list:
        for output in output_list:
            if expected in output:
                matches.append(expected)
                break

    with open('result.txt', 'a+') as f:
        f.write(f"{identifier}\n")
        f.write(f"Total Number of test classes: {total_class_count}\n")
        f.write(f"Total Number of test cases: {total_test_count}\n")
        f.write(f"Number of test case after reduction: {len(output_list)}\n")
        f.write(f"Number of matches: {len(matches)}\n")
        f.write(f"Expected Number of matches: {len(expected_list)}\n")
        f.write(f"{round(len(matches)*100/(len(expected_list)+1e-14),2)}"+'\n\n')
    with open('result.csv', 'a+') as f:
        f.write(f"{identifier},{total_test_count},{len(output_list)},{len(matches)},{len(expected_list)},{total_class_count}\n")



def find(identifier):
    with open('io/ast/'+identifier+'.json', 'r') as file:
        ast_data = json.load(file)
    static_fields = find_static_fields(ast_data)

    test_dependencies = find_test_methods_and_dependencies(ast_data, static_fields, identifier)

    write_dependencies_to_file(test_dependencies, identifier)
    print_results(identifier)