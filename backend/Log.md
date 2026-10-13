# 📝 Exercise Log — hello_tasks.py

## Issues Faced

### 1. Logical Operator: `and` vs `or`
- **Problem:** Used `and` in the condition `if task_name == "null" and task_name == ""` — this can never be `True` because a string can't be both `"null"` and `""` at the same time.
- **Fix:** Changed `and` to `or`.
```diff
- if task_name == "null" and task_name == "":
+ if task_name == "null" or task_name == "":
```

### 2. Type Error: Concatenating `int` with `str`
- **Problem:** `task_count` is an integer, so `"Task Count:.." + task_count` raises a `TypeError`.
- **Fix:** Wrapped `task_count` with `str()`.
```diff
- print("Task Count:.." + task_count)
+ print("Task Count:.." + str(task_count))
```

### 3. Numbered List Starting at 0 Instead of 1
- **Problem:** `task_count` was printed before being incremented, so the first task was numbered `0`.
- **Fix:** Moved `task_count += 1` before the `print` statement.
```diff
- print("Task added :..." + str(task_count) + "." + task_name.upper())
- task_count += 1
+ task_count += 1
+ print("Task added :..." + str(task_count) + "." + task_name.upper())
```

### 4. Running the Script — Wrong Command
- **Problem:** Used `run hello_task.py` which is not a valid command.
- **Fix:** Use `python` to run Python scripts.
```diff
- run hello_task.py
+ python backend/hello_tasks.py
```

### 5. File Name Typo
- **Problem:** Ran `python hello_task.py` — missing the **s** in `hello_tasks.py`.
- **Fix:** Use the correct file name `hello_tasks.py`.

### 6. File Path Missing `backend/` Folder
- **Problem:** Ran from the workspace root without specifying the `backend/` subdirectory.
- **Fix:** Include the folder path: `python backend/hello_tasks.py`.

---

## Refactoring — `Updated Code with refactoring` (commit `1270a10`)

### 7. Missing Input Prompts
- **Problem:** All `input()` calls had no prompt string, so the user sees a blank cursor with no idea what to type.
- **Fix:** Added descriptive prompts and `.strip()` to clean whitespace.
```diff
- name = input()
+ name = input("What's your name? ").strip()
```
```diff
-     task_name = input()
+     task_name = input("Enter a task: ").strip()
```

### 8. String Concatenation → f-strings
- **Problem:** Used `+` concatenation with manual `str()` casts — harder to read and error-prone.
- **Fix:** Replaced with f-strings throughout.
```diff
- print("Welcome to First Python Chapter :..." + name)
+ print(f"Welcome to your first Python project, {name}!")
```
```diff
-         print("Task added :..." + str(task_count) + "." + task_name.upper())
+         print(f"Task added: {task_count}. {task_name.upper()}")
```
```diff
- print("Task Count:.." + str(task_count))
+ print(f"Task count: {task_count}")
```

### 9. Pythonic Empty-String Check
- **Problem:** `if task_name == "null" or task_name == ""` is verbose and the `"null"` check is unnecessary.
- **Fix:** Used `if not task_name` which is the idiomatic Python way to test for empty/blank strings.
```diff
-     if task_name == "null" or task_name == "":
+     if not task_name:
```

### 10. Removed Wasted `input()` Before the Loop
- **Problem:** There was a standalone `task_name = input()` before the loop that captured input but was immediately overwritten inside the loop — wasted input.
- **Fix:** Removed the redundant `input()` call.
```diff
- task_name = input()
  task_count = 0
```

### 11. Unused Loop Variable
- **Problem:** `for i in range(3)` — `i` is never used inside the loop.
- **Fix:** Replaced with `_` to signal an intentionally unused variable.
```diff
- for i in range(3):
+ for _ in range(3):
```

---

## Fix — `day 1: fix wasted input, use f-strings` (commit `81cfcca`)

### 12. Tasks Not Stored — Only Printed Inline
- **Problem:** Each task was printed immediately with `print(f"Task added: …")` but never stored, so there was no way to display a summary list at the end.
- **Fix:** Added a `tasks` list, appended valid tasks to it, and used `enumerate` to print a numbered summary.
```diff
  task_count = 0
+ tasks = []
```
```diff
-         print(f"Task added: {task_count}. {task_name.upper()}")
+         tasks.append(task_name)
+
+ for number, task in enumerate(tasks, start=1):
+     print(f"{number}. {task}")
```

---

## Lessons Learned
- Always use `or` when checking multiple possible values for the same variable.
- Use `str()` to convert numbers before string concatenation.
- Increment counters **before** using them if you want 1-based numbering.
- Use the correct file name, path, and command (`python`) to run scripts.
- Add **prompt strings** to `input()` so users know what to type.
- Use **f-strings** instead of `+` concatenation — they're cleaner and avoid `TypeError`.
- Use `.strip()` on user input to handle accidental whitespace.
- Use `if not value` for empty-string checks — it's the Pythonic way.
- Remove dead code (unused variables, wasted `input()` calls).
- **Store data in a list** when you need to process or display it later, rather than printing inline.
- Use `enumerate(list, start=1)` for clean 1-based numbered output.
