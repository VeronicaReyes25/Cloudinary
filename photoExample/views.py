from photoExample.models import photoExample
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
import cloudinary, json
from photoExample.serializers import PhotoExampleSerializer

class photoExampleviewSet(viewsets.ModelViewSet):
    queryset = photoExample.objects.all()
    serializer_class = PhotoExampleSerializer

    @action(methods=['post'], detail=False)
    def uploadImage(self, request):
        #Gets json from request body-->{“photo”: “cadena de imagen formateada en base64”}
        data = json.loads(request.body) #converting request.body to json 
        """
        this is a post request to upload a photo to cloudinary
        converting a base64 string that contains the photo 
        and saves the response from the post
        """
        respon= cloudinary.uploader.upload(data["photo"]) #the method from cloudbinary returns an url on a json
        #Save in table the URL from the upload 
        p = photoExample.objects.create(url=respon["url"]) 
        #Send message of success
        content = {'message': 'image uploaded and saved', 'photo': p.url}
        return Response(content, status=status.HTTP_201_CREATED)