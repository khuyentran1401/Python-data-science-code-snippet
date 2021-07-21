from yarl import URL 

url = URL('https://github.com')
new_url = url/ "search" % 'q=data+science'
print(new_url) # https://github.com/search?q=data+science

print(new_url.host) # github.com
print(new_url.path) # /search
print(new_url.query_string) # q=machine learning


