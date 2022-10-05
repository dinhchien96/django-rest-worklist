from django.shortcuts import render, get_object_or_404

from .models import Work
from .serializers import WorkSerializer
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


# Create your views here.
class CreateTask(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = self.request.user)
            return Response({
                'data' : serializer.data,
                }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UpdateTask(APIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Work.objects.all()

    def patch(self, request, pk):
        user_task = self.queryset.filter(user_id = request.user.user_id)
        task = get_object_or_404(user_task, pk=pk)
        serializer = WorkSerializer(task, data=request.data, many = False)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data' : serializer.data,
                }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DeleteTask(APIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Work.objects.all()

    def delete(self, request, pk):
        user_task = self.queryset.filter(user_id = request.user.user_id)
        task = get_object_or_404(user_task, pk=pk)
        task.delete()
        return Response({'messages': 'Task deleted'}, status=HTTP_204_NO_CONTENT)


class ViewTask(APIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Work.objects.all()

    def get(self, request, pk = None):
        user_task = self.queryset.filter(user_id = request.user.user_id)
        if pk is not None:
            task = get_object_or_404(user_task, pk=pk)
            serializer = WorkSerializer(task)
            return Response({
                'data' : serializer.data,
                }, status=HTTP_200_OK)
        serializer = WorkSerializer(user_task, many = True)
        return Response({
                'data' : serializer.data,
                }, status=HTTP_200_OK)