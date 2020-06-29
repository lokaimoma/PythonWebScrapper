from dataclasses import dataclass, field
import uuid
from models import Model
from typing import Dict
import requests
from bs4 import BeautifulSoup
import re

#to use this moduel import the module and use the Item.new_item(url, tag_name, query)
#to make things simple

@dataclass(eq=False)
class Item(Model):
    url: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    collection: str = field(init=False, default="items")

    def __post_init__(self):
        self.price = None

    def json(self):
        return {
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query,
            "_id": self._id
        }

    def calc(self):
        page = requests.get(self.url)
        content = page.content

        soup = BeautifulSoup(content, "html.parser")
        s1 = soup.find(self.tag_name, self.query)
        s1 = s1.text.strip()

        pattern = re.compile(r"(\d+,?.?\d*\.?\d*)")
        match = pattern.search(s1)
        match = match.group(1)
        match = match.replace(",", "")
        match = match.replace(" ", "")
        match = float(match)

        self.price = match
        
    @staticmethod
    def new_item(url, tag_name, query):
        item = Item(url, tag_name, query)
        item.calc()
        item.save_to_mongo()
        return item

