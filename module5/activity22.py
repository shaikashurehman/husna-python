class Employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print("Destructor called")
def create_obj():
    print('making object...')
    onj=Employee()
    print('function end...')
    return object

print('calling create_obj() function...')
obj=create_obj()
print('program end...')