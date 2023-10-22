import asyncio
import aiohttp
import json

class CourseDataGenerator:
    def __init__(self):
        self.base_url = "https://www.coursediggers.com/data"
        self.course_ids = range(1, 10628)
        self.course_names_to_ids = {}

    async def fetch_course_data(self, session, course_id):
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
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_course_data(session, course_id) for course_id in self.course_ids]
            results = await asyncio.gather(*tasks)

        self.course_names_to_ids = {name: course_id for name, course_id in results if course_id is not None}

    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.course_names_to_ids, json_file, indent=4)

    def generate_json(self, filename='course_name_to_ids.json'):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.generate_json_data())
        self.save_to_json(filename)

