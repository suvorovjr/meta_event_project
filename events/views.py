from rest_framework import views
from rest_framework import response, status
from .services import get_facebook_pages
from django.conf import settings
from .serializers import FacebookPagesSerializer
from django.db import transaction


class GetFacebookPagesAPIView(views.APIView):
    @transaction.atomic
    def post(self, requests, *arg, **kwargs):
        facebook_pages = get_facebook_pages(access_token=settings.FACEBOOK_ACCESS_TOKEN)

        if facebook_pages is None:
            return response.Response({'Error': 'Ошибка при отправке запроса.'}, status=status.HTTP_400_BAD_REQUEST)

        created_objects = []

        for page in facebook_pages.data:
            page_data = {
                'social_platform_id': page.id,
                'name': page.name,
                'page_token': page.access_token
            }
            serializer = FacebookPagesSerializer(data=page_data)
            if serializer.is_valid():
                created_page = serializer.save()
                created_objects.append(created_page)

        if len(created_objects) > 1:
            serializer = FacebookPagesSerializer(created_objects, many=True)
        else:
            serializer = FacebookPagesSerializer(created_objects[0])

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
