from html.parser import HTMLParser
import urllib.request


class WebsiteCounter:
    """Class website counter"""
    def __init__(self):
        self.button_sum = 0
        self.html_response = ''

    def load_website(self, url):
        """Function responsible for download website's html"""
        if not ('https://' or 'http://') in url:
            url = 'https://' + url
        try:
            with urllib.request.urlopen(url) as response:
                self.html_response = response.read()
        except urllib.request.HTTPError:
            print("Can't download website.")
            return False
        except:
            print("Something wrong with website.")
            return False

    def count_buttons(self):





def main():
    cou = WebsiteCounter()
    cou.load_website('onet.pl')


if __name__ == '__main__':
    main()