from django.http import HttpResponse
from django.views.generic import View
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import (Student, Level,
                     DepartmentalInfo, ExecutiveTenure,
                     ExecutivePost, ExecutiveMember,
                     PollQuestion, PollChoice, PollParticipant)

from .serializers import (StudentSerializer, LevelSerializer,
                            DepartmentalInfoSerializer, ExecutiveTenureSerializer,
                            ExecutivePostSerializer, ExecutiveMemberSerializer,
                            PollQuestionSerializer, PollChoiceSerializer,
                            PollParticipantSerializer)
# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse('Welcome to ICCSA App. You can go to /api/v1')

class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provide list, create, retrieve, update, and destroy actions.

    Additionally the extra highlight action is provided.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LevelViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DepartmentalInfoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = DepartmentalInfo.objects.all()
    serializer_class = DepartmentalInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ExecutiveTenureViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = ExecutiveTenure.objects.all()
    serializer_class = ExecutiveTenureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ExecutivePostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = ExecutivePost.objects.all()
    serializer_class = ExecutivePostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ExecutiveMemberViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = ExecutiveMember.objects.all()
    serializer_class = ExecutiveMemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PollQuestionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = PollQuestion.objects.all()
    serializer_class = PollQuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PollChoiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = PollChoice.objects.all()
    serializer_class = PollChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PollParticipantViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = PollParticipant.objects.all()
    serializer_class = PollParticipantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
