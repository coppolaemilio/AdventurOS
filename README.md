[AdventurOS] (http://adventuros.evelend.com)
==========
Explore a unique adventure based on the content of your computer.

##Supported Platforms
* Windows
* Linux
* Mac OS

##File structure
indexer.py
This file is the one which takes care of indexing your folders for the game to read.

config.ini
In this file you'll find all game settings, such as resolution, vsync, game version, controls and so on.


The folder named "main" contains all the information about the game. 
Items, monsters, music, sprites... If you wish to start modding
the game, the first step would be copying the entire folder,
renaming it with your mod's name and change inside the config.ini file
the value of the variable called "module".

The game will load all resources from your mod folder and if a file is not
found it will access the main one.




##About
This repository will contain all the content needed for creating AdventurOS mods. 
* Item creation
* NPC and mobs
* Quests
* Skills and magic
* And many more!




==========
Have a question? [Ask on our help desk.](http://adventuros.evelend.com/help/)
