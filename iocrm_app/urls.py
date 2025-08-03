from django.urls import path
from iocrm_app import views

urlpatterns = [
    path("tr", views.tr_list, name="tr_list"),
    path("pr", views.pr_list, name="pr_list"),
    path("ar", views.ar_list, name="ar_list"),
    path('ar/<int:pk>/', views.ar_detail, name='ar_detail'),
    path('pr/<int:pk>/', views.pr_detail, name='pr_detail'),
    path('tr/<int:pk>/', views.tr_detail, name='tr_detail'),
    path('ar/new/', views.ar_new, name='ar_new'),
    path('ar/<int:pk>/edit/', views.ar_edit, name='ar_edit'),
    path('pr/new/', views.pr_new, name='pr_new'),
    path('pr/<int:pk>/edit/', views.pr_edit, name='pr_edit'),
    path('tr/new/', views.tr_new, name='tr_new'),
    path('tr/<int:pk>/edit/', views.tr_edit, name='tr_edit'),
]