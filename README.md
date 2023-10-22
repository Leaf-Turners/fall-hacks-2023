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
    data = await sfu_api_wrapper.course_offering('cmpt', '120', 'd100')
    print(data.instructors[0].name)


if __name__ == '__main__':
    asyncio.run(main())
```
