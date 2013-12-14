#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2012, 2013 Emilio Coppola emilio@evelend.com
import os, sys ,time
from sys import platform as _platform

if _platform == "win32": 
    slash="\\"
    s_path = os.path.join(os.environ['LOCALAPPDATA'],"AdventurOS")
elif _platform == "darwin":
    slash="/"
    s_path = os.path.join(os.environ['HOME'], 'Library','Application Support', 'com.yoyogames.macyoyorunner')
else:
    s_path = os.getcwd() #where the cwd file is
    slash="/"
print"""
,---.    |                |              ,---.,---.
|---|,---|.    ,,---.,---.|--- .   .,---.|   |`---.
|   ||   | \  / |---'|   ||    |   ||    |   |    |
`   '`---'  `'  `---'`   '`---'`---'`    `---'`---'
            welcome to indexer v0.0.11"""
            
running = True
working = False #When indexing a folder
l = check_lm = command = ""
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

def index_folder():
    the_file = []
    if "\n" in command:
        os.chdir(unicode(command[:-1], "utf8"))
    else:
        os.chdir(unicode(command, "utf8"))

    previous_dir= str(os.getcwd()).split(slash)[-2]
    the_file.append("!"+command+"\n")
    if "<"+previous_dir=="<C:":
		the_file.append("<"+previous_dir+"/\n")
    else:
    	the_file.append("<"+previous_dir+"\n")

    files = [f for f in os.listdir('.')]
    for i in files:
        if os.path.isdir(i):
            ftype=">"
        else:
            ftype="*"
        if i[0]!=".":
            the_file.append(ftype+i+"\n")
    os.chdir(s_path)
    print "[>] Done."
    return the_file

def check_access(lista, f_lm):
    #Windows method
    print "[>] Reading: "+command
    lasttime = f_lm
    with open(f, 'w') as the_file: 
        for line in lista:
            if ">" in line:
                target = command+'/'+line.replace(">","")
                target = target.replace("\n", "")
                #print target
                if confirm_access(target)=="yes":
                    the_file.write(line)
                    f_lm = check_lm = lasttime
                else:
                    the_file.write(line.replace(">","|"))
                    f_lm = check_lm = lasttime
            else:
                the_file.write(line)
                f_lm = check_lm = lasttime

def confirm_access(folder):
    #the best way to check if you have access to a folder under Windows.
    try:
        for t in os.listdir(folder):
            return "yes"
    except WindowsError:
        return "no"

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
            the_file = index_folder()
            working=False
            print "[>] Indexing folder"
            check_access(the_file, f_lm)
            f_lm = os.path.getmtime(f)

    time.sleep(0.1)

raw_input()