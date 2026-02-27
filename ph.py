import turtle as t
print("物理计算V1.0.0.0 [© Aogawa]")
print("输入你要计算的内容 [ 1-浮力 2-压强 3-重力 4-密度]")
a=int(input("请输入:"))
print("是否循环绘制图像 [ 1-是 2-否]")
b=int(input("请输入:"))
if a>4:
    print("你到底有没有听我说话zwz")
    print("我刚刚说1-浮力 2-压强 3-重力 4-密度！")
if b>2:
    print("你到底有没有听我说话zwz")
    print("我刚刚说1-是 2-否！")
if b==1:
    print("OK,turtle库，启动！")
    
#加载turtle
if b==1:
    print("等等turtle把坐标轴画好...")
    t.goto(0,400)
    t.goto(0,-400)
    t.goto(0,0)
    print("画画中...")
    t.goto(400,0)
    t.goto(-400,0)
    print("turtle画完了！")
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
#turtle画浮力
if a==1 and b==1:
    print("你的哪个数值在持续变化呢")
    print("F浮=ρ液gV排")
    print("Y轴是F浮哦")
    j=int(input("输入变化范围(最大值)："))
    i=int(input("输入变化范围(最小值)："))
    D1=int(input("另一个定值是："))
    for k in range(i,j):
        Fft=k*10*D1
        t.goto(k,Fft)
    

