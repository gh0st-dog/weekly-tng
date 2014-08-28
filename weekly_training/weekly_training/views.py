__author__ = 'buyvich'

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class Index(TemplateView):

    template_name = 'index.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Index, self).dispatch(request, *args, **kwargs)
