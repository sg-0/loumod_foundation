#!/usr/bin/env python

# first there was nothing, then comes time:
from time import *
# later there born a process:
from threading import Thread
# some more porcesses have to be queued:
from queue import Queue
# to help other people we decided to include some important packages
import Braille2AsciiTranslator
# @the end someone developed bluetooth:
from bluetooth import *


import subprocess


class CommunicationHandler(Thread):


    def __init__(self, fifo = Queue()): 
        Thread.__init__(self) 

        subprocess.call(['sudo', 'hciconfig', 'hci0', 'up'])
        subprocess.call(['sudo', 'hciconfig', 'hci0', 'sspmode','1'])
        subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
        subprocess.call(['sudo', 'hciconfig', 'hci0', 'name', 'Esys-1422'])
        subprocess.call(['sudo', 'bluetooth-agent','1234'])
        
        self.fifo = fifo
        self.newdata = True
        self.server_sock=BluetoothSocket( RFCOMM )
        self.server_sock.bind(("",PORT_ANY))
        self.server_sock.listen(0)

        port = self.server_sock.getsockname()[1]

        uuid = "00001101-0000-1000-8000-00805F9B34FB"
        
        advertise_service( self.server_sock, "BRAILLE_RFCOMM_SERVER",
                   service_id       = uuid,
                   service_classes  = [ uuid, SERIAL_PORT_CLASS ],
                   profiles         = [ SERIAL_PORT_PROFILE ]
        )

        self.start()
        print("READY FOR CONNECTIONS, RFCOMM channel %d" % port)
    

    def authenticate(self):
        self.client_sock.send("\002\000\rSNesys12-2\000\003")
        self.client_sock.send("\002\000\bSHes1\000\003")
        self.client_sock.send("\002\000\tSS1422\000\003")
        self.client_sock.send("\002\000\aSLGR\000\003")
        self.client_sock.send("\002\000\005SG\f\003")
        self.client_sock.send("\002\000\005ST\a\003")
        self.client_sock.send("\002\000\024SW2.13-12-06-2012\000\003")
        self.client_sock.send("\002\000\024SP1.00 26-04-2006\000\003")
        self.client_sock.send("\002\000\004SI\003")
        self.client_sock.send("\002\000\020VTverbunden\000\000\000\003")

    def fifo_cleanup(self):
        while not self.fifo.empty():
            self.fifo.get()

    def fifo_append(self, data):
        for byte in data:
            self.fifo.put(byte)

    def getMoreScreenContent(self):
        self.client_sock.send("\002\000\bKC\002\000\000\000\003")
        self.client_sock.send("\002\000\bKC\000\000\000\000\003")
    
    def run(self):
        while True:

            self.client_sock, self.client_info = self.server_sock.accept()
            
            print("INBOUND CONNECTION ", self.client_info)

            try:
                while True:
                    data = self.client_sock.recv(1024)
                    if len(data) == 0: break
                    #hexstring = data.encode("hex")

                    print("COMMAND RECEIVED: " + str(data.hex()))
                    #bytes.fromhex(str(data))
                    
                    try:
                        if len(data) == 18:
    
                            #if self.newdata:
                            #    print("clean fifo")
                            #    self.fifo_cleanup()
                            
                            screen_data = data[5:17]

                            self.fifo_append(screen_data)
                            print("Append: ")
                            for byte in screen_data:
                                print( Braille2AsciiTranslator.translate(byte), end="" )
                            
                            #if data[15] == 0 and data[16] == 0:
                            #    print ("next time will come new data")
                            #    while not self.fifo.empty():
                            #        print( Braille2AsciiTranslator.translate(self.fifo.get()), end="" )
                            #    self.newdata = True
                            #else:
                            #    self.getMoreScreenContent()
                            #    print ("next time will come not new data")
                            #    self.newdata = False
                    except:
                        print("wrong type")	
                        pass		
                    
                    if data == b'\x02\x00\x04SI\x03':
                        self.authenticate()

            except IOError:
                pass

            print("socket closed")

            self.client_sock.close()

        # Close the Socket
        server_sock.close()
        print("SELF-DESTRUCT COMPLETE")

def main():
    comm_handler = CommunicationHandler()
    print("process started")


if __name__ == "__main__": main()