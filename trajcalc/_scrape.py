"""

"""


import typing

import bs4
import requests

from .logger import logger


def get_soup(url: str) -> bs4.BeautifulSoup:
    """

    :param url:
    :return:
    """
    _res = requests.get(url)
    logger.debug("Response (%s): %d", _res.url, _res.status_code)

    _soup = bs4.BeautifulSoup(_res.text, features="lxml")
    return _soup


def soup(url: str) -> typing.Callable:
    """

    """
    def decorator(func: typing.Callable) -> typing.Callable:
        """

        """
        def wrapper(*args, **kwargs) -> typing.Any:
            """

            """
            _soup = get_soup(url)
            _res = func(_soup, *args, **kwargs)
            return _res

        return wrapper

    return decorator
