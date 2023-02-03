from django import forms
from django.urls import reverse_lazy
from django.views import generic as views

# from django import views

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from cbv_demo.web.models import Employee


# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Hello world')
#
#
# class MyView(View):
#     def get(self, request):
#         return HttpResponse('result')


# class My_view(View):
#     def get(self, request):
#         return render(request, 'index.html')


class My_view(views.View):
    def get(self, request):
        context = {
            'title': 'From CBV',
        }
        return render(request, 'index.html', context)

    def post(self, request):
        pass


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'From Template View'}  # static content

    def get_context_data(self, **kwargs):  # dinamic context - if we have different employees it shows different result
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class IndexViewWithListView(views.ListView):
    # context_object_name = 'employees'
    model = Employee
    template_name = 'index.html'
    extra_context = {'title': 'List view'}

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class DetailsView(views.DetailView):
    context_object_name = 'employee'
    model = Employee
    template_name = 'details.html'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                }
            )
        }


class EmployeeCreateView(views.CreateView):
    template_name = 'create.html'
    model = Employee
    fields = '__all__'
    success_url = '/'

    # form_class = EmployeeCreateForm

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     for name, field in form.fields.items():
    #         field.widget.attrs['placeholder'] = 'Enter ' + name
    #     return form


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'edit.html'

    # def get(self, *args, **kwargs):
    #     result = super().get(*args, **kwargs)
    #     print(self.args, self.kwargs)
    #     return result

    def get_success_url(self):
        result = reverse_lazy('employee details', kwargs={
            'pk': self.object.pk,
        })
        return result
