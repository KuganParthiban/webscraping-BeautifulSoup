from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.jobstreet.com.my/python-jobs').text
soup = BeautifulSoup(html_text, 'lxml')

job = soup.find('div', class_='z1s6m00 _1hbhsw67i _1hbhsw66e _1hbhsw69q _1hbhsw68m _1hbhsw6n _1hbhsw65a _1hbhsw6ga _1hbhsw6fy')


job_title = job.find('h1', class_="z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ii").text
location = job.find_all('span', class_='z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ih')[0].text
salary = job.find_all('span', class_='z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ih')[1].text

print(salary)

