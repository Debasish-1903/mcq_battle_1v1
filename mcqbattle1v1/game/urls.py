from django.urls import path
from .views import GameListCreateView, GameRetrieveUpdateDestroyView, AttemptCreateView, ParticipantGameStateRetrieveUpdateView
from .views import lobby_view,join_game_view
urlpatterns = [
    path('', GameListCreateView.as_view(), name='game-list-create'),
    path('<uuid:pk>/', GameRetrieveUpdateDestroyView.as_view(), name='game-detail'),
    path('attempts/', AttemptCreateView.as_view(), name='attempt-create'),
    path('game-state/<int:participant>/', ParticipantGameStateRetrieveUpdateView.as_view(), name='game-state-detail'),

    path('lobby/', lobby_view, name='lobby'),
    path('join/<uuid:game_id>/', join_game_view, name='join-game'),
]
