from .models import Employee, Project, ProjectParticipation
from .forms import EmployeeForm, ProjectForm
from django.shortcuts import render, get_object_or_404, redirect
import logging

logger = logging.getLogger(__name__)
logger.info("Testing Employee model: " + str(Employee.objects.all()))


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'research_data/employee_list.html', {'employees': employees})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'research_data/project_list.html', {'projects': projects})


def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'research_data/employee_form.html', {'form': form})


def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'research_data/project_form.html', {'form': form})


def employee_edit(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'research_data/employee_form.html', {'form': form})


def project_edit(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'research_data/project_form.html', {'form': form})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    participants = project.participants.all()
    return render(request, 'research_data/project_detail.html', {'project': project, 'participants': participants})


def home(request):
    return render(request, 'research_data/home.html')
