from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    content = file.read()


soup = BeautifulSoup(content, "html.parser")

form_tag = soup.find("input")
max_len = form_tag.get("maxlength")
print(form_tag)
print(max_len)