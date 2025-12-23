from django.db import models
from auth_app.models import User

class Sheet(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_sheets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shared_with = models.ManyToManyField(User, related_name='shared_sheets', blank=True)

    def __str__(self):
        return self.title

class Column(models.Model):
    COLUMN_TYPES = [
        ('text', 'Text'),
        ('date', 'Date'),
        ('dropdown', 'Dropdown'),
        ('contact', 'Contact List'),
        ('checkbox', 'Checkbox'),
        ('duration', 'Duration'),
        ('predecessor', 'Predecessor'),
    ]
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name='columns')
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=COLUMN_TYPES)
    position = models.PositiveIntegerField()
    options = models.JSONField(blank=True, null=True)  # For dropdown options

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.sheet.title} - {self.title}"

class Row(models.Model):
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name='rows')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    position = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['position']

class Cell(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='cells')
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cells')
    value = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True) # For hyperlinks

    class Meta:
        unique_together = ('row', 'column')

class Dependency(models.Model):
    predecessor = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='successors')
    successor = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='predecessors')
    type = models.CharField(max_length=10) # e.g., 'FS', 'SS', 'FF', 'SF'
    lag = models.DurationField(blank=True, null=True)

class Attachment(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
