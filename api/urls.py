from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth_app.urls')),
    path('sheets/', include('sheets.urls')),
]
