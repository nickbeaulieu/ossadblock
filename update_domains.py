#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

import requests


def get_lines_from_url(url):
    response = requests.get(url, timeout=5)
    print('Response code: ', response.status_code)
    lines = response.text.splitlines()
    return lines 


url_list = []

# Domain list
lines = get_lines_from_url("https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt")

for line in lines:
    if "#" not in line and "/0.0.0.0" not in line: 
        line = line.replace('address=/', '')
        line = line.replace('/::', '')
        assert '/' not in line, "/ artifact found" 
        assert ":" not in line, ": artifact found"
        url_list.append(line)


# Hostnames List
lines = get_lines_from_url("https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt")

for line in lines:
    if "#" not in line and "0.0.0.0" not in line: 
        line = line.replace(':: ', '')
        assert '/' not in line, "/ artifact found" 
        assert ":" not in line, ": artifact found"
        url_list.append(line)


with open( 'domains_to_block.js', 'w+' ) as f:
    print('const blocked = [', file=f)
    for url in url_list:
        print('"*://*.' + url + '/*",', file=f)
    print('];', file=f)


url = 'https://javascript-minifier.com/raw'
data = {'input': open('domains_to_block.js', 'rb').read()}
response = requests.post(url, data=data)

print(response.text)