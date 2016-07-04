from lib.yanslate import Yanslate
#from lib.record import Record
from lib.text import Text, Speech
#from lib.speech import speech
#from lib.record1 import record_to_file
import os
import sys

yan = Yanslate( 'api_key' )
s = Speech( 'username', 'password' )
t = Text( 'username', 'password' )

while True:
	try:	
		print "Talk"
		# record_to_file('poop.wav') this doesnt work on some systems best if we just use arecord
                os.system('arecord -r 48000 -f S16_LE -d 5 poop.wav 2>/dev/null')
                print "Getting text"
		res = t.getText( 'poop.wav' )
		translate = res['results'][0]['alternatives'][0]['transcript']
                print "Translating text"
                lang = 'fr'
		ass = yan.trans(translate , lang)
                trans = u'{}'.format( ass[1]['text'][0] )
                print "{} translated to {} is: {}".format( translate, lang, trans  )
                s.voices( lang )
		s.getSpeech( trans ) # i know sloppy coding but idgaf
		os.system('aplay p1.wav 2>/dev/null')

	except KeyboardInterrupt:
		print()
		sys.exit()
	except IndexError:
		pass
        except Exception, e:
                print e

