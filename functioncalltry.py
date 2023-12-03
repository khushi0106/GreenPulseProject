import jdoodle
response = jdoodle.compile_and_execute_code()
print("Compiled by jdoodle: ", response)

if response == True:
    import pylint
    lint_response = pylint.run_pylint()
    print("\nResponse from pylint: \n")
    print(lint_response)
       
    import psutillog
    util_cpu, util_cpucount, util_memory = psutillog.run_code_file()
    print("\nResponse from psutil: ")
    print("\nCPU Utilization per thread: ")
    print(util_cpu)
    print("\nCPU Thread Count: ")
    print(util_cpucount)
    print("\nMemory Utilization: ")
    print(util_memory)



"""
import pyRAPL
pyRAPL.setup(devices=None, socket_ids=None)

try:
    
    dataoutput= pyRAPL.outputs.DataFrameOutput()
    with pyRAPL.Measurement('bar',output=dataoutput):
        a=6
        b=19
        print(a,b)
  # ...
  # Instructions to be evaluated.
  # ...

    dataoutput.data.head()
    
except pyRAPL.PyRAPLCantRecordEnergyConsumption(devices=None) as e:
    print('error:', e)
          
result = measurement.result
print("Energy Consumption Results:")
print("Total Energy (Joules):", result.pkg)
print("Energy per Package Domain (Joules):", result.pkg_domain)
print("Energy per Dram Domain (Joules):", result.dram)
        
         


try:
    pyRAPL.begin()
    
    pyRAPL.end()
except Exception as e:
    print('error: ' + str(e))
    
    
    
measurement = pyRAPL.Measurement("SampleCode")
sensor = pyRAPL.DevicePackageDomain()

try:
    # Start energy consumption recording
    measurement.begin()

    # Run your sample code
    subprocess.check_output(["python", "samplecode.py"], text=True)

    # End energy consumption recording
    measurement.end()
finally: 
    # Access the energy consumption results
    result = measurement.result
    print("Energy Consumption Results:" , result)
    #print("Total Energy (Joules):", result.pkg)
    #print("Energy per Package Domain (Joules):", result.pkg_domain)
    #print("Energy per Dram Domain (Joules):", result.dram)


num = 11
# If given number is greater than 1
if num > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")

    """