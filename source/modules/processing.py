 def multiproccess(tasks_to_process):
    processed_info = []
    for task in tasks_to_process:
        print(f"  Processing task: {task.name} ({task.task_type})")
        processed_info.append(task.getInfo())
    return processed_info
   
def active_tasks(tasks):
  for i range(tasks):
    pass
