from .instructor import Instructor
from .schedule import CourseSchedule


class CourseOutline:
    def __init__(self, raw_data):
        raw_data_info = raw_data.get('info', {})

        # Define a list of attribute names
        attribute_names = [
            'outlinePath', 'deliveryMethod', 'departmentalUgradNotes', 'designation',
            'type', 'courseDetails', 'title', 'prerequisites', 'description',
            'name', 'dept', 'educationalGoals', 'classNumber', 'shortNote',
            'number', 'section', 'units', 'corequisites', 'registrarNotes',
            'gradingNotes', 'term', 'notes', 'degreeLevel'
        ]

        # Create attributes dynamically
        for attribute_name in attribute_names:
            setattr(self, attribute_name, raw_data_info.get(attribute_name, ''))

        # Create instructors, course_schedule, and exam_schedule lists
        self.instructors = [Instructor(instructor_data) for instructor_data in raw_data.get('instructor', [])]
        self.course_schedule = [CourseSchedule(schedule_data) for schedule_data in raw_data.get('courseSchedule', [])]
        self.exam_schedule = [CourseSchedule(schedule_data) for schedule_data in raw_data.get('examSchedule', [])]
