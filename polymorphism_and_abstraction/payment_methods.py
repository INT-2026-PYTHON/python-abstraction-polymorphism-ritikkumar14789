"""
## 2. Payment Methods — Duck Typing Polymorphism  *(Medium)*

=================================================
PAYMENT METHODS (DUCK TYPING)
=================================================

Problem Statement:
Build THREE INDEPENDENT classes that do NOT
share a common parent:

   class CreditCard:
       pay(amount)
   class UPI:
       pay(amount)
   class Cash:
       pay(amount)

Even though they have no common base class,
each one has a method named `pay(amount)`.
A single function `checkout(payment_method,
amount)` should work with ALL of them, just by
calling `payment_method.pay(amount)`.

This is DUCK TYPING POLYMORPHISM:
   "If it walks like a duck and quacks like a
    duck, it's a duck."
   If an object has a `pay()` method, the
   function treats it as a payment method.


-------------------------------------------------
Input Example:
methods = [
   CreditCard("Alice", "4111-1111-1111-1111"),
   UPI("bob@upi"),
   Cash("Carol"),
]

for m in methods:
    checkout(m, 500)

Output Example:
[CreditCard] Alice paid 500 via card 4111-1111-1111-1111
[UPI]        bob@upi paid 500
[Cash]       Carol paid 500 in cash

-------------------------------------------------
Explanation:
- `checkout` does not care which CLASS the
  object is, only that the object has a
  `pay()` method.
- This is polymorphism WITHOUT inheritance —
  Python doesn't require a shared base class.
- Adding a new payment method later (e.g.
  PayPal) only requires writing a new class
  with a `pay()` method; `checkout` keeps
  working unchanged.
=================================================

"""

class DebitPayment:

    def __init__(self, user, card_number):
        self.user = user
        self.card_number = card_number

    def pay(self, amount):
        print(f"{self.user} completed ₹{amount} payment using Debit Card ({self.card_number})")


class MobilePay:

    def __init__(self, upi_address):
        self.upi_address = upi_address

    def pay(self, amount):
        print(f"{self.upi_address} transferred ₹{amount} through UPI")


class HandCash:

    def __init__(self, customer):
        self.customer = customer

    def pay(self, amount):
        print(f"{self.customer} paid ₹{amount} with cash")


def make_payment(method, total):
    method.pay(total)


payment_methods = [
    DebitPayment("Alice", "4111-1111-1111-1111"),
    MobilePay("bob@upi"),
    HandCash("Carol")
]


for item in payment_methods:
    make_payment(item, 500)