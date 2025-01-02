from django.http import JsonResponse
import environ

env = environ.Env()

def members(request):
    CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)

    SQL_HOST = env("SQL_HOST", default=None)
    SQL_TABLE = env("SQL_TABLE", default=None)
    SQL_USER = env("SQL_USER", default=None)
    SQL_PASSWORD = env("SQL_PASSWORD", default=None)

    return JsonResponse({
        "secrets": {
            "CLOUDRUN_SERVICE_URL": CLOUDRUN_SERVICE_URL,
            "SQL_HOST": SQL_HOST,
            "SQL_TABLE": SQL_TABLE,
            "SQL_USER": SQL_USER,
            "SQL_PASSWORD": SQL_PASSWORD,
        }
    })