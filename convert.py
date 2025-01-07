# Write a function that takes an arg expressed in meters and returns the equivalent in miles, yards, feet and inches
def convert(metri):
    inch = 0.0254
    result1 = metri / inch

    foot = 12 * inch
    result2 = metri / foot 

    yard = 3 * foot
    result3 = metri / yard

    miles =  1760 * yard
    result4 = metri / miles

    return print(f"inch {result1}, foot {result2}, yard {result3}, miles {result4}")
