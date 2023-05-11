##
## EPITECH PROJECT, 2022
## scrap
## File description:
## Scrapper.py
##

from bs4 import BeautifulSoup as bs
import requests
import json
from pprint import pprint

class Scrapper:
    def __init__(self, page_text: str):
        self.page_text = page_text
        self.parser = bs(self.page_text, "html.parser")
        self.data = self.parser.find_all(["div"], "FkdJRd vRIAEd dS8AEf")
        pprint(self.data)

