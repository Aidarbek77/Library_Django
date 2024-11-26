from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

Gender = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=Gender)

    class Meta:
        model = models.CustomUser
        Fields = ('username',
                  'email',
                  'phone_number',
                  'password1'
                  'password2 '
                  'first_name'
                  'last_name',
                  'age',
                  'gender',
                  )
        def save(self, commit=True):
            user = super(CustomRegistrationForm, self).save(commit=True)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user

@receiver(post_save, sender=models.CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    print("сигнал обработан ")
    age = instance.age
    if age <= 5
        instance.club = 'вы слишком малы'
    elif age >=5 and age <= 10:
        instance.club = 'detskui club'
    elif age >=11 and age <= 18:
        instance.club = 'podrostok'
    elif age >=19 and age <= 45:
        instance.club = 'vzroslyi club'
    else:
        instance.club = 'слишком стары '
    instance.save()
