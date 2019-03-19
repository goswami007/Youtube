'''
upload_size? : this is the first request that is sent and replies with a number(22921)
get_media: this request gets sent just after the above request
upload_metadata: send all information in this header
uploader.php
uploader.php
up_speed
up_speed
upcode: this gives file id and upload code(success/failure)
get_file_status: will give the url of the file to download

file_id: 5ed60f7022df43d398bde2945f44c057
session_id: ec64e5ad5103e8ca4519fd5338cbd6d2
user_fn: URL: https://goalkicker.com/AngularJSBook/
user_fn_hash: 1c18d1a7700afd26569cc47c5c6eda21
file_source: html
file_size: 22047
file_hash: 
file_out_format: GIF
pack_id: 627d76
send_db_token: 
send_gd_token: 
file_url: https://goalkicker.com/AngularJSBook/

'''

#import requests
import cloudconvert
import time

'''
class Convert:
    def __init__(self, url, params={}, type="get"):
        self.headers = {"Content-Type": "text/html; charset=UTF-8",
                    "Cache-Control": "no-cache, private",
                    "Connection": "keep-alive",
                    "Content-Encoding": "gzip",
                    "Server": "nginx"}
        self.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        
        self.params = params

        if type == "post":
            self.r = requests.post(url, data=self.params, timeout=5)
        else:
            self.r = requests.get(url, params=self.params, headers=self.headers)

    def response(self):
        print(self.r.json())
        
'''
if __name__ == "__main__":
    start = time.time()
    print("started")
    api = cloudconvert.Api('11BdTzt6LFSV8KtdoxHMFsGr0WiNjeXO48aaskUW0O7DETx0W7UkmL0GOH8MllLo')
    
    process = api.convert({
    "inputformat": "weba",
    "outputformat": "mp3",
    "input": "upload",
    "file": open('low.weba', 'rb')
    })
    print("Waiting...")
    utime = time.time()
    process.wait()
    waited = time.time()
    print("Waited for:", waited-utime, "seconds")
    print("downloading...")
    process.download()
    end = time.time()
    print("completed in:", end-start, "seconds")






    '''
    convertio = Convert(url="https://api.convertio.co/convert", type="post",
                        params={"file": "https://goalkicker.com/DotNETFrameworkBook/",
                        "outputformat": "pdf", "apikey": "8ff13f25b15ba49b28913802f893be3b",
                        "input": "url"})
    convertio.response()
    
    upload_size = Convert(url="https://convertio.co/process/upload_size",
                    {"url":"https://goalkicker.com/AndroidBook/"},
                    type="get")
    get_media = Convert(url="https://convertio.co/process/get_media",
                    {"url":"https://goalkicker.com/AndroidBook/"},
                    type="post")

    upload_size.response()
    get_media.response()
    '''
'''
from openal import *
import pyogg
import time

source = oalOpen("new1.opus", ext_hint="webm")

source.play()

while source.get_state() == AL_PLAYING:
    time.sleep(1)
    
# remember, don't forget to quit
    oalQuit()
'''