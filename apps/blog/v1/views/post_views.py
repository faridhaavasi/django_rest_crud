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


class CreatPost(APIView):
    serializer_class = PostInputSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            post_create_instance(
                author_id=request.user.id,
                title=serializer.validated_data.get("title"),
                description=serializer.validated_data.get("description")

            )
            return base_response(
                status_code=status.HTTP_201_CREATED,
                code=response_code.CREATED,
                result={'result': serializer.data, 'code': response_code.CREATED},
            )
        return base_response_with_error(status_code=status.is_server_error(code=response_code.BAD_REQUEST),
                                        code=response_code.BAD_REQUEST,
                                        error="data is not valid",)

class UpdatePost(APIView):
    serializer_class = PostInputSerializer
    def put(self, request, pk):
        instance = Post.objects.get(pk=pk)
        serializer = self.serializer_class(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            post_update_instance(pk=pk, **serializer.validated_data)
            return base_response(
                status_code=status.HTTP_200_OK,
                code=response_code.OK,
                result={'result': serializer.data, 'code': response_code.OK},
            )
        return base_response_with_error(status_code=status.is_server_error(code=response_code.BAD_REQUEST),
                                        code=response_code.BAD_REQUEST,
                                        error="data is not valid", )