import requests
from urllib.parse import unquote

link = []
reverse = False
link.append("https://r3---sn-huoa-qxal.googlevideo.com/videoplayback?txp=5533432&gir=yes&key=yt6&signature=CC6BBCFD44A768E6D154A165A3675C750E72E1F9.AEEC8329DE57C2F128397DBE7F4712FB224BCF88&lmt=1540058598602900&source=youtube&dur=293.941&requiressl=yes&fvip=3&itag=140&expire=1552497668&keepalive=yes&id=o-AHYKb3lZYVhr5Ye2ueP9LSeQ45e0nsDg4tiFctsjSkj1&mm=31%2C29&mn=sn-huoa-qxal%2Csn-qxa7snel&ei=pOeIXI2-MpXcoAPk_KiwAg&clen=4669189&ms=au%2Crdu&mt=1552475976&mv=m&pl=20&ip=59.177.132.14&initcwndbps=175000&ipbits=0&c=WEB&mime=audio%2Fmp4&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Crequiressl%2Csource%2Cexpire")
link.append("https://r3---sn-huoa-qxal.googlevideo.com/videoplayback?txp=5511222&gir=yes&key=yt6&signature=B9B4A0215DBEA881393961BB4D69E1D2EEE67BF5.BB0C26DE948B8FF4E81D3BC47BD225F793EBFA8B&lmt=1540073703913045&source=youtube&dur=293.901&requiressl=yes&fvip=3&itag=249&expire=1552497668&keepalive=yes&id=o-AHYKb3lZYVhr5Ye2ueP9LSeQ45e0nsDg4tiFctsjSkj1&mm=31%2C29&mn=sn-huoa-qxal%2Csn-qxa7snel&ei=pOeIXI2-MpXcoAPk_KiwAg&clen=2067741&ms=au%2Crdu&mt=1552475976&mv=m&pl=20&ip=59.177.132.14&initcwndbps=175000&ipbits=0&c=WEB&mime=audio%2Fwebm&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Crequiressl%2Csource%2Cexpire")
for url in link:    
    url = unquote(url)
    headers = {"content-type": "audio/webm",
                "Content-Encoding": "gzip",
                "Accept-Encoding": "identity;q=1, *;q=0",
                "Range": "bytes=0-",
                "Content-Range": "bytes 0-1042000/142001",
                "Server": "gvs 1.0",
                "chrome-proxy": "frfr",
                "Referer": url,
                "accept-ranges": "bytes",
                "alt-svc": "quic=':443'; ma=2592000; v='46,44,43,39'",
                "client-protocol": "quic",
                "cache-control": "private, max-age=21247",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}

    separated = url.split('?')
    params = dict(item.split('=') for item in separated[1].split('&'))

    r = requests.get(separated[0], params=params, headers=headers)
    name = "high.webm"
    if reverse == True:
        name = "low.webm"
    reverse = True
    with open(name, 'wb') as f:
          f.write(r.content)

'''
"Content-Encoding": "gzip",
"Accept-Encoding": "identity;q=1, *;q=0",
"Range": "bytes=0-",
"Content-Range": "bytes 0-1042000/142001",
'''
