dot1 = [float(i) for i in input().split()]
dot2 = [float(i) for i in input().split()]

print ("%.3f" % ((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2) ** 0.5)
