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

async def medianGetter(course_name):
    if course_name in course_name_to_id:
        course_id = course_name_to_id[course_name]
        async with aiohttp.ClientSession() as session:
            course_data = await fetch_course_data(session, course_id)
        
        if 'name' in course_data and 'data' in course_data:
            course_name = course_data['name']
            median_grade = course_data['data'][0][0]
            return f"Course Name: {course_name}, Median Grade: {median_grade}"
        else:
            return "Failed to fetch data for the course."
    else:
        return "Course name not found in the dictionary."

if __name__ == '__main__':
    user_input = input("Enter a course name: ")
    result = asyncio.run(medianGetter(user_input))
    print(result)
