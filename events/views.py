from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Count
from datetime import date, timedelta
from .models import Category, Event, Participant
from .forms import CategoryForm, EventForm, ParticipantForm

def dashboard(request):
    filter_type = request.GET.get('filter', 'all')
    total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    upcoming_events_count = Event.objects.filter(date__gte=date.today()).count()
    past_events_count = Event.objects.filter(date__lt=date.today()).count()
    
    today_events = Event.objects.filter(date=date.today()).select_related('category').annotate(
        participant_count=Count('participants')
    )
    
    if filter_type == 'upcoming':
        events = Event.objects.filter(date__gte=date.today()).select_related('category').annotate(
            participant_count=Count('participants')
        ).order_by('date', 'time')
    elif filter_type == 'past':
        events = Event.objects.filter(date__lt=date.today()).select_related('category').annotate(
            participant_count=Count('participants')
        ).order_by('-date', '-time')
    elif filter_type == 'all':
        events = Event.objects.select_related('category').annotate(
            participant_count=Count('participants')
        ).order_by('-date', '-time')
    else:
        events = Event.objects.filter(date=date.today()).select_related('category').annotate(
            participant_count=Count('participants')
        ).order_by('time')
    
    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events_count': upcoming_events_count,
        'past_events_count': past_events_count,
        'today_events': today_events,
        'events': events,
        'filter_type': filter_type,
    }
    
    return render(request, 'events/dashboard.html', context)

# event crud
def event_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    
    events = Event.objects.select_related('category').annotate(
        participant_count=Count('participants')
    )
    
    if query:
        events = events.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )
    if category_id:
        events = events.filter(category_id=category_id)
    if start_date:
        events = events.filter(date__gte=start_date)
    if end_date:
        events = events.filter(date__lte=end_date)
        
    categories = Category.objects.all()
    
    context = {
        'events': events,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
        'start_date': start_date,
        'end_date': end_date,
    }
    
    return render(request, 'events/event_list.html', context)


def event_detail(request, id):
    event = get_object_or_404(
        Event.objects.select_related('category').prefetch_related('participants'),
        id=id
    )
    
    context = {
        'event': event,
    }
    
    return render(request, 'events/event_detail.html', context)


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully')
            return redirect('event_list')
    else:
        form = EventForm()
    
    context = {
        'form': form,
        'title': 'Create Event',
        'button_text': 'Create Event',
    }
    
    return render(request, 'events/event_form.html', context)


def event_edit(request, id):
    event = get_object_or_404(Event, id=id)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', id=id)
    else:
        form = EventForm(instance=event)
    
    context = {
        'form': form,
        'title': 'Edit Event',
        'button_text': 'Update Event',
        'event': event,
    }
    
    return render(request, 'events/event_form.html', context)


def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('event_list')


# category crud
def category_list(request):
    categories = Category.objects.annotate(event_count=Count('events'))
    
    context = {
        'categories': categories,
    }
    
    return render(request, 'events/category_list.html', context)


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'title': 'Create Category',
        'button_text': 'Create Category',
    }
    
    return render(request, 'events/category_form.html', context)


def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'title': 'Edit Category',
        'button_text': 'Update Category',
        'category': category,
    }
    
    return render(request, 'events/category_form.html', context)


def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('category_list')

# participents crud
def participant_list(request):
    participants = Participant.objects.annotate(event_count=Count('events'))

    context = {
        'participants': participants,
    }
    
    return render(request, 'events/participant_list.html', context)


def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant created successfully!')
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    
    context = {
        'form': form,
        'title': 'Add Participant',
        'button_text': 'Add Participant',
    }
    
    return render(request, 'events/participant_form.html', context)


def participant_edit(request, id):
    participant = get_object_or_404(Participant, id=id)
    
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant updated successfully!')
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    
    context = {
        'form': form,
        'title': 'Edit Participant',
        'button_text': 'Update Participant',
        'participant': participant,
    }
    
    return render(request, 'events/participant_form.html', context)


def participant_delete(request, id):
    participant = get_object_or_404(Participant, id=id)
    participant.delete()
    messages.success(request, 'Participant deleted successfully!')
    return redirect('participant_list')
