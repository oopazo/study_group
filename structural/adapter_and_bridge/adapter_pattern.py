from typing import Any


def get_file():
    pass


def get_folio_from_json(json) -> str:
    pass


def get_amount_from_json(json) -> int:
    pass


def get_supplier_from_json(json) -> str:
    pass


def get_folio_from_csv(file) -> str:
    pass


def get_amount_from_csv(file) -> int:
    pass


def get_supplier_from_csv(file) -> str:
    pass


class Invoice:

    def __init__(self):
        self.folio = None
        self.amount = None
        self.supplier = None

    def build(self):
        file = get_file()
        if isinstance(file, dict):
            self.folio = get_folio_from_json(file)
            self.amount = get_amount_from_json(file)
            self.supplier = get_supplier_from_json(file)
        elif isinstance(file, list):
            self.folio = get_folio_from_csv(file)
            self.amount = get_amount_from_csv(file)
            self.supplier = get_supplier_from_csv(file)


class AbstractService:

    def __init__(self):
        self.file = self.__get_file()

    def __get_file(self) -> Any:
        pass

    def get_folio(self) -> str:
        pass

    def get_amount(self) -> int:
        pass

    def get_supplier(self) -> str:
        pass


class JsonService(AbstractService):

    def __init__(self):
        super().__init__()

    def get_folio(self) -> str:
        print('Get Folio')
        return 'Folio'

    def get_amount(self) -> int:
        print('Get Amount')
        return 1

    def get_supplier(self) -> str:
        print('Get Supplier')
        return 'Supplier'


class CsvService(AbstractService):

    def __init__(self):
        super().__init__()

    def get_folio(self) -> str:
        print('Get Folio')
        return 'CSV Folio'

    def get_amount(self) -> int:
        print('Get Amount')
        return 1

    def get_supplier(self) -> str:
        print('Get Supplier')
        return 'CSV Supplier'


class InvoiceAbstractAdapter(Invoice):

    def __init__(self, source: AbstractService):
        super().__init__()
        self.source = source

    def build(self):
        self.folio = self.source.get_folio()
        self.amount = self.source.get_amount()
        self.supplier = self.source.get_supplier()


def publish_invoice(invoice: Invoice):
    invoice.build()


if __name__ == '__main__':
    invoice = Invoice()
    publish_invoice(invoice)

    json_adapter: AbstractService = JsonService()
    invoice_adapter = InvoiceAbstractAdapter(json_adapter)
    publish_invoice(invoice_adapter)

    csv_adapter: AbstractService = CsvService()
    invoice_adapter = InvoiceAbstractAdapter(csv_adapter)
    publish_invoice(invoice_adapter)
