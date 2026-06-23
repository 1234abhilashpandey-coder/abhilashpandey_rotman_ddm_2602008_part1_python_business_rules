# ---------- Constants ----------

DELIVERY_WAIVER_THRESHOLD = 5000           # Delivery is free once amount after discount exceeds this
LOAN_PROJECTION_MONTHS = 24                # Requested loan amount is spread over this many months
VALID_SEGMENTS = ("Standard", "Premium", "Enterprise")
VALID_VALUE_CATEGORIES = ("Low", "Medium", "High")
CASHBACK_CITIES = ("Lucknow", "Delhi", "Mumbai", "Bangalore", "Hyderabad")


# ---------- Generic input helpers ----------

def get_non_negative_number(prompt, value_type=float):
    """Keep asking until the user enters a number >= 0."""
    while True:
        raw = input(prompt).strip()
        try:
            value = value_type(raw)
        except ValueError:
            print("  -> Invalid input. Please enter a valid number.")
            continue
        if value < 0:
            print("  -> Invalid input. Value cannot be negative. Please try again.")
            continue
        return value


def get_positive_number(prompt, value_type=float):
    """Keep asking until the user enters a number > 0."""
    while True:
        raw = input(prompt).strip()
        try:
            value = value_type(raw)
        except ValueError:
            print("  -> Invalid input. Please enter a valid number.")
            continue
        if value <= 0:
            print("  -> Invalid input. Value must be greater than 0. Please try again.")
            continue
        return value


def get_number_in_range(prompt, min_value, max_value, value_type=float):
    """Keep asking until the user enters a number within [min_value, max_value]."""
    while True:
        raw = input(prompt).strip()
        try:
            value = value_type(raw)
        except ValueError:
            print("  -> Invalid input. Please enter a valid number.")
            continue
        if value < min_value or value > max_value:
            print(f"  -> Invalid input. Value must be between {min_value} and {max_value}. Please try again.")
            continue
        return value


def get_non_empty_string(prompt):
    """Keep asking until the user enters a non-blank string."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("  -> Invalid input. This field cannot be empty. Please try again.")
            continue
        return value


def get_value_from_set(prompt, allowed_values):
    """Keep asking until the user enters one of the allowed values (case-insensitive)."""
    lookup = {v.lower(): v for v in allowed_values}
    while True:
        raw = input(prompt).strip()
        if raw.lower() in lookup:
            return lookup[raw.lower()]
        print(f"  -> Invalid input. Allowed values are: {', '.join(allowed_values)}. Please try again.")


# ---------- Formatting helpers ----------

def format_currency(amount):
    return f"Rs. {amount:,.2f}"


def format_percentage(value):
    return f"{value:.2f}%"


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)
