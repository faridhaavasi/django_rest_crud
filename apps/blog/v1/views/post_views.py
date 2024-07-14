from rest_framework.views import APIView
from apps.api.response import base_response, base_response_with_error
from rest_framework import status
from apps.api import response_code
from apps.blog.v1.serializers.post_serializers import PostInputSerializer, PostOutputSerializer
from apps.blog.v1.selectors.pst_selectors import select_post_all, select_post_specific_instance
from apps.blog.v1.sevices.post_services import post_create_instance, post_update_instance
from drf_spectacular.utils import extend_schema, OpenApiRequest, OpenApiResponse
from rest_framework.response import Response
from apps.blog.models import Post


class PostsShowDetail(APIView):
    serializers_class = PostOutputSerializer

    @extend_schema(responses=serializers_class)
    def get(self, request):
        queyset = select_post_all()

        serializer = self.serializers_class(instance=queyset, many=True)

        return base_response(
            status_code=status.HTTP_200_OK,
            code=response_code.OK,
            result={'result': serializer.data, 'code': response_code.OK},
        )
    @extend_schema(responses=serializers_class)
    def get(self, request, pk):
        instance = select_post_specific_instance(pk=pk)
        serializer = self.serializers_class(instance=instance)
        return base_response(
            status_code=status.HTTP_200_OK,
            code=response_code.OK,
            result={'result': serializer.data, 'code': response_code.OK},
        )
