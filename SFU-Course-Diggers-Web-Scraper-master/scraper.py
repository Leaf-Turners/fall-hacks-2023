import aiohttp
import asyncio

COURSE_DIGGER_JSON_URL = "http://www.coursediggers.com/data/{}.json"

# Create a dictionary to map course names to IDs
course_name_to_id = {}

async def fetch_all_course_data():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_course_data(session, course_id) for course_id in range(1, 10627)]
        await asyncio.gather(*tasks)

async def fetch_course_data(session, course_id):
    url = COURSE_DIGGER_JSON_URL.format(course_id)
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            if 'name' in data:
                course_name = data['name']
                course_name_to_id[course_name] = course_id

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all_course_data())

    # Print the course name to ID mapping dictionary
    print("Course Name to ID Mapping:")
    for name, course_id in course_name_to_id.items():
        print(f"{name}: {course_id}")

    user_input = input("Enter a course name: ")

    if user_input in course_name_to_id:
        course_name = user_input
        course_id = course_name_to_id[course_name]

        print(f"Fetching data for {course_name}...")

        loop.run_until_complete(fetch_course_data(course_id))
        
        if course_id in course_name_to_id:
            course_data_json = course_name_to_id[course_id]
            print(f"Course Name: {course_data_json['name']}")
            print(f"Median Grade: {course_data_json['data'][0][0]}")
            # Add more attributes as needed
        else:
            print("Failed to fetch data for the course.")
    else:
        print("Course name not found in the dictionary.")

if __name__ == '__main__':
    main()
