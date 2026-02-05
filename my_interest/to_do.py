""""
This program take input from the user
TO do list for day.
After completing it will remove from the list

"""
task={}

def add_to_list(data):
        task[len(task)]=data
def delete_task(unique):
    if unique in task:
        task.pop(unique)
        temp={}
        for i,val in enumerate(task.values()):
            temp[i]=val
        task.clear()
        task.update(temp)
        print("Task Removed")
    else:
        print("Task Not Found")
def display_task():
    for key,val in task.items():
        print("---------------------------")
        print(f"{ key }| { val }")
start_task= True
while start_task:
    user_tsk= input(" Add the task. Type yes  \n or To remove the task Type rm  \n or To close the app Type No \n To display task Type Display or dis :").lower()
    if user_tsk=='yes':
        data =input("Enter the task ")
        add_to_list(data)
    elif user_tsk=='rm':
        print(task)
        print("which task need to remove pls enter task number ")
        user_delete_tsk =int(input("enter the number to delete the task "))
        delete_task(user_delete_tsk)
    elif user_tsk=='dis' or user_tsk=='display':
        display_task()
    else:
        print("Have Great Day")
        start_task=False
