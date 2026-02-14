from django import forms
from .models import Category, Event, Participant


class CategoryForm(forms.ModelForm):
    """Form for Category model"""
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter category name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter category description',
                'rows': 4
            }),
        }


class EventForm(forms.ModelForm):
    """Form for Event model"""
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter event name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter event description',
                'rows': 4
            }),
            'date': forms.DateInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'type': 'time'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter event location'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
        }


class ParticipantForm(forms.ModelForm):
    """Form for Participant model"""
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter participant name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter email address'
            }),
            'events': forms.SelectMultiple(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
        }
