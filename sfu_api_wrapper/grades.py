import asyncio
import aiohttp
import json
from typing import Dict, Optional, Any, Tuple

class CourseDataGenerator:
    """
    Generates a mapping of course numbers to Course Digger JSON file IDs for querying purposes.

    The Course Digger website associates an integer with a JSON path file to be queried by an HTTP request.

    Attributes:
        base_url (str): The base URL of the Course Digger data.
        course_ids (range): A range of course IDs to be used for querying.
        course_names_to_ids (dict): A mapping of course names to corresponding Course Digger file IDs.
    """

    def __init__(self):
        self.base_url = "https://www.coursediggers.com/data"
        self.course_ids = range(1, 10628)
        self.course_names_to_ids = {}

    async def fetch_course_data(self, session: aiohttp.ClientSession, course_id: int) -> Tuple[str, Optional[int]]:
        """
        Fetches course data for a given Course Digger file ID.

        Args:
            session (aiohttp.ClientSession): An aiohttp client session.
            course_id (int): The Course Digger file ID to fetch data for.

        Returns:
            Tuple[str, Optional[int]]: A tuple containing the course name and Course Digger file ID.
        """
        url = f"{self.base_url}/{course_id}.json"
        async with session.get(url) as response:
            if response.status == 200:
                try:
                    data = await response.json()
                    return data.get('name', ''), course_id
                except json.JSONDecodeError:
                    pass
            return '', None

    async def generate_json_data(self):
        """
        Generates a mapping of course names to Course Digger file IDs by making asynchronous requests.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_course_data(session, course_id) for course_id in self.course_ids]
            results = await asyncio.gather(*tasks)

        self.course_names_to_ids = {name: course_id for name, course_id in results if course_id is not None}

    def save_to_json(self, filename: str):
        """
        Saves the course names to Course Digger file IDs mapping to a JSON file.

        Args:
            filename (str): The name of the JSON file to save the mapping to.
        """
        with open(filename, 'w') as json_file:
            json.dump(self.course_names_to_ids, json_file, indent=4)

    def generate_json(self, filename: str = 'course_name_to_ids.json'):
        """
        Generates the course names to Course Digger file IDs mapping and saves it to a JSON file.

        Args:
            filename (str, optional): The name of the JSON file to save the mapping to. Default is 'course_name_to_ids.json'.
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.generate_json_data())
        self.save_to_json(filename)

if __name__ == '__main__':
    generator = CourseDataGenerator()
    generator.generate_json()