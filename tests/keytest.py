import keyboard as key
#key.wait("k")
#key.send("a",do_release=False)
while True:
    if key.is_pressed('w'):
        print("w p")
        while True:
            if key.is_pressed('w') == False:
                print("w released")
                break
    if key.is_pressed('s'):
        print("s p")
        while True:
            if key.is_pressed('s') == False:
                print("s released")
                break
    if key.is_pressed('a'):
        print("a p")
        while True:
            if key.is_pressed('a') == False:
                print("w released")
                break
    if key.is_pressed('d'):
        print("d p")
        while True:
            if key.is_pressed('d') == False:
                print("d released")
                break