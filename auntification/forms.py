from django.contrib.auth.forms import UserCreationForm
from auntification.models import CustomUser


class CustomeUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone_number',)
        help_texts = {
            'username': '',
        }