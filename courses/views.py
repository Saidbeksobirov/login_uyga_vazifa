from django.shortcuts import render, redirect

from courses.forms import CoursesForm
from courses.models import CoursesModel


def login_view(request):
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            CoursesModel.objects.create(
                full_name=form.cleaned_data['full_name'],
                phone_number=form.cleaned_data['phone_number'],
                age=form.cleaned_data['age'],
            )
            return redirect('courses:login')
    else:
        form = CoursesForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)


def courses_view(request):
    result = CoursesModel.objects.all()
    context = {
        'result': result
    }
    return render(request, 'courses.html', context)




