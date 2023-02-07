from bs4 import BeautifulSoup

with open("teachers.xml", "r") as f:
    file = f.read()

# 'xml' is the parser used. For html files, which BeautifulSoup is typically used for, it would be 'html.parser'.
soup = BeautifulSoup(file, "xml")

names = soup.find_all("name")
for name in names:
    print(name.text)
