def euclidean_algorithm(a, b):
    if b == 0:
        return a
    else:
        return euclidean_algorithm(b, a % b)
    
print(euclidean_algorithm(30, 18)) #6