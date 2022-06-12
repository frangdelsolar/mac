from django.db.models import Q

def filter_queryset(search_fields, queryset, request):
    keyword = request.GET.get('search')
    if not keyword:
        return queryset
    Qr = None
    for field in search_fields:
        q = Q(**{"%s__contains" % field: keyword })
        if Qr:
            Qr = Qr | q # or & for filtering
        else:
            Qr = q
    return queryset.filter(Qr)