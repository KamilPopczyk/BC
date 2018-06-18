from html.parser import HTMLParser
import urllib.request
from contextlib import closing
import socket


class ButtonCounter(HTMLParser):
    """Class button counter"""

    def __init__(self):
        HTMLParser.__init__(self)
        self.button_sum = 0

    def handle_starttag(self, tag, attrs):
        """Search buttons"""
        if tag == 'button':     # html tag <button>
            self.button_sum = self.button_sum + 1

        if tag == 'input':      # html tag <input> with type = submit,reset,button
            for attr in attrs:
                if attr[0] == 'type':
                    if attr[1] == 'submit' or attr[1] == 'reset' or attr[1] == 'button':
                        self.button_sum = self.button_sum + 1

        if tag == 'a':          # html tag <a> with class which contains keywords: btn, button
            for attr in attrs:
                if attr[0] == 'class':
                    if attr[1].lower().find('btn') >= 0 or attr[1].lower().find('button') >= 0:
                        self.button_sum = self.button_sum + 1



class WebsiteCounter:
    """Class website counter"""
    def __init__(self):
        self.button_sum = 0
        self.html_response = ""

    def load_website(self, url):
        """Function responsible for download website's html"""
        if url is 'localhost':
            locahost_url = 'http://localhost:'     # example: http://localhost:8080/'
            used_port = 0
            for port in range(8000, 8081):            # Let's find used port
                with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                    res = sock.connect_ex(('localhost', port))
                    if res == 0:
                        used_port = port
            try:
                with urllib.request.urlopen(locahost_url + str(port) + '/') as response:
                    self.html_response = str(response.read())
            except urllib.request.HTTPError:
                print("Can't download website.")
                return False
            except:
                print("Unused port: " + str(port))
        # end if localhost
        else:
            if not ('https://' or 'http://') in url:
                url = 'https://' + url
            try:
                with urllib.request.urlopen(url) as response:
                    self.html_response = str(response.read())
            except urllib.request.HTTPError:
                print("Can't download website.")
                return False
            except:
                print("Something wrong with website.")
                return False


    def count_buttons(self):
        html_parser = ButtonCounter()
        html_parser.feed(self.html_response)
        print(html_parser.button_sum)

def main():
    cou = WebsiteCounter()
    cou.load_website('localhost') # poprawic localhost ! www.boredbutton.com
    cou.count_buttons()


if __name__ == '__main__':
    main()