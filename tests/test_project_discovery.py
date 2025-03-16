import unittest
import os
from src.project_discovery import discover_project_files, generate_compile_commands, extract_compile_info

class TestProjectDiscovery(unittest.TestCase):

    def setUp(self):
        self.sample_project_dir = "tests/sample_project"
        # self.compile_commands_path = generate_compile_commands(self.sample_project_dir) # Skip compile_commands generation

    def test_discover_project_files(self):
        print("\nRunning test_discover_project_files...") # Add print statement at the beginning
        source_files, header_files = discover_project_files(self.sample_project_dir, compile_commands_path=None) # Pass None to skip compile_commands usage
        expected_source_files = sorted([
            "src/main.cpp",
            "src/utils.cpp",
        ])
        expected_header_files = sorted([
            "include/utils.h",
        ])
        print("\nDiscovered Source Files (in test) - BEFORE SORTING:", list(source_files)) # Print discovered source files BEFORE sorting
        print("\nDiscovered Source Files (in test):", sorted(source_files)) # Print discovered source files in test
        print("Expected Source Files (in test):", expected_source_files) # Print expected source files in test
        print("\nContents of sample_project_dir:", os.listdir(self.sample_project_dir)) # Print contents of sample_project_dir

        source_dir_contents = os.listdir(os.path.join(self.sample_project_dir, "src")) # List contents of src dir
        include_dir_contents = os.listdir(os.path.join(self.sample_project_dir, "include")) # List contents of include dir
        print("\nContents of source_dir:", source_dir_contents) # Print contents of source_dir
        print("\nContents of include_dir:", include_dir_contents) # Print contents of include_dir


        self.assertEqual(sorted(source_files), expected_source_files)
        self.assertEqual(sorted(header_files), expected_header_files)

    def test_extract_compile_info(self):
        compile_info = extract_compile_info(self.compile_commands_path, self.sample_project_dir)
        self.assertIn("src/main.cpp", compile_info)
        self.assertIn("src/utils.cpp", compile_info)

        main_cpp_info = compile_info["src/main.cpp"]
        self.assertIn("-I/home/fischeri/Projects/cpp_parser/tests/sample_project/include", main_cpp_info['compile_command'])

        utils_cpp_info = compile_info["src/utils.cpp"]
        self.assertIn("-I/home/fischeri/Projects/cpp_parser/tests/sample_project/include", utils_cpp_info['compile_command'])
import unittest
import os
from src.project_discovery import discover_project_files, generate_compile_commands, extract_compile_info

class TestProjectDiscovery(unittest.TestCase):

    def setUp(self):
        self.sample_project_dir = "tests/sample_project"
        # self.compile_commands_path = generate_compile_commands(self.sample_project_dir) # Skip compile_commands generation

    def test_discover_project_files(self):
        print("\nRunning test_discover_project_files...") # Add print statement at the beginning
        source_files, header_files = discover_project_files(self.sample_project_dir, compile_commands_path=None) # Pass None to skip compile_commands usage
        expected_source_files = sorted([
            "src/main.cpp",
            "src/utils.cpp",
        ])
        expected_header_files = sorted([
            "include/utils.h",
        ])
        print("\nDiscovered Source Files (in test) - BEFORE SORTING:", list(source_files)) # Print discovered source files BEFORE sorting
        print("\nDiscovered Source Files (in test):", sorted(source_files)) # Print discovered source files in test
        print("Expected Source Files (in test):", expected_source_files) # Print expected source files in test
        print("\nContents of sample_project_dir:", os.listdir(self.sample_project_dir)) # Print contents of sample_project_dir

        source_dir_contents = os.listdir(os.path.join(self.sample_project_dir, "src")) # List contents of src dir
        include_dir_contents = os.listdir(os.path.join(self.sample_project_dir, "include")) # List contents of include dir
        print("\nContents of source_dir:", source_dir_contents) # Print contents of source_dir
        print("\nContents of include_dir:", include_dir_contents) # Print contents of include_dir


        self.assertEqual(sorted(source_files), expected_source_files)
        self.assertEqual(sorted(header_files), expected_header_files)

    def test_extract_compile_info(self):
        compile_info = extract_compile_info(self.compile_commands_path, self.sample_project_dir)
        self.assertIn("src/main.cpp", compile_info)
        self.assertIn("src/utils.cpp", compile_info)

        main_cpp_info = compile_info["src/main.cpp"]
        self.assertIn("-I/home/fischeri/Projects/cpp_parser/tests/sample_project/include", main_cpp_info['compile_command'])

        utils_cpp_info = compile_info["src/utils.cpp"]
        self.assertIn("-I/home/fischeri/Projects/cpp_parser/tests/sample_project/include", utils_cpp_info['compile_command'])

if __name__ == '__main__':
    unittest.main()
