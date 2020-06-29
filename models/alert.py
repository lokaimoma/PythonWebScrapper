from models import Model, Store, Item
from models.users import User
from dataclasses import dataclass, field
import uuid
from flask import session

@dataclass(eq=False)
class Alert(Model):
    name: str
    item_id: str
    user_email: str
    price: float
    price_limit: float
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    collection: str = field(init=False, default="alerts")


    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)
        self.user = User.find_by_email(self.user_email)


    def json(self):
        return {
            "name": self.name,
            "user_email": self.user_email,
            "price": self.price,
            "price_limit": self.price_limit,
            "item_id": self.item_id,
            "_id": self._id
        }

    def new_alert(name, url, price_limit):
        store = Store.get_store(url)

        item = Item.new_item(url, store.tag_name, store.query)

        Alert(name, item._id, session['email'], item.price, price_limit).save_to_mongo()
        
