import pyautogui
pyautogui.PAUSE = 1 #暂停1s
pyautogui.FAILSAFE = True #启动自动防止故障功能
print(pyautogui.size())
width,height = pyautogui.size()
for i in range(2):
    pyautogui.moveTo(100,100,duration=0.25) #根据屏幕绝对位置移动到位置（100,100）,花费0.25秒
    pyautogui.moveTo(200,100,duration=0.25)
    pyautogui.moveTo(200,200,duration=0.25)
    pyautogui.moveTo(300,200,duration=0.25)
    pyautogui.moveTo(300,300,duration=0.25)

for i in range(2):
    pyautogui.moveRel(100,0,duration=0.25)#根据当前位置移动（100,0），花费0.25秒
    pyautogui.moveRel(-100,0,duration=0.25)#根据当前位置移动（-100,0），花费0.25秒

pyautogui.position() #获取鼠标位置

pyautogui.click(100,50,button='left') #在（100,50）位置左击
pyautogui.click(100,50,button='right') #在（100，50位置右击）
pyautogui.mouseDown() #鼠标下移，参数同上
pyautogui.mouseUp() #鼠标上移，参数同上
pyautogui.dragTo() #绝对位置拖动，参数同上
pyautogui.dragRel() #相对位置拖动，参数同上
pyautogui.scroll(200) #滚动屏幕，参数同上
pyautogui.screenshot() #获取屏幕快照，参数同上

#屏幕快照分析
im = pyautogui.screenshot()
im.getpixel(50,200)
pyautogui.pixelMatchesColor(50,200,(130,135,144))#匹配像素点RGB颜色，返回True\False0lo

pyautogui.typewrite('Hello world!')