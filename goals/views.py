from rest_framework import permissions
from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView

from django.db.models import Q
from goals.models import GoalCategory, Goal


class GoalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalCategory
        read_only_fields = ('id', 'created', 'updated')
        fields = ('title', 'created', 'updated')


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        read_only_fields = ('id', 'created', 'updated')


class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = GoalSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).order_by('due_date')


class GoalCategoryListView(ListAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(user=self.request.user) | Q(user=None))
        return queryset


class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GoalCreateView(CreateAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    # TODO validate common and self created category, unique constraints

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
