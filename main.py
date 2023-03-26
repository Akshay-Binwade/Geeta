import requests
from bs4 import BeautifulSoup
from vendors.chapterCont import Adhyay
from vendors.search import Shloka

print("Welcome to the Holy Bhagwad Gita...!!!\n")

if __name__ == '__main__':
    print("Please choose from below: ")

    url = "https://www.holy-bhagavad-gita.org"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.content, "html.parser")

    names = soup.find(attrs={"class": "chaptersHolder clearfix"}).find_all(attrs={"class": "chapterDesc"})

    for i in range(18):
        print(f"Adhyay {i+1}:", names[i].text.strip())
    while True:
        basic = input("\nc: Choose Adhyaya\ns: Search\ne: Exit\nPlease select one response from above: ")
        if basic.lower() == "c":
            choice = input("Enter Adhyaya number: ")
            obj = Adhyay()
            obj.description(choice)

        elif basic.lower() == "s":
            c = Shloka()
            c.get_shloka()

        elif basic.lower() == "e":
            break

        else:
            print("Wrong choice, please choose again...")
