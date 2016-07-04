import requests
import shutil
import json

class Text:
    def __init__(  self, uname, pword  ):
        self.api_url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
        self.api_username = uname
        self.api_password = pword

        self.headers={'Content-Type': 'audio/wav'}

    def getText( self, audioFile ):
        audio = open( audioFile, 'rb')
        r = requests.post(self.api_url, data=audio,
                          headers=self.headers,
                          auth=(self.api_username, self.api_password))
        audio.close()
        return (r.json())

class Speech:
    def __init__(  self, uname, pword  ):
        self.default         = 'en-US_AllisonVoice'
        self.api_url         = 'https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?voice='
        self.api_voices      = 'https://stream.watsonplatform.net/text-to-speech/api/v1/voices'
        self.api_username    = uname
        self.api_password    = pword

        self.headers={'Content-Type': 'application/json', 'Accept': 'audio/wav'}

    def getSpeech( self, text ):

        data = {'text': text}
        r = requests.post('%s%s' % (self.api_url, self.default), data=json.dumps(data),
                        headers=self.headers,
                        auth=(self.api_username, self.api_password),
                        stream=True)
        #print r.content
        with open('p1.wav', 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        del r
    def voices( self, lang ):

        r = requests.get(self.api_voices, auth=(self.api_username,self.api_password))
        voices = r.json()
        #print voices['voices']
        for i in voices['voices']:
            #print ' %s => %s' % (i['name'], i['url'])
            if lang in i['name']:
                self.default = i['name'] 
                break

