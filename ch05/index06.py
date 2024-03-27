name_list = ["드링킹 요구르트", "딸기 우유", "홈런공"]
price_list = [1800, 1500, 1000]
qty_list = [4, 2, 3]

for i in range(len(name_list)):
    name = name_list[i]
    sales = price_list[i] * qty_list[i]
    print(name + " 매출액 : " + str(sales))
