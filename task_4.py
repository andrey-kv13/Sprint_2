class EmployeeSalary:
    
    def __init__(self, name, hours, rest_days, email, hourly_payment = 400,):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        self.hourly_payment = hourly_payment
        
    @classmethod
    def get_hours(cls, rest_days):
        hours = (7 - rest_days) * 8
        return hours
        
    @classmethod
    def get_email(cls, name):
        email = f"{name}@email.com"
        return email
        
    def set_hourly_payment(self,new_hourly_payment):
        self.hourly_payment = new_hourly_payment
    
    def salary(self):
        hours = self.get_hours(self.rest_days)
        salary = hours * self.hourly_payment
        return salary