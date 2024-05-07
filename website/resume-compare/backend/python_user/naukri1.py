import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import csv
BASE_URL = "https://www.careerbuilder.co.in"

urls = []
jobs = []

def get_naukri_url(query):
    base_url = "https://www.careerbuilder.co.in/jobs?keywords="
    search_query = quote_plus(query)
    search_url = base_url + search_query
    
    return search_url

def extract(url):
    headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'}

    response = requests.get(url, headers=headers)
    
    # print(response.status_code)
    if response.status_code == 200:
       # Parse the HTML content
       soup = BeautifulSoup(response.content, "html.parser")
       return soup
    else:
        return None

def transform_url(soup):
    divs = soup.find_all('li', {'class' : ['data-results-content-parent', 'relative bg-shadow']})
    for path in divs:
        try:
            url = BASE_URL + path.find('a', {'class' : ['data-results-content', 'data-results-content block', 'job-listing-item']}).get('href')
        except:
            url = None
        urls.append(url)
    return

def transform(soup):
    try:
        title = soup.find('h1', class_= "h3 dark-blue-text b jdp_title_header upcase").text
    except:
        title = None
    try:
        div_tag = soup.find("div", class_="col big col-mobile-full jdp-left-content")
        description = div_tag.get_text(separator=" ", strip=True)
    except:
        description = None
    try:
        skills = extracted_text = [li.get_text() for li in soup.select("ul.pl0.no-marker li")]
    except:
        skills = None

    Data = {"title": title, "description": description, "skills": skills}
    jobs.append(Data)

# Example usage
search_query = input("Enter your search query: ")
result_url = get_naukri_url(search_query)

# print(result_url)
soup = extract(result_url)
# print(soup)
transform_url(soup)

print(urls)
index = 5
for i in urls:
    if index == 0:
        break
    index = index - 1
    soup = extract(i)
    transform(soup)
    # print(i)


naukri1 = []

for job in jobs:


    naukri1.append(job['description'])

