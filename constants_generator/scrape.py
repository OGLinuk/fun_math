'''
Math Constants Scraper
https://en.wikipedia.org/wiki/List_of_mathematical_constants
'''
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

def main():

    # BeautifulSoup implementation
    url = 'https://en.wikipedia.org/wiki/List_of_mathematical_constants'
    sauce = uReq(url)
    page_html = sauce.read()
    sauce.close()
    soup = bs(page_html, "html.parser")

    # HTML parsing
    containers = soup.find_all('small')
    for container in containers:
        try:
            float(container.get_text())
            print(container.get_text())

            with open('constants.txt', 'ab+') as f:
                f.write(bytes('{}\n'.format(container.get_text()), 'UTF-8'))

        except Exception as e:
            print(str(e))
            with open('errors.txt', 'ab+') as f:
                f.write(bytes('{}\n'.format(str(e)), 'UTF-8'))
            continue

if __name__ == '__main__':
    main()
