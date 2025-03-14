### **Design Document: C/C++ Project Analysis and Database Generation Library**

---

## **1. Purpose and Scope**
**Objective**:  
Create a library that automatically parses C/C++ projects (using CMake as the build system) and constructs a relational database representing the codebase's structure, dependencies, and semantic elements. The database should enable full reconstruction of the project's architecture for downstream tools (e.g., IDEs, documentation generators, or static analyzers).

**Key Requirements**:  
- **Automatic Discovery**: Dynamically identify project files, dependencies, and build configurations.  
- **Semantic Parsing**: Extract code entities (functions, classes, variables) and their relationships.  
- **Database Consistency**: Ensure the database reflects the latest state of the codebase, with incremental updates to minimize overhead.  
- **CMake Integration**: Leverage build system metadata for accurate parsing.  

---

## **2. High-Level Architecture**
The system comprises three core modules:  

### **2.1 Project Discovery**  
- **Input**: CMake project root directory.  
- **Process**:  
  1. Generate a `compile_commands.json` file via CMake to capture compiler flags, include paths, and source files.  
  2. Scan the project directory to identify all C/C++ files (including headers not explicitly listed in CMake).  
- **Output**: List of files, compiler flags, and include directories.  

### **2.2 Semantic Parsing**  
- **Input**: Source files and compiler flags from Project Discovery.  
- **Process**:  
  1. Use Clang’s Abstract Syntax Tree (AST) parser to extract code entities (namespaces, classes, functions, variables).  
  2. Resolve inter-file dependencies (e.g., `#include` directives).  
- **Output**: Structured representation of code elements and their relationships.  

### **2.3 Database Integration**  
- **Input**: Parsed code entities and dependencies.  
- **Process**:  
  1. Map parsed data to a relational schema (e.g., tables for files, functions, classes, dependencies).  
  2. Track file modifications using content hashing to enable incremental updates.  
- **Output**: Relational database (SQL) with tables representing the project’s structure and semantics.  

---

## **3. Key Technologies**  
| Component              | Technology       | Role                                                                 |  
|------------------------|------------------|----------------------------------------------------------------------|  
| **Build System**       | CMake            | Generates compilation commands and project metadata.                |  
| **AST Parser**         | libclang/clangd  | Parses C/C++ code into semantic elements (classes, functions, etc.).|  
| **Database ORM**       | SQLAlchemy       | Maps parsed data to SQL tables and manages transactions.            |  
| **Change Detection**   | SHA-256 Hashing  | Identifies modified files to avoid redundant parsing.               |  

---

## **4. Data Model**  
### **Core Tables**  
- **Project**: Metadata about the analyzed project (name, root directory).  
- **File**: Paths and types (source/header) of project files.  
- **Function**: Functions with attributes (name, scope, associated class/namespace).  
- **Class**: Classes and their methods/properties.  
- **FileDependency**: Relationships between files (e.g., `#include` directives).  
- **FileModification**: Timestamps and content hashes for incremental updates.  

### **Example Query**  
Find global functions across the project:  
```sql  
SELECT Function.Name, File.Path  
FROM Function  
JOIN File ON Function.FileID = File.FileID  
WHERE Function.IsGlobal = TRUE;  
```  

---

## **5. Workflow**  
1. **Initialization**:  
   - Run CMake to generate build metadata.  
   - Scan the project directory to identify all relevant files.  
2. **Parsing**:  
   - Parse each file’s AST to extract entities and dependencies.  
3. **Database Population**:  
   - Insert/update records in the database.  
4. **Incremental Updates**:  
   - Recompute file hashes to detect changes and update only modified files.  

---

## **6. Design Decisions**  
- **Why CMake?**  
  CMake is widely adopted, and its `compile_commands.json` provides accurate compiler flags critical for parsing (e.g., include paths, macros).  
- **Why Clang?**  
  Clang’s AST parser is robust, supports modern C/C++ standards, and enables precise extraction of semantic elements.  
- **Why Relational Database?**  
  Relational models naturally represent hierarchical code structures (e.g., classes ↔ methods) and simplify querying for downstream tools.  

---

## **7. Advantages**  
- **Zero Manual Configuration**: Works out-of-the-box with any CMake project.  
- **Efficiency**: Incremental parsing reduces processing time for large projects.  
- **Extensibility**: The database schema can be extended to support new entity types (e.g., templates, macros).  
- **Tool-Agnostic**: Enables integration with IDEs, linters, or documentation generators.  

---

## **8. Limitations and Future Work**  
- **Limitations**:  
  - Heavy reliance on CMake; projects using other build systems require adapters.  
  - Template-heavy code may require additional parsing logic.  
- **Future Enhancements**:  
  - Support for non-CMake projects (e.g., Bazel, Makefiles).  
  - Cross-project dependency analysis (e.g., third-party libraries).  

---

This document provides a high-level blueprint for the library, balancing technical clarity with brevity. Implementation details (e.g., specific code snippets, SQL schema definitions) can be elaborated in a separate **Technical Specification** document.
