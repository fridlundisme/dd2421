import monkdata as mdata
import dtree as dtree
import drawtree_qt5 as draw

print("Entropy of monkdata2 " + str(dtree.entropy(mdata.monk2)))
print("Entropy of monkdata3 " + str(dtree.entropy(mdata.monk3)))

for x in mdata.attributes:
    ag1 = dtree.averageGain(mdata.monk1,x)
    ag2 = dtree.averageGain(mdata.monk2,x)
    ag3 = dtree.averageGain(mdata.monk3,x)
    print('Average gain in dataset monk1 and attribute ' + str(x.name) + ' is %.6f' % ag1)
    print("Average gain in dataset monk2 and attribute " + str(x.name) + " is %.6f" % ag2)
    print("Average gain in dataset monk3 and attribute " + str(x.name) + " is %.6f" % ag3)

print("\n")


for x in range(1,5):
    highest_avg = 0
    highest_attribute = 0
    s = dtree.select(mdata.monk1,mdata.attributes[4],x)
    for y in mdata.attributes:
        avg_g = dtree.averageGain(s,y)
        print("Average gain in dataset monk1 and subset s" + str(x) + " and attribute " + str(y.name) + " is %.6f. Majority: " % avg_g + str(dtree.mostCommon(s)) )
        if(avg_g > highest_avg):
            highest_avg = avg_g
            highest_attribute = int(y.name[1])

    print("Highest avg: %.6f in attr: " % highest_avg + str(highest_attribute))
    for z in range(1, len(mdata.attributes[int(highest_attribute -1)].values) + 1):
        s2 = dtree.select(s, mdata.attributes[int(highest_attribute - 1)], z)
        print(dtree.mostCommon(s2))

    print("\n")

t1 = dtree.buildTree(mdata.monk1,mdata.attributes)
print("Test data check: %.6f\n" % dtree.check(t1,mdata.monk1test))
print("Training data check: %.6f\n" % dtree.check(t1,mdata.monk1))

t2 = dtree.buildTree(mdata.monk2,mdata.attributes)
print("Test data check: %.6f\n" % dtree.check(t2,mdata.monk2test))
print("Training data check: %.6f\n" % dtree.check(t2,mdata.monk2))

t3 = dtree.buildTree(mdata.monk3,mdata.attributes)
print("Test data check: %.6f\n" % dtree.check(t3,mdata.monk3test))
print("Training data check: %.6f\n" % dtree.check(t3,mdata.monk3))
