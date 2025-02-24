def is_teacher_suspicious(n, tasks):
    visited_tasks = set()
    last_task = None  # Keep track of the last solved task

    for task in tasks:
        if task != last_task:  # We switched to a new task
            if task in visited_tasks:  # If it's already completed before, return NO
                return "NO"
            visited_tasks.add(task)  # Mark the task as completed
        last_task = task  # Update the last task

    return "YES"

# Read input
t = int(input().strip())  # Number of test cases
for _ in range(t):
    n = int(input().strip())  # Number of days
    tasks = input().strip()  # Task sequence
    print(is_teacher_suspicious(n, tasks))
