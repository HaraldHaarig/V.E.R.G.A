import difflib 
import os
import subprocess


def startGame(gameName):
    
    dirname = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\'+gameName
    # giving file extension
    ext = ('.exe')
    # iterating over all files
    
    
    try:
        for files in os.listdir(dirname):
            if files.endswith(ext):
                print(files)
                if files != "UnityCrashHandler32.exe" and files != "UnityCrashHandler64.exe": 
                    exe_path=r""+dirname+"\\"+files
                    print(exe_path)
                    subprocess.Popen(exe_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    return 0
        return -1
    except NotADirectoryError:
        print("Open is not Possible the Game Directory has most likely another name")
        return -1