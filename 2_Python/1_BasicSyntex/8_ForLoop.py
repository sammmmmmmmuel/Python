for i in range(1, 11):
    print("i times : ", i)

apple = [["iphone11", "iphone X", "iphone 14"], ["ipad air", "ipad pro", "ipad"],
         ["macbook air", "macbook pro", "macbook"]]

for devices in apple: 
    # print(devices)
    for device in devices:
        print(device, end=", ")   # can use: print(device, end=" "), or print(device)
    print("")

position = [[13, 5], [32, 2], [22, 8]] # x and y axis

position = [[x+3, y+2] for x, y in position]

print(position)
## for x, y in positions:
##      x += 3
##      y += 2
##      position.append([x, y])
