"""Module for custom functions"""
from django.core.paginator import Paginator
from django.conf import settings


def make_pagination(request, to_paginate, items_per_page=settings.MESSENGER_ITEMS_PER_PAGE):
    """
    Function to create pagination for specified object
    :param request:
    :param to_paginate: the django paginated queryset
    :param items_per_page: number of items to show on page
    :return: specified page and last page as tuple
    """
    pages = Paginator(to_paginate, items_per_page)
    last_page = pages.num_pages
    page = pages.get_page(request.GET.get('p'))
    return page, last_page
