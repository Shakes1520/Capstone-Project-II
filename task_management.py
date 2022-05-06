
#=====importing libraries===========
from datetime import date
from ast import Try
import datetime

def reg_user ():
 with open("test.txt","r") as reg_file:
  #data=reg_file.read()
  username=input("Please enter the username: ")
  password=input("Please enter the password: ")
  password_conf=input("Please confirm the password: ")
  preffered_password=not password.islower() and not password.isupper()
  usernames=[]
  passwords=[]
  for lines in reg_file:
     in_file_username,in_file_password=lines.split(",")
     in_file_password=in_file_password.strip()
     usernames.append(in_file_username)
     passwords.append(in_file_password)
  data=dict(zip(usernames,passwords))
  
 if password!=password_conf:
    print("Password, do not match please try again")
    reg_user()

 else:
   if username in usernames:
    print(f"The username {username} is already in use try a different username")
    reg_user()
   elif preffered_password==False:
    print("The password does not meet the requirements")
    print("You must at least have an uppercase and lower case")
    reg_user()
   elif any(map(str.isdigit,password))==False:
       print("Your Password must contain a number") 
       reg_user()
   elif len(password)<8:
     print("Your password is too short, please re-enter the password ")
     reg_user()
   else:
       print("Successfully registered!")
       with open ("test.txt","a") as reg_file:
        reg_file.write(username+","+password+"\n")
       reg_file.close()
 
def login_menu():
  username=input("Please enter the username: ")
  password=input("Please enter the password: ")

  passwords=[]
  usernames=[]
  with open ("test.txt","r") as login_file:
  
   for lines in login_file:
    in_file_username,in_file_password=lines.split(",")
    in_file_password=in_file_password.strip()
    usernames.append(in_file_username)
    passwords.append(in_file_password)
   data_dict=dict(zip(usernames,passwords))
   try:
      if data_dict[username]:
        try:
          if password==data_dict[username]:
            print(f"Access granted, welcome {username}")
            choice=input("""
                r  -  register user
                a  -  add task
                va -  view all task
                vm -  view my task
                gr -  generate reports
                ds -  display statistics
                e  -  exit
                            """)
            if choice=='r' or choice=='R':
              reg_user ()
            elif choice=='a' or choice=='A':
              add_task()
            elif choice=='va' or choice=='VA':
              view_all()
            elif choice=='vm' or choice=='VM':
              view_mine()
            elif choice=='gr' or choice=='GR':
              generate_reports()
            elif choice=='ds' or choice=='DS':
              display_stats()
          else:
            print("Incorrect username or password, please try again")
        except:
          print("Incorrect username or password, please try again!!")
      else:
        print("User not found in the user file")
   except:
       print("Invalid selection,please try again") 
  
def add_task():

  bool_test=True
  while bool_test:
    task_list=[]
    task_num=input("What task number are you adding: ")
    task_num=int(task_num)
    task_list.append(task_num)
    responsible_person=input("Enter the name of the person responsible for the task: ")
    #Prompting the user to enter the tiltle of the task
    task_title=input("Please enter title of the task: ")
    #Prompting the user to write to the description of the task
    task_descr=input("Please write the description of the task: ")
    #Getting the current date
    today=date.today()
    assign_date=str(today.strftime("%d-%b-%Y"))
    #Prompting the user to enter the due date of the task
    due_date=input("Please indicate the due date: ")
    #Prompting the user to enter the status of the task
    task_compl=input("Please by No or Yes the completion status of the task: ") 
    #Openning the text file
    with open("tasks.txt","a") as file:
      file.write(str(task_list)+","+str(task_title)+","+str(responsible_person)+","+str(assign_date)+","+str(due_date)+","+str(task_compl)+","+task_descr+"\n")
    file.close()
    loop_termination=input("Do you want to want to add more task, enter yes or no :")
    if loop_termination=='Yes' or loop_termination=='yes' or loop_termination=='YES':
      continue
    elif loop_termination=='No' or loop_termination=='no' or loop_termination=='NO':
      break   

def view_all():
  count=0
  with open("tasks.txt","r") as data:
         
    for info in data:  
       
      info=info.strip()   
      name=info.split(",")
            
      task_title=name[0]
      assigned_user=name[1]
      assigned_date=name[2]
      due_date=name[3]
      task_status=name[4]
      task_description=name[5]

      #Incrementing the count on every iteration  
      count+=1
      print(f"""Task number: {count}\nTask title: {task_title}\nAssign to: {assigned_user}\nAssigned date: {assigned_date}\nDue date: {due_date}\nTask complete? {task_status}\nTask description: {task_description}\n""") 
       
