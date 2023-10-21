import requests
import sqlite3

import requests

COURSE_DIGGER_JSON_URL = "http://www.coursediggers.com/data/{}.json"

# Create a dictionary to map course names to IDs
course_name_to_id = {}

def populate_course_name_to_id():
    for course_id in range(1, 10627):
        course_url = COURSE_DIGGER_JSON_URL.format(course_id)
        course_data = requests.get(course_url)
        if course_data.status_code == requests.codes.ok:
            course_data_json = course_data.json()
            if 'name' in course_data_json:
                course_name = course_data_json['name']
                course_name_to_id[course_name] = course_id

def main():
    populate_course_name_to_id()
    user_input = input("Enter a course name: ")

    if user_input in course_name_to_id:
        course_name = user_input
        course_id = course_name_to_id[course_name]

        course_url = COURSE_DIGGER_JSON_URL.format(course_id)
        course_data = requests.get(course_url)

        if course_data.status_code == requests.codes.ok:
            course_data_json = course_data.json()
            print(f"Course Name: {course_data_json['name']}")
            print(f"Median Grade: {course_data_json['data'][0][0]}")
            # Add more attributes as needed
        else:
            print("Failed to fetch data for the course.")
    else:
        print("Course name not found in the dictionary.")

if __name__ == '__main__':
    main()
