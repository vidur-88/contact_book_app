from django.core import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import json

from .services import get_contacts, create_contact, delete_contact, edit_contact


# Create your views here.
class Contacts(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = get_contacts(request.GET)
        return Response(serializers.serialize('json', content), content_type='application/json')


class Create(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            msg = create_contact(request.body)
            return Response(msg, content_type='application/json')
        except Exception as e:
            return Response(e.args, content_type='application/json')


class Delete(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            msg = delete_contact(request.body)
            return Response(msg, content_type='application/json')
        except Exception as e:
            return Response(e.args, content_type='application/json')


class Edit(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            msg = edit_contact(request.body)
            return Response(msg, content_type='application/json')
        except Exception as e:
            return Response(e.args, content_type='application/json')
