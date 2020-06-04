# Solution by using diagnols pattern
# https://www.youtube.com/watch?v=hSeGuxCn3mg

def shapeArea(n):
    if n == 1:
        return 1
    area = (n*n) + (n-1)*(n-1)
    return area