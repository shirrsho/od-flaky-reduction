import json
import os
from pathlib import Path

from astextractor import ASTExtractor
from find_shared_states import find
from repos import projects

ast_extractor = ASTExtractor("ASTExtractor-0.5.jar", "ASTExtractor.properties")

def write_static_fields_to_file(static_fields, identifier):
    """Write all found static fields to an output file."""
    data = json.loads(static_fields)

    # Create the directory if it doesn't exist
    Path('io/ast').mkdir(parents=True, exist_ok=True)

    
    with open('io/ast/'+identifier+'.json', "w") as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)

def gen_ast(project_dir, output_file):
    
    ast = ast_extractor.parse_folder(project_dir, 'JSON')
    # print(ast)
    # Write the results to the output file
    write_static_fields_to_file(ast, output_file)
    print(f"Shared static fields written to {output_file}")
    return ast

if __name__ == "__main__":
    projects = projects
    
    for project in projects:
        gen_ast(project["repo"], project["identifier"])
        find(project["identifier"])