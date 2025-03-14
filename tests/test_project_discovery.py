import unittest
import os
from src.project_discovery import discover_project_files, generate_compile_commands, extract_compile_info

class TestProjectDiscovery(unittest.TestCase):

    def setUp(self):
        self.sample_project_dir = "tests/sample_project"
        self.compile_commands_path = generate_compile_commands(self.sample_project_dir)

    def test_discover_project_files(self):
        source_files, header_files = discover_project_files(self.sample_project_dir)
        expected_source_files = sorted([
            "src/main.cpp",
            "src/utils.cpp",
        ])
        expected_header_files = sorted([
            "include/utils.h",
        ])
        self.assertEqual(sorted(source_files), expected_source_files)
        self.assertEqual(sorted(header_files), expected_header_files)
        print("\nDiscovered Source Files (in test):", sorted(source_files)) # Print discovered source files in test
        print("Expected Source Files (in test):", expected_source_files) # Print expected source files in test

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
