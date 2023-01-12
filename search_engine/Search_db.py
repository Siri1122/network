#import logging
#from searchLogging import Filelog
import sqlite3
#from searchfile import SearchFile
#from locatedrives import SearchEngine
class SearchDB:
    def __init__(self):
        self.con = sqlite3.connect('c://sqlite//hcl.db')
        self.cur = self.con.cursor()
    def searchDB(self,name):
        self.con = sqlite3.connect('c://sqlite//hcl.db')
        self.cur = self.con.cursor()
        sql= """select * from filelog1 where filename like '%{0}' """.format(name)
        self.cur.execute(sql)
        path=self.cur.fetchone()
        if path==None:
            return 0
        else:
            return 1
    def insertDB(self,filename):
        sql="""insert into filelog1(filename) values(?);"""
        data=(filename,)
        self.cur.execute(sql,data)
        self.con.commit()
        print("added successfully")
        return "added successfully"
    def updateDb(self,filename):
        sql="""update filelog1 set filename=? where id=10"""
        data=(filename,)
        self.cur.execute(sql,data)
        self.con.commit()
        print("updated")
        return "updated"
    def deleteDb(self,id):
        sql="""delete from filelog1 where id=?"""
        data=(id,)
        self.cur.execute(sql,data)
        self.con.commit()
        print("deleted")
        return "deleted"
# if name=='main':
#     db = SearchDB()
#     name=input("enter filename:")
#     print(name)
#     log=Filelog()
#     #Id=int(input("Enter Id:"))
#     #db.deleteDb(Id)
#     row=db.searchDB(name)
#
#     if row==0:
#         locate = SearchEngine()
#         search = SearchFile(locate.locate_Activedrives(), name)
#         result=search.search_file1()
#         db.insertDB(result)
#         logging.info(result)
#     else:
#         print("exits")
#         # logging.info(path)