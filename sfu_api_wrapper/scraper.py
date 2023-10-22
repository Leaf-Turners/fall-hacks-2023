import aiohttp
import asyncio
import json
import os

COURSE_DIGGER_JSON_URL = "http://www.coursediggers.com/data/{}.json"

current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, 'course_name_to_ids.json')

# Load the course name to ID mapping from a JSON file
with open(json_file_path, 'r') as json_file:
    course_name_to_id = json.load(json_file)


async def fetch_course_data(session, course_id):
    
    """
    This function fetches course data from CourseDiggers using the provided session and course ID.
    
    Args:
        session (aiohttp.ClientSession): An aiohttp session for making HTTP requests.
        course_id (int): The unique identifier for the course on CourseDiggers.

    Returns:
        json dictionary: Based on the session and course_id, return the json containing the course data,
        such as keys that include the coursename, the course median grade and the fail rate.
        The data requested returns None if the data cannot be fetched and we cannot retrieve data 
        from CourseDiggers at that specific ID.
    """
    
    url = COURSE_DIGGER_JSON_URL.format(course_id)
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return data  # Return the JSON data


async def get_median_grade(course_name):

    """
    Retrieves the median grade for a given course and returns it as a string.

    Args:
        course_name (str): The course name in the format "DEPARTMENT COURSE_NUMBER," e.g., "CMPT 310."

    Returns:
        str: If the formatted course name was a key inside our dictionary in the JSON file course_name_to_id, we'd retrieve the value
        which is the Course Digger website id. At this website id, we retrieve the course name and median grade, e.g., "Course Name: CMPT 310, Median Grade: 80.5."
        Otherwise, it returns an error message if the course data cannot be fetched.
    """
    
    if course_name in course_name_to_id:
        course_id = course_name_to_id[course_name]
        async with aiohttp.ClientSession() as session:
            course_data = await fetch_course_data(session, course_id)
        
        if 'name' in course_data and 'data' in course_data:
            course_name = course_data['name']
            median_grade = course_data['data'][0][0]
            return median_grade
        else:
            return "Failed to fetch data for the course."
    else:
        return "Course name not found in the dictionary."


async def get_fail_rate(department: str, course_number: str) -> str:

    """
    Retrieves the fail rate for a given course and returns it as a string.

    Args:
        department (str): The department abbreviation, e.g., "CMPT."
        course_number (str): The course number, e.g., "310."

    Returns:
        str: If the formatted department and course_number was a key inside our dictionary in the JSON file course_name_to_id, we'd retrieve the value
        which is the Course Digger website id. At this website id, we retrieve a string containing the fail rate for the course.
        Otherwise, returns an error message if the course data cannot be fetched.
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
    Retrieves detailed course information from CourseDiggers API.

    Args:
        department (str): The department abbreviation, e.g., "CMPT."
        course_number (str): The course number, e.g., "310."

    Returns:
        dict: If the formatted department and course_number was a key inside our dictionary in the JSON file course_name_to_id, we'd retrieve the value
        which is the Course Digger website id. At this website id, we retrieve a 
        dictionary containing detailed course information where the
        keys may include 'name' and 'data' for course name and grade information.
        Otherwise, returns None if the data cannot be fetched.
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

