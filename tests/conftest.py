def pytest_configure():
    from django.conf import settings
    settings.configure(
        URLS_EXCLUDED_FROM_SIGNATURE_CHECK=[],
        DIRECTORY_API_CLIENT_EXTERNAL_BASE_URL='https://api.com',
        DIRECTORY_API_CLIENT_EXTERNAL_API_KEY='test-api-key',
        DIRECTORY_API_CLIENT_EXTERNAL_SENDER_ID='test-sender-id',
        DIRECTORY_API_CLIENT_EXTERNAL_DEFAULT_TIMEOUT=5,
    )
