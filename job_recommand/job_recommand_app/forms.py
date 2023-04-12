from .models import Account
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
