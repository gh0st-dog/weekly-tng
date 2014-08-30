__author__ = 'buyvich'

import json

from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core import serializers

from .models import Training


class Index(TemplateView):

    template_name = 'index.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Index, self).dispatch(request, *args, **kwargs)


class TrainingView(View):

    @method_decorator(login_required)
    def get(self, request):
        trainings = Training.objects.filter(user=request.user).all()
        return HttpResponse(json.dumps(serializers.serialize('json', trainings)),
                            content_type='application/json')

    @method_decorator(login_required)
    def post(self, request):
        Training.objects.create(name=request.POST.get('name'),
                                user=request.user,
                                goal=request.POST.get('goal'),
                                tng_type='number')
        return HttpResponse('Training added successfully')

