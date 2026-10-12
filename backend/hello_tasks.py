name = input()

print("Welcome to First Python Chapter :..." + name)

task_name = input()
task_count = 0

for i in range(3):
    task_name = input()
    
    if task_name == "null" or task_name == "":
        print("No task added")
    else:
        task_count += 1
        print("Task added :..." + str(task_count) + "." + task_name.upper())
        


print("Task Count:.." + str(task_count))
