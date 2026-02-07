import math

def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate the probability of exactly k successes in n Bernoulli trials.
    
    Args:
        n: Total number of trials
        k: Number of successes
        p: Probability of success on each trial
    
    Returns:
        Probability of k successes
    """
    # Your code here
    if n < 0 or k < 0 or k > n or not (0 <= p <= 1):
        return -1
    
    val1=math.comb(n,k)
    val2=p**k
    val3=(1-p)**(n-k)

    return val1*val2*val3