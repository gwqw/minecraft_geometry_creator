import objects_creator as oc

def test_cuboid():
    cub = oc.Cuboid(0,0,0, 10, 10, 10, "")
    res = cub.create_matrix()
    print(res)

def triangle_prizm():
    tp = oc.TrianglePrismX(0,0,0, 5, 1, "")
    res = tp.create_matrix()
    print(res)

def cylinder():
    cyl = oc.CylinderZ(0,0,0,10,20,"")
    res = cyl.create_matrix()
    print(res)

if __name__ == "__main__":
    cylinder()

