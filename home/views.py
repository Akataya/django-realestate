from django.shortcuts import render
from property.models import Property, Category
from agents.models import Agent
from django.db.models import Count
from about.models import Service


def home(request):
    category_list = Category.objects.annotate(property_count=Count('property')).values('category_name', 'property_count',
                                                                                       'image', 'major')
    property_list = Property.objects.all()
    agent_list = Agent.objects.all()
    services = Service.objects.all()
    template = 'home/index.html'
    context = {
        'category_list_home': category_list,
        'property_list_home': property_list,
        'agent_list_home': agent_list,
        'services': services
    }
    return render(request, template, context)