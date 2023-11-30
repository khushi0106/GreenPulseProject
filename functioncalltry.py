import jdoodle
response = jdoodle.compile_and_execute_code()
print(response)

if response == True:
    import pylint
    lint_response = pylint.run_pylint()
    print(lint_response)
       
    import psutillog
    util_cpu, util_cpucount, util_memory = psutillog.run_code_file()
    print(util_cpu, util_cpucount, util_memory)
               


