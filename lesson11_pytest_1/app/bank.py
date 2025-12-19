

def calculate_discount(price, category):
    """Нараховує знижку: 'VIP' - 20%, 'Student' - 10%, іншим - 0%."""
    if price < 0:
        raise ValueError("Ціна не може бути від'ємною")
    
    if category == "VIP":
        return price * 0.8
    elif category == "Student":
        return price * 0.9
    else:
        return price
