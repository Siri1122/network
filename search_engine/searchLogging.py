import logging
import re
class Filelog:
    def __init__(self):
        logging.basicConfig(filename="filelog1.txt",level=logging.INFO)
    def search_log(self,filename):
        file=open("filelog1.txt","r")
        str="siri1.txt"
        data=re.compile(str)
        res=data.search(str)
        line=file.readline()
        print(res.group(0))