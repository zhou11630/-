print("****************************")
print("****************************")
print("欢迎来到研究生重复性实验大冒险")
print("****************************")
print("****************************")
print("                          \n")
print("按任意键继续游戏\n")
input("")
print("游戏中你将扮演一位要赶在deadline之前完成实验的研究生，重复其他论文的实验结果，你可以选择进行实验的策略，不同的策略会有不同的成功率，或完成时间")
print("按任意键继续游戏\n")
input("")
print("开始游戏！！！！")
print("你来到实验室，看到空无一人，于是。。。\n")
print("你打算打扫房间选A，打算实验台选B，烧水喝茶选C，给同学打电话一起做实验选D\n")
choice1=input("")
if choice1=='A':
    print("房间里面很脏，你渡过了辛苦的一天，离deadline还剩4天\n")
elif choice1=='B':
    print("实验台焕然一新，你离deadline还剩4天\n")
elif choice1=='C':
    print("你渡过了舒服的一天，离deadline还剩5天\n")
elif choice1=='D':
    print("同学在图书馆约会，你数了数头发，很沮丧，离dealline还剩3天\n")
else:
    print("拼写错误，你错过了人生~~~")
    input("")

