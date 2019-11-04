import re
import urllib.request
from bs4 import BeautifulSoup

class Proxy:
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    cols = ['last_updated', 'ip', 'port', 'country', 'blank', 'type', 'response']
    def __init__(self, link):
        self.link = link
        self.top_proxies = None
        self.soup = self.make_soup()
        self.order_proxy()
    def make_soup(self):
        request = urllib.request.Request(self.link, headers=Proxy.headers)
        response = urllib.request.urlopen(request, timeout=10)
        response_data = response.read().decode("utf-8")
        soup = BeautifulSoup(response_data, 'html.parser')
        return soup
    def order_proxy(self):
        rows = self.soup.find_all('td',)
        rows = rows[1:]
        proxies = {
            'last_updated': [],
            'ip': [],
            'port': [],
            'country': [],
            'blank': [],
            'type': [],
            'response': []
        }
        for index, val in enumerate(rows):
            index = index % 7
            val = re.sub(r'<.*?>' , '',str(val))
            if index == 1 or index == 2:
                val = re.split(r'\'' ,str(val))[1]
            if index == 6:
                val = int(val[:-2])
                proxies[Proxy.cols[index]].append(val)
            else:
                proxies[Proxy.cols[index]].append(val)
        top_response_index = sorted(range(len(proxies['response'])),
                                    key=lambda i: proxies['response'][i])
        self.top_proxies = []
        for index in top_response_index:
            if proxies['type'][index] == "SOCK5":
                val = proxies['ip'][index] + ':' + str(proxies['port'][index])
                self.top_proxies.append(val)
    def print_all_proxies(self):
        if self.top_proxies:
            for p in self.top_proxies:
                print(p)
        else:
            print("Please define proxy list!")
    def get_proxy(self):
        if self.top_proxies:
            return self.top_proxies[0]
        else:
            print("No proxy found!")
            return None
    def delete_proxy(self):
        self.top_proxies = self.top_proxies[1:]


#print(response_data)
link = 'http://www.gatherproxy.com/sockslist'
p = Proxy(link)