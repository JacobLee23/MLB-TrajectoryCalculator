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
    res = requests.get(url)
    logger.debug("Response (%s): %d", res.url, res.status_code)

    soup = bs4.BeautifulSoup(res.text, features="lxml")
    return soup


def _soup(url: str) -> typing.Callable:
    """

    """
    def decorator(func: typing.Callable) -> typing.Callable:
        """

        """
        def wrapper(*args, **kwargs) -> typing.Any:
            """

            """
            soup = get_soup(url)
            res = func(soup, *args, **kwargs)
            return res

        return wrapper

    return decorator
