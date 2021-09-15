import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Get an instance of a logger
logger = logging.getLogger(__name__)

from .serializers import EventBaseSerializer, event_serializers

@api_view(['POST'])
def event(request):
    base_serializer = EventBaseSerializer(request.data)
    if not base_serializer.is_valid():
        return Response(base_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    event_name = base_serializer.data['name']

    serializer = event_serializers.get(event_name)
    if not serializer:
        logger.error('Payload error: event name not valid')
        return Response({'error:':'Event name not valid'}, status=status.HTTP_400_BAD_REQUEST)

    if not serializer.is_valid():
        logger.error(f'Payload error: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # TODO: call here celery task to run in background

    return Response(serializer.data, status=status.HTTP_201_CREATED)