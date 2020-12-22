from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.session import Session
from ..serializers import SessionSerializer, UserSerializer

# Create your views here.
class Sessions(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = SessionSerializer
    def get(self, request):
        """Index request"""
        # Get all the sessions:
        # sessions = Session.objects.all()
        # Filter the sessions by owner, so you can only see your owned sessions
        sessions = Session.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = SessionSerializer(sessions, many=True).data
        return Response({ 'sessions': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['session']['owner'] = request.user.id
        # Serialize/create session
        session = SessionSerializer(data=request.data['session'])
        # If the mango data is valid according to our serializer...
        if session.is_valid():
            # Save the created session & send a response
            session.save()
            return Response({ 'session': session.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(session.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the session to show
        session = get_object_or_404(Session, pk=pk)
        # Only want to show owned sessions?
        if not request.user.id == session.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this session')

        # Run the data through the serializer so it's formatted
        data = SessionSerializer(session).data
        return Response({ 'session': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate session to delete
        session = get_object_or_404(Session, pk=pk)
        # Check the session's owner agains the user making this request
        if not request.user.id == session.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this session')
        # Only delete if the user owns the session
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['session'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['session'].get('owner', False):
            del request.data['session']['owner']

        # Locate Session
        # get_object_or_404 returns a object representation of our session
        session = get_object_or_404(Session, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == session.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this session')

        # Add owner to data object now that we know this user owns the resource
        request.data['session']['owner'] = request.user.id
        # Validate updates with serializer
        data = SessionSerializer(session, data=request.data['session'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
