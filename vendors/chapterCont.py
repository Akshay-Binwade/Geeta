import requests
from bs4 import BeautifulSoup
from vendors.search import Shloka


class Adhyay:
    ''' Here the urls are assembled according to the selected language and the info about chosen adhyay is printed.'''
    def __init__(self):
        self.url_eng = "https://www.holy-bhagavad-gita.org/chapter/{}"
        self.url_hindi = "https://www.holy-bhagavad-gita.org/chapter/{}/hi"
        while True:
            self.lang = input("Please choose language, (English-1, Hindi-2): ")
            if self.lang not in ["1","2"]:
                print("Wrong choice...!!!")
            else:
                break

    def description(self,number: str) -> str:
        ''' First prints description of chosen adhyay and allows to find shlokas from it'''
        if self.lang == str(1):
            self.url = self.url_eng.format(number)
        else:
            self.url = self.url_hindi.format(number)

        resp = requests.get(self.url)

        soup = BeautifulSoup(resp.content, "html.parser")

        original = soup.find(attrs={"class":"chapterIntro"}).contents
        # breakpoint()
        for i in original:
            print(i.text)
        total = soup.find(attrs={"class":"verseTable clearfix"}).find_all("a")[-1]
        print(f"There are total {total.text.strip()} shlokas in this adhyaya")

        a=0
        # while True:
        while a != "c":
            decide = input("Want to continue to explore shlokas? (y/n): ")
            if decide.lower() == "y":
                while a!="c":
                    num_ = input("Please Enter shloka no: ")
                    while True:
                        if self.lang == str(1):
                            self.url_b = self.url.format(number) + f"/verse/{num_}"
                            # print(self.url_b)
                        else:
                            self.url_b = self.url_hindi.format(f"{number}/verse/{num_}")
                            # print(self.url_b)

                        s = Shloka()
                        s.part_shloka(self.url_b)

                        a = input("\nn: Next\ns: Search\nc: Cancel\n")
                        if a.lower()=="n":
                            num_ = str(int(num_)+ 1)
                        elif a.lower()=="s":
                            break
                        elif a.lower()=="c":
                            break

            elif decide.lower() == "n":
                break

            else:
                print("Wrong choice...")


# inp = input("Enter Adhyay no: ")
# c = Adhyay()
# c.description(inp)