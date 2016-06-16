from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import View

from WebApp.apps.content.models import Contents


class MainView(View):
    def get(self, request):
        context = {
            'contents': Contents.objects.all()
        }
        return TemplateResponse(request, 'Webapp/apps/content/index.html', context)

    def post(self, request):
        title, content = request.POST.get('title'), request.POST.get('content')
        Contents.objects.create(title=title, content=content, create_dt=datetime.now())

        return HttpResponseRedirect(reverse('main'))
