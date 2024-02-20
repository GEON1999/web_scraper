import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-front-end-programming-jobs#job-listings"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", "jobs").find_all("li", "feature")

i = 0

for job in jobs :
    i = i + 1
    company, position, region = job.find_all("span", "company")
    company = company.text
    position = position.text
    region = region.text
    title = job.find("span", "title").text
    print("company :", company, "/ position :", position, "/ region :", region, "/ title :", title, f"------{i}\n")


