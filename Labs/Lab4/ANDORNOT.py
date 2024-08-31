import numpy as np

def step_function(x):
    return 1 if x >= 0 else 0

def AND_gate(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.7
    inputs = np.array([x1, x2])
    weighted_sum = np.sum(inputs * np.array([w1, w2]))
    output = step_function(weighted_sum + b)
    return output

def OR_gate(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.2
    inputs = np.array([x1, x2])
    weighted_sum = np.sum(inputs * np.array([w1, w2]))
    output = step_function(weighted_sum + b)
    return output

def NOT_gate(x):
    w, b = -0.5, 0.2
    weighted_sum = x * w
    output = step_function(weighted_sum + b)
    return output

# Test the gates
print("AND Gate")
print(AND_gate(0, 0)) # 0
print(AND_gate(0, 1)) # 0
print(AND_gate(1, 0)) # 0
print(AND_gate(1, 1)) # 1

print("OR Gate")
print(OR_gate(0, 0)) # 0
print(OR_gate(0, 1)) # 1
print(OR_gate(1, 0)) # 1
print(OR_gate(1, 1)) # 1

print("NOT Gate")
print(NOT_gate(0)) # 1
print(NOT_gate(1)) # 0