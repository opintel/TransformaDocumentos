from django.conf import settings


def global_conf(request):
    return  {'settings': settings}
