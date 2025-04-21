from django.urls import include, path

urlpatterns = [
    path("", include("resume.urls")),
    path('streaming/', include('streaming.urls')),
]
