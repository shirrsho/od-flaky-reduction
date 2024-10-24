import json

from astextractor import ASTExtractor
from find_shared_states import find

ast_extractor = ASTExtractor("ASTExtractor-0.5.jar", "ASTExtractor.properties")

def write_static_fields_to_file(static_fields, output_file):
    """Write all found static fields to an output file."""
    data = json.loads(static_fields)
    with open(output_file, "w") as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)

def gen_ast(project_dir, output_file):
    
    ast = ast_extractor.parse_folder(project_dir, 'JSON')
    print(ast)
    # Write the results to the output file
    write_static_fields_to_file(ast, output_file)
    print(f"Shared static fields written to {output_file}")
    return ast

if __name__ == "__main__":
    projects = [
        {
            "repo": "C:\\Users\\shirsho\\Desktop\\Thesis, Flaky Tests\\repos\\Activiti-b11f757a48600e53aaf3fcb7a3ba1ece6c463cb4\\Activiti-b11f757a48600e53aaf3fcb7a3ba1ece6c463cb4\\activiti-spring-boot-starter\\src",
            "original_order":"C:\\Users\\shirsho\\Desktop\\Thesis, Flaky Tests\\original-orders\\Activiti_Activiti-activiti-spring-boot-starter-b11f757-original_order",
            "ast":"ast.json",
            "output_order":"orders.txt"
        },
        # Add more directories here
    ]
    
    for project in projects:
        ast = gen_ast(project["repo"], project["ast"])
        find(ast, project["output_order"], project["original_order"])