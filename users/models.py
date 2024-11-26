from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=8)
    gender = models.CharField(max_length=1,
                              choices=GENDER, default='M')
    club = models.CharField(max_length=50, default='клуб не найден')

    def save(self, *args, **kwargs):
        if self.age < 5:
            self.club = 'Ваш возраст мал для клуба'
        elif 5 <= self.age <= 10:
            self.club = 'Детский клуб'
        elif 11 <= self.age <= 18:
            self.club = 'Подростковый клуб'
        elif 19 <= self.age <= 45:
            self.club = 'Взрослый клуб'
        else:
            self.club = 'Ваш возраст составляет больше 45 '

        super().save(*args, **kwargs)