w,h,b = map(int,input().split())

pixel = w * h * b / 8 / 1024/ 1024

print(round(pixel,2),' MB')