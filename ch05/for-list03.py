name_set = ["드링킹 요구르트", "딸기 우유"]
price_set = [1800, 1500]
qty_set = [4, 2]

for i in [0, 1]:
    name = name_set[i]
    sales = price_set[i] * qty_set[i]
    print(name + " 매출액 : " + str(sales))
