from django import forms
from first_app.models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['roll']
        
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'btn-primary'}),
            'name': forms.TextInput(),
            # 'roll': forms.PasswordInput()
        }
        help_texts ={
              'name': "Write Your Full Name",
            #   'roll': "Enter Your Student ID"
         }
        error_messages = {
            'name': {'required': 'Your name required'}
        }