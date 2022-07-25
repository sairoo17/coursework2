from tkinter import *
from PIL import ImageTk, Image
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb
from functools import partial

# Major functions of file manager

# open a file box window 
# when we want to select a file
def open_window():
    return easygui.fileopenbox(filetypes = ['*.txt',"*.py", "*.csv", "*.jpeg", "*.jpg", "*.png"])

# open file function
def open_file():
    filepath = open_window()
    
    try:
        os.system("open " + filepath)
    except:
        mb.showinfo('confirmation', "File not found!")

# copy file function
def copy_file():
    source117 = open_window()
    destination117=filedialog.askdirectory()
    shutil.copy(source117,destination117)
    mb.showinfo('confirmation', "File Copied !")

# delete file function
def delete_file():
    dele_file = open_window()
    if os.path.exists(dele_file):
        os.remove(dele_file)             
    else:
        mb.showinfo('confirmation', "File not found !")

# rename file function
def rename_file():
    choosenFile = open_window()
    path17 = os.path.dirname(choosenFile)
    extension=os.path.splitext(choosenFile)[1]
    print("Enter new name for the chosen file")
    newName1=input()
    path = os.path.join(path17, newName1+extension)
    print(path)
    os.rename(choosenFile,path) 
    mb.showinfo('confirmation', "File Renamed !")

# move file function
def move_file():
    source1 = open_window()
    destination1 =filedialog.askdirectory()
    if(source1==destination1):
        mb.showinfo('confirmation', "source1 and destination1 are same")
    else:
        shutil.move(source1, destination1)  
        mb.showinfo('confirmation', "File Moved !")

# function to make a new folder
def make_folder():
    newFolder1Path = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder1=input()
    path = os.path.join(newFolder1Path, newFolder1)  
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")

# function to remove a folder
def remove_folder():
    delFolder1 = filedialog.askdirectory()
    os.rmdir(delFolder1)
    mb.showinfo('confirmation', "Folder Deleted !")

# function to list all the files in folder
def list_files():
    folderList1 = filedialog.askdirectory()
    sortlist1=sorted(os.listdir(folderList1))       
    i=0
    print("Files in ", folderList1, "folder are:")
    while(i<len(sortlist1)):
        print(sortlist1[i]+'\n')
        i+=1

def access_fm():
    new= Toplevel(root)

    Button(new, text = "Open a File", command = open_file).grid(row=15, column =2)

    Button(new, text = "Copy a File", command = copy_file).grid(row = 25, column = 2)

    Button(new, text = "Delete a File", command = delete_file).grid(row = 35, column = 2)

    Button(new, text = "Rename a File", command = rename_file).grid(row = 45, column = 2)

    Button(new, text = "Move a File", command = move_file).grid(row = 55, column =2)

    Button(new, text = "Make a Folder", command = make_folder).grid(row = 75, column = 2)

    Button(new, text = "Remove a Folder", command = remove_folder).grid(row = 65, column =2)

    Button(new, text = "List all Files in Directory", command = list_files).grid(row = 85,column = 2)


def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    if username.get() == "admin" and password.get() == "admin":
        access_fm()

#Creating the UI of our file manager

root = Tk()

root.geometry('400x150')  
root.configure(bg='red')
root.title('File Manager Login')

#username label and text entry box
username_label = Label(root, text="User Name", bg='#fff').grid(row=0, column=0)
username = StringVar()
username_entry = Entry(root, textvariable=username, fg='#fff').grid(row=0, column=1)  

#password label and password entry box
password_label = Label(root,text="Password", bg='#fff').grid(row=1, column=0)  
password = StringVar()
password_entry = Entry(root, textvariable=password, show='*', fg='#fff').grid(row=1, column=1)  

validate_login = partial(validateLogin, username, password)

#login button
login_button = Button(root, text="Login", command=validate_login).grid(row=4, column=0)  
root.mainloop()

