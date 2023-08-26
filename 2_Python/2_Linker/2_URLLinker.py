from tkinter import *
import webbrowser
import os
import csv

# Load Save File
# save_path = os.path.dirname(__file__)

# with open(f"{save_path}/save.csv", 'r') as read_file:
#     reader = csv.reader(read_file)
#     for row in reader:
#         links = row

# read_file.close()


# Configuration // Setting

links = [
    "https://google.com/",
    "https://youtube.com/",
    "https://reddit.com/",
    "https://docs.google.com/document/d/1pUKaxjoHqXmKy_XzWHsN0ea5Z-WO6hRhoa9GYGLfijk/edit/",
]

target_url = links[0]

root = Tk()
root.title('[Samuel] DIRECT LINKS')     # Can write or not
root.geometry()

# Information Section

info = '''
==============================
    Samuel's Direct Links
==============================
'''

label_frame = Frame(root, padx=5, pady=5)
label_frame.pack()

info_label = Label(label_frame, text=info)
info_label.pack(fill="x") 

# Radiobutton Section
links_frame = Frame(root, relief="solid", pady=5)
links_frame.pack() # can say "fill='x'" or not

def change_path():
    global target_url
    target_url = links[selected.get()]

    link_lable.config(text=target_url)

selected = IntVar() # IntVar = Integer Variable
link1 = Radiobutton(links_frame, text="Google" , value=0 , variable=selected, padx=5, pady=5, command=change_path)
link2 = Radiobutton(links_frame, text="Youtube" , value=1 , variable=selected, padx=5, pady=5, command=change_path)
link3 = Radiobutton(links_frame, text="Reddit" , value=2 , variable=selected, padx=5, pady=5, command=change_path)
link4 = Radiobutton(links_frame, text="Google Doc" , value=3 , variable=selected, padx=5, pady=5, command=change_path)

link1.grid(row=1 , column=1 , sticky="w")  # use sticky="w" with column or can use columnspan=2, sticky="ew"
link2.grid(row=1 , column=2 , sticky="w")
link3.grid(row=2 , column=1 , sticky="w")
link4.grid(row=2 , column=2 , sticky="w")

link_lable_frame = LabelFrame(root, text="Target Path", pady=5)
link_lable_frame.pack(fill="x")    

link_lable = Label(link_lable_frame, text=target_url, width=30, wraplength=300, justify="left")
link_lable.pack()


# Button Section
btn_frame = Frame(root)
btn_frame.pack(side="bottom", fill="x")

def openLink():
    webbrowser.open(target_url)

open_btn = Button(btn_frame, text="Open in Browser", command=openLink)
open_btn.pack(side="right")

close_btn = Button(btn_frame, text="EXIT", command=root.quit)
close_btn.pack(side="right")


root.mainloop()

