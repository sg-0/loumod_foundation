#!/usr/bin/python


from queue import Queue
from time import sleep
from button_reader import ButtonReader
from output_config import OutputConfiguration
from braille_actuator import BrailleActuator
from communication_handler import CommunicationHandler

def main():
    fifo = Queue()
    output_config = OutputConfiguration( 2 )
    button_reader = ButtonReader( output_config )
    button_reader.start()
    braille_actuator = BrailleActuator( fifo, output_config )
    braille_actuator.start()
    communication_handler = CommunicationHandler( fifo )
    communication_handler.start()
    communication_handler.join()
    #test( fifo )


def test( fifo ):

    # MeteoSwiss
    braille_bytes = b'\x02\x00\x10BS)Im\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03'
    for bit in braille_bytes:
        fifo.put( bit )

    # Bluefruit LE 
    braille_bytes = b'\x02\x00\x10BS\xc3\x07%\x11\x0b\x17%\n\x1e\x00GQ\x03'
    for bit in braille_bytes:
        fifo.put( bit )

    # Play Store
    braille_bytes = b'\x02\x00\x10BSO\x07\x01=\x00N\x1e\x15\x17\x11\x00\x00\x03'
    for bit in braille_bytes:
        fifo.put( bit )

    # Notizen
    braille_bytes = b'\x02\x00\x10BS]\x15\x1e\n5\x11\x1d\x00\x00\x00\x00\x00\x03'
    for bit in braille_bytes:
        fifo.put( bit )

if __name__ == "__main__": main()


