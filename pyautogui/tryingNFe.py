import pyautogui as pag
import time as tm
import pyperclip as ppc

file = open("command001.txt")
copies = []

for line in file:
    # print(line)
    block = line.split(" ")
    match block[0]:
        case "move":
            if len(block) == 3:
                pag.move((int) (block[1]),(int) (block[2]))
            elif len(block) == 4:
                pag.move((int) (block[1]),(int) (block[2]),(int)(block[3]))
            else:
                raise print(f"ERROR - not defined more than 4 or less than 3 parameters at '{block[0]}' : {block}")
        case "moveTo":
            if len(block) == 3:
                pag.moveTo((int) (block[1]),(int) (block[2]))
            elif len(block) == 4:
                pag.moveTo((int) (block[1]),(int) (block[2]),(int)(block[3]))
            else:
                raise print(f"ERROR - not defined more than 4 or less than 3 parameters at '{block[0]}' : {block}")
        case "sleep":
            if len(block) == 2:
                tm.sleep((int) (block[1]))
            else:
                raise print(f"ERROR - not defined more or less than 2 parameters at '{block[0]}' : {block}")
        case "discount":
            if len(block) == 2:
                for i in range((int)(block[1])):
                    print(5-i)
                    tm.sleep(1)
                print(0)
            else:
                raise print(f"ERROR - not defined more or less than 2 parameters at '{block[0]}' : {block}")
        case "click":
            if len(block) == 3:
                pag.click((int)(block[1]),(int)(block[2]))
            elif len(block) == 4:
                pag.click((int)(block[1]),(int)(block[2]),(int)(block[3]))
            else:
                raise print(f"ERROR - not defined more than 4 ou less than 3 parameters at '{block[0]}' : {block}")
        case "print":
            if len(block) >= 2:
                i = 0
                sentence = ""
                for item in block:
                    if item == "print":
                        i+=1
                        continue
                    if i == 1:
                        sentence += item[1::]
                    elif i == len(block)-1:
                        sentence += item[:-2]
                    else:
                        sentence += item[::]
                    if i!=len(block)-1:
                        sentence += " "
                    i+=1
                print(sentence)

            else:
                raise print(f"ERROR - not defined less than 2 parameters at 'print' : {block}")
        case "copy":
            if len(block) >= 2:
                i = 0
                sentence = ""
                for item in block:
                    if item == "copy":
                        i+=1
                        continue
                    if i == 1:
                        sentence += item[1::]
                    elif i == len(block)-1:
                        sentence += item[:-2]
                    else:
                        sentence += item[::]
                    if i!=len(block)-1:
                        sentence += " "
                    i+=1
                copies.append(sentence)
            else:
                raise print(f"ERROR - not defined less than 2 parameters at 'print' : {block}")
        case "paste":
            if len(block) == 2:
                print(copies)
                ppc.copy(copies[(int)(block[1])])
                pag.write(ppc.paste())
            else:
                raise print(f"ERROR - not defined more or less than 2 parameters at 'print' : {block}")
        case _:
            raise print(f"ERROR - instruction not defined '{block[0]}'")            


