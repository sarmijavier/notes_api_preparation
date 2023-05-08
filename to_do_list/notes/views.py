"""
This is the views of Notes application
"""
from rest_framework import mixins, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from notes.permissions import IsOwnerOrReadOnly, IsOwner
from notes.models import Note
from notes.serializers import NoteSerializer, UserSerializer


class NoteList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        generics.GenericAPIView
):
    """
    This is view to get the notes of the user,
    and create a new note
    """
    serializer_class = NoteSerializer
    permission_classes = [
        AllowAny, IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView
):
    """
    This view get, edit and delete a note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserView(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    This view allows to create new users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'})

        login(request, user)
        return Response({'success': True})
