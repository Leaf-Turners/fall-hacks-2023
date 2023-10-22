# Python 
Fall hacks 2023.

## Build

Run the command: `python setup.py sdist bdist_wheel`

## Usage

1. Use `pip` to install the module from the `dist` folder, for example: `pip install path/to/local/installation/dist/sfuapiwrapper-1.0.0.tar.gz`
2. Use the module like this:

```python
import sfu_api_wrapper
import asyncio


async def main():
    # Get a course.
    data = await sfu_api_wrapper.course_offering('cmpt', '120', 'd100')
    print(data.instructors[0].name)
        
    # Get a list of all departments.
    print(await sfu_api_wrapper.departments())
    
    # Get all years SFU's API supports.
    print(await sfu_api_wrapper.years())
    
    # Get all terms in a certain year.
    print(await sfu_api_wrapper.terms(2022))


if __name__ == '__main__':
    asyncio.run(main())
```
