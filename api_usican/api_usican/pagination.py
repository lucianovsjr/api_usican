from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    max_page_size = 500
    page_query_param = "page"
    page_size_query_param = "page_size"
