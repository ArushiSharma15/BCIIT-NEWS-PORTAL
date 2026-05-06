from django.shortcuts import render
from bciitapp.forms import EnquiryForm
from bciitapp.models import Club, Faculty, Event

# Create your views here.
def home(request):
    return render(request,'bciitapp/bciit.html')


def student(request):
    clubs = Club.objects.all()
    return render(request, 'bciitapp/student.html', {'clubs': clubs})


def club_detail(request, id):
    club = Club.objects.get(id=id)
    return render(request, 'bciitapp/club_detail.html', {'club': club})


def faculty(request):
    faculty = Faculty.objects.all()
    return render(request, 'bciitapp/faculty.html', {'faculty': faculty})


def faculty_detail(request, id):
    teacher = Faculty.objects.get(id=id)
    return render(request, 'bciitapp/faculty_detail.html', {'teacher': teacher})


def event(request):
    events = Event.objects.all()
    return render(request, 'bciitapp/event.html', {'events': events})


def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'bciitapp/event_detail.html', {'event': event})


def enquiry_view(request):
    form=EnquiryForm()

    if request.method == 'POST':
        form=EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            form=EnquiryForm()

    return render(request,'bciitapp/enquiry.html',{'form':form})
