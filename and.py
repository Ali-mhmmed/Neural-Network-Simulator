def update_weights(w1, w2, w_bias, x1, x2, a):
    S = x1 * w1 + x2 * w2 + w_bias
    if S >= 0:
        O = 1
    else:
        O = 0
    
    T = x1 and x2  # AND gate
    
    err = T - O
    
    w1_new = w1 + err * x1 * a
    w2_new = w2 + err * x2 * a
    w_bias_new = w_bias + err * a  # Update bias weight directly
    
    return w1_new, w2_new, w_bias_new


# Initialize weights
w1 = float(input("Enter initial value for w1: "))
w2 = float(input("Enter initial value for w2: "))
w_bias = float(input("Enter initial value for w_bias: "))

# Learning rate
a = float(input("Enter learning rate (a): "))

# Input values
x_values = [(0, 0), (0, 1), (1, 0), (1, 1)]

err = 1  # Initialize err to a non-zero value

while err != 0:
    err = 0  # Reset err for each iteration
    
    for x1, x2 in x_values:
        w1, w2, w_bias = update_weights(w1, w2, w_bias, x1, x2, a)
        
        S = x1 * w1 + x2 * w2 + w_bias
        O = 1 if S >= 0 else 0  # Update O based on the correct condition
        T = x1 and x2
        
        err += abs(T - O)  # Accumulate the absolute error
        
    if err == 0:
        break
    
# Print the final weights
print("w1 =", w1)
print("w2 =", w2)
print("w_bias =", w_bias)