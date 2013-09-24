import os
import sys
import time
import platform
if platform.system()=="Windows": os.system('color 3')

print"""
,---.    |                |              ,---.,---.
|---|,---|.    ,,---.,---.|--- .   .,---.|   |`---.
|   ||   | \  / |---'|   ||    |   ||    |   |    |
`   '`---'  `'  `---'`   '`---'`---'`    `---'`---'
            welcome to indexer v0.0.03"""
            
s_path = os.getcwd() #where the program is
running=True
working=False #When indexing a folder
l= check_lm= command= ""
message_wait="[>] Waiting game's output."
f = os.path.join(s_path,"cwd")
f_lm = os.path.getmtime(f)

def check_command():
    try:
        with open(f, 'r') as the_file: 
            output = the_file.readline()
            if output[0]=="!":
                return output[1:]
    except:
       return ""

def index_folder(the_file):
    if "\n" in command:
        os.chdir(unicode(command[:-1]))
    else:
        os.chdir(unicode(command))
    files = [f for f in os.listdir('.')]
    for i in files:
        if os.path.isdir(i):
            ftype=">"
        else:
            ftype="*"
        if i[0]!=".":
            the_file.write(ftype+i+"\n")
    os.chdir(s_path)
    print "[>] Done."

while running==True:
    command = check_command()
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
    else:
        if command!="":
            with open(f, 'w') as the_file:
                index_folder(the_file)
                working=False
            f_lm = os.path.getmtime(f)

            print "[>] Indexing folder"
    time.sleep(0.1)