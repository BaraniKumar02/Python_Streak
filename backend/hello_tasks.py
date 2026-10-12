name = input("What's your name? ").strip()
print(f"Welcome to your first Python project, {name}!")

task_count = 0

for _ in range(3):
    task_name = input("Enter a task: ").strip()

    if not task_name:
        print("No task added")
    else:
        task_count += 1
        print(f"Task added: {task_count}. {task_name.upper()}")

print(f"Task count: {task_count}")
