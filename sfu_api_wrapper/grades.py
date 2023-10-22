import asyncio
import aiohttp
import json


async def fetch_course_data(session, course_id):
    url = f"https://www.coursediggers.com/data/{course_id}.json"
    async with session.get(url) as response:
        if response.status == 200:
            try:
                data = await response.json()
                return course_id, data
            except json.JSONDecodeError:
                pass
                # print(f"Failed to decode JSON for course ID {course_id}")
        else:
            pass
            # print(
            #     f"Request failed for course ID {course_id}: {response.status}")
        return course_id, None


async def main():
    course_ids = range(1, 10628)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_course_data(session, course_id) for course_id in
                 course_ids]
        results = await asyncio.gather(*tasks)

    course_data = {course_id: data for course_id, data in results if
                   data is not None}

    course_names_to_ids = {data.get('name', ''): course_id for course_id, data in results if data is not None}

    with open('course_names_to_ids.json', 'w') as json_file:
        json.dump(course_names_to_ids, json_file, indent=4)

    # You can now work with the `course_data` dictionary
    # print(course_data)
    # For example, if you want to access the data for course ID 123:
    data_for_course_123 = course_data.get(123)
    print(data_for_course_123)
    print(course_names_to_ids['BPK 111'])


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
