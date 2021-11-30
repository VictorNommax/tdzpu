from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from main.models import Products
from .forms import ContactForm


def sendEmail(request):
    RECIPIENTS_EMAIL = 'tdzhd.ru.message.from.site@gmail.com'
    DEFAULT_FROM_EMAIL = 'tdzhd.ru.message.from.site@gmail.com'
    product = int(request.GET['product'])-1
    item = Products.objects.all()
    what = item[product].name
    message = '';
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        subject = item[product].name
        phone = request.POST['phone']
        plus = request.POST['message']
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            #subject = form.cleaned_data['subject']
            from_email = 'tdzhd.ru.message.from.site@gmail.com'
            person = form.cleaned_data['person']
            response = form.cleaned_data['response']
            try:
                message = f'Клиент: {person}, Email для ответа: {response}, Телефон для ответа: {phone}, Дополнительное сообщение: {plus}.'
                send_mail(f'{subject} от {from_email}', message,
                DEFAULT_FROM_EMAIL, [RECIPIENTS_EMAIL])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('home')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "mailto/mailto.html", {'form': form, 'what': what})
