<<<<<<< HEAD
import base.py
class CourseOutlinesAPI:
    base_url = "http://www.sfu.ca/bin/wcm/course-outlines"
    
    def response(self, url):
        response = requests.get(url)
        return response.json()

    def get_years(self):
        url = f"{self.base_url}"
        return self.response(url)

    def get_terms(self, year):
        url = f"{self.base_url}?{year}"
        return self.response(url)

    def get_departments(self, year, term):
        url = f"{self.base_url}?{year}/{term}"
        return self.response(url)

    def get_course_numbers(self, year, term, department):
        url = f"{self.base_url}?{year}/{term}/{department}"
        return self.response(url)

    def get_course_sections(self, year, term, department, course_number):
        url = f"{self.base_url}?{year}/{term}/{department}/{course_number}"
        return self.response(url)

    def get_course_outline(self, year, term, department, course_number, course_section):
        url = f"{self.base_url}?{year}/{term}/{department}/{course_number}/{course_section}"
        return self.response(url)
    
    
# Example usage
if __name__ == "__main__":
    api = CourseOutlinesAPI()

    # Get the list of years
    years = api.get_years()
    print("Years:", years)

    # Get the list of terms for a specific year
    terms = api.get_terms("2015")
    print("Terms:", terms)

    # Get the list of departments for a specific year and term
    departments = api.get_departments("2015", "summer")
    print("Departments:", departments)

    # Get the list of course numbers for a specific year, term, and department
    course_numbers = api.get_course_numbers("2015", "summer", "cmpt")
    print("Course Numbers:", course_numbers)

    # Get the list of course sections for a specific year, term, department, and course number
    course_sections = api.get_course_sections("2015", "summer", "cmpt", "110")
    print("Course Sections:", course_sections)

    # Get a specific course outline for a given year, term, department, course number, and section
    course_outline = api.get_course_outline("2015", "summer", "cmpt", "110", "c100")
    print("Course Outline:", course_outline)
    
    
    
    
    
    
    
    
    
    
    
import aiohttp
import asyncio

async def fetch_course_information_async(department, number, section, year='current', term='current'):
    base_url = "https://www.sfu.ca/bin/wcm/course-outlines?"
    endpoint = f"{year}/{term}/{department}/{number}/{section}"
    url = f"{base_url}?{endpoint}"

    url = "https://www.sfu.ca/bin/wcm/course-outlines?current/current/macm/101/d100"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    course_data = await response.text()
                    return course_data
                elif response.status == 404:
                    print("Course information not found.")
                    return None
                else:
                    print(f"API request failed with status code: {response.status}")
                    return None
        except aiohttp.ClientError as e:
            print(f"Request error: {e}")
            return None

# Example usage
if __name__ == "__main__":
    department = 'macm'
    number = '101'
    section = 'd100'

    loop = asyncio.get_event_loop()
    course_info = loop.run_until_complete(fetch_course_information_async(department, number, section))
    
    if course_info:
        print("Course Information:")
        print(course_info)
=======
import aiohttp
import asyncio


class Requests:

    def __init__(self) -> None:
        pass

    async def fetch_course_information_async(url : str):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        course_data = await response.text()
                        return course_data
                    elif response.status == 404:
                        print("Course information not found.")
                        return None
                    else:
                        print(f"API request failed with status code: {response.status}")
                        return None
            except aiohttp.ClientError as e:
                print(f"Request error: {e}")
                return None

# Example usage
if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    course_info = loop.run_until_complete(Requests.fetch_course_information_async("https://www.sfu.ca/bin/wcm/course-outlines?current/current/macm/101/d100"))

    print(course_info)
>>>>>>> 5c2850a166a9ffa2afc7326a7084fcb5cf3d98eb
