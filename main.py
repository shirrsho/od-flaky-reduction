import json
import os
from pathlib import Path

from astextractor import ASTExtractor
from find_shared_states import find

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
    projects = [
        {
            "repo": "io/repos/Activiti-b11f757a48600e53aaf3fcb7a3ba1ece6c463cb4/activiti-spring-boot-starter/src",
            "identifier": "Activiti-b11f757a48600e53aaf3fcb7a3ba1ece6c463cb4-activiti-spring-boot-starter",
            "original_order":"io/original_orders/Activiti_Activiti-activiti-spring-boot-starter-b11f757-original_order"
        },
        {
            "repo": "io/repos/fastjson-5c6d6fd471ea1fab59f0df2dd31e0b936806780d/src",
            "identifier": "fastjson-5c6d6fd471ea1fab59f0df2dd31e0b936806780d",
            "original_order":"io/original_orders/alibaba_fastjson-.-5c6d6fd-original_order"
        },
        {
            "repo": "io/repos/hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea/hadoop-common-project/hadoop-auth/src",
            "identifier": "hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea-hadoop-common-project-hadoop-auth",
            "original_order":"io/original_orders/apache_hadoop-hadoop-common-project_hadoop-auth-cc2babc-original_order"
        },
        {
            "repo": "io/repos/hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea/hadoop-hdfs-project/hadoop-hdfs-nfs/src",
            "identifier": "hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea-hadoop-hdfs-project-hadoop-hdfs-nfs",
            "original_order":"io/original_orders/apache_hadoop-hadoop-hdfs-project_hadoop-hdfs-nfs-cc2babc-original_order"
        },
        # Add more directories here
        
    ]
    
    for project in projects:
        gen_ast(project["repo"], project["identifier"])
        find(project["identifier"], project["original_order"])