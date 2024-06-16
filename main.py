from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

# icon
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

# top
top = PhotoImage(file="Images/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

# bottom box
Label(root, width=72, height=18, bg="#A8DBFA").pack(side=BOTTOM)

# two boxes
box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# scale
scale = PhotoImage(file="Images/scale.png")
Label(root, image=scale, bg="#A8DBFA").place(x=20, y=310)

#################### Slider1 ####################################
current_value = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = Image.open("Images/man.png")
    resized_image = img.resize((50, 50))  # Size should be a tuple
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

# Command to change background color of scale
style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale",
                   command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

#################################################################

##@@@@@@@@@@@@@@@@@@@@@@@@@@ Slider2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

# Command to change background color of scale
style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale",
                   command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Entry box
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)

# man image
secondimage = Label(root, bg="#A8DBFA")
secondimage.place(x=70, y=530)

# BMI result
bmi_result = Label(root, text="", bg="#A8DBFA", font=("Arial", 20))
bmi_result.place(x=150, y=450)

def calculate_bmi():
    try:
        height_val = float(Height.get())
        weight_val = float(Weight.get())
        if height_val > 0:
            bmi = weight_val / ((height_val / 100) ** 2)
            if bmi <= 25:
                bmi_result.config(text=f"BMI: {bmi:.2f} (Normal)")
            else:
                bmi_result.config(text=f"BMI: {bmi:.2f} (Overweight)")
        else:
            bmi_result.config(text="Invalid height")
    except ValueError:
        bmi_result.config(text="Enter valid numbers")

# Calculate BMI button
calc_button = Button(root, text="Calculate BMI", command=calculate_bmi, bg="#A8DBFA", font=("Arial", 15))
calc_button.place(x=170, y=380)

root.mainloop()
