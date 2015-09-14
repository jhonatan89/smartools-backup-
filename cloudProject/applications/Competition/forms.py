import django


class CreateNewCompetition(django.forms.Form):
    name = django.forms.CharField(label='Competition Name', max_length=100)
    image = django.forms.ImageField(label='Choose Picture')
    description = django.forms.CharField(label='Add a description', max_length=500, widget=django.forms.Textarea)