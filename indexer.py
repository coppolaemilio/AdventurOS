import os
import sys
import time

print"""
,---.    |                |              ,---.,---.
|---|,---|.    ,,---.,---.|--- .   .,---.|   |`---.
|   ||   | \  / |---'|   ||    |   ||    |   |    |
`   '`---'  `'  `---'`   '`---'`---'`    `---'`---'
            welcome to indexer v0.0.01
"""
running=True
working=False #When indexing a folder
l = check_lm = ""
message_wait="[>] Waiting game's output."
f= os.path.join("cwd")
f_lm = os.path.getmtime(f)
s_path = os.getcwd() #where the game is
command=""
os.system('color 3')

def check_command():
    try:
        with open(f, 'r') as the_file: 
            output= the_file.readline()
            if "!" in output:
                command=output[1:]
                return command
    except:
       command=""

def index_folder(the_file):
    os.chdir(command)
    files = [f for f in os.listdir('.')]
    for i in files:
        if os.path.isdir(i):
            ftype=">"
        else:
            ftype="*"
        
        the_file.write(ftype+i+"\n")
    os.chdir(s_path)

while running==True:
    command=check_command()
    if working==False:
        if l!= message_wait:
            l = message_wait
            print l
        try:
            check_lm = os.path.getmtime(f)
        except:
            check_lm = ""
        if f_lm!= check_lm: #Start working
            working=True
            l=""
    if working==True:
        if command!="":
            try:
                with open(f, 'w') as the_file:
                    index_folder(the_file)
                    working=False
                f_lm = os.path.getmtime(f)
                
                print "[>] Indexing folder"
            except:
                print "[!] Re-trying to read the file."
    time.sleep(0.1)
