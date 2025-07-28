class EmployeeSalary:
    
    def __init__(self, name, hours, rest_days, email, hourly_payment=400):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        self.hourly_payment = hourly_payment
        
    @classmethod
    def get_hours(cls, name, rest_days, hours=None, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email) 
    
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment
    
    def salary(self):
        hours = self.get_hours()
        salary = hours * self.hourly_payment
        return salary