import unittest
from FileManagerPackage.FileManager import FileManager as filemanger # from package.Module import Class as varName

class Test_FileManager(unittest.TestCase):
    """Testsclass for FileManager Unittests"""

    def test_FileManager_string_entered(self):
        s = FileManager.string_entered("hallo")
        self.assertEqual(s,"hallobla")
        return


    def test_FileManager_main(self):
        #FileManager.main(scriptname = "scriptname" ,directory =
        #"dir",orgnzbname="orgnzbname",jobname="jobname",reportnumber="reportnumber",category="category",
        #                   group="group",postprocstatus="postprocstatus",url="url")
        #sys.argv = ["scriptname", "dir"]
        fm = filemanger()
        fm.main();
        return


if __name__ == '__main__':
    unittest.main()