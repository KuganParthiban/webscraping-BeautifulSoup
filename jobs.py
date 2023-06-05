import csv
from bs4 import BeautifulSoup
import requests

base_url = 'https://www.jobstreet.com.my/python-jobs'
page_number = 1

# Create a CSV file and write the header
with open('jobs_python.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Salary', 'Location'])

    while True:
        # Make a GET request to the current page
        url = f'{base_url}?page={page_number}'
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')

        # Find job listings on the current page
        jobs = soup.find_all('div', class_='z1s6m00 _1hbhsw67i _1hbhsw66e _1hbhsw69q _1hbhsw68m _1hbhsw6n _1hbhsw65a _1hbhsw6ga _1hbhsw6fy')

        # Exit the loop if no jobs are found
        if not jobs:
            break

        # Process each job on the current page
        for job in jobs:
            job_title = job.find('h1', class_="z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ii").text
            location_and_salary = job.find_all('span', class_='z1s6m00 _1hbhsw64y y44q7i0 y44q7i3 y44q7i21 y44q7ih')

            # Extract the location and salary from the list
            location = location_and_salary[0].text if location_and_salary else 'N/A'
            salary = location_and_salary[1].text if len(location_and_salary) > 1 else 'N/A'
            salary = salary.replace('MYR', '').strip()

            # Write the job details to the CSV file
            writer.writerow([job_title, salary, location])

        # Move to the next page
        page_number += 1
