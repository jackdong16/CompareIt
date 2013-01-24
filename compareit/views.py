from django.template import Context, loader
from compare.models import Topic
from django.http import HttpResponse

#application view
def index(request):
    latest_poll_list = Topic.objects.all()
    t = loader.get_template('homepage/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))
