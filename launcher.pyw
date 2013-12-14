import Tkinter, os, ConfigParser
from urllib2 import urlopen
from sys import platform as _platform
import shutil

class Launcher:
    def __init__(self):
        root.configure(background='white')
        photo = Tkinter.PhotoImage(file=os.path.join('files',"launcher.gif"))
        label = Tkinter.Label(image=photo, bd=-2)
        label.image = photo
        label.pack()

        Tkinter.Label(text='Launcher v0.0.2', background="white").pack()
        updates = Tkinter.Text(height=10, width=49, bd=0)
        url="http://adventuros.evelend.com/include/buildupdates.txt"
        try:
            data = urlopen(url).read()
        except:
            data = "Error retrieving information from "+url+"\nAre you connected to the internet?"    
        updates.insert(Tkinter.INSERT, data)
        updates.config(state=Tkinter.DISABLED)
        updates.pack()

        Tkinter.Button(text='Start Game', command=self.start_game).pack()
        Tkinter.Button(text='Check for updates', command=self.update).pack()
        Tkinter.Button(text='Exit', command=exit).pack() 

    def update(self):
    	print "fuck yeah"

    def start_game(self):
        if _platform == "linux" or _platform == "linux2":
            print "GNU/Linux"
        elif _platform == "darwin":
            s_path = os.path.join('AdventurOS.app','Contents', 'Resources')+"/"
            if os.path.exists(s_path)==False:
                os.mkdir(s_path)

            shutil.copyfile('config.ini', s_path+"config.ini")
            shutil.copyfile('saves.ini', s_path+"saves.ini")
            
            try:
               with open(s_path+"cwd"):
                   pass
            except:
                with open(s_path+"cwd", 'a'):
                    os.utime(s_path+"cwd", None)

            self.copy_dir('main', s_path+"main/")

            os.system("open "+os.path.join('AdventurOS.app'))
            os.system("python "+os.path.join('indexer.py'))
            root.destroy()

        elif _platform == "win32":
            os.startfile(os.path.join('indexer.py'))
            os.startfile('AdventurOS.exe')
            root.destroy()

    def copy_dir(self, from_path, to_path):
        if os.path.exists(to_path):
            shutil.rmtree(to_path)
        shutil.copytree(from_path, to_path)

    def center(self, win): #by Honest Abe stackoverflow.com
        win.update_idletasks()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = win.winfo_width() + (frm_width*2)
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        x = (win.winfo_screenwidth() / 2) - (win_width / 2)
        win_height = win.winfo_height() + (titlebar_height + frm_width)
        y = (win.winfo_screenheight() / 2) - (win_height / 2)
        geom = (win.winfo_width(), win.winfo_height(), x, y)
        win.geometry('{0}x{1}+{2}+{3}'.format(*geom))

root=Tkinter.Tk()
root.resizable(0,0)
root.title("AdventurOS Launcher")
widget = Launcher()
widget.center(root)
root.mainloop()