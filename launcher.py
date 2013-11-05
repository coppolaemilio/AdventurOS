import Tkinter, tkFont
from urllib2 import urlopen

class Demo:
    def __init__(self):
        font = tkFont.Font(family="Helvetica",size=43)
        Tkinter.Label(text='AdventurOS', font=font).pack()
        Tkinter.Label(text='Launcher v0.0.1').pack()
        Tkinter.Frame(height=2, bd=1, relief=Tkinter.GROOVE).pack(fill=Tkinter.X, padx=5, pady=5)
        updates = Tkinter.Text(height=10, width=70)
        data = urlopen("http://adventuros.evelend.com/include/buildupdates.txt").read()
        updates.insert(Tkinter.INSERT, data)
        updates.config(state=Tkinter.DISABLED)
        updates.pack()
        Tkinter.Frame(height=2, bd=1, relief=Tkinter.GROOVE).pack(fill=Tkinter.X, padx=5, pady=5)
        Tkinter.Button(text='Start Game', command=self.test).pack()
        Tkinter.Button(text='Exit', command=exit).pack() 

    def test(self):
        print "cacaseca"


if __name__ == '__main__':
    root=Tkinter.Tk();
    root.title("Adventuros");
    widget = Demo()
    root.mainloop()