def view_mine():
   #Prompting the user to enter the assigned user
  responsible_user=input("Please enter the name of the responsible user: ")
  
  count = 0
  task_all_list = []
  task_list = []
  with open("tasks.txt","r") as data:
    file_content = data.readlines()
    
    for info in file_content:
      
      name=info.split(", ") 
      task_all_list.append(name)
      if responsible_user == name[1]:
        
        task_list.append(name)        
        task_title = name[0]
        assigned_user = name[1]
        assigned_date = name[2]
        due_date = name[3]
        task_status = name[4]
        task_description = name[-1]
        count+=1
        print(f"""Task number: {count}\nTask title: {task_title}\nAssign to: {assigned_user}\nAssigned date: {assigned_date}\nDue date: {due_date}\nTask complete? {task_status}\nTask description: {task_description}""")
    
    print("To return to the main menu, enter -1")
    #Pompting the user to enter the number of the line to be edited
    task_to_edit=int(input("Please enter the task you want to edit: "))

    if task_to_edit>=1:
        #Accessing the line to be edited by the user
      selected_task_to_edit = task_list[task_to_edit-1]    

      #Prompting the user to either enter mark or edit the line
      task_mark_status=input("Do you want to mark or edit the task? Enter (mark) to mark and (edit) to edit the task: ") 
    
      if task_mark_status=="Mark" or task_mark_status=="mark"or task_mark_status=="MARK": 
      
        #Prompting the user to write yes to mark the task status
        mark_status=input("Please enter Yes to mark the task complete: ")
        selected_task_to_edit[4]=mark_status

        #Oppening the text file write the edited data in the line
        with open("tasks.txt","w") as file_edit:
          for line in task_all_list:
            file_edit.write(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[-1]}")
    
      #Edidting the accessed line       
      elif task_mark_status=="Edit" or task_mark_status=="edit" or task_mark_status=="EDIT":
      
        #Prompting the either or not edit the assigned person
        assign_edit_option=input("Do you want to change the assigned person, enter yes/no: ")
      
        if assign_edit_option=='Yes' or assign_edit_option=='yes' or assign_edit_option=='YES':
          #Prompting the user to enter the name of the new person
          assign_new_person=input("Please enter the new person for the task: ")
          selected_task_to_edit[1]=assign_new_person

       #Oppening the text file write the edited data in the line 
          with open("tasks.txt","w") as file_edit:
            for line in task_all_list:
             file_edit.write(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[-1]}")
      
          #Editing the due date of the task
        due_data_edit_option=input("Do you want to change the due date, yes or no: ")
        if due_data_edit_option=="Yes" or due_data_edit_option=="yes" or due_data_edit_option=="YES":
        
          #Prompting the user to enter the new due date
          new_due_date=input("Please enter the new due date: ")
          selected_task_to_edit[3]=new_due_date

          #Openning the text file to write the edited information
          with open("tasks.txt","w") as file_edit:

            #Writing the edited information the text file
            for line in task_all_list:
              file_edit.write(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[-1]}")
    elif task_to_edit == -1:
        login_menu()

