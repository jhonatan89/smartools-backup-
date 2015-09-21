import django
from bootstrap3_datetime.widgets import DateTimePicker


class CreateNewCompetition(django.forms.Form):
    name = django.forms.CharField(label='Competition tittle', max_length=100)
    startDate = django.forms.DateTimeField(label='Opening time',
                                           widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                                                          "pickTime": True}))
    endDate = django.forms.DateField(label='Closing time',
                                     widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                                                    "pickTime": True}))
    image = django.forms.ImageField(label='Choose Picture')
    description = django.forms.CharField(label='Add description', max_length=200, widget=django.forms.Textarea)