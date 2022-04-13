import copy
import random

### We are to - indirectly - deal with a Kolmogorovian discrete probability density. Solution inspired by Landon Schlangen. 

### We define a 
class Hat:
    ## We don't know how many arguments are going to be passed to this method. So we don't know how much memory is to be alocated for the execution of said method. How can we circunvent this problem? In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols: *args (Non-Keyword Arguments) and **kwargs (Keyword Arguments)
    ## In particular, we are to use **kwargs which is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

    def __init__(self, **kwargs):
        self.contents = [alpha for alpha, beta in kwargs.items() for _ in range(beta)] ## With this we create a way to create a variable-length list. 
    
    ##With this method we indicate the number of experiments to be perfomed. 
    def draw(self, n):
        n = min(n, len(self.contents)) ## we draw a certain amount of balls. Implementing it this way we are saying we are to draw either n balls, if n<length.list, or viceversa.
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]

### We define a function, experiment, which will give us the results of performing a certain amount of experiments. As num_experiments are performed, these results will converge, in functional distribution sense, to the exact, theoretical probabilities. 

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat) ## with this we alocate memory to have a copy of the original variable. This is an intermediate variable if you will. 
        balls_drawn = another_hat.draw(num_balls_drawn) ## this is the number of drawn balls. 
        totalBalls = sum([1 for alpha, beta in expected_balls.items() if balls_drawn.count(alpha) >= beta])
        m += 1 if totalBalls == len(expected_balls) else 0
    p_m = m/num_experiments
    return p_m
 ### Note that the sum of all probabilites, \sum_{m} p_m, is normalized to 1.