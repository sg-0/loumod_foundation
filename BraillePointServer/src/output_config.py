class OutputConfiguration(object):

  def __init__( self, output_delay = 0.5, vibration = False ):
    self.output_delay = output_delay
    self.min_delay = 0.1
    self.delta_delay = 0.1
    self.vibration = vibration

  def set_vibration( self, vibration ):
    self.vibration = vibration

  def increase_delay( self ):
    self.output_delay += self.delta_delay
    print( "increased delay: {}".format( self.get_delay() ) )

  def decrease_delay( self ):
    if self.output_delay > (self.min_delay + 0.05):
        self.output_delay -= self.delta_delay
        print( "decreased delay: {}".format( self.get_delay() ) )
    else:
        self.output_delay = self.min_delay

  def get_delay( self ):
    return self.output_delay