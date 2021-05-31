from django import forms
from .models import Tenant, TC, Rent, Worker, Pavilion


class FilterTCForm(forms.ModelForm):
    class Meta:
        model = TC
        fields = ['title', 'status', ]
        widgets = {
            'title': forms.TextInput(),
            'status': forms.Select(choices=[('План', 'План'), ('Строительство', 'Строительство'),
                                            ('Реализация', 'Реализация')]),
        }


class AddTCForm(forms.ModelForm):
    class Meta:
        model = TC
        fields = ['title', 'status', 'count_pavilions',
                  'city', 'cost', 'add_value_rito', 'storeys', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=[('План', 'План'), ('Строительство', 'Строительство'),
                                            ('Реализация', 'Реализация')],
                                   attrs={'class': 'form-control'}
                                   ),
            'count_pavilions': forms.NumberInput(attrs={'min': '0', 'max': '4', 'step': '1'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'add_value_rito': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.1'}),
            'storeys': forms.NumberInput(attrs={'min': '0', 'max': '4', 'step': '1'}),
        }


class FilterPavilion(forms.ModelForm):
    class Meta:
        model = Pavilion
        fields = ['floor', 'status', ]

        widgets = {
            'floor': forms.NumberInput(attrs={'min': '0', 'max': '4', 'step': '1', }),
            'status': forms.Select(choices={('Все', 'Все'),
                                            ('Арендован', 'Арендован'), ('Свободен', 'Свободен'), }),
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['full_name', 'email', 'password',
                  'role', 'phone', 'gender', 'photo']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices={('Мужчина', 'Мужчина'), ('Женщина', 'Женщина'), }),
            'photo': forms.ClearableFileInput()
        }

class FilterWorker(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['role']
        widjets = {
            'role': forms.Select(choices={('Администратор', "Администратор", 'Менеджер C', 'Менеджер C',
                                           'Менеджер А', 'Менеджер А')}),
        }
