from django import forms

from apps.promotion.models import SubscriptionModel


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = SubscriptionModel
        fields = ['email']
