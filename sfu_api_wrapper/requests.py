import aiohttp
import json


class CourseOutlinesAPI:
    base_url = "http://www.sfu.ca/bin/wcm/course-outlines"

    @staticmethod
    async def call_api(url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        course_data = await response.text()
                        return json.loads(course_data)
                    elif response.status == 404:
                        print("Course information not found.")
                        return None
                    else:
                        print(f"API request failed with status code: {response.status}")
                        return None
            except aiohttp.ClientError as e:
                print(f"Request error: {e}")
                return None

    @staticmethod
    async def get_years():
        url = f"{CourseOutlinesAPI.base_url}"
        return await CourseOutlinesAPI.call_api(url)

    @staticmethod
    async def get_terms(year):
        url = f"{CourseOutlinesAPI.base_url}?{year}"
        return await CourseOutlinesAPI.call_api(url)

    @staticmethod
    async def get_departments(year, term):
        url = f"{CourseOutlinesAPI.base_url}?{year}/{term}"
        return await CourseOutlinesAPI.call_api(url)

    @staticmethod
    async def get_course_numbers(year, term, department):
        url = f"{CourseOutlinesAPI.base_url}?{year}/{term}/{department}"
        return await CourseOutlinesAPI.call_api(url)

    @staticmethod
    async def get_course_sections(year, term, department, course_number):
        url = f"{CourseOutlinesAPI.base_url}?{year}/{term}/{department}/{course_number}"
        return await CourseOutlinesAPI.call_api(url)

    @staticmethod
    async def get_course_outline(year, term, department, course_number, course_section):
        url = f"{CourseOutlinesAPI.base_url}?{year}/{term}/{department}/{course_number}/{course_section}"
        return await CourseOutlinesAPI.call_api(url)
