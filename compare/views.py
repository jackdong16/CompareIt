from django.template import Context, loader
from compare.models import Topic
from django.http import HttpResponse

#compare module view
def index(request):
    latest_poll_list = Topic.objects.all()
    t = loader.get_template('topics/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))

def detail(request, topic_id):
    return HttpResponse("You're looking at poll %s." % topic_id)

def results(request, topic_id):
    return HttpResponse("You're looking at the results of poll %s." % topic_id)

def vote(request, topic_id):
    return HttpResponse("You're voting on poll %s." % topic_id)