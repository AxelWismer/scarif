from django import template
from django.template.loader import get_template
from django.contrib.admin.views.main import (
    PAGE_VAR,
)

from django.utils.html import format_html

from core.utils import get_app_list

register = template.Library()
assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag

@register.simple_tag
def custom_admin_list_filter(cl, spec):
    tpl = get_template(spec.template)
    selected = ""
    for choice in list(spec.choices(cl)):
        if choice['selected']:
            selected = 'true'
    return tpl.render({
        'title': spec.title,
        'choices': list(spec.choices(cl)),
        'spec': spec,
        'selected': selected
    })

DOT = '.'
@register.simple_tag
def paginator_number(cl, i):
    if i == DOT:
        return '... '
    elif i == cl.page_num:
        return format_html('<li class="page-item"><a class="border border-primary-dark rounded page-link text-primary-dark">{}</a></li>', i+1)
    else:
        last_page_index = cl.paginator.num_pages-1
        if i == last_page_index:
            return format_html(
                '<li class="page-item"><a class="rounded border-0 page-link text-primary-dark" href="{}">{}</a></li><li class="page-item"><a class="rounded page-link border-0 text-primary-dark" href="{}"><span aria-hidden="true">&raquo;</span></a></li>',
                cl.get_query_string({PAGE_VAR: i}),
                i+1,
                cl.get_query_string({PAGE_VAR:cl.page_num+1}),
            )
        elif i == 0:
            return format_html(
                '<li class="page-item"><a class="rounded page-link border-0 text-primary-dark" href="{}"><span aria-hidden="true">&laquo;</span></a></li><li class="page-item"><a class="rounded border-0 page-link text-primary-dark" href="{}">{}</a></li>',
                cl.get_query_string({PAGE_VAR:cl.page_num-1}),
                cl.get_query_string({PAGE_VAR: i}),
                i+1
            )
        return format_html(
            '<li class="page-item"><a class="rounded border-0 page-link text-primary-dark" href="{}">{}</a></li>',
            cl.get_query_string({PAGE_VAR: i}),
            i+1
        )

@assignment_tag(takes_context=True)
def custom_get_menu(context):
    return get_app_list(context)
