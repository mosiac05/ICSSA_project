from rest_framework import serializers
from .models import (Student, Level,
                     DepartmentalInfo, ExecutiveTenure,
                     ExecutivePost, ExecutiveMember,
                     PollQuestion, PollChoice, PollParticipant)

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    # level = serializers.HyperlinkedIdentityField(view_name='level-highlight', format='html')

    class Meta:
        model = Student
        fields = ['id', 'is_active', 'email', 'access_code', 'first_name', 'last_name', 'matric_number','level', 'date_created']
        # read_only_fields = ['access_code', 'date_created']

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    # students = serializers.HyperlinkedRelatedField(many=True, view_name='level-detail', read_only=True)

    class Meta:
        model = Level
        fields = ['id', 'name']

class DepartmentalInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DepartmentalInfo
        fields = ['id', 'title', 'body']

class ExecutiveTenureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExecutiveTenure
        fields = ['id', 'year', 'title', 'is_active']

class ExecutivePostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExecutivePost
        fields = ['title']

class ExecutiveMemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExecutiveMember
        fields = ['member', 'tenure', 'post']

class PollQuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PollQuestion
        fields = ['level', 'question', 'running_hours', 'status']

class PollChoiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PollChoice
        fields = ['poll', 'choice']

class PollParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PollParticipant
        fields = ['poll', 'student', 'choice']
