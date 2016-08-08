from __future__ import absolute_import
import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name, default=None):
    """Get the environment variable or return exception."""
    try:
        value = os.environ[var_name]
        if value is True or value.lower() == 'true'\
                or value == '1' or value == 1:
            return True
        if value is False or value.lower() == 'false'\
                or value == '0' or value == 0:
            return False
        return value
    except KeyError:
        if default is None:
            error_msg = "Set the %s environment variable" % var_name
            raise ImproperlyConfigured(error_msg)
        return default

def env_variable_exists(var_name):
    """Get the environment variable or return exception."""
    try:
        value = os.environ[var_name]
        return True
    except KeyError:
        return False


def retry(func, times, default=None):
    if times == 0:
        if default:
            return default
        raise Exception('{0} failed too many times'.format(func))
    try:
        return func()
    except:
        times = times - 1
        return retry(func, times, default=default)