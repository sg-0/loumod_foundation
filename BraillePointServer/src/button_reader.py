from threading import Thread
import RPi.GPIO as GPIO              
from time import sleep, time
from output_config import OutputConfiguration

class ButtonReader( Thread ):

  def __init__( self, outputconfig = OutputConfiguration() ):
    Thread.__init__( self )
    
    self.outputconfig = outputconfig

    GPIO.setmode( GPIO.BCM )

    GPIO.setwarnings( False )
    GPIO.setup( 4, GPIO.OUT )
    GPIO.output( 4, 0 )

    self.button_low  = 2
    self.button_high = 27

    GPIO.setup( self.button_low,  GPIO.IN )
    GPIO.setup( self.button_high, GPIO.IN )
    
    self.start()
  
  def run( self ):
    try:
      while True:
        if not GPIO.input( self.button_low ):
          start_time = time()
          while not GPIO.input( self.button_low ):
            sleep( 0.1 )
          time_button_low = time() - start_time
          if float( time_button_low ) < 0.5:
            self.outputconfig.decrease_delay()
          
        if GPIO.input( self.button_high ):
          start_time = time()
          while GPIO.input( self.button_high ):
            sleep( 0.1 )
          time_button_high = time() - start_time
          if float( time_button_high ) < 0.5:
            self.outputconfig.increase_delay()

    except KeyboardInterrupt:
	    GPIO.cleanup() 