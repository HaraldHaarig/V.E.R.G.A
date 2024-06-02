import os
import subprocess

def startGame(gameName):
    
    dirname = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\'+gameName
    # giving file extension
    ext = ('.exe')
    # iterating over all files
    for files in os.listdir(dirname):
        if files.endswith(ext):
            print(files)  # printing file name of desired extension
            exe_path=r""+dirname+"\\"+files
            print(exe_path)
            subprocess.Popen(exe_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)