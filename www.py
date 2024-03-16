import re

def remove_comments(file_path):
    try:
        with open('in.text', 'r') as file:
            content = file.read()

            # Use regular expression to remove both single-line and multi-line comments
            content_without_comments = re.sub(r'//.*?$|/\*.*?\*/', '', content, flags=re.MULTILINE | re.DOTALL)

        
            file.write(content_without_comments)

        print(f"Comments removed successfully from {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
cpp_file_path = 'path/to/your/file.cpp'
remove_comments(cpp_file_path)
