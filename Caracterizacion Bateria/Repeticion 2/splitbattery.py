

f = open("battery_data.txt", "a")
with open("turtlebot_battery_test_2.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if "battery:" in part:
                f.write(line.split()[1])
                f.write("\n")

f = open("timestamp_data.txt", "a")
with open("turtlebot_battery_test_2.txt") as openfile:
    for line in openfile:
        for part in line.split():
            # print(part);
            if ("secs:" in part) and ("nsecs:" not in part):
                # print(line.split()[1])
                f.write(str((int(line.split()[1])-1580220819)/60))
                f.write("\n")
