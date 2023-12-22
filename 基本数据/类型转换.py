# 将数字类型转换成字符串类型
int_str = str(666)
print(type(int_str), int_str)

float_str = str(3.1415)
print(type(float_str), float_str)

# 将字符串类型转换成数字类型
str_int = int("20231217")
print(type(str_int), str_int)

str_float = float("2023.1217")
print(type(str_float), str_float)

print("整数类型与浮点类型的转换")
float_int = int(3.56)
print(type(float_int), float_int)

float_int2 = float(float_int)
print(type(float_int2), float_int2)

int_float = float(666)
print(type(int_float), int_float)

int_str = 999
print(type(int_str), int_str)