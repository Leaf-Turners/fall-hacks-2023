from ..requests import CourseOutlinesAPI
from ..api_classes import course


async def course_offering(department: str, number: str, section: str, year: int = 'current', term: str = 'current'):
    raw_data = await CourseOutlinesAPI.get_course_outline(year, term, department, number, section)
    return_course = course.CourseOutline(raw_data)

    return return_course
