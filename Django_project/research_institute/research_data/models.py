from django.db import models


class Employee(models.Model):
    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    passport_number = models.CharField(max_length=10)
    passport_series = models.CharField(max_length=10)
    tax_id = models.CharField(max_length=12)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    funding = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class ProjectParticipation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="participants")
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee} - {self.project}"
