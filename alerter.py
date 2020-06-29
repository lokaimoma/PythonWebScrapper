import gmailFier
import time
from models import Alert, Item

alerts = Alert.find_all
for a in alerts:
    item1 = Item.find_only_one("_id", a.item_id)
    item1.calc()
    a.price = item1.price
    a.update_mongo(a._id)

    if a.price >= a.price_limit:
        



