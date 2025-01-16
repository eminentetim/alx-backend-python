from django.urls import path, include
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet

# Create a root router
router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversations')

# Create a nested router for messages within a conversation
nested_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),        # Include default routes
    path('', include(nested_router.urls)),  # Include nested routes
]