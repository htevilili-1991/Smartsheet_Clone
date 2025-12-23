from rest_framework import serializers
from .models import Sheet, Column, Row, Cell, Dependency, Attachment, Comment
from auth_app.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)

    class Meta:
        model = Attachment
        fields = '__all__'

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = ('id', 'column', 'value', 'link')

class RowSerializer(serializers.ModelSerializer):
    cells = CellSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    children = serializers.SerializerMethodField()

    class Meta:
        model = Row
        fields = ('id', 'sheet', 'parent', 'position', 'created_at', 'updated_at', 'cells', 'comments', 'attachments', 'children')

    def get_children(self, obj):
        return RowSerializer(obj.children.all(), many=True).data

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'

class SheetSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    shared_with = UserSerializer(many=True, read_only=True)
    columns = ColumnSerializer(many=True, read_only=True)
    rows = serializers.SerializerMethodField()

    class Meta:
        model = Sheet
        fields = ('id', 'title', 'owner', 'created_at', 'updated_at', 'shared_with', 'columns', 'rows')

    def get_rows(self, obj):
        # Return only top-level rows
        return RowSerializer(obj.rows.filter(parent__isnull=True), many=True).data

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = '__all__'
