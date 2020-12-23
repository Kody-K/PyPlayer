from playsound import playsound
import glob
from tkinter import *
from tkinter import filedialog

print('''
__________        __________.__                              
\______   \___.__.\______   \  | _____  ___.__. ___________  
 |     ___<   |  | |     ___/  | \__  \<   |  |/ __ \_  __ \ 
 |    |    \___  | |    |   |  |__/ __ \\___  \  ___/|  | \/ 
 |____|    / ____| |____|   |____(____  / ____|\___  >__|    
           \/                         \/\/         \/        
Created By:- Kody-K

''')

music = input("Enter Path to .mp3 File, use *.mp3 if you wanna play all .mp3 from your specified folder: ")

def pyplayer(path):
    for song in glob.glob(path):
        print('Playing ' + song + ' ')
        playsound(song)

pyplayer(music)
