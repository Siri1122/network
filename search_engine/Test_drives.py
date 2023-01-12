import pytest
from searchfile import SearchFile
from locatedrives import SearchEngine
from Search_db import SearchDB
class Test_Search:
    def testdrive(self):
        obj=SearchEngine()
        result=obj.locate_Activedrives()
        self.expected=['C']
        if result==self.expected:
            assert True
        else:
            assert False
    def test_searchfile(self):
        obj=SearchFile("C","siri1.txt")
        result=obj.search_file1()
        if result[0]=='C:\searching\siri2.txt':
            assert True
        else:
            assert False
    def test_serachindb(self):
        obj=SearchDB()
        re=obj.searchDB('C:\searching\siri1.txt')
        assert re==1
    def test_insertindb(self):
        obj=SearchDB()
        re=obj.insertDB('C:\searching\siri1.txt')
        assert re=="added successfully"
    def test_updateindb(self):
        obj=SearchDB()
        re=obj.updateDb('C:\searching\snehai1.txt')
        assert re=="updated"
    def test_deleteindb(self):
        obj=SearchDB()
        re=obj.deleteDb(6)
        assert re=="deleted"