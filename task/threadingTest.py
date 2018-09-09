import threading,time
def takeanap():
    time.sleep(5)
    print('Wake up')

threadObj = threading.Thread(target=takeanap())
threadObj.start()

print('Enf of program')