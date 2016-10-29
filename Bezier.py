import GridTools

class GridBezierCurve :

    def __init__(self, start,end, control1) :
        self.start = start
        self.end = end
        self.control1 = control1

    def write_to_dictionary(self, output, smoothness,width) :
        for t in [ (1/smoothness)*x for x in range(0,smoothness)] :
            pt = tuple( [int((1-t**2)*self.start[i] + 2*(1-t)*t*self.control1[i] + t**2 * self.end[i]) for i in [0,1]])
            for q in GridTools.manhattan_disc(pt,width) :
                output[q] = 0

