from django.shortcuts import render,HttpResponse

def book_detail_query_string(request):
    book_id=request.GET.get('id')
    return HttpResponse(f"您要找的是{book_id}号")


def book_detail_query(request,book_id):
    return HttpResponse(f"您要找的图书是{book_id}")