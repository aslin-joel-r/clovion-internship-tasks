# views.py
from django.shortcuts import render, redirect
from .forms import StudentMarksForm

def enter_marks(request):
    if request.method == 'POST':
        form = StudentMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display-marks')  # Redirect to a success page
    else:
        form = StudentMarksForm()
    return render(request, 'enter_marks.html', {'form': form})
