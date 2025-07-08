from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project
from django.db.models import Q
from django.shortcuts import redirect
from .forms import ProjectForm , IssueForm

@login_required
def project_list(request):
    projects = Project.objects.filter(
        Q(owner=request.user) | Q(members=request.user)
    ).distinct()
    return render(request, "tracker/project_list.html", {"projects": projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            form.save_m2m()  # save the many-to-many (members)
            return redirect('tracker:project_list')
    else:
        form = ProjectForm()

    return render(request, 'tracker/project_form.html', {'form': form})

@login_required
def issue_create(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.save()
            return redirect('tracker:project_list')  # will create issue list later
    else:
        form = IssueForm()

    return render(request, 'tracker/issue_form.html', {'form': form})

