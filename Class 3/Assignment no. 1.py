price=int(input("what is your total?"))
askCoupon=(input ("put any coupons you have:"))
discountedprice = 0
coupondiscount = 0
if price > 500:
    discountedprice = price * 0.05
if askCoupon == "Save10":
    coupondiscount= price *0.1
finalprice = price - discountedprice+coupondiscount
print(f"""
    ---------- total -------------
      total       :     {price}
    ------ Price discount --------
    Dicount because of cost :     {discountedprice}
    ------ Coupon discount -------
    Dicount because of coupon:       {coupondiscount}
    ----- Final Total ------------ 
    End total :                {finalprice}
""")