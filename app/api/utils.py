from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework.response import Response
from rest_framework.settings import DEFAULTS
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if not response:
        return response

    data = {}
    errors = []
    for field, value in response.data.items():
        err_str = value
        if isinstance(value, list):
            val = " ".join(value)
            if field != DEFAULTS['NON_FIELD_ERRORS_KEY']:
                err_str = "{} : {}".format(field, val)
            else:
                err_str = val
        errors.append(err_str)

    if len(errors):
        data['error'] = errors if len(errors) > 1 else errors[0]

    data['status'] = response.status_code

    return Response(data, response.status_code, exception=True,
                    content_type='application/json')
