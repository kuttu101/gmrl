from django.urls import path
from . import views



urlpatterns = [
	path('', views.product_list, name='index'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('shop/',views.shop,name="shop"),
    path('signup/',views.signup,name="signup"),
    path('why/',views.whye,name="why"),
    path('contact/',views.contactt,name="contact"),
    path('login/',views.user_logine,name="login"),
    path('logout/',views.logoute,name="logout"),
    path('testimonial/',views.testimonials,name="testimonial"),
    path('newadd/<int:products_id>/',views.newadd,name='newadd'),
    path('feedback/',views.feedback,name='feedback'),
    path('search/',views.search,name='search'),
]
