from rest_framework_nested import routers
from .views import (
    SheetViewSet, ColumnViewSet, RowViewSet, CellViewSet,
    DependencyViewSet, AttachmentViewSet, CommentViewSet
)

router = routers.SimpleRouter()
router.register(r'', SheetViewSet, basename='sheets')

sheets_router = routers.NestedSimpleRouter(router, r'', lookup='sheet')
sheets_router.register(r'columns', ColumnViewSet, basename='sheet-columns')
sheets_router.register(r'rows', RowViewSet, basename='sheet-rows')
sheets_router.register(r'dependencies', DependencyViewSet, basename='sheet-dependencies')

rows_router = routers.NestedSimpleRouter(sheets_router, r'rows', lookup='row')
rows_router.register(r'cells', CellViewSet, basename='row-cells')
rows_router.register(r'attachments', AttachmentViewSet, basename='row-attachments')
rows_router.register(r'comments', CommentViewSet, basename='row-comments')


urlpatterns = router.urls + sheets_router.urls + rows_router.urls
