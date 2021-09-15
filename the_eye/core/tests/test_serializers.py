from ..serializers import (
    EventBaseSerializer,
    PageViewSerializer,
    CtaClickSerializer,
    SubmitFormInteractionSerializar,
)


def test_base_serializer_valid():
    data = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "pageview",
        "data": {
            "host": "www.consumeraffairs.com",
            "path": "/",
        },
        "timestamp": "2021-01-01 09:15:27.243860",
    }

    serializer = EventBaseSerializer(data=data)
    assert serializer.is_valid()


def test_base_serializer_invalid():
    data = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "data": {
            "host": "www.consumeraffairs.com",
            "path": "/",
        },
        "timestamp": "2021-01-01 09:15:27.243860",
    }

    serializer = EventBaseSerializer(data=data)
    assert not serializer.is_valid()


def test_page_view_serializer_valid():
    data = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "pageview",
        "data": {
            "host": "www.consumeraffairs.com",
            "path": "/",
        },
        "timestamp": "2021-01-01 09:15:27.243860",
    }

    serializer = PageViewSerializer(data=data)
    assert serializer.is_valid()


def test_page_view_serializer_invalid():
    data = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "pageview",
        "data": {
            "host": "www.consumeraffairs.com",
        },
        "timestamp": "2021-01-01 09:15:27.243860",
    }

    serializer = PageViewSerializer(data=data)
    assert not serializer.is_valid()


def test_cta_click_serializer_valid():
    data = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "cta click",
        "data": {
            "host": "www.consumeraffairs.com",
            "path": "/",
            "element": "chat bubble",
        },
        "timestamp": "2021-01-01 09:15:27.243860",
    }

    serializer = CtaClickSerializer(data=data)
    assert serializer.is_valid()


def test_cta_click_serializer_invalid():
    data = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "cta click",
        "data": {
            "path": "/",
            "element": "chat bubble",
        },
        "timestamp": "2021-01-01 09:15:27.243860",
    }

    serializer = CtaClickSerializer(data=data)
    assert not serializer.is_valid()


def test_submit_form_serializer_valid():
    data = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "form interaction",
        "name": "submit",
        "data": {
            "host": "www.consumeraffairs.com",
            "path": "/",
            "form": {"first_name": "John", "last_name": "Doe"},
        },
        "timestamp": "2021-01-01 09:15:27.243860",
    }

    serializer = SubmitFormInteractionSerializar(data=data)
    assert serializer.is_valid()


def test_submit_form_serializer_invalid():
    data = {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "form interaction",
        "name": "submit",
        "data": {
            "host": "www.consumeraffairs.com",
            "path": "/",
        },
        "timestamp": "2021-01-01 09:15:27.243860",
    }

    serializer = SubmitFormInteractionSerializar(data=data)
    assert not serializer.is_valid()
