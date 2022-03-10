from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    OPTIONS = [
        ("1", "Пакет 1"),
        ("2", "Пакет 2"),
        ("3", "Пакет 3"),
    ]
    choice = forms.TypedChoiceField(choices=OPTIONS, widget=forms.Select(attrs={'class': 'form-select'}))
