import sys
import os
#from os.path import join, getsize
import shutil
import logging

class FileManager:
    """Filemanager Class"""

    def main(self):
        #try:
        #    print(sys.argv)
        #    (scriptname,directory,orgnzbname,jobname,reportnumber,category,group,postprocstatus,url) = sys.argv
        #    print(sys.argv)

        #except:
        #    print("No commandline parameters found")
        #    sys.exit(1)

        # continue script
    
        for root, dirs, files in os.walk('C:\TestFileshare'):
            print(root, "consumes", end = "")
            print(sum([os.path.getsize(os.path.join(root, name)) for name in files]), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories
            # Your code goes here

        # Success code
        #sys.exit(0)
        return

    def string_entered(self, a):
        return(a + "bla")

    if __name__ == '__main__':
        main()