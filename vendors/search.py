import requests
from bs4 import BeautifulSoup

class Shloka:
    def __init__(self):
        self.url = "https://www.holy-bhagavad-gita.org/chapter/{}/verse/{}"

    def get_shloka(self) -> str:
        '''Takes two inputs as adhyaya number and shloka number'''
        chapter = input(("Enter Adhyay no: "))
        verse = input(("Enter Shloka no: "))

        url = self.url.format(chapter, verse)

        while True:
            self.lang = input("Please choose language, (English-1, Hindi-2): ")
            if self.lang not in ["1", "2"]:
                print("Wrong choice...!!!")
            else:
                break

        if self.lang == str(2):
            url = url +"/hi"

        resp = requests.get(url)

        soup = BeautifulSoup(resp.content, "html.parser")

        original = soup.find(attrs={"lang":"sa","id":"originalVerse"}).text.rstrip()
        print(original, "\n")

        # print(soup.prettify())
        mean = soup.find(attrs={"id":"translation"}).text.strip()
        mod_mean = (mean.split())
        print(" ".join(mod_mean[2:]))

    def part_shloka(self, url):
        resp = requests.get(url)

        soup = BeautifulSoup(resp.content, "html.parser")

        original = soup.find(attrs={"lang": "sa", "id": "originalVerse"}).text.rstrip()
        print(original, "\n")

        # print(soup.prettify())
        mean = soup.find(attrs={"id": "translation"}).text
        mod_mean = (mean.split())
        print(" ".join(mod_mean[2:]))

# c = Shloka()
# c.get_shloka()