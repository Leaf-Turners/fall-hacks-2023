from instructor import Instructor
from schedule import CourseSchedule
class CourseOutline:
    def __init__(self, raw_data):
        self.outline_path = raw_data['outlinePath']
        self.delivery_method = raw_data['deliveryMethod']
        self.departmental_ugrad_notes = raw_data['departmentalUgradNotes']
        self.designation = raw_data['designation']
        self.type = raw_data['type']
        self.course_details = raw_data['courseDetails']
        self.title = raw_data['title']
        self.prerequisites = raw_data['prerequisites']
        self.description = raw_data['description']
        self.name = raw_data['name']
        self.dept = raw_data['dept']
        self.educational_goals = raw_data['educationalGoals']
        self.class_number = raw_data['classNumber']
        self.short_note = raw_data['shortNote']
        self.number = raw_data['number']
        self.section = raw_data['section']
        self.units = raw_data['units']
        self.corequisites = raw_data['corequisites']
        self.registrar_notes = raw_data['registrarNotes']
        self.grading_notes = raw_data['gradingNotes']
        self.term = raw_data['term']
        self.notes = raw_data['notes']
        self.degree_level = raw_data['degreeLevel']
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