from typing import Iterable
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from enum import Enum


class Error(Enum):
    DEFAULT = {"code": -100, "detail": _("Oops!. Something went wrong, please contact us")}
    _DEFAULT_MESSAGE = {"code": -99, "detail": _("Default: {}")}


class APIError(Exception):
    def __init__(self, error: Error, extra=None):
        self.extra = extra or {}
        self.error = error
        self.extra = extra or None
        error_detail = error.value
        if self.extra:
            # Extra values can be used in foramtting a string that contains {}
            if isinstance(self.extra, list):
                error_detail['detail'] = error_detail['detail'].format(*extra)

        # try:
        #     logger.info(error.value)
        # except BaseException:
        #     pass
        super().__init__(error_detail)
