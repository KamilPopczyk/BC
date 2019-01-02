from html.parser import HTMLParser
import urllib.request
from contextlib import closing
import socket
import os
import sys
from pathlib import Path


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
# End ButtonCounter class

class WebsiteCounter:
    """Class website counter"""
    __button_sum = 0
    __html_response = ""
    __url = ""

    def __init__(self, url):
        self.__load_website(url)

    def __load_website(self, url):
        """Function responsible for download website's html"""
        if url == 'localhost':                        
            self.__url = 'localhost'
            localhost_url = 'http://localhost:'        # example: http://localhost:8080/'
            used_port = 0
            for port in range(8000, 8081):            # Let's find used port , range is short because of speed
                with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                    res = sock.connect_ex(('localhost', port))
                    if res == 0:
                        used_port = port
            url = localhost_url + str(used_port) + '/'

        else:
            self.__url = url                            # save url
        # end if localhost

        if url.find('https://') and url.find('http://') < 0:
            url = 'http://' + url
        try:
            with urllib.request.urlopen(url) as response:
                self.__html_response = str(response.read())
        except urllib.request.HTTPError:
            print("Can't download website: " + url)
            return False
        except:
            print("Something wrong with website.")
            return False

    def count_buttons(self):
        """Count button on downloaded website"""
        button_counter = ButtonCounter()
        button_counter.feed(self.__html_response)
        self.__button_sum = button_counter.button_sum

    @property
    def give_info(self):                               # return info , url and buttons sum
        """Give url and button sum"""
        return [str(self.__url), str(self.__button_sum)]
# End WebsiteCounter class

def load_file(file_name):
    """Load file with websites"""
    websites_list = []
    if os.path.isfile(file_name):  # exist ?
        with open(file_name, "r") as fileData:
            for data_line in fileData:
                data_line = data_line.replace("\n", "")  # new line?  I don't need that
                websites_list.append(data_line)
        fileData.closed
    else:
        print("File don't exist.")
        return False
    return websites_list


def save_to_file(file_name, websites_list):
    """Save counted buttons to file"""
    file_path = Path(file_name)
    if not file_path.exists():                      # safety first
        with open(file_name, 'w+') as file:
            file.write('address,number_of_buttons ' + '\n')
            for site in websites_list:
                file.write(site[0] + ',' + site[1] + '\n')
        file.closed
    else:
        print("Error, file " + "'" + file_name + "'" + " already exists ")
        return False


def main():
    arguments = sys.argv
    if len(arguments) < 3:
        print("Not enough arguments ! ")
    else:
        websites_list_counted = []                  # save counted websites
        websites_list = load_file(arguments[1])     # websites from file
        if websites_list is False:
            print("Error, check file to load ")
        else:
            for site in websites_list:              # count buttons loop
                counter = WebsiteCounter(site)
                counter.count_buttons()
                websites_list_counted.append(counter.give_info)

            if not save_to_file(arguments[2], websites_list_counted) is False:
                print("Success")


if __name__ == '__main__':
    main()
