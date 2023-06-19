import tkinter
from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("To Do List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]

def add_Task():
    task= task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("D:\Python Projects\To_Do_list\Task_List.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def delete_task():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("D:\Python Projects\To_Do_list\Task_List.txt",'w') as taskfile1:
            for task in task_list:
                taskfile1.write(task+"\n")

def openTaskFile():
    try:
        global task_list
        with open ("D:\Python Projects\To_Do_list\Task_List.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file= open("D:\Python Projects\To_Do_list\Task_List.txt",'w')
        file.close()



 


#icon
root.iconbitmap("D:\Python Projects\To_Do_list\icon.ico")

#top bar
Top_bar_image = PhotoImage(file="D:\Python Projects\To_Do_list\images\img.png")
Label(root,image=Top_bar_image).pack()

#doc image
doc_image = PhotoImage(file="D:\Python Projects\To_Do_list\images\dock.png")
Label(root,image=doc_image,bg="#32405b").place(x=30,y=25)

#main

frame1 = Frame(root,width=400,height=50,bg="white")
frame1.place(x=0,y=180)

task=StringVar()
task_entry = Entry(frame1,width = 18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)

#button
button=Button(frame1,text="ADD",font="arial 20 bold" , width=6,bg="#5a95ff",fg="#fff",bd=0,command=add_Task)
button.place(x=300,y=0)

#listbox
frame2 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame2.pack(pady=(160,0))

listbox = Listbox(frame2,font=("arial",12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT ,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame2)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon=PhotoImage(file="D:\Python Projects\To_Do_list\images\delete.png")
Button(root,image=Delete_icon,bd=0,command=delete_task).pack(side=BOTTOM,pady=13)






root.mainloop()