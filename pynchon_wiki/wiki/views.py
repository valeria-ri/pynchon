from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Book, Chapter, TableChronology


@login_required
def index(request):
    """ Главная страница. """
    template = 'wiki/index.html'
    context = {'url_name': 'index'}
    return render(request, template, context=context)


@login_required
def about(request):
    """ Страница описания. """
    template = 'wiki/about.html'
    return render(request, template)


@login_required
def rainbow(request):
    """ Страница книги радуга тяготения. """

    template = 'wiki/rainbow.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'url_name': 'rainbow',
        'breadcrumbs': breadcrumbs
    }
    return render(request, template, context=context)


def rainbow_part1(request):
    template = 'wiki/rainbow_part1.html'
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        },
        {
            'title': 'Раздел 1: для чего читать радугу',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {'url_name': 'rainbow_part1', 'breadcrumbs': breadcrumbs}
    return render(request, template, context=context)


def rainbow_part2(request):
    template = 'wiki/rainbow_part2.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        },
        {
            'title': 'Раздел 2: примечания к каждой главе',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part3(request):
    template = 'wiki/rainbow_part3.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')},
        {
            'title': 'Раздел 3: краткое содержание и комментарии по главам',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part4(request):
    template = 'wiki/rainbow_part4.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')},
        {
            'title': 'Раздел 4: статьи с объяснениями',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part5(request):
    template = 'wiki/rainbow_part5.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        },
        {
            'title': 'Раздел 5: персонажи - таблица и схема',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part6(request):
    template = 'wiki/rainbow_part6.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        },
        {
            'title': 'Раздел 6: хронология романа',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part7(request):
    template = 'wiki/rainbow_part7.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')},
        {
            'title': 'Раздел 7: объяснение',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_notes(request, chapter_number):
    """ Страница главы, на которой видно все примечания к главе. """

    template = 'wiki/rainbow_notes.html'
    chapter = get_object_or_404(Chapter, number=chapter_number)
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        },
        {
            'title': 'Раздел 2: примечания к каждой главе',
            'url_name': reverse('wiki:rainbow_part2')
        },
        {
            'title': 'Примечание'
        }
    ]
    context = {
        'chapter': chapter,
        'comments': chapter.comments.all(),
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_comments(request, chapter_number):
    """ Страница главы, на которой видно все комментарии к главе. """

    template = 'wiki/rainbow_comments.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    chapter = get_object_or_404(Chapter, number=chapter_number)
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        },
        {
            'title': 'Раздел 3: краткое содержание и комментарии по главам',
            'url_name': reverse('wiki:rainbow_part3')},
        {
            'title': 'Комментарий'
        }
    ]
    context = {
        'book': book,
        'comments': chapter.comments.all(),
        'chapter': chapter,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def double_katie(request):
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        },
        {
            'title': 'Раздел 4',
            'url_name': reverse('wiki:rainbow_part1')
        },
        {
            'title': 'Двойничество Катье',
            'url_name': reverse('wiki:double_katie')
        }
    ]
    return render(request, 'wiki/double_katie.html',
                  context={'breadcrumbs': breadcrumbs})


def chronology(request):
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Радуга: Разделы',
            'url_name': reverse('wiki:rainbow')
        },
        {
            'title': 'Раздел 6',
            'url_name': reverse('wiki:rainbow_part1')
        },
        {
            'title': 'Хронология',
            'url_name': reverse('wiki:chronology')
        }
    ]
    context = {
        'rows': TableChronology.objects.all(),
        'breadcrumbs': breadcrumbs
    }
    return render(request, 'wiki/chronology.html', context)
