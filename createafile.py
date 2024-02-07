file_path = 'example.txt'

# You can specify the full path if needed, like 'C:/path/to/your/directory/example.txt'

with open(file_path, 'w') as file:
    # Write content to the file
    file.write("Hello, this is a sample text!")

print(f"File '{file_path}' created successfully.")