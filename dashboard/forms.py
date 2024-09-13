from django import forms
from main.models import Position, Shift, StaffShift

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']
        
class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['s_time', 'e_time']

class StaffShiftForm(forms.ModelForm):
    class Meta:
        model = StaffShift
        fields = ['staff', 'shift', 'start_time']