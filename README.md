# Python API Wraper
Fall hacks 2023.

## Description

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
   ├─ course_names_to_ids.json
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

## Steps

## Participants
- Kevin Litvin ktl13@sfu.ca   
- Ewan Brinkman erb5@sfu.ca  
- Adam Bahrami afb2@sfu.ca  
- Marcus Yellowley mty5@sfu.ca  
- Nolan Campbell ngc2@sfu.ca

## Acknowledgements
- SFU API https://www.sfu.ca/outlines/help/api.html
- aiohttp

## GitHub Project Repository
https://github.com/Leaf-Turners/fall-hacks-2023

## Video Tutorial


## Build

Run the command: `python setup.py sdist bdist_wheel`

## Usage

1. Use `pip` to install the module from the `dist` folder, for example: `pip install path/to/local/installation/dist/sfuapiwrapper-1.0.0.tar.gz`
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
