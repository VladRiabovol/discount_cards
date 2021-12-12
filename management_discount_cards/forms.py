from django import forms


class CardDeleteForm(forms.Form):
    widget_attrs = {'class': 'form-control'}

    id = forms.IntegerField(label="Enter id of card", widget=forms.widgets.TextInput())


class ChangeStatusForm(forms.Form):
    CHOICES = (
        ('True', 'enabled'),
        ('False', 'disabled'),
    )
    id = forms.IntegerField(widget=forms.widgets.TextInput(
                            attrs={**{'id': 'id'}}))
    enabled = forms.BooleanField(required=False)
    disabled = forms.BooleanField(required=False)


