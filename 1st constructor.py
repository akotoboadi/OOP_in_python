class  Stats:
    def __init__(self,numbers):
        self.numbers = numbers
    def mean(self):
        sum=0
        for number in self.numbers:
            sum = number + sum
        return(sum/len(self.numbers))
    def median(self):
        if len(self.numbers) % 2 != 0:
            return(self.numbers[int(len(self.numbers)/2)])
        else:
            half_length = (int(len(self.numbers)/2))
            nth_term = self.numbers[half_length-1]
            next_term = self.numbers[half_length]
            avg_terms = (nth_term +next_term) / 2
            return (avg_terms)
    def mode(self):
        return(max(set(self.numbers), key=self.numbers.count))

stat = Stats([1,1,1,1,2,4,7,8])
print(f"The mean is {stat.mean()}")
print(f" The mode is {stat.mode()}")
print(f"The median is {stat.median()}")
#The median works only when the numbers are entered in either ascending or descending order.