from Scrapper import *

def main():
    page_text = ""
    with open("./rawtest.txt", "r") as f:
        page_text = f.read()
    s = Scrapper(page_text)

if __name__ == "__main__":
    main()
