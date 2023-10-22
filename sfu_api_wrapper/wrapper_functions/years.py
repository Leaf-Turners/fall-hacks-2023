from ..requests import CourseOutlinesAPI


async def years():
    return [item['text'] for item in await CourseOutlinesAPI.get_years()]
