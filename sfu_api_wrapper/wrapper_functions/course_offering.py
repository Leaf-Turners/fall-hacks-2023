from ..requests import CourseOutlinesAPI
from ..api_classes import course
from ..scraper import get_median_grade
from ..scraper import get_fail_rate


async def course_offering(department: str, number: str, section: str, year: int = 'current', term: str = 'current'):
    raw_data = await CourseOutlinesAPI.get_course_outline(year, term, department, number, section)
    median_grade = await get_median_grade(
        f"{raw_data['info']['dept'].upper()} {raw_data['info']['number']}")
    fail_rate = await get_fail_rate(raw_data['info']['dept'].upper(),
                                    raw_data['info']['number'])

    return_course = course.CourseOutline(raw_data, median_grade, fail_rate)

    return return_course
