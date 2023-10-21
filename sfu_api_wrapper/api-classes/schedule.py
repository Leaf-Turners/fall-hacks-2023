class CourseSchedule:
    def __init__(self, raw_data):
        self.start_time = raw_data['startTime']
        self.start_date = raw_data['startDate']
        self.end_time = raw_data['endTime']
        self.end_date = raw_data['endDate']
        self.section_code = raw_data['sectionCode']
        self.is_exam = raw_data['isExam']
        self.days = raw_data['days']
        self.campus = raw_data['campus']