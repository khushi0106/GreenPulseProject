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
        memory_info = psutil.virtual_memory().percent
        cpu_count1 = psutil.cpu_count()
        
        #cpu_times_per = psutil.cpu_times_percent()
        #cpu_times_per_user=psutil.cpu_times_percent().user 
        cpu_times_per_system=psutil.cpu_times_percent().system
        
       
        disk_usage=psutil.disk_usage('/').percent
        disk_io=psutil.disk_io_counters()
        disk_part=psutil.disk_partitions()
        load_avg = psutil.getloadavg()
        net_connection=psutil.net_connections()
        net_if=psutil.net_if_addrs()
        net_if_stats=psutil.net_if_stats()
        net_io_counter=psutil.net_io_counters()
        
        # Print or log the resource usage
        print(f"CPU Usage: {cpu_percent}%")
        print(f"cpu count= {cpu_count1}")
        print(f"Memory Usage: {memory_info}%")
        
        #print(f" CPU times percentage: {cpu_times_per}%")
        #print(f"User CPU times percentage: {cpu_times_per_user}%")
        print(f"System CPU times percentage: {cpu_times_per_system}%")
       
        print(f"disk usage: {disk_usage}%")
        print(f"disk io counters: {disk_io}%")
        print(f"disk partitions: {disk_part}%")
        print(f"Load average: {load_avg}%")
        #print(f"net connections: {net_connection}%")
        #print(f"net if address: {net_if}%")
        print(f"net if stats: {net_if_stats}%")
        print(f"net io counter: {net_io_counter}%")
        
    return cpu_percent, cpu_count1, memory_info, cpu_times_per_system, disk_usage

    # Process has completed, get final resource usage
    # final_cpu_percent = psutil.cpu_percent(percpu=True)
    # final_memory_info = psutil.virtual_memory()

    #print(f"Final CPU Usage: {final_cpu_percent}%")
    #print(f"Final Memory Usage: {final_memory_info.percent}%")

# Replace 'your_code_file.py' with the path to your Python code file
#code_file_path = 'samplecode.py'

#run_code_file()