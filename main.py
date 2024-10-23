import json

from astextractor import ASTExtractor

ast_extractor = ASTExtractor("ASTExtractor-0.5.jar", "ASTExtractor.properties")

def write_static_fields_to_file(static_fields, output_file):
    """Write all found static fields to an output file."""
    data = json.loads(static_fields)
    with open(output_file, "w") as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)

def main(project_dir, output_file):
    
    ast = ast_extractor.parse_folder(project_dir, 'JSON')
    print(ast)
    # Write the results to the output file
    write_static_fields_to_file(ast, output_file)
    print(f"Shared static fields written to {output_file}")

if __name__ == "__main__":
    # Path to the Java source files directory
    project_dir = "/Users/shirsho/developer/thesis/fastjson/src"
    output_file = "ast.json"
    
    main(project_dir, output_file)
