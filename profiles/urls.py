from rest_framework.routers import DefaultRouter
from profiles.views import (
    ProfileListView,
)

router = DefaultRouter()
router.register("profile", ProfileListView)

urlpatterns = [

]

urlpatterns += router.urls
