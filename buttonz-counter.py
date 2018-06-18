from html.parser import HTMLParser
import urllib.request


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
                    if attr[1].lower().find('btt') >= 0 or attr[1].lower().find('button') >= 0:
                        self.button_sum = self.button_sum + 1


class WebsiteCounter:
    """Class website counter"""
    def __init__(self):
        self.button_sum = 0
        self.html_response = ""

    def load_website(self, url):
        """Function responsible for download website's html"""
        if url is 'localhost':
            localhost = urllib.urlopen("http://localhost:8280/")
            print(localhost.read(100))

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
    cou.load_website('www.boredbutton.com') # poprawic localhost ! www.boredbutton.com
    cou.count_buttons()


if __name__ == '__main__':
    main()