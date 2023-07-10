from pymongo import MongoClient
from typing import List


class Document:
    def __init__(self) -> None:
        self.is_doc = None

    def is_document(self):
        pass


class CachedCollection(Document):
    def __init__(self, path) -> None:
        self.path = path

    def is_document(self):
        return False

    def __str__(self) -> str:
        return f"path={self.path}"


class CachedDocument(CachedCollection):
    def __init__(self, name) -> None:
        self.name = name

    def is_document(self):
        return True

    def __str__(self) -> str:
        return f"name={self.name}"


class Tracker:
    """Composite"""

    def __init__(self) -> None:
        self.documents: List[Document] = []

    def add(self, child: Document):
        self.documents.append(child)

    def remove(self, child: Document):
        pass

    def get_cached_documents(self, candidates: List[str]):
        search_docs = set()
        for document in self.documents:
            if document.is_document():
                search_docs.add(document.name)
        return set(candidates) - search_docs

    def get_cached_folders(self, candidates: List[str]):
        search_dirs = set()
        for folder in self.documents:
            if not folder.is_document():
                search_dirs.add(folder.path)
        return set(candidates) - search_dirs


def load_composite(db):
    country = "CO"
    tracker = Tracker()
    tracker.add(CachedCollection(path=country))
    for entry in db[country].find({}):
        provider = entry["provider"]
        tracker.add(CachedCollection(path=provider))
        for account in entry["accounts"]:
            account_id = account["account_id"]
            tracker.add(CachedCollection(path=account_id))
            for key in account.keys():
                tracker.add(CachedCollection(path=key))
                if key != account_id and type(account[key]) == dict:
                    documents = account[key]["xml"]
                    for doc_name in documents:
                        cached_document = CachedDocument(name=doc_name)
                        tracker.add(cached_document)
    return tracker


def get_cached_docs(tracker):
    docs_from_db = ["uDbIkzVZWL.xml", "wsgkjgkcqt.xml", "qAgFDTrrGf.xml"]
    docs_not_in_db = ["uDbIkzVZWL.mp3", "wsgkjgkcqt.jpg", "qAgFDTrrGf.pdf"]
    candidates = docs_from_db + docs_not_in_db
    # Check what candidates have been tracked before:
    cached_docs = tracker.get_cached_documents(candidates)
    print("Documents not stored in db:")
    print(cached_docs)


def get_cached_folders(tracker):
    folders_from_db = ["CO", "ALEGRA", "20230701"]
    folders_not_in_db = ["CL", "SII", "20230705"]
    candidates = folders_from_db + folders_not_in_db
    # Check what candidates have been tracked before:
    cached_folders = tracker.get_cached_folders(candidates)
    print("Folders not stored in db:")
    print(cached_folders)


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    # Getting collection to work with:
    db = client["composite"]
    # Loading Documents and Collections:
    tracker = load_composite(db)
    # Example for leaf:
    get_cached_docs(tracker)
    # Example for container:
    get_cached_folders(tracker)
