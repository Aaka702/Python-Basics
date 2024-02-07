file_path = 'example.txt'

with open(file_path, 'r') as file:
    # Read the content of the file
    file_content = file.read()

print(f"Content of '{file_path}':\n{file_content}")
