import random


def coupon_code(count):
    coupon_list = []

    while count != 0:
        code = (str(random.randint(100000, 999999)))
        coupon_list.append(code)
        count -= 1
    return coupon_list


if __name__ == "__main__":
    no_of_coupon = int(input("Enter the No of coupons needed: "))
    print("Coupons are : {}".format(coupon_code(no_of_coupon)))
