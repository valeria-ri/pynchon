import re
from django import template

from core.models import TopMenu
from core.utils import get_mounth_name


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def sort_queryset(queryset, sort_obj):
    def sort_obj_key(obj):
        try:
            parts = getattr(obj, sort_obj).split('.')
            if len(parts) != 2:
                return (0, 0)
            return tuple(map(int, parts))
        except (AttributeError, ValueError):
            return (0, 0)

    return sorted(queryset, key=sort_obj_key)


@register.simple_tag
def show_top_menu():
    menu = TopMenu.objects.filter(
        is_active=True, deleted_at__isnull=True
    ).order_by('sort')
    return menu


@register.filter
def search_highlight(value, query):
    return re.sub(
        r'(%s)' % re.escape(query),
        r'<span class="highlighted">\1</span>', value, flags=re.IGNORECASE
    )


@register.filter
def class_name(value):
    return value.__class__.__name__


@register.filter
def custom_slice(value, q):
    n = value.find(q)
    start_index = max(0, n - 500)
    end_index = min(len(value), n + 500)
    return value[start_index:end_index]


@register.filter
def month_genitive(month_number):
    return get_mounth_name(month_number, case='genitive')
