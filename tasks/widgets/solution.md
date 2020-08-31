# Widgets

## DB Schema

```
class Customer:
    name: str

class Packaging:
    type: str

class Supplier:
    name: str

class Warehouse:
    name: str

class Widget:
    name: str
    supplier: Supplier
    cost: Decimal
    warehouse: Warehouse
    quantity: int
    min_quantity: int

class Order:
    widget: Wiget
    packaging: Packaging
    quantity: int
    customer: Customer
    price: Decimal
```

### What you think this system would do?

I have no idea. It looks like some kind of order system, maybe for a shop.

### Any questions or concerns you have regarding this dataset?

* how does the packaging works?
* why do some customers pay more for the same product?
