from django.urls import path

from cbv_demo.web.views import My_view, IndexViewWithTemplate, IndexViewWithListView, DetailsView, EmployeeCreateView, \
    EmployeeUpdateView
from django.views import generic as views

urlpatterns = [
    # path('', My_view.as_view()),
    path('', IndexViewWithListView.as_view()),
    path('redirect-to-index/', views.RedirectView.as_view(url='/')),
    path('details/<int:pk>/', DetailsView.as_view(), name='employee details'),
    path('create/', EmployeeCreateView.as_view(), name='create employee'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee update'),
]
