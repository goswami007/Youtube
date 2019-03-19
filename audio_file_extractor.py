import urllib.request
import re
import html
from urllib.parse import unquote

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

##video_link = input("Enter video url: ")
video_link = "https://www.youtube.com/watch?v=wcZofRQFf9c"

request = urllib.request.Request(video_link, headers=headers)
response = urllib.request.urlopen(request, timeout=10)
response_data = response.read().decode("utf-8")

##print(response_data)

search_term = "mime%3Daudio"
re_exp = re.compile(r'(https(.|\n){,1000}' + search_term +'(.|\n){,1000}mv%3Dm)')

find = re_exp.findall(response_data)
if len(find) != 0:
    encoded_link = find[0][0]
    print("Encoded link:", encoded_link)
    
    secure_link = unquote(encoded_link)
    print("Secure link: ", secure_link)



else:
    print("No url found!!!")

##    link = re.split(r'%[0-9A-F][0-9A-F]', encoded_link)
##    print("The url is:", html.unescape(audio_link))
