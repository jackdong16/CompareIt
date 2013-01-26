from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

from compare.models import Topic
from django.http import HttpResponse

#application view
# def index(request):
#     latest_poll_list = Topic.objects.all()
#     t = loader.get_template('homepage/index.html')
#     c = Context({
#         'latest_poll_list': latest_poll_list,
#     })
#     return HttpResponse(t.render(c))
def index(request):
    latest_poll_list = Topic.objects.all()
    return render_to_response('homepage/index.html',
                              latest_poll_list,
                              context_instance=RequestContext(request))

def popular(request):
    latest_poll_list = Topic.objects.all()
    return render_to_response('rank/list.html',
                          latest_poll_list,
                          context_instance=RequestContext(request))