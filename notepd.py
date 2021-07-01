from tkinter import*
from tkinter import Menu
from tkinter import messagebox
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os


window=Tk()
window.geometry("455x233")
window.title("Untitled - Notepad")
 

def exitfile():
    window.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def new():
    global file
    window.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",
                               filetypes=[("All Files","*.*"),("Text Documents","*.txt*")])

        if file=="":
          file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            window.title(os.path.basename(file)+"-Notepad")


    else:
         f=open(file,"w")
         f.write(TextArea.get(1.0,END))
         f.close()
         

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files","*.*"),("TextDocument","*.txt*")])
    if file=="":
        file=None

    else:
         window.title(os.path.basename(file)+"-Notepad")
         TextArea.delete(1.0,END)
         f=open(file,"r")
         TextArea.insert(1.0,f.read())
         f.close()
    

def about():
    messagebox.showinfo("Notepad","Notepad by Mansi Tiwari")


menu=Menu(window)
new_item=Menu(menu,tearoff=0)
new_item.add_command(label="New",command=new)
new_item.add_command(label="Save",command=save)
new_item.add_command(label="Open",command=openfile)
new_item.add_command(label="Exit",command=exitfile)
menu.add_cascade(label="File",menu=new_item)

new_item1=Menu(menu,tearoff=0)
new_item1.add_command(label="Cut",command=cut)
new_item1.add_command(label="Copy",command=copy)
new_item1.add_command(label="Paste",command=paste)
menu.add_cascade(label="Edit",menu=new_item1)

new_item2=Menu(menu,tearoff=0)
new_item2.add_command(label="About Notepad",command=about)
menu.add_cascade(label="Help",menu=new_item2)

#Add TextArea
TextArea = Text(window, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

window.config(menu=menu)


