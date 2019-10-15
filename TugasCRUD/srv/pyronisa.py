import Pyro4
from crudnisa import *

def server():
    #run name server local  pyro4-ns -n localhost -p 7777
    daemon = Pyro4.Daemon(host="localhost")
    ns = Pyro4.locateNS("localhost",7777)
    x_GreetServer = Pyro4.expose(crudnisa)
    uri_greetserver = daemon.register(x_GreetServer)
    print("URI greet server : ", uri_greetserver)
    ns.register("nisa", uri_greetserver)
    daemon.requestLoop()

if __name__ == '__main__':
    server()