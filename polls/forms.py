from django import forms
from polls.models import db_models
class db_forms(forms.Form):
    class Meta:
        model = db_models
        fields = "__all__"