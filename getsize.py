import os
from tkinter import filedialog
import sys

def getDirPath():
        if len(sys.argv) < 2:
                path = filedialog.askdirectory()
                if path == "":
                        return os.getcwd()
                return path
        else:
                return sys.argv[1]
        
def getFileSizes(path):
        vcd = True # to get the folder names in the original directry
        sizeDict = {}
        sizeDictForFiles = {}
        somethingwentwrong = False
        for (dirpath,foldernames,filenames) in os.walk(path, topdown=True):
                # dirpath = current directory path
                # foldername = folders inside the current directory
                # filename = 
                if vcd : 
                        # Only runs in the first itteration
                        for folder in  foldernames:
                                sizeDict[folder] = 0
                        filesList = filenames 
                        vcd = False
                        
                else:  
                        if dirpath == path:
                                currentfolder = dirpath
                        elif len(path) == 3: # when reading Disks
                                currentfolder = dirpath.replace(path,"").split("/")[0]
                                currentfolder = currentfolder.split("\\")[0]
                        else:
                                currentfolder = dirpath.replace(path,"").split("\\")[1]
                                
                        for filename in filenames:
                                if currentfolder in sizeDict.keys():
                                        sizeDict[currentfolder] += os.path.getsize(f"{dirpath}\\{filename}")
                                else:
                                        somethingwentwrong = True
                                        
        for filename in filesList:
                sizeDictForFiles[filename] = os.path.getsize(f"{path}\\{filename}")
                
        if somethingwentwrong:
                print("Something went wrong!")
                
        return sizeDict,sizeDictForFiles

class Display:
        def __init__(self,folderD,fileD):
                self.folderD = folderD
                self.fileD = fileD
                self.largestFirst = True
                self.KiloByte = 1024
                self.MegaByte = 1024*1024
                
                self.disBytes = 1024*1024
                self.disBytesStr = " MB"
        
        def displayNormal(self):
                width = 34
                print("-"*width)
                print("              Folders")
                print("-"*width)
                for key, value in self.folderD.items():
                        fvalue = round(value/self.disBytes , 2)
                        if len(key) <= 20:
                                space = width - len(key) - len(str(fvalue)) - 3
                                print(f"{key}{"."*space}{fvalue}{self.disBytesStr}")
                        else:
                                space = width - 20 - len(str(fvalue)) - 3
                                print(f"{key[0:20]}{"."*space}{str(fvalue)}{self.disBytesStr}")
                
                print()
                print("-"*width)
                print(f"              Files")
                print("-"*width)
                for key, value in self.fileD.items():
                        fvalue = round(value/self.disBytes , 2)
                        if len(key) <= 20:
                                space = width - len(key) - len(str(fvalue))
                                print(f"{key}{"."*space}{fvalue}{self.disBytesStr}")
                        else:
                                space = width - 20 - len(str(fvalue))
                                print(f"{key[0:20]}{"."*space}{str(fvalue)}{self.disBytesStr}")
        
        def display(self):
                # Not Finished
                from rich.table import Table
                from rich.console import Console
                
                
                table = Table(title = "Folder Size")
                table.add_column("Folder Name",justify="left" ,style="bold #E4B1F0")
                table.add_column("Folder Size",justify="right", style="bold #E4B1F0")
                for key,value in self.folderD.items():
                        table.add_row(f"{key if (len(key) <= 20) else key[0:20]}",f"{"{:.2f}".format(value/(1024 ))} KB")
                consol = Console()
                consol.print(table)
                
                table = Table(title = "File Size")
                table.add_column("File Name",justify="left" ,style="bold #E4B1F0")
                table.add_column("File Size",justify="right", style="bold #E4B1F0")
                for key,value in self.fileD.items():
                        table.add_row(f"{key if (len(key) <= 20) else key[0:20]}",f"{"{:.2f}".format(value/(1024 ))} KB")
                consol = Console()
                consol.print(table)

        def displayBySize(self):
                def sortBySize(dictToSort):
                        sortedDict = {}
                        if self.largestFirst:
                                for value in (sorted(dictToSort.values(),reverse=True)):
                                        sortedDict[list(dictToSort.keys())[list(dictToSort.values()).index(value)]] = value
                        else:
                                for value in (sorted(dictToSort.values(),reverse=False)):
                                        sortedDict[list(dictToSort.keys())[list(dictToSort.values()).index(value)]] = value
                                        
                        return sortedDict

                self.folderD = sortBySize(self.folderD)
                self.fileD = sortBySize(self.fileD)
                self.display()
                        
def main():
        dirpath = getDirPath()
        
        sizesDictForDir,sizeDictForFiles = getFileSizes(dirpath)
        app = Display(sizesDictForDir,sizeDictForFiles)
        app.displayNormal()
        
main()