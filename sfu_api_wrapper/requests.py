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