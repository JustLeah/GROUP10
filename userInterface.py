import os
import tkinter
#create a new object called window
window = tkinter.Tk()

#Add a title, set the size and add a logo
window.title("COMSC Learning Styles")
window.geometry("400x600")
window.wm_iconbitmap('assets/cardiff.ico')

#create a label widget called 'button1'
button1 = tkinter.Button(window, text="Button 1")
button1.pack()

#draw the window, and start the 'application'
window.mainloop()