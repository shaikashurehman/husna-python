basket1={"apple","banana","mango","apple","grape"}
basket2={"mango","kiwi","banana","kiwi"}
print(basket1)
print(basket2)
basket1.add("orange")
common_fruits=basket1.intersection(basket2)
print("common fruits",common_fruits)