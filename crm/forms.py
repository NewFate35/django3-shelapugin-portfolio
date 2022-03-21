from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    OPTIONS = [
        ("1", "Тариф 'Online'"),
        ("2", "Тариф 'Персональный тренер'"),
        ("3", "Тариф 'Группа'"),
    ]
    choice = forms.TypedChoiceField(choices=OPTIONS, widget=forms.Select(attrs={'class': 'form-select'}))
