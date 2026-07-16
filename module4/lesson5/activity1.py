items=["pencil","eraser","notebook","sharpencer","glue"]
stock_counts=[12,0,8,5,3]
inventory={item:count for item,count in zip(items,stock_counts)}
print("full inventory:",inventory)
in_stock_item=[item for item in items if  inventory[item]>0]
print("item in stock:",in_stock_item)
chosen_item=input("which item do u want to buy?")
if chosen_item not in inventory or inventory[chosen_item]==0:
    print(chosen_item,"is out of stock!stopping the checker.")
    exit()
prices=[10,5,40,15,20]
markup=int(input("enter the markup amount to ad to every price:"))
marked_up_prices=list(map(lambda p:p+ markup,prices))
print("marked up prices:",marked_up_prices)
item_index=items.index(chosen_item)
chosen_price=marked_up_prices[item_index]
print("price of",chosen_item,"after markup:",chosen_price)
