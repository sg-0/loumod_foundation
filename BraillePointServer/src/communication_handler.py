from threading import Thread
from queue import Queue
import translator_b2a
from bluetooth import *


import subprocess


class CommunicationHandler( Thread ):


    def __init__( self, fifo = Queue() ): 
        Thread.__init__( self ) 

        self.fifo = fifo
        self.received_data = False
		
        self.server_sock=BluetoothSocket( RFCOMM )
        self.server_sock.bind( ("",PORT_ANY) )
        self.server_sock.listen( 0 )

        port = self.server_sock.getsockname()[1]

        uuid = "00001101-0000-1000-8000-00805F9B34FB"

        advertise_service( self.server_sock, "BRAILLE_RFCOMM_SERVER",
                   service_id       = uuid,
                   service_classes  = [ uuid, SERIAL_PORT_CLASS ],
                   profiles         = [ SERIAL_PORT_PROFILE ]
        )

        print( "READY FOR CONNECTIONS, RFCOMM channel %d" % port )

    def authenticate( self ):
        self.client_sock.send( "\002\000\rSNesys12-2\000\003" )
        self.client_sock.send( "\002\000\bSHes1\000\003" )
        self.client_sock.send( "\002\000\tSS1422\000\003" )
        self.client_sock.send( "\002\000\aSLGR\000\003" )
        self.client_sock.send( "\002\000\005SG\f\003" )
        self.client_sock.send( "\002\000\005ST\a\003" )
        self.client_sock.send( "\002\000\024SW2.13-12-06-2012\000\003" )
        self.client_sock.send( "\002\000\024SP1.00 26-04-2006\000\003" )
        self.client_sock.send( "\002\000\004SI\003" )
        self.client_sock.send( "\002\000\020VTverbunden\000\000\000\003" )

    def fifo_cleanup( self ):
        while not self.fifo.empty():
            self.fifo.get()

    def fifo_append( self, data ):
        for byte in data:
            self.fifo.put( byte )

    def getMoreScreenContent( self ):
        self.client_sock.send( "\002\000\bKC\002\000\000\000\003" )
        self.client_sock.send( "\002\000\bKC\000\000\000\000\003" )

    def run( self ):
        while True:

            self.client_sock, self.client_info = self.server_sock.accept()

            print( "INBOUND CONNECTION ", self.client_info )

            try:
                while True:

                    data = self.client_sock.recv( 1024 )

                    if len( data ) <= 0: break
                    if len(data) == 18:
                        self.received_data = True

                        screen_data = data[5:17]

                        self.fifo_append( screen_data )
                        print(" ")

                    if self.received_data and self.fifo.empty():
                        self.getMoreScreenContent()

                    if data == b'\x02\x00\x04SI\x03':
                        self.authenticate()

            except IOError:
                pass

            print("socket closed")
            self.received_data = False
            self.client_sock.close()

        # Close the Socket
        self.receive_data = False
        self.server_sock.close()

def main():
    comm_handler = CommunicationHandler()
    print("process started")


if __name__ == "__main__": main()
