from task import taskEntity

ArrayTask = []
whileStatus = True

while whileStatus:
  print("\n TODO LIST")
  print("1. Add Task")
  print("2. Update Task")
  print("3. Delete Task")
  print("4. Show Tasks")
  print("5. Find Task")
  print("6. Exit")
  choice = int(input("Enter your choice: "))

  ############################################
  # TODO LIST
  ############################################

  # ADD TASK
  if choice == 1:
    createTask = taskEntity(input("Enter Task Name: "), "Pending")
    ArrayTask.append(createTask)
    print("Task Added Successfully, Task ID:", createTask.task_id)

  #UPDATE TASK
  elif choice == 2:
    task_id = input("Enter Task ID: ")
    task_name = input("Enter Task Name: ")
    task_status = input("Enter Task Status: ")
    for task in ArrayTask:
      if task.task_id == task_id:
        task.update_task(task_name, task_status)
        print("Task Updated Successfully")

  #DELETE TASK
  elif choice == 3:
    task_id = input("Enter Task ID: ")
    for task in ArrayTask:
      if task.task_id == task_id:
        ArrayTask.remove(task)
        print("Task Deleted Successfully")
  
  #SHOW TASKS
  elif choice == 4:
    for task in ArrayTask:
      print(task)

  #FIND TASK
  elif choice == 5:
    task_id = input("Enter Task ID: ")
    for task in ArrayTask:
      if task.task_id == task_id:
        print(task)

  #EXIT
  elif choice == 6:
    print("Thank you for using TODO LIST!")
    whileStatus = False

  #INVALID CHOICE
  else: 
    print("Invalid Choice")
    continue

test = {"nome": "Rafael"}
newElementAge = test.add("idade", 25)