import cfscrape
import requests
import time
import urllib.request
from bs4 import BeautifulSoup
from match import Match


def scraper():
    # url = "https://www.hltv.org/"
    matches = []
    # We need to use this to avoid getting flaged as bot.
    # worker = cfscrape.create_scraper()
    # response = worker.get(url).content

    f = open("hltv_page.txt", "r")
    # I placed the page in a txt file so we do not spam the real page with request for now.
    response = f.read()
    f.close()

    soup = BeautifulSoup(response, "html.parser")
    all_matches_raw = soup.findAll("a", {"class": "hotmatch-box a-reset"})

    for match in all_matches_raw:
        current_teams = match.findAll("span", {"class", "team"})
        current_teams_time = match.findAll("div", {"class", "middleExtra"})
        if len(current_teams) == 2:
            matches.append(Match(current_teams[0].get_text(), current_teams[1].get_text(),
                                 current_teams_time[0].get_text()))
            # TODO: Get the start number of the game, get the flags of the game.

    for m in matches:
        print(m)


if __name__ == "__main__":
    scraper()
