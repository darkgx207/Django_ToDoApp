from django.forms import ModelForm

from website.models import Tasks

class EditTask(ModelForm):
    class Meta:
        model = Tasks
        fields = ['task','description']