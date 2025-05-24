import requests
from bs4 import BeautifulSoup
import csv
def scrape_homepage():
    url= "https://nkp.gov.np"
    payload = {'mudda_number': '',
                'faisala_date_from': '',
                'faisala_date_to':'',
                'mudda_type':'',
                'mudda_name':'',
                'badi':'',
                'pratibadi':'',
                'judge':'',
                'ijlas_type':'',
                'nirnaya_number':'',
                'faisala_type':'',
                'keywords':'सम्बन्ध+विच्छेद',
                'edition':'',
                'year':'',
                'month':'',
                'volume':'',
                'Submit':'खोज्%E2%80%8Dनुहोस्#',
                }
    response = requests.get(url,params=payload)

    print(response.headers)
    response.encoding='utf-8'
    soup=BeautifulSoup(response.text,'html.parser')
    print(soup)
    print(soup.find_all('a'))

    for link in soup.find_all('a'):
        if("https://nkp.gov.np/full_detail/" in link.get('href')):
            print(link.get('href'))
            _,_,case_code= link.get('href').partition("https://nkp.gov.np/full_detail/")
            scrape_case(link.get('href'),case_code)

def scrape_case(url,case_code):
    payload={"keywords":"सम्बन्ध%20विच्छेद"}

    response = requests.get(url, params=payload)
    response.encoding='utf-8'
    soup=BeautifulSoup(response.text,'html.parser')

    print(response.text)
    filename="case_no_"+case_code+".html"
    with open(filename, "w", encoding = 'utf-8') as file:

        head_tags=soup.head
        body_tags=soup.find_all('p')

        file.write(str(soup.find_all("p")))
        # file.write(str(soup.prettify()))
        # file.write(str(soup.get_text()))

    with open('case-list.csv', 'a', newline='') as csvfile:
        casewriter = csv.writer(csvfile, delimiter=' ',)
        casewriter.writerow(case_code)

if __name__ == "__main__":
    scrape_homepage()