def user_overview():
  
  today = datetime.datetime.today()
  generated_task_count=0
  user_count=0
  task_all_list=[]
  user_assigned_tasks_count=0
  assigned_user_percantage=0
  completed_task_count=0
  incompleted_task_count=0
  completed_user_percantage=0
  over_due_task_count=0
  incompleted_user_percantage=0
  overdue_user_percentage=0
  with open("test.txt","r") as file:
    data=file.readlines()
    for line in data:
        user_count+=1
    print(f"There are {user_count} registered users")

  with open("tasks.txt","r") as file_task:
    data_tasks=file_task.readlines()
    for line in data_tasks:
        generated_task_count+=1
    print(f"There are {generated_task_count} generated tasks")
  #Prompting the user to enter the assigned user
  responsible_user=input("Please enter the name of the user you want to check: ")
  with open("tasks.txt","r") as data:
    #Reading the content of the text file
    file_content = data.readlines()
    for info in file_content:
      #Adding the content in the list
      task_all_list.append(info)
      #Splitting the content by the comma 
      name=info.split(", ") 
      #Checking the lines with the prompted assigned user
      if responsible_user==name[1]:
          user_assigned_tasks_count+=1
          task_title=name[4]
        # Accessing each comma seperated data in the text file    
          if task_title=='Yes' or task_title=='yes':
            completed_task_count+=1
          elif task_title=='No' and datetime.datetime.strptime(name[3].strip(), '%d-%m-%Y') > today :
            incompleted_task_count+=1
          elif datetime.datetime.strptime(name[3].strip(), '%d-%m-%Y') < today and task_title=='No':
            over_due_task_count+=1
    assigned_user_percantage=(user_assigned_tasks_count/user_count)*100
    print(user_assigned_tasks_count)
    print(f"User task percentage is {assigned_user_percantage}")
    
    print(f"{responsible_user} have {completed_task_count}  completed task(s) ")
    completed_user_percantage = (completed_task_count/user_assigned_tasks_count)*100
    completed_user_percantage = round(completed_user_percantage,2)
    print(f"Completed user task percentage is {completed_user_percantage} %")
    incompleted_user_percantage = (incompleted_task_count/user_assigned_tasks_count)*100
    incompleted_user_percantage = round(incompleted_user_percantage,2)
    print(f"Still to be task percentage is {incompleted_user_percantage} %")
    overdue_user_percentage = (over_due_task_count/user_assigned_tasks_count)*100
    overdue_user_percentage = round(overdue_user_percentage,2)
    print(f"Overdue task(s) percentage is {overdue_user_percentage} %")

  with open("user_overview.txt","a") as file:
    file.write(str(user_count)+", "+str(generated_task_count)+", "+str(user_assigned_tasks_count)+", "+str(assigned_user_percantage)+", "+str(completed_user_percantage)+", "+str(incompleted_user_percantage)+", "+str(overdue_user_percentage)+"\n")

def task_overview():
  today = datetime.datetime.today()
  over_due_task_count=0
  incomplete_task_count=0
  completed_task_count=0
  task_count=0
  with open("tasks.txt", "r") as f:
    for line in f:
      value = line.split(", ")
      task_count+=1
      if value[-2] == "No":
        incomplete_task_count+=1
        if datetime.datetime.strptime(value[3].strip(), '%d-%m-%Y') < today:
                over_due_task_count+=1
        elif value[-2] == 'Yes':
          completed_task_count+=1
    print(f"The tasks are {task_count}") 
    print(f"Complete  tasks are {completed_task_count}")
    print(f"Uncompleted  tasks are {incomplete_task_count}")
    print(f"Over due tasks are {over_due_task_count}")

    incomplete_percentage = (incomplete_task_count/task_count)*100
    incomplete_percentage = round(incomplete_percentage,2)
    print(f"Uncompleted task percentage is {incomplete_percentage} %")

    over_due_percentage = (over_due_task_count/task_count)*100
    over_due_percentage = round(over_due_percentage,2)
    print(f"Over due task percentage is {over_due_percentage} %")
    with open ("task_overwrite.txt","a") as file: 
      file.write(str(task_count)+", "+str(completed_task_count)+", "+str(incomplete_task_count)+", "+str(over_due_task_count)+",          "+str(incomplete_percentage)+", "+str(over_due_percentage)+'\n')
   
def generate_reports():

  user_overview()
  print("\n")
  task_overview()
  print("Done generating the reports, thank you!!")
 
def display_stats():

  print("Task overview report:")
  with open("task_overwrite.txt","r") as file:
    data = file.readlines()
    for lines in data:
      lines=lines.split(", ")
      print(f"The total numbers of generated tasks : {lines[0]} ")
      print(f"The total number of completed tasks: {lines[1]} ")
      print(f"The total number of uncompleted tasks: {lines[2]}")
      print(f"The total number of tasks that have not been completed and that are overdue {lines[3]}")
      print(f"The percentage of tasks that are incomplete: {lines[4]}%")
      print(f"The percentage of tasks that are overdue {lines[5]}%")
  print("\n")   
  print("User overview report:")
  with open("user_overview.txt","r") as file:
      data=file.readlines()
      for lines in data:
        lines=lines.split(", ")
        print(f"The total number of users registered: {lines[0]} ")
        print(f"The total number of tasks that have been generated and tracked: {lines[1]} ")
        print(f"The total number of tasks assigned to that user: {lines[2]}")
        print(f"The  percentage of the total number of tasks have been assigned to that user?: {lines[3]}%")
        print(f"The percentage of the tasks assigned to that user have been completed: {lines[4]}%")
        print(f"The percentage of the tasks assigned to that user must still be completed?: {lines[5]}%")
        print(f"The percentage of the tasks assigned to that user have not yet been completed and are overdue: {lines[6]}%")

        
 
login_menu()




