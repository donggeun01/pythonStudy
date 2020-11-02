import mycircle as my
import math

print('모듈을 사용하여 원의 면적과 둘레를 구합니다.')

print("%.2f" %my.circle_area(5))
print("%.2f" %my.circle_circum(5))

degree = int(input("각도"))
radian = degree * math.pi / 180
print('sin',degree,'',math.sin(degree * math.pi / 180))
print('pos',degree,'',math.cos(degree * math.pi / 180))

