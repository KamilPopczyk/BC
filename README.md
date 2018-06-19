# Task12

Solution of Task2 - Buttonz Counter

## Getting Started

These instructions will get you how to run.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6
```

### Run

In commandline:

```
sprint-planning-helper.py file_with_websites file_to_save.csv
```

## Tests


### Localhost

Simple script to start server:

```python
import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
```
Index file was the same as in instruction. 

### Results for example input file
Input file:
```
loacalhost
www.boredbutton.com
```
Output file:
```
address,number_of_buttons
localhost,4
www.boredbutton.com,1
```
 
