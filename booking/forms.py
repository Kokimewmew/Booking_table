from django.forms import ModelForm

from booking.models import Services
from users.forms import StyleFormMixin


class ServicesForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
