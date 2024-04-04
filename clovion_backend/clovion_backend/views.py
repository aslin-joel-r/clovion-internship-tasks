# views.py
from django.shortcuts import render, redirect
from .models import StudentMarks

def enter_marks(request):
    if request.method == 'POST':
        tamil = int(request.POST.get('tamil'))
        english = int(request.POST.get('english'))
        maths = int(request.POST.get('maths'))
        science = int(request.POST.get('science'))
        social = int(request.POST.get('social'))

        # Calculate total and average marks
        total_marks = tamil + english + maths + science + social
        average_marks = total_marks / 5

        # Create a new StudentMarks object and save it
        student_marks = StudentMarks.objects.create(
            tamil=tamil,
            english=english,
            maths=maths,
            science=science,
            social=social,
            total_marks=total_marks,
            average_marks=average_marks
        )
        student_marks.save()

        return redirect('result')  # Redirect to a success page
    else:
        return render(request, 'enter_marks.html')

def result(request):
    # Retrieve the latest student marks data
    latest_student_marks = StudentMarks.objects.latest('id')
    context = {
        'total_marks': latest_student_marks.total_marks,
        'average_marks': latest_student_marks.average_marks
    }
    return render(request, 'result.html', context)
