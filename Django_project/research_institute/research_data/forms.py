from django import forms
from .models import Employee, Project


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'middle_name', 'passport_number', 'passport_series', 'tax_id',
                  'date_of_birth', 'position']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'funding']
