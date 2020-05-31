

f = open("timestamp_data.txt", "a")
with open("turtlebot_battery_test_1.txt") as openfile:
    i=0
    for line in openfile:
        f.write(str(int((0.00062*i)+148.42)))
        f.write("\n")
        i+=1
