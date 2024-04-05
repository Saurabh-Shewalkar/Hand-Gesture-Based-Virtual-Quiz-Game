import customtkinter as ctk

window = ctk.CTk()
window.title('Customtkinter app')
window.geometry('600x400')


label = ctk.CTkLabel(window, text='Registration page', font=("Arial", 20, "bold"), text_color="red")
label.pack()

label = ctk.CTkLabel(window, text='Enter your name :',font=("Arial", 14, "bold"))
label.place(x=100, y=50)

label = ctk.CTkLabel(window, text='Enter your Email :',font=("Arial", 14, "bold"))
label.place(x=100, y=100)

label = ctk.CTkLabel(window, text='Create a UserName :',font=("Arial", 14, "bold"))
label.place(x=100, y=150)

label = ctk.CTkLabel(window, text='Create a new Password :',font=("Arial", 14, "bold"))
label.place(x=100, y=200)

label = ctk.CTkLabel(window, text='Confirm Password :',font=("Arial", 14, "bold"))
label.place(x=100, y=250)

textBox = ctk.CTkTextbox(window, width=150, height=2)  # Adjust width and height as needed
textBox.place(x=300, y=50)  # Adjust x and y as needed

textBox = ctk.CTkTextbox(window, width=150, height=2)  # Adjust width and height as needed
textBox.place(x=300, y=100)

textBox = ctk.CTkTextbox(window, width=150, height=2)  # Adjust width and height as needed
textBox.place(x=300, y=150)

textBox = ctk.CTkTextbox(window, width=150, height=2)  # Adjust width and height as needed
textBox.place(x=300, y=200)

textBox = ctk.CTkTextbox(window, width=150, height=2)  # Adjust width and height as needed
textBox.place(x=300, y=250)

button = ctk.CTkButton(window, text="Submit")
button.place(x=200, y=320)

window.mainloop()
