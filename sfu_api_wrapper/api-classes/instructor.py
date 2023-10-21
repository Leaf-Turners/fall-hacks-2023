class Instructor:
    def __init__(self, raw_data):
        self.name = raw_data.get('name', '')
        self.last_name = raw_data.get('lastName', '')
        self.first_name = raw_data.get('firstName', '')
        self.common_name = raw_data.get('commonName', '')
        self.office = raw_data.get('office', '')
        self.office_hours = raw_data.get('officeHours', '')
        self.email = raw_data.get('email', '')
        self.phone = raw_data.get('phone', '')
        self.role_code = raw_data.get('roleCode', '')
        self.profile_url = raw_data.get('profileUrl', '')
