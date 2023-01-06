Numeric = int | float

def clamp(val: Numeric, min_val: Numeric, max_val: Numeric) -> Numeric:
    return max(min_val, min(val, max_val))
