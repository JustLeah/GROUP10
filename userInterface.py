import os
import tkinter
#create a new object called window
window = tkinter.Tk()

#Add a title, set the size and add a logo
window.title("COMSC Learning Styles")
window.geometry("400x600")

iconlocation = os.getcwd() + '/assets/'
iconname = 'cardiff.ico'


if "nt" == os.name:
    window.wm_iconbitmap(r'assets/cardiff.ico')
else:
    window.wm_iconbitmap(bitmap = r''+iconlocation+'@cardiff.ico') 


#draw the window, and start the 'application'
window.mainloop()