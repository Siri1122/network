import os,string
from Exception_Class import File
import win32api
class SearchEngine:
    def __init__(self):
        pass
    def locate_Alldrives(self):
        d=win32api.GetLogicalDriveStrings()
        d=d.split('\000')[:-1]
        print(d)
    def locate_Activedrives(self):
        try:
            a = [x for x in string.ascii_uppercase if os.path.exists(x + ":")]
            if a==[]:
                raise File("No drives are present in the system")
            else:
                return a
        except File as f:
            print(f)

search=SearchEngine()
print(search.locate_Activedrives())
search.locate_Alldrives()