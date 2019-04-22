from bs4 import BeautifulSoup
import urllib.request
html = urllib.request.urlopen("https://www.felixcloutier.com/x86/")
soup = BeautifulSoup(html, 'html.parser')
elem = soup.findAll('a')
allWords =  []
for i in range(1,len(elem)):
    if elem[i].text not in allWords:
        allWords.append(elem[i].text)
print(len(allWords))
f = open("instructionSet.txt", "w")
for i in range(len(allWords)):
    f.write(allWords[i])
    f.write("\n")
