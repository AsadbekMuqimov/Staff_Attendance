from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet, StaffAttendanceViewSet, PositionViewSet, ShiftViewSet, StaffShiftViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet)
router.register(r'staff-attendance', StaffAttendanceViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'shifts', ShiftViewSet)
router.register(r'staff-shifts', StaffShiftViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

