## Data Lineage

Ability to trace data from final output back to original source.

Example:

Gold
↓
Silver
↓
Bronze
↓
Raw JSON

Benefits:
- Auditing
- Debugging
- Compliance
- Root cause analysisyes


Spark is not used because a company is large.

Spark is used when a single machine becomes a bottleneck for data processing.

Choose the simplest solution that meets current requirements while keeping future scalability in mind.


Transformation
Operation that creates a new DataFrame but does not immediately execute.

Examples:
filter, select, join, groupBy

Action
Operation that triggers Spark execution.

Examples:
show, count, write, collect

Lazy Evaluation
Spark delays execution until an action is called.

Catalyst Optimizer
Spark component that optimizes execution plans.


DAG (Directed Acyclic Graph)

A graph representing Spark execution steps.

Spark builds a DAG from transformations and executes it only when an action is called.

Example:

Read CSV
   ↓
Filter
   ↓
Select
   ↓
Write


Narrow Transformation

Transformation where each partition can be processed independently.

Examples:
filter
select
withColumn

No shuffle required.

Wide Transformation

Transformation requiring data movement across executors.

Examples:
groupBy
join
distinct
orderBy

Requires shuffle and is expensive.

Shuffle

Movement of data between executors during execution.


Cache

Stores DataFrame in memory for reuse.

Used when a DataFrame is accessed multiple times.

Improves performance by avoiding recomputation.

Spark cache is lazy and becomes effective only after an action.

Persistence

Mechanism to store DataFrames in memory or disk.

Common methods:

cache()
persist()


Job

Created whenever an action is executed.

Examples:
show()
count()
write()

Stage

A phase of execution.
New stages are created at shuffle boundaries.

Task

Smallest execution unit in Spark.
One task processes one partition.

Rule:
One Partition = One Task