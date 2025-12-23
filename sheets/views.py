from rest_framework import viewsets
from auth_app.models import User
from .models import Sheet, Column, Row, Cell, Dependency, Attachment, Comment
from .serializers import (
    SheetSerializer, ColumnSerializer, RowSerializer, CellSerializer,
    DependencySerializer, AttachmentSerializer, CommentSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response

class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.owned_sheets.all() | self.request.user.shared_sheets.all()

    @action(detail=True, methods=['post'])
    def share(self, request, pk=None):
        sheet = self.get_object()
        user_ids = request.data.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)
        sheet.shared_with.add(*users)
        return Response(SheetSerializer(sheet).data)

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def get_queryset(self):
        return Column.objects.filter(sheet_id=self.kwargs['sheet_pk'])

    def perform_create(self, serializer):
        serializer.save(sheet_id=self.kwargs['sheet_pk'])

class RowViewSet(viewsets.ModelViewSet):
    queryset = Row.objects.all()
    serializer_class = RowSerializer

    def get_queryset(self):
        return Row.objects.filter(sheet_id=self.kwargs['sheet_pk'])

    def perform_create(self, serializer):
        serializer.save(sheet_id=self.kwargs['sheet_pk'])

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

    def get_queryset(self):
        return Cell.objects.filter(row_id=self.kwargs['row_pk'])

    def perform_create(self, serializer):
        serializer.save(row_id=self.kwargs['row_pk'])

class DependencyViewSet(viewsets.ModelViewSet):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer

    def get_queryset(self):
        return Dependency.objects.filter(predecessor__sheet_id=self.kwargs['sheet_pk'])

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    def get_queryset(self):
        return Attachment.objects.filter(row_id=self.kwargs['row_pk'])

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user, row_id=self.kwargs['row_pk'])

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(row_id=self.kwargs['row_pk'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, row_id=self.kwargs['row_pk'])
