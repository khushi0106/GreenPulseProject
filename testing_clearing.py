def clear_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write('')
        print(f'The file {file_path} has been cleared.')
    except Exception as e:
        print(f'An error occurred while clearing the file {file_path}: {str(e)}')

# Example usage
file_path = 'requirements.txt'
clear_file(file_path)
