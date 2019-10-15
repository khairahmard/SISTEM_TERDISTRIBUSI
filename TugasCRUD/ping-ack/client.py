import Pyro4,Pyro4.errors
import time
import os

uri = "PYRONAME:nisa@localhost:7777"

def create(filename,content):
    pyro4uri = Pyro4.Proxy(uri)
    pyro4uri._pyroTimeout = 3.0
    print(pyro4uri.create(filename,content))

def read(filename):
    pyro4uri = Pyro4.Proxy(uri)
    pyro4uri._pyroTimeout = 3.0
    print(pyro4uri.read(filename))

def update(filename,content):
    pyro4uri = Pyro4.Proxy(uri)
    pyro4uri._pyroTimeout = 3.0
    print(pyro4uri.update(filename,content))

def delete(filename):
    pyro4uri = Pyro4.Proxy(uri)
    pyro4uri._pyroTimeout = 3.0
    print(pyro4uri.delete(filename))

def listdir():
    pyro4uri = Pyro4.Proxy(uri)
    pyro4uri._pyroTimeout = 3.0
    print ('\n'.join(pyro4uri.listdir()))

if __name__=='__main__':
    file = ""
    while True:
        try:
            print("\n1 Create\n2 Read\n3 Update\n4 Delete\n5 List Directory\n0 Exit\n")
            str = input("option: ")
            strarr = str.split(" ")
            if(strarr[0] == '1'):
                content = input("content: ")
                create(strarr[1],content)
            elif (strarr[0] == '2'):
                read(filename)
            elif(strarr[0] == '3'):
                content = input("content: ")
                update(strarr[1],content)
            elif(strarr[0] == '4'):
                delete(strarr[1])
            elif (strarr[0] == '5'):
                listdir()
            elif(strarr[0] == '0'):
                print("EXIT")
                exit()
            else:
                print("NOT AN OPTION")
        except (Pyro4.errors.TimeoutError, Pyro4.errors.ConnectionClosedError):
            print("Server is presumably down..\nClosing connection..")
            break