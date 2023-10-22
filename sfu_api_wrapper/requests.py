import aiohttp
import json
from typing import Optional, Dict, Any

class CourseOutlinesAPI:
    base_url = "http://www.sfu.ca/bin/wcm/course-outlines"

    @classmethod
    async def call_api(cls, url: str) -> Optional[Dict[str, Any]]:
        """
        Make an asynchronous API call to the specified URL.

        Args:
            url (str): The URL to make the API request to.

        Returns:
            dict or None: The parsed JSON response data if the request is successful, or None if there's an error.
        """
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
    async def get_data(cls, path: str) -> Optional[Dict[str, Any]]:
        """
        Get data from the API for a specified path.

        Args:
            path (str): The path to append to the base URL for the API request.

        Returns:
            dict or None: The parsed JSON response data if the request is successful, or None if there's an error.
        """
        url = f"{cls.base_url}?{path}"
        return await cls.call_api(url)

    @classmethod
    async def get_years(cls) -> Optional[Dict[str, Any]]:
        """
        Get a list of available years for course outlines.

        Returns:
            dict or None: The parsed JSON response data with years if the request is successful, or None if there's an error.
        """
        return await cls.get_data("")

    @classmethod
    async def get_terms(cls, year: str) -> Optional[Dict[str, Any]]:
        """
        Get a list of available terms for a specific year.

        Args:
            year (str): The year for which terms are requested.

        Returns:
            dict or None: The parsed JSON response data with terms if the request is successful, or None if there's an error.
        """
        return await cls.get_data(year)

    @classmethod
    async def get_departments(cls, year: str, term: str) -> Optional[Dict[str, Any]]:
        """
        Get a list of available departments for a specific year and term.

        Args:
            year (str): The year for which departments are requested.
            term (str): The term for which departments are requested.

        Returns:
            dict or None: The parsed JSON response data with departments if the request is successful, or None if there's an error.
        """
        return await cls.get_data(f"{year}/{term}")

    @classmethod
    async def get_course_numbers(cls, year: str, term: str, department: str) -> Optional[Dict[str, Any]]:
        """
        Get a list of available course numbers for a specific year, term, and department.

        Args:
            year (str): The year for which course numbers are requested.
            term (str): The term for which course numbers are requested.
            department (str): The department for which course numbers are requested.

        Returns:
            dict or None: The parsed JSON response data with course numbers if the request is successful, or None if there's an error.
        """
        return await cls.get_data(f"{year}/{term}/{department}")

    @classmethod
    async def get_course_sections(cls, year: str, term: str, department: str, course_number: str) -> Optional[Dict[str, Any]]:
        """
        Get a list of available course sections for a specific year, term, department, and course number.

        Args:
            year (str): The year for which course sections are requested.
            term (str): The term for which course sections are requested.
            department (str): The department for which course sections are requested.
            course_number (str): The course number for which sections are requested.

        Returns:
            dict or None: The parsed JSON response data with course sections if the request is successful, or None if there's an error.
        """
        return await cls.get_data(f"{year}/{term}/{department}/{course_number}")

    @classmethod
    async def get_course_outline(cls, year: str, term: str, department: str, course_number: str, course_section: str) -> Optional[Dict[str, Any]]:
        """
        Get the course outline for a specific year, term, department, course number, and course section.

        Args:
            year (str): The year for which the course outline is requested.
            term (str): The term for which the course outline is requested.
            department (str): The department for which the course outline is requested.
            course_number (str): The course number for which the course outline is requested.
            course_section (str): The course section for which the course outline is requested.

        Returns:
            dict or None: The parsed JSON response data with the course outline if the request is successful, or None if there's an error.
        """
        return await cls.get_data(f"{year}/{term}/{department}/{course_number}/{course_section}")

