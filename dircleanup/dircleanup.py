import os
import shutil

for root, dirs, files in os.walk('.', topdown=False):
        print "Root: %s" % root
        for dir in dirs:
                if dir == '.@__thumb':
                        delpath = os.path.join(root, dir)
                        print "Removing %s" % delpath
                        shutil.rmtree(delpath)
        for file in files:
                if file == '.hightlight':
                        delpath = os.path.join(root, file)
                        print "Removing %s" % delpath
                        os.remove(delpath)
                elif file == 'Picasa.ini':
                        delpath = os.path.join(root, file)
                        print "Removing %s" % delpath
                        os.remove(delpath)
                elif file == 'Thumbs.db':
                        delpath = os.path.join(root, file)
                        print "Removing %s" % delpath
                elif file == '.DS_Store':
                        delpath = os.path.join(root, file)
                        print "Removing %s" % delpath
                elif file == '._.DS_Store':
                        delpath = os.path.join(root, file)
                        print "Removing %s" % delpath
