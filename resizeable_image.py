import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        w = self.width
        h = self.height
#        print("")
#        print ("width " + str(w))
#        print("height " + str(h))
        energy = {}
        paths = []
        parents = {}
        
        for j in range(h):
            for i in range(w):
                a = [100000, i, j-1]
                b = [100000, i-1, j-1]
                c = [100000, i+1, j-1]
                if (j > 0):
                    a[0] = energy[(i,j-1)]
                    if (i > 0):
                        b[0] = energy[(i-1,j-1)]
                    if (i < w-1):
                        c[0] = energy[(i+1,j-1)]
                if (j==0):
                    minEnergy = 0
                    par = None
                else:
                    minEnergy = min(a[0],b[0],c[0])
                    if (a[0] == minEnergy):
                        par = (a[1],a[2])
                    elif (b[0] == minEnergy):
                        par = (b[1],b[2])
                    else:
                        par = (c[1],c[2])
                energy[(i,j)] = minEnergy + self.energy(i,j)
                if (par is not None):
                    parents[(i,j)] = par
#                    print("adding parent for (" + str(i) + ", " + str(j) + ") " + str(parent))
                
        minVal = 100000*h
        index = -1
        for i in range(w):
            if energy[(i,h-1)] <= minVal:
                minVal = energy[(i,h-1)]
                index = i
#            print("index = " + str(index) + " minval = " + str(minVal))
        result = []
        result.append((index,h-1))
        x = index
        y = h-1
        nextParent = parents.get((x,y))
        while (nextParent is not None):
            result.append(nextParent)
            x = nextParent[0]
            y = nextParent[1]
            nextParent = parents.get((x,y))
    
#        print("result: " + str(result))
#        print("parent: " + str(parents.get((160,61))))
        return result        
        

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
