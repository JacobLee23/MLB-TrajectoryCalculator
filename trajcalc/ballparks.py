"""

"""


import re

import bs4
import numpy as np
import pandas as pd

from . import _scrape
from .logger import logger


@_scrape.soup(
    url="https://en.wikipedia.org/wiki/Ballpark"
)
def current_ballparks(soup: bs4.BeautifulSoup) -> pd.DataFrame:
    """

    """
    css = "div.mw-parser-output > table:nth-last-of-type(2)"
    table = soup.select_one(css)
    logger.debug("Select One [%s]", css)

    table_rows = table.select("tr")[1:]
    logger.debug("Select [%s]: %d", "tr", len(table_rows))
    hrefs = [
        [e.select_one("a").attrs.get("href") for e in r.select("td")[:3]]
        for r in table_rows
    ]
    hrefs_df = pd.DataFrame(
        [[f"https://en.wikipedia.org{h}" for h in x] for x in hrefs],
        columns=["Stadium_URL", "Team_URL", "City_URL"]
    )

    df = pd.read_html(str(table))[0]
    df.applymap(lambda s: s.strip())
    df.rename(columns={"Cap.": "Capacity"}, inplace=True)
    df.iloc[:, 3] = df.iloc[:, 3].apply(
        lambda s: float(re.search(r"\d+", "".join(s.split(","))).group())
    )
    df.iloc[:, 4:] = df.iloc[:, 4:].applymap(
        lambda s: float(re.search(r"\d+", s).group()) if s != "TBA" else np.nan
    )
    df.insert(1, "Stadium_URL", hrefs_df.loc[:, "Stadium_URL"])
    df.insert(3, "Team_URL", hrefs_df.loc[:, "Team_URL"])
    df.insert(5, "City_URL", hrefs_df.loc[:, "City_URL"])

    return df
