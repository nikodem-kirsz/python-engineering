def set_global():
    global global_var
    global_var = 20

set_global()
print(global_var)  # Output: 20

def outer_function():
    outer_var = 10

    def inner_function():
        nonlocal outer_var
        outer_var = 20

    inner_function()
    print(outer_var)  # Output: 20

outer_function()