from .models import Comments
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from django.forms import ModelForm, IntegerField, TextInput, Textarea


class CommentsForm(ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = Comments
        userid = IntegerField()
        fields = ['userid','user','text','captcha']

        widgets = {
            "user":TextInput(attrs={
                'visibility':'hidden',
            }),
            "text":Textarea(attrs={
                'placeholder':'Написать отзыв..',
            }),
        }
