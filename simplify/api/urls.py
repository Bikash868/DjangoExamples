from django.urls import path
from products.views import product_view, question_view, question_details

urlpatterns = [
    path('',product_view, name='product_view'),
    path('questions/all', question_view, name='question_view'),
    path('questions/<int:question_id>', question_details, name='question_details')
]