name_list = ["드링킹 요구르트", "딸기 우유"]
price_list = [1800, 1500]
qty_list = [4, 2]

for i in [0, 1]:
    name = name_list[i]
    sales = price_list[i] * qty_list[i]
    print(name + " 매출액: " + str(sales))
