def discount(price, percent, d=True):
    if not (0 <= percent <= 100):
        raise ValueError(f"Плохие проценты {percent}")
    if d:
        return round(price * (1-percent/100)) # Цена со скидкой
    else:
        return 5/0



class Cart:
    def __init__(self):
        self.items =[]
    def add(self,name,price,qty=1):
        if qty<=0:
            raise ValueError(f"Плохие проценты")
        self.items.append((name,price,qty))

    def total(self,percent=0):
        s=sum([p*q for _, p, q in self.items ])
        return discount(s,percent)