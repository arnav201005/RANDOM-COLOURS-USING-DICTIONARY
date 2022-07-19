from tkinter import*
import random
root=Tk()

root.title("DICTIONARY")
root.geometry("400x400")

dictionary = {"Colour" : ["gray","white", "pink", "orange", "yellow", "black", "green", "blue", "red"]}

def change():
    random_no = random.randint(0,8)
    print(dictionary["Colour"][random_no])
    root.configure(background = dictionary["Colour"][random_no])
    
btn = Button(root,text = "Click me!", command = change)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()