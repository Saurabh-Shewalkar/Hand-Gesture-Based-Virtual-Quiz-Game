from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pyodbc
import os


def call_other_script():
    # Add code to call another script (if needed)
    login_window.destroy()
    os.system('python HomePage.py')

def signup_page():
    os.system('python DatabaseRegestration.py')


def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    os.environ['user'] = usernameEntry.get()


    # Establish a connection to the database
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=DESKTOP-4AA8FNG;DATABASE=kaustubh;UID=sa;PWD=kau12345')
        cursor = connection.cursor()

        # Execute a query to check if the username and password exist in the users table
        cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (username, password))
        row = cursor.fetchone()

        if row:
            # messagebox.showinfo("Login Successful", "Welcome!")
            call_other_script()  # Call another script upon successful login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

        connection.close()
    except pyodbc.Error as e:
        messagebox.showerror("Database Error", f"Error: {str(e)}")

#functionality part

def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0,END)


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

# storing Login Info




# GUI Part
login_window = Tk()
login_window.geometry('990x620+50+50')
login_window.resizable(0,0)
login_window.title('Login page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

Title = Label(login_window, text='Virtual Quiz Platform', font=('Helvetica',28,'bold'),
              bg='#FFEEDC', fg='firebrick1')
Title.place(x=130, y=120)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light',23,'bold'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light',11,'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light',11,'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Microsoft Yahei UI Light',9,'bold'), fg='firebrick1', activeforeground='firebrick1')
forgetButton.place(x=715, y=310)

loginButton = Button(login_window, text='Login', font=('Open Sans',16,'bold'),
                     fg='white', bg='firebrick1', activebackground='firebrick1',
                     activeforeground='white', cursor='hand2', bd=0, width=19, command=login)
loginButton.place(x=578, y=370)

signupLabel = Label(login_window, text='Don\'t have an account?',font=('Open Sans',9,'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=590, y=450)

newaccountButton = Button(login_window, text='Create new one', font=('Open Sans',9,'bold underline'),
                     fg='black', bg='white', activebackground='white',
                          cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=727, y=450)

login_window.mainloop()