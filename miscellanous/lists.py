
furniture = ['table', 'chair', 'rack', 'shelf']

furniture.append('mirror')

furnitureCp = furniture.copy()
furniture.append('desk')
furnitureCp.append('another_shelf')

furniture.index('desk')

furniture.insert(3, 'sofa')
print(f'insert furniture {furniture}')

print(f'furniture: {furniture}, \nfurnitureCp: {furnitureCp}')

print(len(furniture))

furniture[0], furniture[3] = furniture[3], furniture[0]

print(f'furniture: {furniture}')

furniture = sorted(furniture, key=(lambda item: item))

print(furniture[1:-1])

for item in furniture:
    print(f'item: {item}')

for index, item in enumerate(furniture):
    print(f'index: {index}, value: {item}')

furnitureCp.append('rolling_chair')
furniture.append('pillow')
for item, itemCp in zip(furniture, furnitureCp):
    print(f'furniture item: {item} furnitureCp item: {itemCp}')

print('rack' in ['table', 'chair', 'rack', 'shelf']) # True
print('bed' in ['table', 'chair', 'rack', 'shelf']) # False
print('bed' not in furniture)
print('bed' in furniture)

