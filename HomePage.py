import tkinter as tk
from PIL import Image, ImageTk
import os

def call_other_script():
    os.system("python HandCode.py")

value = os.environ['user']


root = tk.Tk()

# Set background color to black
root.configure(bg="#6699CC")

labeUser = tk.Label(root, text=value, bg="#6699CC", fg="white", font=("Arial", 18))
labeUser.place(x=100, y=50)

# Create a label
label = tk.Label(root, text="Virtual Quiz game using Hand Gesture", bg="#6699CC", fg="white", font=("Arial", 18))

# Create a label
label2 = tk.Label(root, text="Please select the topic for quiz", bg="#6699CC", fg="red", font=("Arial", 14))

# Set the position of the label using place
label.place(x=300, y=50)
label2.place(x=350, y=100)

# Load image
image = Image.open("button_net.jpg")
photo = ImageTk.PhotoImage(image)

image2 = Image.open("button_java.jpg")
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open("button_python.jpg")
photo3 = ImageTk.PhotoImage(image3)

image4 = Image.open("button_angular.jpg")
photo4 = ImageTk.PhotoImage(image4)

# Create a button with the image
button1 = tk.Button(root, image=photo, command=call_other_script)
button1.place(x=200, y=150)  # Set x and y coordinates

# Create another button with the image at a different position
button2 = tk.Button(root, image=photo2, command=call_other_script)
button2.place(x=600, y=150)  # Set x and y coordinates

# Create another button with the image at a different position
button2 = tk.Button(root, image=photo3, command=call_other_script)
button2.place(x=200, y=400)  # Set x and y coordinates

# Create another button with the image at a different position
button2 = tk.Button(root, image=photo4, command=call_other_script)
button2.place(x=600, y=400)  # Set x and y coordinates

# Set the size and position of the window
window_width = 1000
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()
