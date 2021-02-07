# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import requests, json


#python request examples
#https://www.pythonforbeginners.com/requests/using-requests-in-python

#import json
#url = 'https://api.github.com/some/endpoint'
#payload = {'some': 'data'}
#headers = {'content-type': 'application/json'}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    github_url = "https://api.github.com/user/repos"
    data = json.dumps({'name': 'test', 'description': 'some test repo'})
    r = requests.post(github_url, data, auth=('user', '*****'))
    print(r.json)
    print("hello world")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
