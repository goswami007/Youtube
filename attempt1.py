import urllib.request
import re
import html
import librosa.effects
import wave
import sys
import pyaudio
import numpy as np
import time


class Fetch:
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    def __init__(self, link):
        request = urllib.request.Request(link, headers=Fetch.headers)
        response = urllib.request.urlopen(request, timeout=5)
        self.response_data = response.read().decode("utf-8")
        self.link = ""

    def extract(self):
        pattern = re.compile(
            r'"(https:\\/\\/r.{1,2}---sn-huoa-qxal\.googlevideo\.com\\/videoplayback\?.{,700}mime=audio.*?)"')
        matches = pattern.findall(self.response_data)

        for link in matches:
            link = link.replace("\\\\u0026", "&")
            self.link = link.replace("\\", "")
            print(self.link)
        exit()

    def download(self):
        print("downloading...")
        with urllib.request.urlopen(self.link, timeout=10) as response, open("downloaded.weba", 'wb') as file:
            data = response.read()
            np_data = np.frombuffer(data)
            rate = 44100
            librosa.output.write_wav('new.wav', np_data, rate)
            file.write(data)
            base = os.path.splitext(file)[0]
            os.rename(file, base + ".wav") 
        print("done")
        #exit()

class Song:
    def __init__(self, url):
        self.link = Fetch(url)
        self.link.extract()
        self.play = Play(self.link)
        self.link.download()

    def play_song(self):
        self.play.start_stream()

    def pitch_shift(self, pitch):
        self.play.pitch = pitch

def main():
    site = "https://www.youtube.com/watch?v=dGwau9Vcc0o"
    pitch = 4

    new_music = Song(site)
    #new_music.play_song()
    #new_music.pitch_shift(pitch)

if __name__ == "__main__":
    main()
'''
original
https://r3---sn-qxa7sn7r.googlevideo.com/videoplayback?expire=1552146815&id=o-AIs0CwmBHwVGF2z-OpyD8H_VdwaIUTwPeWD9X0yZ9Cvs&lmt=1552118125432667&ip=59.177.110.204&ei=H42DXIbtM-S4z7sP2aiW6AU&pl=18&source=youtube&sparams=clen,dur,ei,expire,gir,id,ip,ipbits,itag,keepalive,lmt,mime,mm,mn,ms,mv,pl,requiressl,source&keepalive=yes&c=WEB&mime=audio%2Fwebm&clen=2281958&fvip=3&ipbits=0&requiressl=yes&txp=3511222&dur=345.161&itag=249&signature=581A585F86A60758832710662C9336ECA3ACA98C.52DAEE63A217A526D179BEBEA2EEBEF7DD2CFA28&key=cms1&gir=yes&redirect_counter=1&cm2rm=sn-huoa-qxal7s&req_id=e1e34410e6ffa3ee&cms_redirect=yes&mm=29&mn=sn-qxa7sn7r&ms=rdu&mt=1552125565&mv=m

mine
https://r3---sn-huoa-qxal.googlevideo.com/videoplayback?expire=1552146815&id=o-AIs0CwmBHwVGF2z-OpyD8H_VdwaIUTwPeWD9X0yZ9Cvs&lmt=1552118125432667&ip=59.177.110.204&ei=H42DXIbtM-S4z7sP2aiW6AU&pl=18&initcwndbps=191250&source=youtube&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Crequiressl%2Csource%2Cexpire&keepalive=yes&c=WEB&mime=audio%2Fwebm&clen=2281958&fvip=3&ipbits=0&mm=31%2C29&requiressl=yes&txp=3511222&dur=345.161&ms=au%2Crdu&mv=m&mt=1552125132&itag=249&mn=sn-huoa-qxal%2Csn-qxa7sn7r&signature=198740DFD8A843A267EBEFFDACC2C96C5FB055DA.A474D90830BE80B5C67A2CB461B6E3564FA48527&key=yt6&gir=yes

'''