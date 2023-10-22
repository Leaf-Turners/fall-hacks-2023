import aiohttp
import json

class CourseOutlinesAPI:
    base_url = "http://www.sfu.ca/bin/wcm/course-outlines"

    @classmethod
    async def call_api(cls, url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    elif response.status == 404:
                        print("Course information not found.")
                    else:
                        print(f"API request failed with status code: {response.status}")
            except aiohttp.ClientError as e:
                print(f"Request error: {e}")

    @classmethod
    async def get_data(cls, path):
        url = f"{cls.base_url}/{path}"
        return await cls.call_api(url)

    @classmethod
    async def get_years(cls):
        return await cls.get_data("")

    @classmethod
    async def get_terms(cls, year):
        return await cls.get_data(year)

    @classmethod
    async def get_departments(cls, year, term):
        return await cls.get_data(f"{year}/{term}")

    @classmethod
    async def get_course_numbers(cls, year, term, department):
        return await cls.get_data(f"{year}/{term}/{department}")

    @classmethod
    async def get_course_sections(cls, year, term, department, course_number):
        return await cls.get_data(f"{year}/{term}/{department}/{course_number}")

    @classmethod
    async def get_course_outline(cls, year, term, department, course_number, course_section):
        return await cls.get_data(f"{year}/{term}/{department}/{course_number}/{course_section}")

