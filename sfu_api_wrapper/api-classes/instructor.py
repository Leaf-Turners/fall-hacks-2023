class Instructor:
    def __init__(self, raw_data):
        self.name = raw_data.name
        self.last_name = raw_data.lastName
        self.first_name = raw_data.firstName
        self.common_name = raw_data.commonName
        self.office = raw_data.office
        self.office_hours = raw_data.officeHours
        self.email = raw_data.email
        self.phone = raw_data.phone
        self.role_code = raw_data.roleCode
        self.profile_url = raw_data.profileUrl