# C/C++ Project Parser - Development Plan

## Overview
This document outlines the development plan for a Python library that parses C/C++ projects using CMake and constructs a SQLite database representing the codebase's structure, dependencies, and semantic elements.

## Project Structure
```
cpp_parser/
├── src/
│   ├── __init__.py
│   ├── project_discovery.py    # CMake integration and file discovery
│   ├── semantic_parser.py      # Clang AST parsing
│   ├── database.py             # SQLite database integration with SQLAlchemy
│   └── utils.py                # Helper functions
├── tests/
│   ├── __init__.py
│   ├── test_project_discovery.py
│   ├── test_semantic_parser.py
│   ├── test_database.py
│   └── sample_project/         # Test C++ project with CMake
│       ├── CMakeLists.txt
│       ├── src/
│       │   ├── main.cpp
│       │   └── utils.cpp
│       └── include/
│           └── utils.h
├── docs/
│   ├── iteration_summaries/    # Documentation of each iteration
│   └── api_reference.md
├── requirements.txt
├── setup.py
└── README.md
```

## Development Iterations

### Iteration 1: Project Setup and Discovery Module

**Prototype Goals:**
1. Set up project structure and dependencies
2. Implement basic CMake integration to generate `compile_commands.json`
3. Create file discovery functionality to identify all C/C++ files

**Testing Approach:**
- Create a simple test C++ project with CMake
- Verify correct identification of source and header files
- Validate extraction of compiler flags and include paths

**Expected Outcomes:**
- Working project discovery module
- Documentation of challenges and improvements for next iteration

### Iteration 2: Semantic Parsing with Clang

**Prototype Goals:**
1. Set up libclang integration
2. Implement basic AST traversal to extract:
   - Functions (name, parameters, return type)
   - Classes (name, methods, properties)
   - Namespaces
3. Resolve basic file dependencies (#include directives)

**Testing Approach:**
- Parse the test project's files
- Verify correct extraction of code entities
- Test dependency resolution between files

**Expected Outcomes:**
- Working semantic parser module
- Documentation of parsing challenges and improvements

### Iteration 3: Database Integration

**Prototype Goals:**
1. Design SQLite schema using SQLAlchemy ORM
2. Implement database models for:
   - Projects
   - Files
   - Functions
   - Classes
   - Dependencies
3. Create functions to populate the database with parsed data

**Testing Approach:**
- Store parsed data from test project
- Execute sample queries to validate data integrity
- Test incremental updates with file modifications

**Expected Outcomes:**
- Working database integration module
- Documentation of database design decisions and improvements

### Iteration 4: Integration and Optimization

**Prototype Goals:**
1. Integrate all modules into a cohesive library
2. Implement incremental parsing with file hashing
3. Add configuration options and CLI interface
4. Optimize performance for larger projects

**Testing Approach:**
- Test with larger, more complex C++ projects
- Measure parsing time and memory usage
- Validate incremental update functionality

**Expected Outcomes:**
- Complete working library
- Performance metrics and optimization opportunities
- Final documentation and usage examples

## Implementation Details

### Project Discovery Module
- Use `subprocess` to run CMake commands
- Parse `compile_commands.json` with Python's JSON module
- Implement recursive directory scanning for header files

### Semantic Parser Module
- Use `clang.cindex` Python bindings for libclang
- Create AST visitor classes for different code entities
- Implement caching to improve parsing performance

### Database Module
- Use SQLAlchemy for ORM
- Define table schemas and relationships
- Implement transaction management for atomic updates

### Testing Framework
- Use pytest for unit and integration tests
- Create a sample C++ project with various features to test parsing
- Implement test fixtures for database and parser setup

## Sample C++ Test Project

The sample project will include:
- Multiple source and header files
- Classes with inheritance and composition
- Templates and template specializations
- Namespaces and nested namespaces
- Global and member functions
- Various access modifiers (public, private, protected)
- Macros and preprocessor directives

## Dependencies

- Python 3.8+
- libclang and Python bindings
- SQLAlchemy
- CMake (for test projects)
- pytest (for testing)

## Installation Steps for libclang

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install libclang-dev python3-clang
```

**macOS:**
```bash
brew install llvm
pip install clang
```

**Windows:**
```bash
pip install clang
# Download LLVM binaries from https://releases.llvm.org/
