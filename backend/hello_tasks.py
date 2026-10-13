name = input("What's your name? ").strip()
print(f"Welcome to your first Python project, {name}!")

task_count = 0
tasks = []

for _ in range(3):
    task_name = input("Enter a task: ").strip()

    if not task_name:
        print("No task added")
    else:
        task_count += 1
        tasks.append(task_name) 

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print(f"Task count: {task_count}")
