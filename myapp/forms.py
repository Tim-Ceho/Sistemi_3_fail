from django.forms import ModelForm
from myapp.models import User

class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields =["username","email", "password" ]
