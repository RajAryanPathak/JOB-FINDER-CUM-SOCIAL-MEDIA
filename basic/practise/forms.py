from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name',
                  'address',
                  'phone',
                  'propic',
                  'Bio'
                  ]  # __all__'


class UpdateUserWebsite(ModelForm):
    class Meta:
        model = UserWebsite
        fields = ['li',
                  'instagram',
                  'github'
                  ]


class UpdateUserEdu(ModelForm):
    class Meta:
        model = UserEdu
        fields = ['TenName',
                  'tenthmarks',
                  'twelveName',
                  'Twelvwmarks',
                  'Graduationmarks',
                  'gradName']
        # '__all__'

class WriteBlog(ModelForm):
    class Meta:
        model = Blog
        fields = ['post',
                  'postpic'
                  ]
        # '__all__'
