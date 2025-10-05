import random

coin = 100  # 金币
blood = 100  # 血量

while blood > 0 and coin > 0:
    room = random.choice(["怪物房", "商店", "宝箱房", "陷阱房"])
    print(f"\n你进入了 {room}！")

    if room == "怪物房":
        choice = input("选择你的行动：1.攻击  2.逃跑\n")
        if choice == "1":
            result = random.choice(["success", "fail"])
            if result == "success":
                coin += 10
                print("你打败了怪物，获得 10 金币！")
            else:
                blood -= 10
                print("被怪物打伤，血量 -10！")
        else:
            print("你选择逃跑，没有获得奖励。")

    elif room == "商店":
        if coin >= 50:
            blood += 20
            coin -= 50
            print("你在商店购买药品，血量 +20，金币 -50。")
        else:
            print("金币不足，无法购买。")

    elif room == "宝箱房":
        coin += 100
        print("你打开宝箱，获得 100 金币！")

    elif room == "陷阱房":
        blood -= 50
        print("糟糕！你踩中了陷阱，血量 -50！")

    print(f"当前状态：金币 {coin}，血量 {blood}")

print("\n游戏结束！")
if blood <= 0:
    print("你死了！💀")
elif coin <= 0:
    print("你破产了！💸")
