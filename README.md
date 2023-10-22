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
3. Run the command: `python setup.py sdist bdist_wheel`

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

_To be added._
