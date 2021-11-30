from django.shortcuts import render, redirect
from django.urls import include
from .models import Comments
from .forms import CommentsForm

# Create your views here.
def toComments(request):
    comments = Comments.objects.all()
    error = ''
    #fix = ''
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        #fix = request.POST['userid']
        if request.user.is_authenticated and int(request.POST['userid']) == request.user.id and str(request.POST['user']) == request.user.username:
            if form.is_valid():
                form.save()
                return redirect('feedback')
            else:
                error = 'Данные введены некорректно.'
        else:
            error = 'Ошибка доступа.'

    form = CommentsForm()

    data = {
        'feedback':comments,
        'form':form,
        'error':error,
        #'fix':fix
    }

    return render(request, 'feedback/feedback.html', data)
