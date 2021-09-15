from rest_framework import serializers


class EventBaseSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length=100, required=True)
    category = serializers.CharField(max_length=50, required=True)
    name = serializers.CharField(max_length=50, required=True)
    timestamp = serializers.DateTimeField(required=True)


class PageViewPayloadSerializer(serializers.Serializer):
    host = serializers.CharField(max_length=200, required=True)
    path = serializers.CharField(max_length=100, required=True)


class CtaClickPayloadSerializer(serializers.Serializer):
    host = serializers.CharField(max_length=200, required=True)
    path = serializers.CharField(max_length=100, required=True)
    element = serializers.CharField(max_length=100, required=True)


class SubmitFormInteraction(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)


class SubmitPayloadSerializer(serializers.Serializer):
    host = serializers.CharField(max_length=200)
    path = serializers.CharField(max_length=100)
    form = SubmitFormInteraction(required=True)


class PageViewSerializer(EventBaseSerializer):
    data = PageViewPayloadSerializer(required=True)


class CtaClickSerializer(EventBaseSerializer):
    data = CtaClickPayloadSerializer(required=True)

class SubmitFormInteractionSerializar(EventBaseSerializer):
    data = SubmitPayloadSerializer(required=True)



event_serializers = {
    'pageview': PageViewSerializer,
    'cta click': CtaClickSerializer,
    'submit': SubmitFormInteractionSerializar,
}