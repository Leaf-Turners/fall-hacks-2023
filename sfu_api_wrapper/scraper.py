import aiohttp
import asyncio
import json
import os

COURSE_DIGGER_JSON_URL = "http://www.coursediggers.com/data/{}.json"

current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, 'course_name_to_ids.json')
<<<<<<< HEAD

# Load the course name to ID mapping from a JSON file
with open(json_file_path, 'r') as json_file:
    course_name_to_id = json.load(json_file)

=======

    # Load the course name to ID mapping from a JSON file
with open(json_file_path, 'r') as json_file:
    course_name_to_id = json.load(json_file)
>>>>>>> 431f762d58f7adab3218cbd444b5a18298f8e4df

async def fetch_course_data(session, course_id):
    url = COURSE_DIGGER_JSON_URL.format(course_id)
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return data  # Return the JSON data


async def median_getter(course_name):
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

async def failRate(department: str, course_number: str) -> str:
    """
    retrive the fail rate for the course 
    """
    department = department.upper()
    course_name = department + " " + course_number
    if course_name in course_name_to_id:
        course_id = course_name_to_id[course_name]
        async with aiohttp.ClientSession() as session:
            course_data = await fetch_course_data(session, course_id)
        
        if 'name' in course_data and 'data' in course_data:
        
            fail_rate = course_data['data'][0][1]  # Added to retrieve the fail rate
            return fail_rate
        else:
            return "Failed to fetch data for the course."
    else:
        return "Course name not found in the dictionary."
    
async def courseDiggerInfo(department: str, course_number: str) -> dict:
    """
    get json file for for the course digger information
    """
    department = department.upper()
    course_name = department + " " + course_number
    if course_name in course_name_to_id:
        course_id = course_name_to_id[course_name]
        async with aiohttp.ClientSession() as session:
            course_data = await fetch_course_data(session, course_id)
        
        if 'name' in course_data and 'data' in course_data:
            return course_data
        else:
            return "Failed to fetch data for the course."
    else:
        return "Course name not found in the dictionary."

    
if __name__ == '__main__':
    #user_input = input("Enter a course name: ")
    result = asyncio.run(courseDiggerInfo('cmpt', '310'))

    print(result)
