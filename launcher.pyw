import Tkinter, os
from urllib2 import urlopen

class Demo:
    def __init__(self):
        photo = Tkinter.PhotoImage(file=os.path.join('files',"launcher.gif"))
        label = Tkinter.Label(image=photo, bd=-2)
        label.image = photo
        label.pack()

        Tkinter.Label(text='Launcher v0.0.1').pack()
        updates = Tkinter.Text(height=10, width=50)
        url="http://adventuros.evelend.com/include/buildupdates.txt"
        try:
            data = urlopen(url).read()
        except:
            data = "Error retrieving information from "+url+"\nAre you connected to the intert?"    
        updates.insert(Tkinter.INSERT, data)
        updates.config(state=Tkinter.DISABLED)
        updates.pack()

        Tkinter.Button(text='Start Game', command=self.startgame).pack()
        Tkinter.Button(text='Exit', command=exit).pack() 

    def startgame(self):
        pass

def center(win): #by Honest Abe stackoverflow.com
    win.update_idletasks()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = win.winfo_width() + (frm_width*2)
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = win.winfo_height() + (titlebar_height + frm_width)
    x = (win.winfo_screenwidth() / 2) - (win_width / 2)
    y = (win.winfo_screenheight() / 2) - (win_height / 2)
    geom = (win.winfo_width(), win.winfo_height(), x, y)
    win.geometry('{0}x{1}+{2}+{3}'.format(*geom))


root=Tkinter.Tk()
root.resizable(0,0)
root.title("AdventurOS Launcher")
widget = Demo()
center(root)
root.mainloop()