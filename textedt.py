from tkinter import *
from tkinter.filedialog import file_menu
from tkinter.messagebox import edit_menu
from tkinter.font import format_menu
from tkinter.scrolledtext import *
from tkinter.filedialog import help_menu

root = Tk()

root.title("TEXT EDITOR AND BUILDER-Untitled")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

menubar = Menu(root)

file_menu.main(root,text,menubar)
edit_menu.main(root,text,menubar)
format_menu.main(root,text,menubar)
help_menu.main(root,text,menubar)

root.mainloop()
