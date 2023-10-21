class CourseSchedule:
    def __init__(self, raw_data):
        self.start_time = raw_data.get('startTime', '')
        self.start_date = raw_data.get('startDate', '')
        self.end_time = raw_data.get('endTime', '')
        self.end_date = raw_data.get('endDate', '')
        self.section_code = raw_data.get('sectionCode', '')
        self.is_exam = raw_data.get('isExam', '')
        self.days = raw_data.get('days', '')
        self.campus = raw_data.get('campus', '')