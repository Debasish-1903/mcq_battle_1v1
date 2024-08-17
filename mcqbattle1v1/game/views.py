from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Game ,Attempt, ParticipantGameState
from .serializer import GameSerializer, AttemptSerializer, ParticipantGameStateSerializer

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

class GameListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       


class GameRetrieveUpdateDestroyView(APIView):
     permission_classes = [IsAuthenticated]

     def get_object(self, pk):
          try:
               return Game.objects.get(pk=pk)
          except Game.DoesNotExist:
               return None

     def get(self, request, pk):
          game = self.get_object(pk)
          if game is None:
               return Response(status=status.HTTP_404_NOT_FOUND)
          serializer = GameSerializer(game)
          return Response(serializer.data, status=status.HTTP_200_OK)

     def put(self, request, pk):
          game = self.get_object(pk)
          if game is None:
               return Response(status=status.HTTP_404_NOT_FOUND)
          serializer = GameSerializer(game, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_200_OK)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
          game = self.get_object(pk)
          if game is None:
               return Response(status=status.HTTP_404_NOT_FOUND)
          game.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)






class AttemptCreateView(generics.CreateAPIView):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer

class ParticipantGameStateRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ParticipantGameState.objects.all()
    serializer_class = ParticipantGameStateSerializer
    lookup_field = 'participant'



@login_required
def lobby_view(request):
    available_games = Game.objects.filter(status='waiting') 
    return render(request, 'game/lobby.html', {'available_games': available_games})

@login_required
def join_game_view(request, game_id):
    game = get_object_or_404(Game, id=game_id, status='waiting')
    
  
    if game.participants.count() >= game.max_participants:
        return redirect('lobby')

    game.participants.add(request.user)
    
  
    ParticipantGameState.objects.create(game=game, participant=request.user)
    
    return redirect('game-detail', game_id=game.id)
