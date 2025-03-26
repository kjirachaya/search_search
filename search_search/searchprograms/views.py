from django.shortcuts import render
from .models import TestRecord

def search(request):
    query = request.GET.get('q', '')
    
    if query:
        results = TestRecord.objects.filter(
            test_id__icontains=query
        ) | TestRecord.objects.filter(
            test_name__icontains=query
        ) | TestRecord.objects.filter(
            tags__icontains=query
        ) | TestRecord.objects.filter(
            keywords__icontains=query
        )
    else:
        results = TestRecord.objects.all()
    
    print(results)
    
    return render(request, 'search.html', {'results': results, 'query': query})
