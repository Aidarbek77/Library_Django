from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin


class AgeClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
            if request.path == '/reqister/' and request.method == 'POST':
                age = int(request.Post.get('age'))
                if age < 5 :
                    return HttpResponseBadRequest('ваш возраст мал переходите в следуюший пункт')
                elif age >= 5 and age < 10:
                    request.club = "детский клуб"
                elif age > 11 and age < 18:
                    request.club = 'Подростковый '
                elif age >= 18 and age <= 45:
                    request.club = 'взрослый'
                else:
                    return HttpResponseBadRequest('больше чем 45 ')
            elif request.path == '/reqister/' and request.method == 'GET':
                setattr(request, 'club', request.club)

