# import httpx
# import asyncio

# async def fetch_url(url):
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         return response

# async def main():
#     # urls = ['https://www.sfu.ca/bin/wcm/course-outlines?current/current/macm/101/d100', 'https://www.sfu.ca/bin/wcm/course-outlines?current/current/macm/101/d100']
#     # tasks = [fetch_url(url) for url in urls]

#     # responses = await asyncio.gather(*tasks)

#     data = await fetch_url('https://www.sfu.ca/bin/wcm/course-outlines?current/current/macm/101/d100')
#     import pdb; pdb.set_trace()
#     # for url, response in zip(urls, responses):
#     #     print(f'Response from {url}:\n{response}')

# if __name__ == '__main__':
#     asyncio.run(main())

import aiohttp
import asyncio

async def fetch_course_information_async(department, number, section, year='current', term='current'):
    base_url = "https://www.sfu.ca/bin/wcm/course-outlines?"
    endpoint = f"{year}/{term}/{department}/{number}/{section}"
    url = f"{base_url}?{endpoint}"

    # url = "https://www.sfu.ca/bin/wcm/course-outlines?current/current/macm/101/d100"
    
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
