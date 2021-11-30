from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from django.forms import TextInput, Textarea

class ContactForm(forms.Form):
    #subject = forms.CharField(label='Тема', required=True)
    person = forms.CharField(label='Как к вам обращаться?', required=True)
    response = forms.EmailField(label='Email для ответа', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=False)
    captcha = ReCaptchaField()

    class Meta:
        widgets = {
            "person":TextInput(attrs={
                'class':'mailfield'
            }),
            "response":TextInput(attrs={
                'class':'mailfield',
                'placeholder':'Ваше мнение..',
            }),
            "message":Textarea(attrs={
                'class':'comment_textarea',
                'placeholder':'Ваше мнение..',
            }),
        }
