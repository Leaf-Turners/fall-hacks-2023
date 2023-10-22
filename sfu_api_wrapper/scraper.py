import aiohttp
import asyncio
import json

COURSE_DIGGER_JSON_URL = "http://www.coursediggers.com/data/{}.json"

# Load the course name to ID mapping from a JSON file
with open('course_names_to_ids.json', 'r') as json_file:
    course_name_to_id = json.load(json_file)

async def fetch_course_data(session, course_id):
    url = COURSE_DIGGER_JSON_URL.format(course_id)
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return data  # Return the JSON data

async def main():
    user_input = input("Enter a course name: ")
    if user_input in course_name_to_id:
        course_id = course_name_to_id[user_input]

        print(f"Fetching data for {user_input}...")

        async with aiohttp.ClientSession() as session:
            course_data = await fetch_course_data(session, course_id)

        if 'name' in course_data:
            print(f"Course Name: {course_data['name']}")
            print(f"Median Grade: {course_data['data'][0][0]}")
            # Add more attributes as needed
        else:
            print("Failed to fetch data for the course.")
    else:
        print("Course name not found in the dictionary.")

if __name__ == '__main__':
    asyncio.run(main())
