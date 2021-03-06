from rest_framework import viewsets, permissions
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import UpdateModelMixin

from .models import Trip
from .serializers import TripSerializer
from rest_framework.response import Response
from rest_framework import status


class TripView(viewsets.ReadOnlyModelViewSet, UpdateModelMixin):
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    permission_classes = (permissions.AllowAny,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class CreateTripView(GenericAPIView):
    serializer_class = TripSerializer

    def get_trip(self):
        return get_object_or_404(self.get_queryset(), id=self.kwargs.get("id"))

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED, data=serializer.data)