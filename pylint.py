import subprocess

def run_pylint():
    
    filename="samplecode.py"
    command = f"pylint {filename}"
    
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output_lines = result.stdout.splitlines()
    return output_lines

# Example usage
#filename = "samplecode.py"
#pylint_output = run_pylint(filename)

# Now you can use 'pylint_output' as needed, such as displaying it on the frontend
#print(pylint_output)
