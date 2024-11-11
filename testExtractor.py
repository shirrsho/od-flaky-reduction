import json
from pathlib import Path
from repos import projects

def is_test_method(file_path):
    """Checks if the file path contains 'test' or 'tests' (case-insensitive)."""
    return 'test' in file_path.lower().split('/') or 'tests' in file_path.lower().split('/')


def find_test_methods(ast):
    """Finds all test methods in the given AST."""
    
    results = []
    
    for file_data in ast['folder']['file']:
        file_ast = file_data['ast']
        file_path = file_data['path']
        methods = []
        
        # Skip if file is not a test file
        if not is_test_method(file_path):
            continue

        compilation_unit = file_ast.get('CompilationUnit', {})
        if isinstance(compilation_unit, dict):
            # Extract package and class name
            package = compilation_unit.get('PackageDeclaration', '').replace('package', '').replace(';', '').strip()
            class_name = file_path.split('/')[-1].replace('.java', '').strip()
            
            # Ensure type_declarations is a list
            type_declarations = compilation_unit.get('TypeDeclaration', [])
            if not isinstance(type_declarations, list):
                type_declarations = [type_declarations]
            
            for type_declaration in type_declarations:
                if isinstance(type_declaration, dict):  # Ensure it's a dictionary
                    method_declarations = type_declaration.get('MethodDeclaration', [])
                    
                    # Ensure method_declarations is a list
                    if not isinstance(method_declarations, list):
                        method_declarations = [method_declarations]

                    # Collect method names
                    for method in method_declarations:
                        if isinstance(method, dict):  # Ensure method is a dictionary
                            method_name = method.get('SimpleName')
                            if method_name:
                                methods.append(method_name)
            
            # Add results as a dictionary for each file
            results.append({
                'package': package,
                'className': class_name,
                'methods': methods
            })

    return results

def write_tests_to_file(tests, identifier):
    """Write the detected dependencies to a file."""
    Path('io/new_tests').mkdir(parents=True, exist_ok=True)
    
    file_path = f'io/new_tests/{identifier}.json'
    
    # Write the JSON data to the file
    with open(file_path, 'w') as ff:
        json.dump(tests, ff, indent=4)


def find(identifier="Achilles-e3099bdce342910951c4862c78751fd81ed4552e-integration-test-2_1"):
    with open('io/ast/'+identifier+'.json', 'r') as file:
        ast_data = json.load(file)
    # Process the AST to find shared static fields
    test_methods = find_test_methods(ast_data)
    # write_tests_to_file(test_methods, identifier)
    return test_methods


import subprocess
import sys

def run_bash_script(method_name, class_name, package_name, root_dir, output_file):
    # Construct the bash command
    bash_command = [
        "bash", "newbash.sh", method_name, class_name, package_name, root_dir, output_file
    ]
    
    try:
        print('-')
        subprocess.run(bash_command, check=True)
        # print(f"Successfully executed the bash script with arguments: {method_name}, {class_name}, {package_name}, {root_dir}, {output_file}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error executing the bash script: {e}")
    except FileNotFoundError as e:
        print(f"Error: Bash script not found. Ensure 'your_bash_script.sh' exists in the same directory. {e}")
        
if __name__ == "__main__":
    projects = projects
    # Extract arguments from the command-line

    for project in projects:
        test_methods = find(project["identifier"])
        # Run the bash script with the given arguments
        for test in test_methods:
            Path('io/new_tests/'+project["identifier"]+"/"+test["className"]).mkdir(parents=True, exist_ok=True)
            if len(test["methods"])==0: continue
            for m in test["methods"]:
                run_bash_script(m, test["className"], test["package"], project["repo"], "io/new_tests/"+project["identifier"]+"/"+test["className"]+"/"+m)