import monkdata as mdata 
import drawtree_qt5 as draw
import dtree as dtree 
import random
import numpy as np

# t1 = dtree.buildTree(mdata.monk1,mdata.attributes)
# pruned_t1 = dtree.allPruned(t1)
# draw.drawTree(pruned_t1)


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def pruneRec(tree,monkval):
    treeList = dtree.allPruned(tree)
    best = tree
    for i in range(len(treeList)):
        for j in range(i+1, len(treeList)):
            k = dtree.check(treeList[i],monkval)
            l = dtree.check(treeList[j],monkval)
            if l > k:
                best = treeList[j]
            else:
                best = treeList[i]
    if best == tree:
        return best
    return pruneRec(best,monkval)
    


def buildTrees():
    fraction = [0.3,0.4,0.5,0.6,0.7,0.8]
    f_len = len(fraction)
    # monk1train = [None] * f_len
    # monk1val = [None] * f_len
    # monk3train = [None] * f_len
    # monk3val = [None] * f_len
    # tree1 = [None] * f_len
    # tree3 = [None] * f_len
    pruned_t = [None] * f_len


    errorList = [[None]*100 for _ in range(6)]
    # Build and prune the trees 
    for x in range(0,len(fraction)):
        p = [0] * 100

        # print("Factor: %.1f" % fraction[x])
        for y in range(0,100):
            monk1train, monk1val = partition(mdata.monk1,fraction[x])
            tree1 = dtree.buildTree(monk1train,mdata.attributes)
            bestPrune = pruneRec(tree1,monk1val)
            errorList[x][y] = dtree.check(bestPrune,monk1val)
    return errorList

def getData1(iterations):
    fraction = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    error = [0] * 6
    for i in range (6):
        error[i] = [0] * iterations
    #print("\nMonk1")
    for f in range(len(fraction)):
        #print("\nFactor: %.1f" % f)
        for i in range(0,iterations):
            monk1train, monk1val = partition(mdata.monk1, fraction[f])
            monk1tree = dtree.buildTree(monk1train, mdata.attributes)
            while True:
                prunelist = dtree.allPruned(monk1tree)
                temptree = monk1tree
                for x in prunelist:
                    if dtree.check(x, monk1val) >= dtree.check(temptree, monk1val):
                        temptree = x

                if temptree == monk1tree:
                    break
                monk1tree = temptree

            error[f][i] = dtree.check(monk1tree, mdata.monk1test)
    return error

def getOliverData():
    return getData1(1000)

def getErrorData():
    return buildTrees()
# buildTrees()
# for x in range(0,len(fraction)):
#     tree3[x] = dtree.buildTree(monk3train[x],mdata.attributes)
#     monk3train[x], monk3val[x] = partition(mdata.monk3,fraction[x])