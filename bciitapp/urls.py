from django.urls import path
from bciitapp import views

urlpatterns = [
    path('',views.home),
    path('faculty/',views.faculty, name='faculty'),
    path('student/',views.student, name='student'),
    path('event/',views.event, name='event'),
    path('enquiry/',views.enquiry_view),

    path('club/<int:id>/', views.club_detail, name='club_detail'),
    path('faculty/<int:id>/', views.faculty_detail, name='faculty_detail'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
]
