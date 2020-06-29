from models import Model
from dataclasses import dataclass, field
import uuid
from typing import Dict
import re


@dataclass(eq=False)
class Store(Model):
    name: str
    url_prefix: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    collection: str = field(init=False, default="stores")


    def json(self):
        return {
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query,
            "_id": self._id
        }

    @classmethod
    def get_store(cls, url):
        pattern = re.compile(r"(https?://.*?/)")
        match = pattern.search(url)
        match = match.group(1)
        return cls.get_by_url(match)
        
    @classmethod
    def get_by_url(cls, url):
        urlregex = {"$regex": "^{}".format(url)}
        return cls.find_only_one("url_prefix", urlregex)
