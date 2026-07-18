gradebook={"a":90,"b":85,"c":78,"d":45,"e":88}
total=0
for score in gradebook.values():
    total=total+score
print("total score",total)
average=total/len(gradebook)
print("average",average)