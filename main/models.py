from django.db import models

class Staff(models.Model):
    firstname = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.firstname} {self.surname}"
    


class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    s_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.s_time} {self.staff}"
    


class Position(models.Model):
    name = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.name
    


class Shift(models.Model):
    s_time = models.TimeField(null=True, blank=True)
    e_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.s_time} - {self.e_time}"
    
    
class StaffShift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    
    
    def __str__(self):
        return f"{self.staff} - {self.shift} - {self.start_time} "
    