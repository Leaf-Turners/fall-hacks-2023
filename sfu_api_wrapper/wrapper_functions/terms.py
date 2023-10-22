from ..requests import CourseOutlinesAPI


async def terms(year: int):
    return [item['value'] for item in await CourseOutlinesAPI.get_terms(year)]
