class CourseOutline:
    def __init__(self, raw_data):
        self.outline_path = raw_data.outlinePath
        self.delivery_method = raw_data.deliveryMethod
        self.departmental_ugrad_notes = raw_data.departmentalUgradNotes
        self.designation = raw_data.designation
        self.type = raw_data.type
        self.course_details = raw_data.courseDetails
        self.title = raw_data.title
        self.prerequisites = raw_data.prerequisites
        self.description = raw_data.description
        self.name = raw_data.name
        self.dept = raw_data.dept
        self.educational_goals = raw_data.educationalGoals
        self.class_number = raw_data.classNumber
        self.short_note = raw_data.shortNote
        self.number = raw_data.number
        self.section = raw_data.section
        self.units = raw_data.units
        self.corequisites = raw_data.corequisites
        self.registrar_notes = raw_data.registrarNotes
        self.grading_notes = raw_data.gradingNotes
        self.term = raw_data.term
        self.notes = raw_data.notes
        self.degree_level = raw_data.degreeLevel