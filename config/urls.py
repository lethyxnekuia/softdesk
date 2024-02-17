from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from softdesk.views import CommentViewSet, IssueViewSet, ProjectViewSet, ContributorViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"contributors", ContributorViewSet)
router.register(r"issues", IssueViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
