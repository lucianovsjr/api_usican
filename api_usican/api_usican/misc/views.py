from django.db.models import ProtectedError

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from api_usican.misc.mixin import get_error_message


class BaseModelViewSet(ModelViewSet):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
        except ProtectedError as e:
            error_message = get_error_message(instance, "PROTECTED")
            return Response(data=error_message, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
