# Web Scraper Using beautifulsoup4 and scapy

from bs4 import BeautifulSoup
import requests


for page in range(1,11):
    print(f"Scraping Data From Page {page}\n")
    url = f"https://internshala.com/internships/python-internship/page-{page}/"
    response = requests.get(url)
    text = response.content
    soup = BeautifulSoup(text, "html.parser")
    internships = soup.find_all('div', class_='internship_meta')

    for internship in internships:
        title = internship.find('a', class_='view_detail_button').text
        company = internship.find('a', class_='link_display_like_text view_detail_button').text.replace('\n                            ', '')
        location = internship.find('a', class_='location_link view_detail_button').text
        stipend = internship.find('span', class_='stipend').text
        published = internship.find('div', class_='status-container').text.replace('\n', '')
        more_info = internship.h3.a['href']

        if 'now' in published or 'hour' in published:
            with open('Few_Hours_Ago.txt', 'a', encoding='utf-8') as file1:
                file1.write(f"Title : {title}\n")
                file1.write(f"Company : {company}\n")
                file1.write(f"Location : {location}\n")
                file1.write(f"Stipend : {stipend}\n")
                file1.write(f"Published : {published}\n")
                file1.write(f"More Info : https://internshala.com/{more_info}\n\n\n")

        if 'day' in published:
            with open('Few_Days_Ago.txt', 'a', encoding='utf-8') as file2:
                file2.write(f"Title : {title}\n")
                file2.write(f"Company : {company}\n")
                file2.write(f"Location : {location}\n")
                file2.write(f"Stipend : {stipend}\n")
                file2.write(f"Published : {published}\n")
                file2.write(f"More Info : https://internshala.com/{more_info}\n\n\n")

        if 'week' in published:
            with open('Few_Weeks_Ago.txt', 'a', encoding='utf-8') as file3:
                file3.write(f"Title : {title}\n")
                file3.write(f"Company : {company}\n")
                file3.write(f"Location : {location}\n")
                file3.write(f"Stipend : {stipend}\n")
                file3.write(f"Published : {published}\n")
                file3.write(f"More Info : https://internshala.com/{more_info}\n\n\n")

print("Scraping Done !")