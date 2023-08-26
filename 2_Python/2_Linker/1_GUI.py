from tkinter import *

root = Tk() # add in notepad
root.title("SAMUEL GUI SAMPLE")
root.geometry("640x480")
root.resizable(TRUE, TRUE)  # is it resizable (which sides are / not)

def pressed() :
    btn1.config(text="pressed") # changing text when button pressed
    label.config(text="pressed!!")

# Button
btn1 = Button(root, text="button1", command=pressed) 
# btn1.pack(side="left")    // position
btn1.pack()

# Frame
frame1 = Frame(root, relief="solid", bd=1)
frame1.pack(fill='both')

# Label
label = Label(frame1, text = "Hello")
label.pack()

def Txt2Label():
    change = txt.get("1.0", END) # "get" important! get = getting something
    label.config(text=change)
    txt.delete("1.0", END)

# Text 
txt = Text(frame1, width=30, height=10)
txt.pack(fill="both")   # fill : x, y, both // x : left to right, y : top to bottom, both : y and x

btn2 = Button(frame1, fg='red', text="Textbox to Label", command=Txt2Label)
btn2.pack(side="right")

# Frame
frame2 = Frame(root, relief="solid", bd=1)
frame2.pack(fill='both')

# Radio Button
selected = IntVar() # IntVar = Integer Variable
radio1 = Radiobutton(frame2, text="1" , value=1 , variable=selected, padx=5, pady=5)
radio2 = Radiobutton(frame2, text="2" , value=2 , variable=selected, padx=5, pady=5)
radio3 = Radiobutton(frame2, text="3" , value=3 , variable=selected, padx=5, pady=5)
radio4 = Radiobutton(frame2, text="4" , value=4 , variable=selected, padx=5, pady=5)
radio5 = Radiobutton(frame2, text="5" , value=5 , variable=selected, padx=5, pady=5)

radio1.grid(row=1 , column=1 , sticky="w")  # use sticky="w" with column or can use columnspan=2, sticky="ew"
radio2.grid(row=1 , column=2 , sticky="w")
radio3.grid(row=2 , column=1 , sticky="w")
radio4.grid(row=2 , column=2 , sticky="w")
radio5.grid(row=3 , columnspan=2 , sticky="ew")

def test() :
    print(selected.get())

btn3 = Button(frame2, text="Radio Test", command=test)
btn3.grid()

root.mainloop()

# source ./samuel/bin/activate