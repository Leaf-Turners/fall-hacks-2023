from ..requests import CourseOutlinesAPI
from ..api_classes import course
from ..scraper import median_getter


async def course_offering(department: str, number: str, section: str, year: int = 'current', term: str = 'current'):
    raw_data = await CourseOutlinesAPI.get_course_outline(year, term, department, number, section)
    median_grade = median_getter(
        f"{raw_data['info']['dept'].upper()} {raw_data['info']['number']}")

    return_course = course.CourseOutline(raw_data, median_grade)

    return return_course
