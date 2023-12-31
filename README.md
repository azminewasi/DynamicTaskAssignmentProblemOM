# Mathematical Formulation and Implementation of Dynamic Task Assignment Problem in 10 Minute School
Code and definition of a dynamic task assignment problem (Mathematical Formulation and Implementation of Dynamic Task Assignment Problem in 10 Minute School) for Operations Management Lab.

# **Problem Description:**
An experienced operations manager is responsible for assigning tasks to a team of six workers (workers 1 to 6) to maximize the output level. Each day, he receives a list of tasks with various characteristics, including task type, count, priority, urgency, time requirement, and quality scores of workers for each task type. The goal is to efficiently assign these tasks to workers while considering their availability, task counts, and the importance of the tasks.

# **Mathematical Formulation:**

## **Indices:**
- $i$: Index for workers, $i \in \{1, 2, 3, 4, 5, 6\}$.
- $j$: Index for tasks, $j \in \{1, 2, \ldots, N\}$, where $N$ is the total number of tasks.

## **Parameters:**
- $T_j$: Task type of task $j$.
- $C_j$: Count of task $j$.
- $P_j$: Priority of task $j$.
- $U_j$: Urgency of task $j$.
- $Q_{ij}$: Quality score of worker $i$ for task type $T_j$.
- $R_j$: Time requirement for task $j$.
- $H_i$: Available working hours per worker $i$.

## **Variables:**
- $X_{ij}$: Binary decision variable indicating whether task $j$ is assigned to worker $i$.

## **Objective Function:**
The objective is to maximize the total output level, which is calculated as the sum of quality scores for each assigned task, weighted by its priority and urgency. The higher the quality score, priority, and urgency, the more critical the task, and it contributes more to the total output level.


$\text{Maximize: } \sum_{i=1}^{6} \sum_{j=1}^{N} X_{ij} \cdot Q_{ij} \cdot P_j \cdot U_j$


This objective function reflects the primary goal of maximizing the overall performance by efficiently assigning tasks to workers based on their quality scores and task characteristics.

## **Constraints:**

1. **Task Assignment Constraint:**
Each task $j$ can be assigned at most once. This constraint ensures that a task is either assigned to a worker or left unassigned.

$\sum_{i=1}^{6} X_{ij} \leq 1 \quad \forall j \in \{1, 2, \ldots, N\}$

2. **Worker Availability Constraint:**
Each worker $i$ can work at most $H_i$ hours per day. This constraint ensures that workers do not exceed their available working hours.

$\sum_{j=1}^{N} X_{ij} \cdot R_j \leq H_i \quad \forall i \in \{1, 2, 3, 4, 5, 6\}$

3. Task Count Constraint:**
Ensure that the total assigned count of each task $j$ matches its given count. This constraint ensures that the assigned task count matches the provided task count for each task type.

$\sum_{i=1}^{6} X_{ij} \cdot C_j = C_j \quad \forall j \in \{1, 2, \ldots, N\}$

**Binary Variable:**

The decision variable $X_{ij}$ is binary and takes a value of 1 if task $j$ is assigned to worker $i$ and 0 if it is not assigned.

# **Explanation:**
This mathematical formulation addresses the operational challenge of assigning tasks to workers to maximize productivity. The objective function seeks to maximize the output level, which is a combination of the quality scores, task priorities, and urgencies. By optimizing these factors, you can ensure that the most important and time-critical tasks are assigned to the most skilled workers.
The constraints ensure that tasks are not over-allocated, workers do not exceed their working hours, and the assigned task counts match the given counts. This formulation strikes a balance between productivity and resource constraints.
Solving this optimization problem will lead to task assignments that achieve the highest possible output level, ultimately improving the operational efficiency of your team.


## Citation
```
@misc{ wasiDAP2023,
title = {Mathematical Formulation and Implementation of Dynamic Task Assignment Problem in 10 Minute School},
author = {Azmine Touhsik Wasi and Anisha Ahmed and Mahir Absar Khan and Abdur Rahman and Rahatun Nesa Priti},
year = {2023},
url = {https://github.com/azminewasi/DynamicTaskAssignmentProblemOM}
}
```
