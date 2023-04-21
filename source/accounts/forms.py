from django import forms
from django.contrib.auth import get_user_model

from posts.models import Post, Comment


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Email')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


class CustomUserCreationForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
        ('Другое', 'Другое'),
    ]
    gender = forms.ChoiceField(label='Пол', choices=GENDER_CHOICES)
    password = forms.CharField(required=True, label='Пароль', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(required=True, label='Подтвердите пароль', strip=False,
                                       widget=forms.PasswordInput)
    inform = forms.CharField(label='Информация', required=False)
    number = forms.IntegerField(label='Телефон', required=False)
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'password_confirm', 'first_name', 'number',
                  'inform', 'gender', 'avatar')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пороли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'email', 'avatar', 'inform', 'gender')
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class PostForm(forms.ModelForm):
    descriptions = forms.CharField(required=False, label='Описание')

    class Meta:
        model = Post
        fields = ('descriptions', 'image',)
        labels = {
            'image': 'Фото',
            'descriptions': 'Описание'
        }


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, required=True, label='Комментарий')

    class Meta:
        model = Comment
        fields = ('text',)

        labels = {
            'text': 'Комментарий'
        }

