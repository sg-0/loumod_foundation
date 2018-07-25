from threading import Thread
from time import sleep
from queue import Queue
from output_config import OutputConfiguration
import translator_b2a
import RPi.GPIO as GPIO  

class BrailleActuator( Thread ):
    
    def __init__( self, fifo = Queue(), output_config = OutputConfiguration() ):
        Thread.__init__( self )
        
        self.fifo = fifo

        self.dots = [ 26, 19, 13, 20, 16, 5, 6, 12 ]
        self.amount_of_pins = 8

        # 1 4
        # 2 5
        # 3 6
        # 7 8

        GPIO.setmode( GPIO.BCM )
        
        GPIO.setwarnings( False )
        
        for dot in self.dots:
             GPIO.setup( dot, GPIO.OUT )

        
        self.output_config = output_config
        
        self.start()
        
    def actuate( self ):
        if not self.fifo.empty():
            byte = self.fifo.get()
            bytes( byte )
            
            for i in range( self.amount_of_pins ):
                GPIO.output( self.dots[i], byte >> i & 1 )
            
            print( translator_b2a.translate(byte), end="" )

            sleep( self.output_config.get_delay() )
            
            for i in range( self.amount_of_pins ):
                GPIO.output( self.dots[i], 0 )
    
    def run(self):
        try:
            while True:
                self.actuate()

        except KeyboardInterrupt:
	        GPIO.cleanup() 