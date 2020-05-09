class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if 2<= len(coordinates)<= 1000:
            for i in range(0,len(coordinates)):
                if len(coordinates[i]) == 2 and -10**4 <= coordinates[i][0] and coordinates[i][1] <=10**4:
                    if i==0:
                        x1=coordinates[i][0]
                        y1=coordinates[i][1]
                        continue
                    if i==1:
                        x2=coordinates[i][0]
                        y2=coordinates[i][1]
                        if x2-x1 == 0:
                            point_on_line = False
                            break
                        else:
                            slope =(y2-y1)/(x2-x1)
                            prev_intercept = y2 -(slope*x2)
                    if i!=0 and i!=1:
                        x = coordinates[i][0]
                        y=  coordinates[i][1]
                        intercept = y - (slope*x)
                        if prev_intercept != intercept:
                            point_on_line = False
                            break
                        else:
                            point_on_line = True
                            continue
        return(point_on_line)