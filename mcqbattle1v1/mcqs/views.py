from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import McqSerializer,GameSerializer
from .models import MCQs
from rest_framework.response import Response
from rest_framework import status
from .models import Game


# Create your views here.

class McqListCreateView(APIView):
       permission_classes=[IsAuthenticated]


       def get(self,request):
        mcqs=MCQs.objects.all()
        serializer= McqSerializer(mcqs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

       def post(self,request):
            serializer=McqSerializer(data=request.data)

            if serializer.is_valid():
                 mcq=MCQs.objects.create(
                      body=serializer.validated_data['body'],
                      explanation=serializer.validated_data['explanation'],
                      options= serializer.validated_data['options'],
                 )
                 mcq.save()
                 return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
             
    
            



class McqRetrieveUpdateDestroyView(APIView):
       permission_classes=[IsAuthenticated]    


       def get_object(self,pk):
            try:
                 return MCQs.objects.get(pk=pk)
            except MCQs.DoesNotExist:
                 return None
                 

       def get(self,request,pk):
            mcq=self.get_object(pk)

            if mcq is None:
                 return Response(status=status.HTTP_404_NOT_FOUND)
            
            serilizer=McqSerializer(mcq)
            return Response(serilizer.data,status=status.HTTP_200_OK)
       

       
       def put(self,request,pk):
             mcq=self.get_object(pk=pk)
             if mcq is None:
                  return Response(status=status.HTTP_404_NOT_FOUND)
             serilizer=McqSerializer(mcq,data=request.data)
             if serilizer.is_valid():
                  mcq.body=serilizer.validated_data['body']
                  mcq.explanation=serilizer.validated_data['explanation']
                  mcq.options=serilizer.validated_data['options']
                  mcq.save()
                  return Response(serilizer.data,status=status.HTTP_200_OK)
             return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

            
       def delete(self,request,pk):
             mcq=self.get_object(pk)
             if mcq is None:
                  return Response(status=status.HTTP_404_NOT_FOUND)
             mcq.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)
       


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