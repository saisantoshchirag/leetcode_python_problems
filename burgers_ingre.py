def numOfBurgers(tomatoSlices, cheeseSlices):

        if tomatoSlices%2!=0 or tomatoSlices < cheeseSlices:
            return []
        jum = (tomatoSlices - 2*cheeseSlices)/2
        small = cheeseSlices - jum
        out = []
        if int(jum)==jum and int(small)==small:
            out.append(int(jum))
            out.append(int(small))
        else:
            return []
print(numOfBurgers(4,7))
