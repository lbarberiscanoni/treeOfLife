import platform
import subprocess

def selfdestruct():
    pathToSelf = subprocess.check_output("locate treeOfLife.py", shell=True)
    subprocess.call("rm -rf " + str(pathToSelf), shell=True)

def checkForHomebrew():
    brewCheck = ""
    try:
        brewCheck = subprocess.check_output("which brew", shell=True)
    except:
        brewCheck = "no brew"

    return brewCheck

def checkForTree():
    treeCheck = ""
    try:
        treeCheck = subprocess.call("which tree", shell=True)
    except:
        treeCheck = "no tree"

    return treeCheck

def getSystem(): 
    return platform.system()

if checkForTree() == "no tree":
    if getSystem() == "Linux":
        subprocess.call("sudo apt-get install tree", shell=True)
    elif getSystem() == "Mac":
        if checkForHomebrew() == "no brew":
            getBrewCommand = "/usr/bin/ruby -e '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'"
            subprocess.call(getBrewCommand, shell=True)
            subprocess.call("brew install tree", shell=True)
        else:
            subprocess.call("brew install tree", shell=True)
    else:
        selfdestruct()
else:
    subprocess.check_output("tree ~ > fileTree.txt", shell=True)
