from yandex_translate import YandexTranslate

class Yanslate:
    def __init__( self, key ):

            self.translate = YandexTranslate( key )
        

    def detect( self, text ):

        print('Detect language:', self.translate.detect( text ))
       
        
    def list( self ):
        print('Languages:', self.translate.langs)


    def trans( self,text, lang ):

    	return ('Translate:', self.translate.translate(text, lang))
