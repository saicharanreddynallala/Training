# import math
# for i in range(40,100):
#     if math.sqrt(i) in range(1,10): // time complexity o(n)
#         print(i)
i=2
while(1):
    if i*i >40 and i*i <100:  # time complexity o(root n)
        print(i*i)
    if i*i>100:
        break
    i=i+1
