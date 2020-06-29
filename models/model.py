from abc import ABCMeta, abstractmethod
from common import Database


class Model(metaclass=ABCMeta):
    @abstractmethod
    def json(self):
        raise NotImplementedError

    def save_to_mongo(self):
        Database.insert(self.collection, self.json())

    def update_mongo(self, _id):
        Database.update(self.collection, query={"_id": _id}, data=self.json())

    @classmethod
    def remove_from_mongo(cls, _id):
        Database.remove(cls.collection, {"_id": _id})

    @classmethod
    def find_only_one(cls, attrib, value):
        return cls(**Database.find_one(cls.collection, {attrib: value}))

    @classmethod
    def find_all(cls):
        datas = Database.find(cls.collection, {})
        return [cls(**data) for data in datas]

    @classmethod
    def get_by_id(cls, _id):
        return cls.find_only_one("_id", _id)

    @classmethod
    def find_many_by(cls, attrib, value):
        data = Database.find(cls.collection, {attrib: value})
        return [cls(**datas) for datas in data]

    @classmethod
    def all(cls):
        return cls.find_all()

