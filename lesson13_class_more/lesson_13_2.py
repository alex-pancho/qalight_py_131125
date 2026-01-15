class Money():

    def __init__(self, amount:float) -> None:
        self.__amount = amount

    def __str__(self):
        return f"{self.__amount:.2f}"

    def __add__(self, other):
        if not isinstance(other, (float, int, Money)):
            raise TypeError(f"int or float is expected, {type(other)} get")
        if isinstance(other, Money) and type(self) == type(other):
            self.__amount = self.__amount + other.amount
            return self.__amount
        elif isinstance(other, (float, int)):
            self.__amount = self.__amount + other
            return self.__amount
        else:
            raise TypeError (f"{type(self)} != {type(other)}, only equal type is supported")

    def __sub__(self, other):
        if not isinstance(other, (float, int, Money)):
            raise TypeError(f"int, float or Money is expected, {type(other)} get")
        if other > self.__amount:
            raise ValueError("Has not cost in ammount, try less value")
        if isinstance(other, Money) and type(self) == type(other):
            self.__amount = self.__amount - other.amount
            return self.__amount
        elif isinstance(other, (float, int)):
            self.__amount = self.__amount - other
            return self.__amount
        else:
            raise TypeError (f"{type(self)} != {type(other)}, only equal type is supported")
    
    @property
    def amount(self):
        return self.__amount




class UAH(Money):

    def __init__(self, amount: float) -> None:
        Money.__init__(self, amount)
        # super().__init__(amount)

    def __str__(self):
        return f"{self.amount:.2f} грн"



class USD(Money):

    def __init__(self, amount: float) -> None:
        Money.__init__(self, amount)
        # super().__init__(amount)

    def __str__(self):
        return f"${self.amount:.2f}"

class ForEx():
    def __init__(self, exchange_rate_by, exchange_rate_sell):
        self.exchange_rate_by = exchange_rate_by
        self.exchange_rate_sell = exchange_rate_sell
    
    def convert(self, cur_amount):
        if isinstance(cur_amount, UAH):
            usd_amount = cur_amount.amount / self.exchange_rate_sell
            return USD(usd_amount)
        if isinstance(cur_amount, USD):
            uah_amount = cur_amount.amount * self.exchange_rate_by
            return UAH(uah_amount)
        else:
            raise TypeError("Wrong type for convert: UAH USD is supported")



if __name__ == "__main__":

    my_fist_money = Money(102.33)
    print(my_fist_money)
    my_fist_money + 22
    print(my_fist_money)
    my_fist_money - 11
    print(my_fist_money)

    # my_fist_money + "abd"
    # print(my_fist_money)

    my_uah_cash = UAH(3000)
    my_wife_uah_cash = UAH(30500)
    print(my_uah_cash)
    print(my_wife_uah_cash)
    print(my_uah_cash + my_wife_uah_cash)

    my_usd_cash = USD(100)
    my_wife_usd = USD(200)
    family_total_cash = my_usd_cash + my_wife_usd
    print(family_total_cash)

    privatbank = ForEx(42.05, 43.57)
    akord_bank = ForEx(41.37, 42.00)

    pb_to_uah = privatbank.convert(my_usd_cash)
    pb_to_usd = privatbank.convert(my_uah_cash)
    ak_to_uah = akord_bank.convert(my_usd_cash)
    ak_to_usd = akord_bank.convert(my_uah_cash)

    print(f"Продати {my_usd_cash}:", pb_to_uah, "|", ak_to_uah)
    print(f"Купити на {my_uah_cash}:", pb_to_usd, "|", ak_to_usd)

"""
    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__matmul__(self, other)
    object.__truediv__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)
"""
