import math

class Operations:
    """
        Calculates the average 
        @:return will return float representation of average
    """
    def average(self, data):
        list = data
        n = len(data)
        sum = 0
        for x in list:
            sum += x
        return round(float((1/n) * sum), 1)
    """
        Calculates the variance 
        @:return will return float representation of variance
    """
    def variance(self, data):
        list = data
        n = len(data)
        average = self.average(list)
        sum = 0
        for x in list:
            sum += float((x - average)*(x - average))
        return round(float(1/(n-1) * sum), 4)

    """
        Calculates the standard deviation 
        @:return will return the s.d
    """
    def standard_deviation(self, data):
        return round(math.sqrt(self.variance(data)), 2)

    """
        Calculates the standard deviation with paired data
        @:return will return the s.d
    """
    def standard_deviation_pair(self, data):
        list = data
        n = len(list)
        regression = self.regression(list)
        b1 = regression[0]
        b0 = regression[1]
        sum = 0
        for i in range(n):
            xi = float(list[i][0])
            yi = float(list[i][1])
            yreg = b0+(b1*xi)
            sum += (yi-yreg)*(yi-yreg)
        return round(math.sqrt((1/(n-1))*sum), 2)

    """
        Calculates the interval
        @:param t distribution value
        @:param std standard_deviation 
        @:return will return the interval value
    """
    def interval(self, t, std, data):
        list = data
        n = len(list)
        xk = 900
        xavg = self.average(self.get_column(list, 0))
        sum = 0
        for i in range(n):
            xi = list[i][0]
            sum += (xi-xavg)*(xi-xavg)
        interval = t*std*math.sqrt(1+(1/n)+((xk-xavg)*(xk-xavg))/(sum*sum))
        return round(interval,2)

    """
        Calculates the inferior and superior limits 
        @:param data paired list value
        @:param interval the interval 
        @:return will return an array containing the lowest and highest point
    """
    def limits(self, data, interval):
        list = data
        reg = self.regression(list)
        b1 = reg[0]
        b0 = reg[1]
        xk = 900
        yk = b0 + (b1 * xk)
        return [round(xk - interval,2), round(xk + interval, 2)]

    """
        Calculates the correlation
        @:param data list paired with values x, y respectively. 
        @:return will return the s.d
    """
    def correlation(self, data):
        temp = data
        for d in temp:
            x = d[0]
            y = d[1]
            xx = round(x*x, 2)
            xy = round(x*y, 2)
            yy = round(y*y, 2)
            d.extend([xx, xy, yy])

        n = len(temp)
        sum_x = self.sum_column(temp, 0)
        sum_y = self.sum_column(temp, 1)
        sum_xx = self.sum_column(temp, 2)
        sum_xy = self.sum_column(temp, 3)
        sum_yy = self.sum_column(temp, 4)

        numerator = n*sum_xy - sum_x*sum_y
        denominator = math.sqrt((n*sum_xx - sum_x*sum_x)*(n*sum_yy-sum_y*sum_y))

        r = numerator/denominator

        return [r, r*r]
    """
        Calculate the regression values b0 and b1
        @:param data paired list value
        @:return returns an array containing b1 and b0 respectively
    """
    def regression(self, data):
        temp = data
        for d in temp:
            x = d[0]
            y = d[1]
            xx = round(x*x, 2)
            xy = round(x*y, 2)
            d.extend([xx, xy])
        n = len(temp)
        avg_x = self.average(self.get_column(temp, 0))
        avg_y = self.average(self.get_column(temp, 1))
        sum_xx = self.sum_column(temp, 2)
        sum_xy = self.sum_column(temp, 3)

        b1 = (sum_xy-n*avg_x*avg_y) / (sum_xx-n*avg_x*avg_x)
        b0 = avg_y-b1*avg_x

        return [b1, b0]

    """
        Returns the sum of a specified column
        @:param data list paired with values x, y respectively. 
        @:param c the column to sum up.
        @:return will return the sum of the column
    """
    def sum_column(self, data, c):
        sum = 0
        for r in range(len(data)):
            sum += data[r][c]
        return sum

    """
        Returns a table with data from a specified column from 2d data list
        @:param data list paired with values x, y respectively. 
        @:param c the column to return.
        @:return will return a table with the specified column
    """
    def get_column(self, data, c):
        temp = []
        for r in range(len(data)):
            temp.append(data[r][c])
        return temp

    """
        Returns a table that contains data between two specified columns
        @:param data list paired with values x, y respectively. 
        @:param c1 range 1
        @:param c2 range 2
        @:return will return a table with data from c1 to c2
    """
    def get_range_column(self, data, c1, c2):
        temp = []
        for c in range(len(data)):
            if c >= c1 and c <= c2:
                temp.append(data[c])
        return temp
