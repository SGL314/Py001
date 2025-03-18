import pyautogui as pag

pag.moveTo(100,100,1)
pag.moveRel(50,50,1)
pag.click(200,200)
pag.dragTo(300,300,1)
pag.scroll(500) # muito estranho
pag.hotkey("ctrl", "r")

# screenshot = pag.screenshot() # interessante pelo gpt
# screenshot.save("screenshot.png")

# file = ...
# location = pag.locateOnScreen(file)
# if location:
#     x, y = pag.center(location) # aliás muito estranho isso
#     pag.click(x, y)

pag.alert("A")
pag.confirm("B")
pag.prompt("C")

print(pag.position())
print(pag.size()) # vê o tamanho
