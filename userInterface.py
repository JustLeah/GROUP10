import os
import tkinter
#create a new object called window
window = tkinter.Tk()

mycolor = '#%02x%02x%02x' % (223,74,90)
window.configure(background=mycolor)


#Add a title, set the size and add a logo
window.title("COMSC Learning Styles")
window.geometry("400x600")
window.wm_iconbitmap('assets/cardiff.ico')

#add a logo to the header of the application
photo = tkinter.PhotoImage(file="assets/cardiffbanner.gif")
w = tkinter.Label(window, image=photo)
w.pack()

#create a label widget called 'button1'
button1 = tkinter.Button(window, text="Button 1")
button1.pack()

#draw the window, and start the 'application'
window.mainloop()