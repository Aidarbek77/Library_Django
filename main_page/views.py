from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# 1. about_me view
def about_me(request):
    # Замените на информацию о себе
    info = "Меня зовут Айдар, я ученик группы46-1B."
    return HttpResponse(info)

# 2. about_my_pets view
def about_my_pets(request):
    # Укажите имя и путь к фото вашего питомца
    pet_name = "Барсик"
    pet_photo_url = "/templates/pet1.jpg"
    return render(request, 'about_my_pets.html', {'pet_name': Барсик, 'pet_photo_url': pet1})

# 3. system_time view
def system_time(request):
    current_time = datetime.now()
    return HttpResponse(f"Системная дата и время: {current_time}")
