from datetime import date

class Invoice:
    def __init__(self, doc_number: str, amount: float, **kwargs) -> None:
        self.doc_number = doc_number
        self.amount = amount
        self.discount_amount = 0.0
        self.assignment_date = None
        self.is_assigned = False
        self.negotiation_date = None
        self.is_negotiated = False

    def get_details(self):
        print(
            f"doc_number={self.doc_number}",
            f"amount={self.amount}",
            f"discount_amount={self.discount_amount}",
            f"assignment_date={self.assignment_date}",
            f"negotiation_date={self.negotiation_date}",
        )

class AssignmentDecorator(Invoice):
    def __init__(self, invoice: Invoice, assignment_date: date) -> None:
        invoice.is_assigned = True
        invoice.assignment_date = assignment_date
        
    def get_details(self):
        return super().get_details()


class NegotiationDecorator(Invoice):
    def __init__(self, invoice: Invoice, negotiation_date: date) -> None:
        invoice.is_negotiated = True
        invoice.negotiation_date = negotiation_date


class DiscountDecorator(Invoice):
    def __init__(self, invoice: Invoice, discount_amount: float) -> None:
        self.invoice = invoice
        self.discount_amount = discount_amount
        invoice.discount_amount += discount_amount
        invoice.amount = self.__discount()

    def __discount(self):
        total = self.invoice.amount - self.discount_amount
        return 0.0 if total < 0 else total


if __name__ == "__main__":
    invoice = Invoice("FE123", 1_000_000)
    invoice.get_details()
    
    print("***********************")
    print("Assignment process...")
    AssignmentDecorator(invoice=invoice, assignment_date=date.today())
    invoice.get_details()
    
    print("***********************")
    print("Discount process...")
    DiscountDecorator(invoice=invoice, discount_amount=100_000)
    invoice.get_details()

    print("***********************")
    print("Negotiation process...")
    NegotiationDecorator(invoice=invoice, negotiation_date=date.today())
    invoice.get_details()

    print("***********************")
    print("Discount process again...")
    DiscountDecorator(invoice=invoice, discount_amount=200_000)
    invoice.get_details()
