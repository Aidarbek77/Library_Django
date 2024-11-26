from django import forms
from . import models, parser_book

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('openlibrary', 'openlibrary'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'openlibrary':
            rezka_pars = parser_rezka.parsing()
            for i in rezka_pars:
                models.openlibrary.objects.create(**i)