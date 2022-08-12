# In this assignment you are going to create a TODO app.
# When the app starts it should present user with the following menu:

# Press 1 to add task
# Press 2 to delete task
# Press 3 to view all tasks
# Press q to quit

def menu():
    while True:

        print("""\n*******  To-Do List  *******
    Press 1 to add task
    Press 2 to delete task
    Press 3 to view all tasks
    Press q to quit""")

        userIn = input('Select an option : ')

        if userIn == '1':
            addTasks()
        elif userIn == '2':
            deleteTasks()
        elif userIn == '3':
            displayTasks()
        elif userIn.lower() == 'q':
            break
        else:
            print(' -- INVALID INPUT -- ')
            break


taskList = {'Name': [], 'Priority': []}
task = taskList['Name']
priority = taskList['Priority']

def addTasks():
    add = input('Enter task : ')
    task.append(add)

    prio = input('Enter priority (High, Medium, Low) : ')
    priority.append(prio)

def displayTasks():
    print(task, priority)
    # print(priority)

def deleteTasks():
    print(task)
    add = input('Enter a task to remove: ')
    task.remove(add)
    prio = taskList['Priority']
    priority.remove(prio)

menu()
























#         # adding a task
#         if prompt == 1:   
#             tasksIn = input('Enter task name : ')
#         for i in range(1, len(tasksIn)):
#                 tasks['name'] = i
#                 print(tasks['name'])
#                 break
            

#         priorityIn = input('Enter tasks priority : ')
#         priorityIn = tasks['Priority']

#         taskList .append(tasks)
#         print(taskList)
            
# # deleting a task

# view all tasks

# press Q to quit