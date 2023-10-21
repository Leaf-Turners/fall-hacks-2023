import aiohttp
import asyncio

class CourseOutlinesAPI:
    base_url = "http://www.sfu.ca/bin/wcm/course-outlines"

    async def callApi(self, url):
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

    async def get_years(self):
        url = f"{self.base_url}"
        return await self.callApi(url)

    async def get_terms(self, year):
        url = f"{self.base_url}?{year}"
        return await self.callApi(url)

    async def get_departments(self, year, term):
        url = f"{self.base_url}?{year}/{term}"
        return await self.callApi(url)

    async def get_course_numbers(self, year, term, department):
        url = f"{self.base_url}?{year}/{term}/{department}"
        return await self.callApi(url)

    async def get_course_sections(self, year, term, department, course_number):
        url = f"{self.base_url}?{year}/{term}/{department}/{course_number}"
        return await self.callApi(url)

    async def get_course_outline(self, year, term, department, course_number, course_section):
        url = f"{self.base_url}?{year}/{term}/{department}/{course_number}/{course_section}"
        return await self.callApi(url)

class Requests:

    @staticmethod
    async def fetch_course_information_async(url: str):
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
    api = CourseOutlinesAPI()

    # Get the list of years
    years = loop.run_until_complete(api.get_years())
    print("Years:", years)

    # Get the list of terms for a specific year
    terms = loop.run_until_complete(api.get_terms("2015"))
    print("Terms:", terms)

    # Get the list of departments for a specific year and term
    departments = loop.run_until_complete(api.get_departments("2015", "summer"))
    print("Departments:", departments)

    # Get the list of course numbers for a specific year, term, and department
    course_numbers = loop.run_until_complete(api.get_course_numbers("2015", "summer", "cmpt"))
    print("Course Numbers:", course_numbers)

    # Get the list of course sections for a specific year, term, department, and course number
    course_sections = loop.run_until_complete(api.get_course_sections("2015", "summer", "cmpt", "110"))
    print("Course Sections:", course_sections)

    # Get a specific course outline for a given year, term, department, course number, and section
    course_outline = loop.run_until_complete(api.get_course_outline("2015", "summer", "cmpt", "110", "c100"))
    print("Course Outline:", course_outline)
