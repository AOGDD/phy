import turtle as t
print("物理计算V1.0.0.0 [© Aogawa]")
print("输入你要计算的内容 [ 1-浮力 2-压强 3-重力 4-密度]")
a=int(input("请输入:"))
print("是否循环绘制图像 [ 1-是 2-否]")
b=int(input("请输入:"))
if a>4:
    print("未知计算重新输入")
if b>2:
    print("未知状态请重新输入")
if b==1:
    print("可视化计算正在更新中，详情请关注我的github")
    
#加载turtle
if b==1:
    print("请等待turtle初始化...")
    t.goto(0,400)
    t.goto(0,-400)
    t.goto(0,0)
    t.write("此功能未完善", font=("黑体", 20, 'bold'))
    print("可视化计算正在更新中，详情请关注我的github")
    print("响应中")
    t.goto(400,0)
    t.goto(-400,0)
    print("turtle初始化完成")
    t.goto(0,0)

#浮力计算模块
if b == 2 and a==2:
    c=int(input("请输入ρ :"))
    e=int(input("请输入V :"))
    print("F浮=ρ液gV排")
    Ff=c*10*e
    print("")
    print("计算完成")
    print("")
    print("【 F浮=",Ff," 】")
    
#压强计算模块
if b == 2 and a==1:
    F=int(input("请输入F :"))
    S=int(input("请输入S :"))
    print("P=F/S")
    P=F/S
    print("")
    print("计算完成")
    print("")
    print("【 P=",P," 】")        

#密度计算模块
if b == 2 and a==4:
    m=int(input("请输入m :"))
    v=int(input("请输入V :"))
    print("ρ= m/v")
    R = m/v
    print("")
    print("计算完成")
    print("")
    print("【 ρ=",R," 】")

#重力计算模块
if b == 2 and a==3:
    m=int(input("请输入m :"))
    print("G=mg")
    G=m*10
    print("")
    print("计算完成")
    print("")
    print("【 G=",G," 】")

