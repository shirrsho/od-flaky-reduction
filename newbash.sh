#!/bin/bash

# Check if exactly 3 arguments are provided
if [ "$#" -ne 5 ]; then
    echo "Usage: $0 <methodName> <className> <package> <rootDir> <outputFile>"
    exit 1
fi

# Assign arguments to variables
METHOD_NAME=$1
CLASS_NAME=$2
PACKAGE=$3
ROOT_DIR=$4
OUTPUT_FILE=$5

# Set the source directory and output directory for compiled classes
SRC_DIR=$ROOT_DIR
OUT_DIR="out"

# Ensure the output directory exists
mkdir -p $OUT_DIR

# Compile the Java file
javac -d $OUT_DIR -cp ".:javaparser-core-3.23.1.jar" MethodStatementCollector.java

# Run the Java program with the provided arguments
java -cp "$OUT_DIR:javaparser-core-3.23.1.jar" MethodStatementCollector "$METHOD_NAME" "$CLASS_NAME" "$PACKAGE" "$SRC_DIR" "$OUTPUT_FILE"
