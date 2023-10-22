from ..requests import CourseOutlinesAPI


async def departments(year: int = 'current', term: str = 'current'):
    return await CourseOutlinesAPI.get_departments(year, term)
