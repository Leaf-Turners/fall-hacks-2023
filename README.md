# Python SFU API Wrapper

We used AI to simplify code, and give a foundation for async https communication.

## Description

An asynchronous API wrapper for SFU's API.

In the industry of development, the widespread usage of APIs has become abundant but necessary. With the diversity of
course selection, being able to interact with SFU's course APIs will be able to turn over a new leaf for the scope of
APIs.

## File Structure
```
fall-hacks-2023
├─ .gitignore
├─ README.md
├─ SFU-Course-Diggers-Web-Scraper-master
│  ├─ .gitignore
│  ├─ LICENSE
│  ├─ README.md
│  └─ scraper.py
├─ dist
│  ├─ sfuapiwrapper-1.0.0-py3-none-any.whl
│  └─ sfuapiwrapper-1.0.0.tar.gz
├─ requirements.txt
├─ setup.py
└─ sfu_api_wrapper
   ├─ __init__.py
   ├─ api_classes
   │  ├─ __init__.py
   │  ├─ course.py
   │  ├─ instructor.py
   │  └─ schedule.py
   ├─ course_name_to_ids.json
   ├─ grades.py
   ├─ requests.py
   ├─ scraper.py
   ├─ version.py
   └─ wrapper_functions
      ├─ __init__.py
      ├─ course_offering.py
      ├─ departments.py
      ├─ terms.py
      └─ years.py

```

## Steps To Set Up And Run Project

### Initial Download Setup

1. Download the source code.
2. Make sure you have python installed.
3. Make sure you install `wheel` with pip.
4. Run the command: `python setup.py sdist bdist_wheel`

### Usage

1. Use `pip` to install the module from the `dist` folder, for example: `pip install path/to/local/installation/dist/sfu_api_wrapper-1.0.0.tar.gz`
2. Use the module like this:

```python
import sfu_api_wrapper
import asyncio


async def main():
    data = await sfu_api_wrapper.course_offering('cmpt', '120', 'd100')
    print(data.instructors[0].name)


if __name__ == '__main__':
    asyncio.run(main())
```

Here are the wrapper functions provided by this API wrapper:
- `await sfu_api_wrapper.course_offering('cmpt', '120', 'd100')`
- `await sfu_api_wrapper.departments())`
- `await sfu_api_wrapper.years())`
- `await sfu_api_wrapper.terms(2022)`

The course_offering wrapper function also gets the median grade and fail rate from course diggers.

## Participants
- Kevin Litvin ktl13@sfu.ca   
- Ewan Brinkman erb5@sfu.ca  
- Adam Bahrami afb2@sfu.ca  
- Marcus Yellowley mty5@sfu.ca  
- Nolan Campbell ngc2@sfu.ca

## Acknowledgements
- SFU API https://www.sfu.ca/outlines/help/api.html
- aiohttp
- Course Diggers https://coursediggers.com/

## GitHub Project Repository
https://github.com/Leaf-Turners/fall-hacks-2023

## Video Tutorial

### Video Link (The Max 3 Minute Video Of How To Compile And Run Video)

https://www.dropbox.com/scl/fi/cppz8ws9ucoqktzlxj3vp/setup_example.mp4?rlkey=j8mqp69mqx5gsf16fmdjcq0h2&dl=0

See the bottom of this README for the code used in this video.

### Bonus Video Showing Example Usage Of Our Library

https://www.dropbox.com/scl/fi/iqe3fill4a18lb61uz83q/example_usage.mp4?rlkey=arbvcxrwkr892aik7kth7djfh&dl=0

This video showcases the seamless integration of our Python SFU API Wrapper with the Python Google Calendar API. In this demonstration, we highlight our hackathon project's functionality, which involves retrieving exam and lecture schedules for Fall 2023 CMPT 120 courses from SFU and seamlessly incorporating them into a Google Calendar. This video provides just one example of the versatile applications of our Python SFU API Wrapper project. Please note that the video may have some delay due to the synchronous call times of the Google Calendar API.

For access to the source code used in this video, visit our GitHub repository: https://github.com/Leaf-Turners/GCalendar-SFU-API

### Code Example In The Max 3 Minute How To Compile And Run Video

```python
import sfu_api_wrapper
import asyncio


async def main():
    print("Course offering:\n")
    course_offering = await sfu_api_wrapper.course_offering('cmpt', '120', 'd100')
    print(course_offering.title)
    print(course_offering.instructors[0].name)
    print(course_offering.designation)
    print("(And the course offering class has more more properties)")
    
    print("\n\n\nAll departments:\n")
    departments = await sfu_api_wrapper.departments()
    for department in departments:
        print(department['text'], end=" ")
    
    print("\n\n\nAll terms:")
    terms = await sfu_api_wrapper.terms(2022)
    print(terms)
    
    print("\n\n\nAll years:")
    years = await sfu_api_wrapper.years()
    print(years)
    
    # The wrapper functions can also have a certain year and term specified.
    
    print("\n\n\nCourse offering, specific time (fall 2016):\n")
    course_offering = await sfu_api_wrapper.course_offering('cmpt', '120', 'd100', 2016, 'fall')
    print(course_offering.title)
    print(course_offering.instructors[0].name)
    print(course_offering.designation)
    print("(And the course offering class has more more properties)")
    
    print("\n\n\nAll departments, specific time (spring 2018):\n")
    departments = await sfu_api_wrapper.departments(2018, 'spring')
    for department in departments:
        print(department['text'], end=" ")

if __name__ == '__main__':
    asyncio.run(main())
```
