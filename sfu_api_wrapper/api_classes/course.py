from .instructor import Instructor
from .schedule import CourseSchedule
from dataclasses import dataclass


@dataclass
class CourseOutline:
    def __init__(self, raw_data, median_grade):
        raw_data_info = raw_data.get('info', {})

        self.median_grade = median_grade

        self.outline_path = raw_data_info.get('outlinePath', '')
        self.delivery_method = raw_data_info.get('deliveryMethod', '')
        self.departmental_ugrad_notes = raw_data_info.get(
            'departmentalUgradNotes', '')
        self.designation = raw_data_info.get('designation', '')
        self.type = raw_data_info.get('type', '')
        self.course_details = raw_data_info.get('courseDetails', '')
        self.title = raw_data_info.get('title', '')
        self.prerequisites = raw_data_info.get('prerequisites', '')
        self.description = raw_data_info.get('description', '')
        self.name = raw_data_info.get('name', '')
        self.department = raw_data_info.get('dept', '')
        self.educational_goals = raw_data_info.get('educationalGoals', '')
        self.class_number = raw_data_info.get('classNumber', '')
        self.short_note = raw_data_info.get('shortNote', '')
        self.number = raw_data_info.get('number', '')
        self.section = raw_data_info.get('section', '')
        self.units = raw_data_info.get('units', '')
        self.corequisites = raw_data_info.get('corequisites', '')
        self.registrar_notes = raw_data_info.get('registrarNotes', '')
        self.grading_notes = raw_data_info.get('gradingNotes', '')
        self.term = raw_data_info.get('term', '')
        self.notes = raw_data_info.get('notes', '')
        self.degree_level = raw_data_info.get('degreeLevel', '')

        # Use list comprehensions to create lists of instructors,
        # course_schedule, and exam_schedule
        self.instructors = [Instructor(instructor_data) for instructor_data in raw_data.get('instructor', [])]
        self.course_schedule = [CourseSchedule(schedule_data) for schedule_data in raw_data.get('courseSchedule', [])]
        self.exam_schedule = [CourseSchedule(schedule_data) for schedule_data in raw_data.get('examSchedule', [])]
