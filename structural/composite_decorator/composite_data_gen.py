from pymongo import MongoClient
import uuid
import random
import string

# CO/provider/account/date/xml/file.xml


def get_base_collection(db, country_code):
    return db[country_code]


def generate_random_documents(k):
    docs = []
    for _ in range(k):
        rnd_str = "".join(random.choice(string.ascii_letters) for i in range(10))
        rnd_str = f"{rnd_str}.xml"
        docs.append(rnd_str)
    return docs


def add_accounts(db_collection):
    for provider in db_collection.find():
        print(provider)
        accounts = []
        for _ in range(10):
            account_data = {
                "account_id": str(uuid.uuid4()),
                "20230701": {"xml": generate_random_documents(100)},
                "20230702": {"xml": generate_random_documents(100)},
                "20230703": {"xml": generate_random_documents(100)},
            }
            accounts.append(account_data)
        data_to_insert = {"accounts": accounts}
        db_collection.update_many({"_id": provider["_id"]}, {"$set": data_to_insert})


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client["composite"]
    # Getting sample base collection:
    collection_co = get_base_collection(db=db, country_code="CO")
    add_accounts(collection_co)
