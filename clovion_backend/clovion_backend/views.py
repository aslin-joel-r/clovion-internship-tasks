# views.py
from django.shortcuts import render, redirect
from .models import StudentMarks  # Import the StudentMarks model

def enter_marks(request):
    if request.method == 'POST':
        tamil = request.POST.get('tamil')
        english = request.POST.get('english')
        maths = request.POST.get('maths')
        science = request.POST.get('science')
        social = request.POST.get('social')

        # Create a new StudentMarks object and save it
        student_marks = StudentMarks.objects.create(
            tamil=tamil,
            english=english,
            maths=maths,
            science=science,
            social=social
        )
        student_marks.save()

        return redirect('result')  # Redirect to a success page
    else:
        return render(request, 'enter_marks.html')
def result():
    return render(request,'result.html')
