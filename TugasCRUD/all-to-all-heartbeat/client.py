import Pyro4
import time
import threading as th
import os

def connect():
    uri = "PYRONAME:nisa@localhost:7777"
    pyro4uri = Pyro4.Proxy(uri)
    return pyro4uri

class pingThread(th.Thread):
    def __init__(self, server):
        th.Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            try:
                self.server.send_heartbeat()
                # time.sleep(4.0)
            except Pyro4.errors.ConnectionClosedError:
                print("\nDisconnected\nConnection closed..")
                break
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def create(filename,content,pyro4uri):
    print(pyro4uri.create(filename,content))

def read(filename,pyro4uri):
    print(pyro4uri.read(filename))

def update(filename,content,pyro4uri):
    print(pyro4uri.update(filename,content))

def delete(filename,pyro4uri):
    print(pyro4uri.delete(filename))

def listdir(pyro4uri):
    print ('\n'.join(pyro4uri.listdir()))

if __name__=='__main__':
    file = ""
    p4 = connect()
    thread = pingThread(p4)
    thread.start()
    while True:
        try:
            print("\n1 Create\n2 Read\n3 Update\n4 Delete\n5 List Directory\n0 Exit\n")
            str = input("option: ")
            strarr = str.split(" ")
            if(strarr[0] == '1'):
                content = input("content: ")
                create(strarr[1],content,p4)
            elif (strarr[0] == '2'):
                read(filename,p4)
            elif(strarr[0] == '3'):
                content = input("content: ")
                update(strarr[1],content,p4)
            elif(strarr[0] == '4'):
                delete(strarr[1],p4)
            elif (strarr[0] == '5'):
                listdir(p4)
            elif(strarr[0] == '0'):
                print("EXIT")
                exit()
            else:
                print("NOT AN OPTION")
        except (Pyro4.errors.ConnectionClosedError, Pyro4.errors.CommunicationError):
            print("Server is presumably down..\nClosing connection..")
            break
        except Pyro4.errors.TimeoutError:
            print("Server Timeout\nClosing connection..")
            thread.stop()
            break