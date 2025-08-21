from django.shortcuts import render,HttpResponse
from .models import Book

def add_book(request):
    book=Book(name='三国演义',author='罗贯中',price='1000')
    book.save()
    return HttpResponse('插入成功')

def read_book(request):
    books=Book.objects.all()
    for book in books:
        print(book.id,book.name,book.put_time,book.price)
    return HttpResponse('查询成功')

def update_book(request):
    book=Book.objects.first()
    book.name='aaaa'
    book.save()
    print('修改成功')
    return HttpResponse('修改成功')

def del_book(request):
    book=Book.objects.filter(name='aaaa')
    book.delete()
    print('删除成功')
    return HttpResponse('删除成功')