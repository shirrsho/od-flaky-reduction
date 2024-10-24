import json

# Open and read the JSON file
# with open('ast.json', 'r') as file:
#     ast_data = json.load(file)

def find_static_fields(ast):
    """Finds all static fields in the given AST."""
    static_fields = set()
    
    for file_data in ast['folder']['file']:
        file_ast = file_data['ast']
        file_path = file_data['path']
        
        type_declarations = file_ast.get('CompilationUnit', {}).get('TypeDeclaration', [])
        
        # Ensure type_declarations is a list
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
                        # Check if "static" modifier is present in field declaration
                        modifiers = field.get('Modifier', [])
                        if isinstance(modifiers, list) and 'static' in modifiers:
                            # Get the field name and add it to the static_fields set
                            variable_name = field.get('VariableDeclarationFragment', None)
                            if variable_name:
                                static_fields.add((file_path, variable_name))
    
    return static_fields

def is_test_method(file_path):
    """Checks if the file path contains 'test' or 'tests' (case-insensitive)."""
    return 'test' in file_path.lower().split('/') or 'tests' in file_path.lower().split('/')

def find_test_methods_and_dependencies(ast, static_fields):
    """Finds test methods and checks if they reference any static fields."""
    dependencies = {}

    for file_data in ast['folder']['file']:
        file_ast = file_data['ast']
        file_path = file_data['path']
        
        # Check if this file likely contains test methods based on the file path
        if not is_test_method(file_path):
            continue
        
        type_declarations = file_ast.get('CompilationUnit', {}).get('TypeDeclaration', [])
        
        # Ensure type_declarations is a list
        if not isinstance(type_declarations, list):
            type_declarations = [type_declarations]
        
        for type_declaration in type_declarations:
            if isinstance(type_declaration, dict):  # Ensure it's a dictionary
                method_declarations = type_declaration.get('MethodDeclaration', [])
                
                if not isinstance(method_declarations, list):
                    method_declarations = [method_declarations]  # Ensure it's a list

                for method in method_declarations:
                    if isinstance(method, dict):  # Ensure method is a dictionary
                        method_name = method.get('SimpleName', None)

                        # Key will now include file path and method name
                        key = f"{file_path}: {method_name}"
                        dependencies[key] = []

                        # Check for field accesses in the method body (mock the logic)
                        for field_path, field_name in static_fields:
                            if file_path in field_path:
                                dependencies[key].append(f"{field_path}: {field_name}")
    
    return dependencies

def write_dependencies_to_file(dependencies, output_file):
    """Write the detected dependencies to a file."""
    with open(output_file, 'w') as f:
        if not dependencies:
            f.write("No test methods found.\n")
        for test_method, shared_states in dependencies.items():
            f.write(f"Test: {test_method}\n")  # Now test method includes file path
            if shared_states:
                f.write("Shared States:\n")
                with open('orders.txt', 'a+') as ff:
                    ff.write(f"{test_method.replace('.java','').replace(' ','').replace('/','.').replace(':','.')}\n")
                for state in shared_states:
                    f.write(f"  - {state}\n")
            f.write("\n")
    print(f"Dependencies written to {output_file}")

def print_results(expected_file, output_file):
    with open(expected_file, 'r') as e :
        expecteds = e.read()
    with open(output_file,'r') as o:
        outputs = o.read()
    expected_list = list(set(expecteds.split('\n')))
    output_list = list(set(outputs.split('\n')))
    
    matches = []
    for expected in expected_list:
        for output in output_list:
            if expected in output:  # Substring check
                matches.append(expected)
                break  # Avoid counting the same expected multiple times

    # Print the number of matches and the matching items
    print(f"Number of matches: {len(matches)}")
    print(f"Expected Number of matches: {len(expected_list)}")
    print(round(len(matches)*100/len(expected_list),2))



def find(ast_data, output_order, original_order):
    # Process the AST to find shared static fields
    static_fields = find_static_fields(ast_data)

    # Find test methods and link them to the static fields they access
    test_dependencies = find_test_methods_and_dependencies(ast_data, static_fields)

    # Write the results to a file
    write_dependencies_to_file(test_dependencies, output_order)
    print_results(original_order, output_order)