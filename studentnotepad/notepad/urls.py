from django.urls import path
from notepad.views import StudentListCreateApiView, StudentDetailApiView, NoteListCreateApiView, NoteDetailApiView


urlpatterns = [
    path('students', StudentListCreateApiView.as_view(), name='student-list-create'),
    path('notes/', NoteListCreateApiView.as_view(), name='note-list-create'),
    path('students/<int:pk>/', StudentDetailApiView.as_view(),name='student-list-delete'),
    path('notes/<int:pk>/', NoteDetailApiView.as_view(), name='note-delete')
]