#LAB-02 - Build an Apply Discount Function
def apply_discount(price, discount):
    if not isinstance(price, (int,float)):
        return 'The price should be a number'
    elif not isinstance(discount, (int,float)):
        return 'The discount should be a number'
    elif price <= 0:
        return 'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    else:
        discount_dolar = price*(discount/100)
        final_price = price - discount_dolar
        return final_price

# Main Test
print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(74.5,20.0))