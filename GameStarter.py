import string
from tokenize import String
from annotated_types import LowerCase
from fuzzywuzzy import fuzz
import os
import subprocess

from numpy import empty


def startGame(gameName):
    path=searchExe(gameName)
    if(path != ""):
        subprocess.Popen(path,stdout=subprocess.PIPE)
        return 0
    else:
        return -1
    
def searchDir(gameName:str):
    origindir='C:\\Program Files (x86)\\Steam\\steamapps\\common'
    maxscore=0
    maxdir=""

    for files in os.listdir(origindir):
        if(fuzz.partial_ratio(files.lower(),gameName.lower())>maxscore):
            maxscore=fuzz.partial_ratio(files.lower(),gameName.lower())
            maxdir=files
            print(maxscore, maxdir)
    
    return maxdir

def searchExe(gameName:str):
    dirname = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\'+searchDir(gameName)
    ext = ('.exe') 
    maxscore=0
    try:
        for files in os.listdir(dirname):
            if files.endswith(ext):
                print(files)
                if(fuzz.partial_ratio(gameName.lower(),files.lower())>maxscore):
                    exe_path=r""+dirname+"\\"+files
                    maxscore=fuzz.partial_ratio(gameName.lower(),files.lower())
        return exe_path
    except NotADirectoryError:
        print("Open is not Possible the Game Directory has most likely another name")
        return ""