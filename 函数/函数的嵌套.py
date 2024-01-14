def fun_a():
    print("-----1-----")


def fun_b():
    print("-----2-----")
    fun_a()
    print("-----3-----")


fun_b()
