from django.contrib.auth.models import User, Group
from images.models import images
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
import cloudinary, json
from images.serializers import UserSerializer, GroupSerializer, ImageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class imagesviewSet(viewsets.ModelViewSet):
    queryset = images.objects.all()
    serializer_class = ImageSerializer

    @action(detail=False)
    def topOne(self, request):
        queryset = images.objects.all()[:1]
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def uploadImage(self, request):
        data = json.loads(request.body)
        respon= cloudinary.uploader.upload(data["photo"])
        print (respon["url"])
        content = {'message': 'image uploaded'}
        return Response(content, status=status.HTTP_200_OK)