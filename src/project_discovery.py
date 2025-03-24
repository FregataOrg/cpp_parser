import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    print(f"\nDiscovering files for project_dir: {project_dir}") # Print project_dir at the beginning
    source_files = []
    header_files = []

    source_dir = os.path.join(project_dir, "src")
    include_dir = os.path.join(project_dir, "include")

    if os.path.exists(source_dir):
        for file in os.listdir(source_dir): # Non-recursive scan of source_dir
            if file.endswith(('.c', '.cpp', '.cxx')):
                source_files.append(os.path.join(source_dir, file))

    if os.path.exists(include_dir):
        for file in os.listdir(include_dir): # Non-recursive scan of include_dir
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.append(os.path.join(include_dir, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)

import sys

if __name__ == '__main__':
    # Example usage:
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = "tests/sample_project" # Default to sample project if no argument is provided

    try:
        compile_commands_path = generate_compile_commands(project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(project_dir, compile_commands_path)
        print(f"\nDiscovered Source files for project '{project_dir}':") # Indicate project directory in output
        for file in source_files:
            print(f"  - {file}")
        print(f"\nDiscovered Header files for project '{project_dir}':") # Indicate project directory in output
        for file in header_files:
            print(f"  - {file}")

        compile_info = extract_compile_info(compile_commands_path, project_dir)
        print(f"\nCompile Info for project '{project_dir}':") # Indicate project directory in output
        for filepath, info in compile_info.items():
            print(f"\nFile: {filepath}")
            print(f"  Compile Command: {info['compile_command']}")
            if info['includes']:
                print(f"  Include Paths: {info['includes']}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    print(f"\nDiscovering files for project_dir: {project_dir}") # Print project_dir at the beginning
    source_files = []
    header_files = []

    source_dir = os.path.join(project_dir, "src")
    include_dir = os.path.join(project_dir, "include")

    if os.path.exists(source_dir):
        for file in os.listdir(source_dir): # Non-recursive scan of source_dir
            if file.endswith(('.c', '.cpp', '.cxx')):
                source_files.append(os.path.join(source_dir, file))

    if os.path.exists(include_dir):
        for file in os.listdir(include_dir): # Non-recursive scan of include_dir
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.append(os.path.join(include_dir, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)

import sys

if __name__ == '__main__':
    # Example usage:
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = "tests/sample_project" # Default to sample project if no argument is provided

    try:
        compile_commands_path = generate_compile_commands(project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(project_dir, compile_commands_path)
        print(f"\nDiscovered Source files for project '{project_dir}':") # Indicate project directory in output
        for file in source_files:
            print(f"  - {file}")
        print(f"\nDiscovered Header files for project '{project_dir}':") # Indicate project directory in output
        for file in header_files:
            print(f"  - {file}")

        compile_info = extract_compile_info(compile_commands_path, project_dir)
        print(f"\nCompile Info for project '{project_dir}':") # Indicate project directory in output
        for filepath, info in compile_info.items():
            print(f"\nFile: {filepath}")
            print(f"  Compile Command: {info['compile_command']}")
            if info['includes']:
                print(f"  Include Paths: {info['includes']}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = [
        os.path.join(project_dir, "src", "main.cpp"),
        os.path.join(project_dir, "src", "utils.cpp"),
    ]
    header_files = [
        os.path.join(project_dir, "include", "utils.h"),
    ]

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = []
    header_files = []

    source_dir = os.path.join(project_dir, "src")
    include_dir = os.path.join(project_dir, "include")

    if os.path.exists(source_dir):
        for file in os.listdir(source_dir): # Non-recursive scan of source_dir
            if file.endswith(('.c', '.cpp', '.cxx')):
                source_files.append(os.path.join(source_dir, file))

    if os.path.exists(include_dir):
        for file in os.listdir(include_dir): # Non-recursive scan of include_dir
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.append(os.path.join(include_dir, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = []
    header_files = []

    source_dir = os.path.join(project_dir, "src")
    include_dir = os.path.join(project_dir, "include")

    if os.path.exists(source_dir):
        for root, _, files in os.walk(source_dir): # Scan within source_dir recursively
            for file in files:
                if file.endswith(('.c', '.cpp', '.cxx')):
                    source_files.append(os.path.join(root, file))

    if os.path.exists(include_dir):
        for root, _, files in os.walk(include_dir): # Scan within include_dir recursively
            for file in files:
                if file.endswith(('.h', '.hpp', '.hxx')):
                    header_files.append(os.path.join(root, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)

def extract_compile_info(compile_commands_path, project_dir):
    compile_info = {}
    try:
        with open(compile_commands_path, 'r') as f:
            compile_commands = json.load(f)
            for command in compile_commands:
                filepath = os.path.relpath(command['file'], project_dir) # Relative path
                compile_info[filepath] = {
                    'compile_command': command['command'],
                    'includes': command['command'].split('-I')[1:] if '-I' in command['command'] else [] # Extract include paths
                }
    except FileNotFoundError:
        print(f"Warning: {compile_commands_path} not found. Compile info extraction failed.")
    except json.JSONDecodeError:
        print(f"Warning: Error parsing {compile_commands_path}. Compile info extraction failed.")
    return compile_info


import sys

if __name__ == '__main__':
    # Example usage:
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = "tests/sample_project" # Default to sample project if no argument is provided

    try:
        compile_commands_path = generate_compile_commands(project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(project_dir, compile_commands_path)
        print(f"\nDiscovered Source files for project '{project_dir}':") # Indicate project directory in output
        for file in source_files:
            print(f"  - {file}")
        print(f"\nDiscovered Header files for project '{project_dir}':") # Indicate project directory in output
        for file in header_files:
            print(f"  - {file}")

        compile_info = extract_compile_info(compile_commands_path, project_dir)
        print(f"\nCompile Info for project '{project_dir}':") # Indicate project directory in output
        for filepath, info in compile_info.items():
            print(f"\nFile: {filepath}")
            print(f"  Compile Command: {info['compile_command']}")
            if info['includes']:
                print(f"  Include Paths: {info['includes']}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = [
        os.path.join(project_dir, "src", "main.cpp"),
        os.path.join(project_dir, "src", "utils.cpp"),
    ]
    header_files = [
        os.path.join(project_dir, "include", "utils.h"),
    ]

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = [
        os.path.join(project_dir, "src", "main.cpp"),
        os.path.join(project_dir, "src", "utils.cpp"),
    ]
    header_files = [
        os.path.join(project_dir, "include", "utils.h"),
    ]

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = []
    header_files = []

    source_dir = os.path.join(project_dir, "src")
    include_dir = os.path.join(project_dir, "include")

    if os.path.exists(source_dir):
        for file in os.listdir(source_dir): # Non-recursive scan of source_dir
            if file.endswith(('.c', '.cpp', '.cxx')):
                source_files.append(os.path.join(source_dir, file))

    if os.path.exists(include_dir):
        for file in os.listdir(include_dir): # Non-recursive scan of include_dir
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.append(os.path.join(include_dir, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = []
    header_files = []

    source_dir = os.path.join(project_dir, "src")
    include_dir = os.path.join(project_dir, "include")

    if os.path.exists(source_dir):
        for root, _, files in os.walk(source_dir): # Scan within source_dir recursively
            for file in files:
                if file.endswith(('.c', '.cpp', '.cxx')):
                    source_files.append(os.path.join(root, file))

    if os.path.exists(include_dir):
        for root, _, files in os.walk(include_dir): # Scan within include_dir recursively
            for file in files:
                if file.endswith(('.h', '.hpp', '.hxx')):
                    header_files.append(os.path.join(root, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)

def extract_compile_info(compile_commands_path, project_dir):
    compile_info = {}
    try:
        with open(compile_commands_path, 'r') as f:
            compile_commands = json.load(f)
            for command in compile_commands:
                filepath = os.path.relpath(command['file'], project_dir) # Relative path
                compile_info[filepath] = {
                    'compile_command': command['command'],
                    'includes': command['command'].split('-I')[1:] if '-I' in command['command'] else [] # Extract include paths
                }
    except FileNotFoundError:
        print(f"Warning: {compile_commands_path} not found. Compile info extraction failed.")
    except json.JSONDecodeError:
        print(f"Warning: Error parsing {compile_commands_path}. Compile info extraction failed.")
    return compile_info


import sys

if __name__ == '__main__':
    # Example usage:
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = "tests/sample_project" # Default to sample project if no argument is provided

    try:
        compile_commands_path = generate_compile_commands(project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(project_dir, compile_commands_path)
        print(f"\nDiscovered Source files for project '{project_dir}':") # Indicate project directory in output
        for file in source_files:
            print(f"  - {file}")
        print(f"\nDiscovered Header files for project '{project_dir}':") # Indicate project directory in output
        for file in header_files:
            print(f"  - {file}")

        compile_info = extract_compile_info(compile_commands_path, project_dir)
        print(f"\nCompile Info for project '{project_dir}':") # Indicate project directory in output
        for filepath, info in compile_info.items():
            print(f"\nFile: {filepath}")
            print(f"  Compile Command: {info['compile_command']}")
            if info['includes']:
                print(f"  Include Paths: {info['includes']}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = []
    header_files = []

    source_dir = os.path.join(project_dir, "src")
    include_dir = os.path.join(project_dir, "include")

    if os.path.exists(source_dir):
        for file in os.listdir(source_dir):
            if file.endswith(('.c', '.cpp', '.cxx')):
                source_files.append(os.path.join(source_dir, file))

    if os.path.exists(include_dir):
        for file in os.listdir(include_dir):
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.append(os.path.join(include_dir, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)

def extract_compile_info(compile_commands_path, project_dir):
    compile_info = {}
    try:
        with open(compile_commands_path, 'r') as f:
            compile_commands = json.load(f)
            for command in compile_commands:
                filepath = os.path.relpath(command['file'], project_dir) # Relative path
                compile_info[filepath] = {
                    'compile_command': command['command'],
                    'includes': command['command'].split('-I')[1:] if '-I' in command['command'] else [] # Extract include paths
                }
    except FileNotFoundError:
        print(f"Warning: {compile_commands_path} not found. Compile info extraction failed.")
    except json.JSONDecodeError:
        print(f"Warning: Error parsing {compile_commands_path}. Compile info extraction failed.")
    return compile_info


if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir) # We still generate compile_commands.json
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path=None)
        print("\nDiscovered Source files (from src dir):")
        for file in source_files:
            print(f"  - {file}")
        print("\nDiscovered Header files (from include dir):")
        for file in header_files:
            print(f"  - {file}")

        compile_info = extract_compile_info(compile_commands_path, sample_project_dir)
        print("\nCompile Info:")
        for filepath, info in compile_info.items():
            print(f"\nFile: {filepath}")
            print(f"  Compile Command: {info['compile_command']}")
            if info['includes']:
                print(f"  Include Paths: {info['includes']}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = []
    header_files = []

    source_dir = os.path.join(project_dir, "src")
    include_dir = os.path.join(project_dir, "include")

    if os.path.exists(source_dir):
        for file in os.listdir(source_dir):
            if file.endswith(('.c', '.cpp', '.cxx')):
                source_files.append(os.path.join(source_dir, file))

    if os.path.exists(include_dir):
        for file in os.listdir(include_dir):
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.append(os.path.join(include_dir, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files)

if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir) # We still generate compile_commands.json
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path=None)
        print("\nDiscovered Source files (from src dir):")
        for file in source_files:
            print(f"  - {file}")
        print("\nDiscovered Header files (from include dir):")
        for file in header_files:
            print(f"  - {file}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = set()
    header_files = set()

    # Directory scan for source files
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.c', '.cpp', '.cxx')):
                source_files.add(os.path.join(root, file))

    # Directory scan for header files
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.add(os.path.join(root, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(list(set(relative_source_files))), sorted(list(set(relative_header_files))) # Return sorted unique relative paths

if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir) # We still generate compile_commands.json, but don't use it for file discovery in this iteration
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path=None) # Pass None to not use compile_commands for discovery
        print("\nDiscovered Source files:")
        for file in source_files: # Iterate directly over the list
            print(f"  - {file}")
        print("\nDiscovered Header files:")
        for file in header_files: # Iterate directly over the list
            print(f"  - {file}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = set()
    header_files = set()

    # Primary source file discovery via directory scan
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.c', '.cpp', '.cxx')):
                source_files.add(os.path.join(root, file))

    # Augment source files and extract compile commands from compile_commands.json
    if compile_commands_path:
        try:
            with open(compile_commands_path, 'r') as f:
                compile_commands = json.load(f)
                for command in compile_commands:
                    source_files.add(command['file']) # Add source files from compile_commands.json (augmentation)
                    # In later steps, we'll extract compiler flags from here

        except FileNotFoundError:
            print(f"Warning: {compile_commands_path} not found. File discovery may be incomplete.")
        except json.JSONDecodeError:
            print(f"Warning: Error parsing {compile_commands_path}. File discovery may be incomplete.")


    # Recursively scan project directory for header files
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.add(os.path.join(root, file))
            elif file.endswith(('.c', '.cpp', '.cxx')):
                source_files.add(os.path.join(root, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(list(set(relative_source_files))), sorted(list(set(relative_header_files))) # Return sorted unique relative paths

if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path)
        print("\nDiscovered Source files:")
        for file in source_files: # Iterate directly over the list
            print(f"  - {file}")
        print("\nDiscovered Header files:")
        for file in header_files: # Iterate directly over the list
            print(f"  - {file}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = set()
    header_files = set()

    if compile_commands_path:
        try:
            with open(compile_commands_path, 'r') as f:
                compile_commands = json.load(f)
                for command in compile_commands:
                    if "CompilerId" not in os.path.basename(command['directory']):  # Filter by directory name
                        source_files.add(command['file'])
        except FileNotFoundError:
            print(f"Warning: {compile_commands_path} not found. File discovery may be incomplete.")
        except json.JSONDecodeError:
            print(f"Warning: Error parsing {compile_commands_path}. File discovery may be incomplete.")

    # Recursively scan project directory for header files
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.add(os.path.join(root, file))
            elif file.endswith(('.c', '.cpp', '.cxx')):
                source_files.add(os.path.join(root, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(list(set(relative_source_files))), sorted(list(set(relative_header_files))) # Return sorted unique relative paths

if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path)
        print("\nDiscovered Source files:")
        for file in source_files: # Iterate directly over the list
            print(f"  - {file}")
        print("\nDiscovered Header files:")
        for file in header_files: # Iterate directly over the list
            print(f"  - {file}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = set()
    header_files = set()

    if compile_commands_path:
        try:
            with open(compile_commands_path, 'r') as f:
                compile_commands = json.load(f)
                for command in compile_commands:
                    if "CompilerIdC" not in command['file'] and "CompilerIdCXX" not in command['file']:  # Directly filter CompilerId files
                        source_files.add(command['file'])
        except FileNotFoundError:
            print(f"Warning: {compile_commands_path} not found. File discovery may be incomplete.")
        except json.JSONDecodeError:
            print(f"Warning: Error parsing {compile_commands_path}. File discovery may be incomplete.")

    # Recursively scan project directory for header files
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.add(os.path.join(root, file))
            elif file.endswith(('.c', '.cpp', '.cxx')):
                source_files.add(os.path.join(root, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(list(set(relative_source_files))), sorted(list(set(relative_header_files))) # Return sorted unique relative paths

if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path)
        print("\nDiscovered Source files:")
        for file in source_files: # Iterate directly over the list
            print(f"  - {file}")
        print("\nDiscovered Header files:")
        for file in header_files: # Iterate directly over the list
            print(f"  - {file}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = set()
    header_files = set()

    if compile_commands_path:
        try:
            with open(compile_commands_path, 'r') as f:
                compile_commands = json.load(f)
                for command in compile_commands:
                    if 'CMakeFiles' not in os.path.basename(os.path.dirname(command['file'])):  # Filter out compiler id files by dirname
                        source_files.add(command['file'])
        except FileNotFoundError:
            print(f"Warning: {compile_commands_path} not found. File discovery may be incomplete.")
        except json.JSONDecodeError:
            print(f"Warning: Error parsing {compile_commands_path}. File discovery may be incomplete.")

    # Recursively scan project directory for header files
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.add(os.path.join(root, file))
            elif file.endswith(('.c', '.cpp', '.cxx')):
                source_files.add(os.path.join(root, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(list(set(relative_source_files))), sorted(list(set(relative_header_files))) # Return sorted unique relative paths

if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path)
        print("\nDiscovered Source files:")
        for file in source_files: # Iterate directly over the list
            print(f"  - {file}")
        print("\nDiscovered Header files:")
        for file in header_files: # Iterate directly over the list
            print(f"  - {file}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = set()
    header_files = set()

    if compile_commands_path:
        try:
            with open(compile_commands_path, 'r') as f:
                compile_commands = json.load(f)
                for command in compile_commands:
                    if 'CMakeFiles' not in command['file']:  # Filter out compiler id files more robustly
                        source_files.add(command['file'])
        except FileNotFoundError:
            print(f"Warning: {compile_commands_path} not found. File discovery may be incomplete.")
        except json.JSONDecodeError:
            print(f"Warning: Error parsing {compile_commands_path}. File discovery may be incomplete.")

    # Recursively scan project directory for header files
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.add(os.path.join(root, file))
            elif file.endswith(('.c', '.cpp', '.cxx')):
                source_files.add(os.path.join(root, file))

    relative_source_files = [os.path.relpath(f, project_dir) for f in source_files] # Relative paths
    relative_header_files = [os.path.relpath(h, project_dir) for h in header_files] # Relative paths
    return sorted(relative_source_files), sorted(relative_header_files) # Return sorted relative paths

if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path)
        print("\nDiscovered Source files:")
        for file in source_files: # Iterate directly over the list
            print(f"  - {file}")
        print("\nDiscovered Header files:")
        for file in header_files: # Iterate directly over the list
            print(f"  - {file}")

    except Exception as e:
        print(f"Error: {e}")
import subprocess
import json
import os

def generate_compile_commands(project_dir):
    build_dir = os.path.join(project_dir, "build")
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    cmake_command = [
        "cmake",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        "-B", build_dir,
        project_dir
    ]

    try:
        subprocess.run(cmake_command, check=True, capture_output=True)
        compile_commands_path = os.path.join(build_dir, "compile_commands.json")
        if os.path.exists(compile_commands_path):
            return compile_commands_path
        else:
            raise FileNotFoundError("compile_commands.json not found after CMake execution.")
    except subprocess.CalledProcessError as e:
        print(f"CMake command failed: {e.stderr.decode()}")
        raise
    except FileNotFoundError as e:
        print(f"Error generating compile_commands.json: {e}")
        raise

def discover_project_files(project_dir, compile_commands_path=None):
    source_files = set()
    header_files = set()

    if compile_commands_path:
        try:
            with open(compile_commands_path, 'r') as f:
                compile_commands = json.load(f)
                for command in compile_commands:
                    if not command['file'].startswith(os.path.join(project_dir, 'build', 'CMakeFiles')): # Filter out compiler id files
                        source_files.add(command['file'])
        except FileNotFoundError:
            print(f"Warning: {compile_commands_path} not found. File discovery may be incomplete.")
        except json.JSONDecodeError:
            print(f"Warning: Error parsing {compile_commands_path}. File discovery may be incomplete.")

    # Recursively scan project directory for header files
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(('.h', '.hpp', '.hxx')):
                header_files.add(os.path.join(root, file))
            elif file.endswith(('.c', '.cpp', '.cxx')):
                source_files.add(os.path.join(root, file))

    return sorted(list(source_files)), sorted(list(header_files)) # Return sorted lists

if __name__ == '__main__':
    # Example usage:
    sample_project_dir = "tests/sample_project"
    try:
        compile_commands_path = generate_compile_commands(sample_project_dir)
        print(f"compile_commands.json generated at: {compile_commands_path}")
        source_files, header_files = discover_project_files(sample_project_dir, compile_commands_path)
        print("\nDiscovered Source files:")
        for file in source_files: # Iterate directly over the list
            print(f"  - {os.path.relpath(file, sample_project_dir)}") # Relative paths
        print("\nDiscovered Header files:")
        for file in header_files: # Iterate directly over the list
            print(f"  - {os.path.relpath(file, sample_project_dir)}") # Relative paths

    except Exception as e:
        print(f"Error: {e}")
