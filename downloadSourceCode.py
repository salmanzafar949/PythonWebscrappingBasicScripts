import  urllib.request
import  re

urls = ["https://www.google.com","http://www.bbc.com/news","https://stackoverflow.com/"]
i=0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)
while i < len(urls):
    file = urllib.request.urlopen(urls[i])
    # text = file.read().decode('iso-8859-1')
    text = str(file.read())
    title = re.findall(pattern, text)
    print(title)
   # print(text[0:100]) # printing first 100 charatcers from the source code
    i+=1