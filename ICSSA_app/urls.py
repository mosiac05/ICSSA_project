from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ICSSA_app import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet),
router.register(r'levels', views.LevelViewSet),
router.register(r'dept-infos', views.DepartmentalInfoViewSet),
router.register(r'executive-tenures', views.ExecutiveTenureViewSet),
router.register(r'executive-posts', views.ExecutivePostViewSet),
router.register(r'executive-members', views.ExecutiveMemberViewSet),
router.register(r'polls', views.PollQuestionViewSet),
router.register(r'poll-choices', views.PollChoiceViewSet),
router.register(r'poll-participants', views.PollParticipantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
