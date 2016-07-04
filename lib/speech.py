import pyttsx
class speech:
    def __init__( self ):
        self.engine = pyttsx.init()
    def say( self, data ):
        self.engine.say(data)
        
        #self.engine = pyttsx.init()

    def __del__( self ):
    	self.engine.runAndWait()
