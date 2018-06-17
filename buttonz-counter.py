from html.parser import HTMLParser
import urllib.request


class ButtonCounter(HTMLParser):
    """Class button counter"""

    def __init__(self):
        HTMLParser.__init__(self)
        self.button_sum = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            self.button_sum = self.button_sum + 1
            print(tag)
            print("Encountered a start tag:", tag)
            for attr in attrs:
                print("     attr:", attr)


class WebsiteCounter(HTMLParser):
    """Class website counter"""
    def __init__(self):
        self.button_sum = 0
        self.html_response = ""

    def load_website(self, url):
        """Function responsible for download website's html"""
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
    cou.load_website('www.boredbutton.com')
    cou.count_buttons()


if __name__ == '__main__':
    main()