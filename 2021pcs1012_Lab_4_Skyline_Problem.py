def createMatrix(rowCount, colCount, dataList):
    buildings = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            # you need to increment through dataList here, like this:
            rowList.append(dataList[3 * i + j])
        buildings.append(rowList)

    return buildings

alpha = []
beta = int(input("Enter the number of buildings: "))
for i in range(beta):
    for j in range(3):
        alpha.append(int(input("Enter the (Left, Height, Right): ")))
buildings = createMatrix(beta,3,alpha)
print(buildings)

edges = []
edges.extend([building[0],building[2]] for building in buildings)
edges = sorted(sum(edges,[])) #sorting and flatening the list of building edges
print(edges)

current = 0
points = []

for i in edges:
  active = []
  active.extend(building for building in buildings if (building[0] <= i and building[2] > i))
  #current observed point is within borders of these buildings (active buildings)
  print(i,active)
  if not active:
    #if there is no active buildings, highest point is 0
    current = 0
    points.append((i,0))
    continue
  max_h = max(building[1] for building in active)
  if max_h != current:
    #if current highest point is lower then highest point of current active buildings change current highest point
    current = max_h
    points.append((i,max_h))

print(points)
