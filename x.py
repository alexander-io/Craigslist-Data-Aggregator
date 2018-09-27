import re, requests

data  =  requests.get('https://seattle.craigslist.org/search/bia?query=bianchi')

output = re.search('result-row', data.text)

substr = data.text[output.start()-len('<li class="'):]

close_li = re.search('</li>', substr)

print(substr[0:close_li.end()])
