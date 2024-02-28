from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('package/', views.package,name='package'),
    path('blog/', views.blog,name='blog'),
    path('branch/', views.branches,name='branch'),
    path('gallery/', views.gallery,name='gallery'),
    path('executive-package/', views.executive_package,name='executive-package'),
    path('ayush-general/', views.ayush_general,name='ayush-general'),
    path('ayush-silver-plan/', views.ayush_silver,name='ayush-silver-plan'),
    path('ayush-gold/', views.ayush_gold,name='ayush-gold'),
    path('ayush-diabetic/', views.ayush_diabetic,name='ayush-diabetic'),
    path('cardiac/', views.cardiac,name='cardiac'),
    path('executive-package/', views.executive_package,name='executive-package'),
    path('gmrl-chambakkara/', views.gmrl_chambakkara,name='gmrl-chambakkara'),
    path('gmrl-vadakkekotta/', views.gmrl_vadakkekotta,name='gmrl-vadakkekotta'),
    path('gmrl-kolenchery/', views.gmrl_kolenchery,name='gmrl-kolenchery'),
    path('gmrl-thrippunithura/', views.gmrl_thrippunithura,name='gmrl-thrippunithura'),
    path('moleculor-biology/', views.moleculor_biology,name='moleculor-biology'),
    path('radiology/', views.radiology,name='radiology'),
    path('test/', views.test,name='test'),
    path('contact-us/', views.contact,name='contact-us'),
    path('appointment/', views.appointment,name='appointment'),
    path('department/', views.department,name='department'),
    path('privacy-policy/', views.privacy_policy,name='privacy-policy'),
    path('terms&conditions/', views.terms_conditions,name='terms&conditions'),
    path('testimonials/', views.testimonials,name='testimonials'),











]