from instructor import Instructor
from schedule import CourseSchedule
class CourseOutline:
    def __init__(self, raw_data):
        self.outline_path = raw_data.get('outlinePath', '')
        self.delivery_method = raw_data.get('deliveryMethod', '')
        self.departmental_ugrad_notes = raw_data.get('departmentalUgradNotes', '')
        self.designation = raw_data.get('designation', '')
        self.type = raw_data.get('type', '')
        self.course_details = raw_data.get('courseDetails', '')
        self.title = raw_data.get('title', '')
        self.prerequisites = raw_data.get('prerequisites', '')
        self.description = raw_data.get('description', '')
        self.name = raw_data.get('name', '')
        self.dept = raw_data.get('dept', '')
        self.educational_goals = raw_data.get('educationalGoals', '')
        self.class_number = raw_data.get('classNumber', '')
        self.short_note = raw_data.get('shortNote', '')
        self.number = raw_data.get('number', '')
        self.section = raw_data.get('section', '')
        self.units = raw_data.get('units', '')
        self.corequisites = raw_data.get('corequisites', '')
        self.registrar_notes = raw_data.get('registrarNotes', '')
        self.grading_notes = raw_data.get('gradingNotes', '')
        self.term = raw_data.get('term', '')
        self.notes = raw_data.get('notes', '')
        self.degree_level = raw_data.get('degreeLevel', '')
        self.instructors = []
        for instructor_raw_data in raw_data.instructor:
            new_instructor = Instructor(instructor_raw_data)
            self.instructors.append(new_instructor)
        self.course_schedule = []
        for courseSchedule_raw_data in raw_data.courseSchedule:
            new_courseSchedule = CourseSchedule(courseSchedule_raw_data)
            self.course_schedule.append(new_courseSchedule)
        self.exam_schedule = []
        for examSchedule_raw_data in raw_data.examSchedule:
            new_examSchedule = CourseSchedule(examSchedule_raw_data)
            self.course_schedule.append(new_examSchedule)