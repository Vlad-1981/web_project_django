from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'    #   подгружает все поля из формы "News"
        fields = ['title', 'content', 'sign_of_publication', 'category']
        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
                    'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):                      #   метод позволяет добавлять название новости, которое начинается ТОЛЬКО с буквы!
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название должно начинаться с буквы!')
        else:
            return title






















    # title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label='Текст', required=False,
    #                           widget=forms.Textarea(attrs={
    #                                                         'class': 'form-control',
    #                                                         'rows': 5}))
    #                                                         #   "required=False" - поле необязательное для заполнения
    # sign_of_publication = forms.BooleanField(label='Опубликовано', initial=True,)
    #                                                         #   "initial=True" - поле отмечено по умолчанию
    # category = forms.ModelChoiceField(empty_label='Выберите категорию',
    #                                   label='Категория',
    #                                   queryset=Category.objects.all(),
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
    #                                                         #   "empty_label=None" - пустое поле вместо черточек "--------"

# class LoginForm(forms.Form):
#     email = forms.EmailField(label='Courriel')
#     password = forms.CharField(
#                                 label='Mot de passe',
#                                 widget = forms.PasswordInput
#     )













