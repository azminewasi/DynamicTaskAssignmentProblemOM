import pandas as pd

# Define task time requirements
task_time_requirements = {
    1: 4,
    2: 6,
    3: 1,
    4: 5,
    5: 2,
    6: 3
}

# Define the quality scores for each worker and task type
quality_df = pd.read_csv("Worker Performance Mattrix.csv") # With columns - task,worker1,worker2,worker3,worker4,worker5,worker6
quality_df = quality_df.drop(columns='task')

# Define available working hours per worker
available_hours_per_worker = 8

# Define the list of tasks with their counts, priorities, and urgencies
tasks_df = pd.read_csv("Assigned Tasks.csv") # With columns - task_no,task_type,count,priority,urgency

# Initialize a dictionary to track assigned tasks and free time per worker
assigned_tasks = {worker: [] for worker in quality_df.columns}
free_time_per_worker = {worker: available_hours_per_worker for worker in quality_df.columns}

# Sort tasks by priority (descending), urgency (descending), and time requirement (ascending)
tasks_df = tasks_df.sort_values(by=["priority", "urgency", "task_type"], ascending=[False, False, True])

# Create a dictionary to keep track of task counts for each unique combination of task type, priority, and urgency
given_task_counts = {}

# Loop through tasks and assign them to workers to maximize output level
for _, row in tasks_df.iterrows():
    task_type = row["task_type"]
    task_no = row["task_no"]
    priority = row["priority"]
    urgency = row["urgency"]

    # Check if the task type, priority, and urgency combination is in the given_task_counts dictionary
    key = (task_type, priority, urgency)
    if key in given_task_counts:
        count = given_task_counts[key]
    else:
        count = row["count"]
        given_task_counts[key] = count

    time_required = task_time_requirements[task_type]

    # Sort workers by quality score for the given task type
    sorted_workers = quality_df.columns.to_list()
    sorted_workers.sort(key=lambda worker: -quality_df.at[task_type, worker])

    # Try to assign the task to available workers
    for worker in sorted_workers:
        for worker in sorted_workers:
            if count > 0 and free_time_per_worker[worker] >= time_required:
                assigned_tasks[worker].append((task_no, task_type, time_required, priority, urgency))
                free_time_per_worker[worker] -= time_required
                count -= 1

# Calculate the total output level
total_output_level = 0
for worker, tasks in assigned_tasks.items():
    for task_no, task_type, time_required, priority, urgency in tasks:
        quality_score = quality_df.at[task_type, worker]
        output_level = quality_score * 1 * urgency * priority
        total_output_level += output_level

printed_lines=[]
# Print the assigned tasks and free time per worker
print("Assigned Tasks:")
for worker, tasks in assigned_tasks.items():
    if tasks:
        for task_no, task_type, time_required, priority, urgency in tasks:
            task_count = assigned_tasks[worker].count((task_no, task_type, time_required, priority, urgency))
            line = f"Worker {worker[-1]} - Task No: {task_no}, Task Type: {task_type}, Assigned: {task_count} - Time Required: {task_count * task_time_requirements[task_type]}"
            if line not in printed_lines:
                print(line)
                printed_lines.append(line)

print("\nFree Time per Worker:")
for worker, time in free_time_per_worker.items():
    print(worker, ":", time)

print("\nTotal Output Level:", total_output_level)

assigned_tasks_all = [item for sublist in assigned_tasks.values() for item in sublist]

# Calculate and print unassigned tasks
unassigned_tasks = []
for _, row in tasks_df.iterrows():
    task_no = row["task_no"]
    task_type = row["task_type"]
    priority = row["priority"]
    urgency = row["urgency"]
    given_count = given_task_counts[(task_type, priority, urgency)]
    assigned_count = sum(1 for (tn, _, _, p, u) in assigned_tasks_all if tn == task_no)
    unassigned_count = given_count - assigned_count
    unassigned_tasks.append((task_no,task_type, priority, urgency, given_count, assigned_count, unassigned_count))
    
sorted_unassigned_tasks = sorted(unassigned_tasks, key=lambda x: x[0])
print("\nUnassigned Tasks:")
for task_no,task_type, priority, urgency, given, assigned, unassigned in sorted_unassigned_tasks:
    print(f"Task No: {task_no}, Task Type: {task_type}, Priority: {priority}, Urgency: {urgency}, Given: {given}, Assigned: {assigned}, Unassigned: {unassigned}")
