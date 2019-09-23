import os
from Pyro4 import expose

class crudnisa(object):

    def __init__(self):
        pass

    def create(self,filename="",content=""):
        path = os.getcwd()
        name = filename
        filename = os.path.join(path, filename)
        _file = open(filename, "w+")
        _file.write(content)
        _file.close()
        return "FILE CREATED"

    def update(self,filename="",content=""):
        path = os.getcwd()
        name = filename
        filename = os.path.join(path, filename)
        if(os.path.exists(filename)):
            _file = open(filename, "w+")
            _file.write(content)
            _file.close()
            return "FILE UPDATED"
        else:
            return "FILE NOT FOUND"

    def read(self,filename=""):
        path = os.getcwd()
        filename = os.path.join(path, filename)
        if(os.path.exists(filename)):
            _file = os.open(filename, os.O_RDWR)
            _read = os.read(fd,1000)
            os.close(_file)
            return _read
        else:
            return "FILE NOT FOUND"

    def delete(self,filename=""):
        path = os.getcwd()
        filename = os.path.join(path, filename)
        if(os.path.exists(filename)):
            os.remove(filename)
            return("FILE DELETED")
        else:
            return "FILE NOT FOUND"

    def listdir(self):
        files = []
        path = os.getcwd()
        for root, directory, file in os.walk(path):
            for f in file:
                if '.txt' in f:
                    files.append(f)
        return files

if __name__ == '__main__':
    _run = crudnisa()