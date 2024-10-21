from django.contrib.messages import success
from django.template.context_processors import request

from .models import Book, Forma, User
from django.shortcuts import render
from .forms import FormaForm, BookForm
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm



def main_page(request):
    return render(request, 'library/main_page.html')


#
# def book_detail(request, pk):
#     book = Book.objects.get(pk=pk)
#     return render(request, 'library/book.html', {'book': book})

def books_list(request):
    books = Book.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search', '')

        if search.strip():
            books = books.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search)
            )
            return render(request, 'library/books.html',
                          {"books": books, "curr_result": search})

    return render(request, 'library/books.html', {"books": books})





def users_list(request):
    users = Forma.objects.all()  # Barcha foydalanuvchilarni olish
    return render(request, 'library/users_list.html', {'users': users})



def form_view(request):
    if request.method == "POST":
        form = FormaForm(request.POST)
        if form.is_valid():
            form.save()
            # Muvaffaqiyatli saqlangandan keyin forma sahifasini ko'rsatish
            return render(request, 'library/forma.html', {'form': form, 'success': True})
    else:
        form = FormaForm()

    return render(request, 'library/forma.html', {'form': form})







def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Fayllarni ham POST orqali olish kerak
        if form.is_valid():
            form.save()
            return render(request, 'library/book_create.html', {
                'form': BookForm(),
                'success': True
            })
    else:
        form = BookForm()

    return render(request, 'library/book_create.html', {
        'form': form,
        'success': False
    })


