from django.shortcuts import render
from django.views.generic import TemplateView


def class_template(request):
    return render(request, 'class_template.html')


#class func_template(TemplateView):
    #template_name = 'func_template.html'
