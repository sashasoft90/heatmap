from shapely.geometry import Point, Polygon

# Create Point objects
p1 = Point(24.952242, 60.1696017)
p2 = Point(6, 6)
p3 = Point(7.5, 9)
p4 = Point(5, 5)

# Create a Polygon
# coords = [(5, 5), (10, 5), (10, 10), (5, 10)]
coords = [(5, 5), (10, 5), (10, 10), (9, 10), (9, 8), (6, 8), (6, 10), (5, 10)]
poly = Polygon(coords)

print(poly)
print(poly.centroid)
print(f"contains p1: {poly.contains(p1)}")
print(f"contains p2: {poly.contains(p2)}")
print(f"contains p3: {poly.contains(p3)}")
print(f"contains p4: {poly.contains(p4)}")
print(f"within p1: {p1.within(poly)}")
print(f"within p2: {p2.within(poly)}")
print(f"within p3: {p3.within(poly)}")
print(f"within p4: {p4.within(poly)}")
print(f"touches p1: {p1.touches(poly)}")
print(f"touches p2: {p2.touches(poly)}")
print(f"touches p3: {p3.touches(poly)}")
print(f"touches p4: {p4.touches(poly)}")
