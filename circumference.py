import math
def calculate_circumference(radius):
    """calculate the circumference of a circle given its radius."""
    circumference=2*math.pi*radius
    return circumference
#example usage:
r=5
print(f"the circumference of a circle with radius{r}is:{calculate_circumference(r):.2f}")