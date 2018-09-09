import pyautogui,time
time.sleep(3)
pyautogui.click()
distance = 200
#画正方形
# while distance > 0:
#     pyautogui.dragRel(distance,0,duration=0.2)
#     distance = distance - 5
#     pyautogui.dragRel(0,distance ,duration=0.2)
#     pyautogui.dragRel(-distance,0 ,duration=0.2)
#     distance = distance - 5
#     pyautogui.dragRel(0,- distance ,duration=0.2)

#画三角
# distance = 100
# while distance > 0:
#     pyautogui.dragRel(distance+5, 0, duration=0.2)
#     distance = distance - 5
#     pyautogui.dragRel(-(distance / 2), distance, duration=0.2)
#     distance = distance - 5
#     pyautogui.dragRel(-(distance / 2)-5, -distance, duration=0.2)
#     distance = distance - 5

pyautogui.dragRel(distance, 0, duration=0.2)
pyautogui.dragRel(-(distance / 2), distance, duration=0.2)
pyautogui.dragRel(-(distance / 2), -distance, duration=0.2)


pyautogui.dragRel(distance,0,duration=0.1)
pyautogui.dragRel(0,distance ,duration=0.1)
pyautogui.dragRel(-distance,0 ,duration=0.1)
pyautogui.dragRel(0,- distance ,duration=0.1)

#
# pyautogui.dragRel(200, 0, duration=0.2)
pyautogui.click()
pyautogui.typewrite('Hello world!')

# distance = 200
# while distance > 0:
#         pyautogui.dragRel(distance, distance*distance, duration=0.2)
#         distance = distance - 5


#画三角
# distance = 200
# while distance > 0:
#     pyautogui.dragRel(distance-5, 0, duration=0.2)
#     pyautogui.dragRel(-(distance / 2), distance, duration=0.2)
#     pyautogui.dragRel(-(distance / 2), -distance, duration=0.2)
#     distance = distance - 5

#画正方形
# while distance > 0:
#     pyautogui.dragRel(distance-10,0,duration=0.1)
#     pyautogui.dragRel(0,distance-10 ,duration=0.1)
#     pyautogui.dragRel(-(distance-10),0 ,duration=0.1)
#     pyautogui.dragRel(0,-(distance-10) ,duration=0.1)
#     distance = distance - 5