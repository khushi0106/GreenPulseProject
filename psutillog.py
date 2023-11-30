import psutil
import subprocess

def run_code_file():
    # Run the code file as a subprocess
    file_path="samplecode.py"
    process = subprocess.Popen(['python', file_path])

    # Monitor resource usage while the process is running
    while process.poll() is None:
        # Get CPU and memory usage of the process
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        memory_info = psutil.virtual_memory()
        cpu_count1 = psutil.cpu_count()

        # Print or log the resource usage
        #print(f"CPU Usage: {cpu_percent}%")
        #print(f"cpu count= {cpu_count1}")
        #print(f"Memory Usage: {memory_info.percent}%")
        
    return cpu_percent, cpu_count1, memory_info.percent

    # Process has completed, get final resource usage
    # final_cpu_percent = psutil.cpu_percent(percpu=True)
    # final_memory_info = psutil.virtual_memory()

    #print(f"Final CPU Usage: {final_cpu_percent}%")
    #print(f"Final Memory Usage: {final_memory_info.percent}%")

# Replace 'your_code_file.py' with the path to your Python code file
#code_file_path = 'samplecode.py'

#run_code_file()