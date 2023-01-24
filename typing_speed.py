from time import *
import random as r


def mistake(para, usertest):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error


def speed(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(userinput) / time_r
    return round(speed)


test = [
    "ome nights the wind never stops, beginning in a clean shrill pitch that broadens and deepens to a careless and suspenseful force, rattling shutters, knocking things off the balconies, creating a pause in one’s mind",
    "a waiting-for-the-full-force-to-hit. Inside the apartment, closet doors swing open, creak shut.",
    "I, the writer of this sentence, the wielder of Riptide also known as Anaklusmos in Greek, the president of Indiana, the reader and fan of The Heroes of Olympus and Percy Jackson by Rick Riordan and the lover of giraffes",
    "An Oklahoma appellate court rejected the appeal of an Indigenous man who claimed the state did not have the jurisdiction to prosecute him for a crime because it was committed within the boundaries of the Kickapoo Tribe’s Oklahoma reservation.",
    "My name is pranav"]
test1 = r.choice(test)
print("*****Typing Speed Calculator*****")
print(test1)
print()
print()

time_1 = time()
input1 = input("Enter:")
time_2 = time()

print("Speed:", speed(time_1, time_2, input1), "w/sec")
print("Error:", mistake(test1, input1))
