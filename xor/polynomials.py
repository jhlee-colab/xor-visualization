from sympy import symbols, exp, Matrix, Max, ln
from sympy.plotting import plot3d

def relu(x):
    t = symbols('t')
    return Matrix([Max(0, t).subs({'t': row}) for row in x]).T

def sigmoid(x):
    t = symbols('t')
    return Matrix([(1/(1+exp(-t))).subs({'t': row}) for row in x]).T

def tanh(x):
    t = symbols('t')
    return Matrix([((exp(t)-exp(-t))/(exp(t)+exp(-t))).subs({'t': row}) for row in x]).T

def softplus(x):
    t = symbols('t')
    return Matrix([ln(1+exp(t)).subs({'t': row}) for row in x]).T

def silu(x):
    t = symbols('t')
    return Matrix([(t/(1+exp(-t))).subs({'t': row}) for row in x]).T

def layer_output(X, weights, biases):
    return X * Matrix(weights.T) + Matrix(biases)


if __name__ == '__main__':
    import torch
    x1, x2 = symbols('x1 x2')
    X = Matrix([[x1, x2]])
    output = layer_output(X, weights=torch.rand(8, 2).numpy(), biases=torch.rand(8).numpy().reshape(1, -1))
    output = sigmoid(output)
    print(output.shape)

    output2 = layer_output(output, weights=torch.rand(4, 8).numpy(), biases=torch.rand(4).numpy().reshape(1, -1))
    output2 = sigmoid(output2)
    print(output2)
    print(output2.shape)
    final_y = layer_output(output2, weights=torch.rand(1, 4).numpy(), biases=torch.rand(1).numpy().reshape(1))
    final_y = sigmoid(final_y)
    plot3d(final_y[0])
