import django


class UploadVideo(django.forms.Form):
    title = django.forms.CharField(label='Video Title', max_length=100)
    clientfirtsName = django.forms.CharField(label='Your First Name')
    clientlastName = django.forms.CharField(label='Your Last Name')
    clientEmail = django.forms.CharField(label='Your email')
    originalVideoPath = django.forms.FileField(label='Choose video')
    description = django.forms.CharField(label='Add a description', max_length=500, widget=django.forms.Textarea)