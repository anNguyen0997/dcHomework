# In this assignment you are going to create a TODO app.
# When the app starts it should present user with the following menu:

# Press 1 to add task
# Press 2 to delete task
# Press 3 to view all tasks
# Press q to quit

prompt = int(input("""Press 1 to add task
Press 2 to delete task
Press 3 to view all tasks
Press q to quit  
 :  """))

taskList = []
tasks = {'Name : ', 'Priority : '}
nameOfTask = ""
taskPriority = ""

if prompt == 1:
    print('Enter task name : ')
    nameOfTask = tasks['Name']
    
