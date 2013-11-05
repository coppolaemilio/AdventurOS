import Tkinter, tkFont, os
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

root=Tkinter.Tk()
root.resizable(0,0)
root.title("AdventurOS Launcher")
root.wm_iconbitmap(os.path.join('files','icon.ico'))
widget = Demo()
root.mainloop()