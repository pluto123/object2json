import json
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class UserInfo:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address


class Order:
    def __init__(self, order_id, user, items):
        self.order_id = order_id
        self.user_info = user
        self.item_list = items


def obj_2_json(data):
    MyEncoder().encode(data)
    # convert to JSON string
    jsonStr = json.dumps(data.__dict__, cls=MyEncoder)
    # print json string
    print(jsonStr)
    return jsonStr


if __name__ == '__main__':
    item1 = Item('book', 12)
    item2 = Item('pen', 3)
    item_list = [item1, item2]
    user_info = UserInfo('steven', '03-5678912', 'Taiwan')
    order = Order(1, user_info, item_list)
    obj_2_json(order)
