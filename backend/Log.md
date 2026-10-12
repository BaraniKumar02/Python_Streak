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

## Lessons Learned
- Always use `or` when checking multiple possible values for the same variable.
- Use `str()` to convert numbers before string concatenation.
- Increment counters **before** using them if you want 1-based numbering.
- Use the correct file name, path, and command (`python`) to run scripts.
