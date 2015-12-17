__author__ = 'taztony2010'

#printing a dictionary function

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

#displayInventory(stuff)

#adding to a dictionary function

def addToInventory(inventory, addItems):

    itemList = inventory

    for item in addItems:
        if item in itemList.keys():
            itemList[item] += 1
        else:
            itemList.setdefault(item, 1)

    return itemList

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)