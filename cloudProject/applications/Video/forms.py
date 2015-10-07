import django
from cloudProject.settings import UPLOAD_VIDEO_TYPE


class UploadVideo(django.forms.Form):
    title = django.forms.CharField(label='Video Title', max_length=100)
    clientfirtsName = django.forms.CharField(label='Your First Name')
    clientlastName = django.forms.CharField(label='Your Last Name')
    clientEmail = django.forms.CharField(label='Your email')
    originalVideoPath = django.forms.FileField(label='Choose video')
    description = django.forms.CharField(label='Add a description', max_length=500, widget=django.forms.Textarea)

    def clean(self):
        cleaned_data = self.cleaned_data
        file = cleaned_data.get("originalVideoPath")
        file_exts = ('.ogg', '.3gpp', '.mp4', '.avi', '.flv')

        if file is None:
            raise django.forms.ValidationError('Please select video file first!!')

        if not file.content_type in UPLOAD_VIDEO_TYPE:  # UPLOAD_VIDEO_TYPE contains mime types of required file
            print UPLOAD_VIDEO_TYPE
            print file.content_type
            raise django.forms.ValidationError('Video accepted only in: %s' % ' '.join(file_exts))

        return cleaned_data
