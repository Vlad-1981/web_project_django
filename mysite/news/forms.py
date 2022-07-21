from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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

# ----------------------------------------------------
# ФОРМА РЕГИСТРАЦИИ ПОЛЬЗОВАТЕЛЯ
# ----------------------------------------------------


class UserRegisterForm(UserCreationForm):


    username = forms.CharField(
                                label='Имя пользователя',
                                widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
                                label='Пароль',
                                help_text='Пароль должен состоять из букв, цифр и др. символов.',   #   Появляется под полем. Подсказка по вводу правильного пароля.
                                widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
                                label='Подтверждение пароля',
                                help_text='Для подтверждения, введите пароль еще раз.',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
                                label='E-mail',
                                widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
                    'username': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'}),
                    'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
                    'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


# ----------------------------------------------------
# ФОРМА АВТОРИЗАЦИИ ПОЛЬЗОВАТЕЛЯ
# ----------------------------------------------------

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
                                label='Имя пользователя',
                                widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
                                label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
















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













