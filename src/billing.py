from src import utils


def get_product_details():
    """Collect and validate product and billing details."""
    utils.print_section("PRODUCT BILLING CALCULATOR")

    name = utils.get_non_empty_string("Enter product name: ")
    category = utils.get_non_empty_string("Enter product category: ")
    quantity = utils.get_positive_number("Enter quantity: ", value_type=int)
    unit_price = utils.get_positive_number("Enter unit price: ")
    discount_pct = utils.get_number_in_range("Enter discount percentage (0-100): ", 0, 100)
    gst_pct = utils.get_non_negative_number("Enter GST percentage: ")
    delivery_charge = utils.get_non_negative_number("Enter delivery charge: ")

    return {
        "name": name,
        "category": category,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_pct": discount_pct,
        "gst_pct": gst_pct,
        "delivery_charge": delivery_charge,
    }


def calculate_billing(product):
    """
    Gross amount      = quantity * unit price
    Discount amount    = gross amount * discount%
    Amount after disc. = gross amount - discount amount
    GST amount         = amount after discount * GST%
    Delivery is waived when amount after discount > DELIVERY_WAIVER_THRESHOLD
    Final amount        = amount after discount + GST amount + delivery (if not waived)
    """
    gross_amount = product["quantity"] * product["unit_price"]
    discount_amount = gross_amount * (product["discount_pct"] / 100)
    amount_after_discount = gross_amount - discount_amount
    gst_amount = amount_after_discount * (product["gst_pct"] / 100)

    delivery_waived = amount_after_discount > utils.DELIVERY_WAIVER_THRESHOLD
    delivery_applied = 0 if delivery_waived else product["delivery_charge"]

    final_amount = amount_after_discount + gst_amount + delivery_applied

    return {
        "gross_amount": gross_amount,
        "discount_amount": discount_amount,
        "amount_after_discount": amount_after_discount,
        "gst_amount": gst_amount,
        "delivery_waived": delivery_waived,
        "delivery_applied": delivery_applied,
        "final_amount": final_amount,
    }


def display_billing(product, bill):
    print()
    print(f"Product Name             : {product['name']}")
    print(f"Category                 : {product['category']}")
    print(f"Quantity                 : {product['quantity']}")
    print(f"Unit Price               : {utils.format_currency(product['unit_price'])}")
    print("-" * 60)
    print(f"Gross Amount             : {utils.format_currency(bill['gross_amount'])}")
    print(f"Discount Amount ({product['discount_pct']}%)    : {utils.format_currency(bill['discount_amount'])}")
    print(f"Amount After Discount    : {utils.format_currency(bill['amount_after_discount'])}")
    print(f"GST Amount ({product['gst_pct']}%)         : {utils.format_currency(bill['gst_amount'])}")
    if bill["delivery_waived"]:
        print(f"Delivery Charge          : Waived (amount after discount exceeds "
              f"{utils.format_currency(utils.DELIVERY_WAIVER_THRESHOLD)})")
    else:
        print(f"Delivery Charge          : {utils.format_currency(bill['delivery_applied'])}")
    print("-" * 60)
    print(f"FINAL PAYABLE AMOUNT     : {utils.format_currency(bill['final_amount'])}")


def run():
    """Entry point called by main.py for menu option 2."""
    product = get_product_details()
    bill = calculate_billing(product)
    display_billing(product, bill)
