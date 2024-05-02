from matplotlib import pyplot as plt
from sympy.plotting import plot3d
from sympy import symbols, Matrix
from .polynomials import layer_output, sigmoid, tanh, softplus, silu
import torch
import numpy as np

def surface_plot(xor_model, fname=None, title='The output surface of XOR model', cmap='RdBu', alpha=0.9):
	x1, x2 = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
	grid = torch.tensor(np.c_[x1.ravel(), x2.ravel()], dtype=torch.float32)

	# z 
	with torch.no_grad():
		z = xor_model(grid).view(x1.shape)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_surface(x1, x2, z, cmap=cmap, alpha=alpha)
	ax.set_title(title)
	ax.set_xlabel('x1')
	ax.set_ylabel('x2')
	ax.set_zlabel('output')
	if fname is not None:
		plt.savefig(fname)
	plt.show()

def surface_plot_sym(xor_model, act_fn, fname=None, title='The output surface of XOR model', cmap='RdBu', alpha=0.9):
	# get linear layers
	layers = [x for x in [module for module in xor_model.modules() if not isinstance(module, torch.nn.Sequential)] if isinstance(x, torch.nn.Linear)]

	# input symbols
	x1, x2 = symbols('x1, x2')
	X_sym = Matrix([[x1, x2]])

	output_eq = X_sym
    	# hidden layer
	for layer in layers[:-1]:
		weights = layer.weight.detach().numpy()
		bias = layer.bias.detach().numpy().reshape(1, -1)
		output_eq = layer_output(output_eq, weights, bias)
		output_eq = act_fn(output_eq)

	# output layer
	output_eq = layer_output(output_eq, layers[-1].weight.detach().numpy(), layers[-1].bias.detach().numpy())
	output_eq = sigmoid(output_eq)[0]
	print('-' * 20)
	print(f'output equation: {output_eq}')
	print()

	img = plot3d(output_eq, (x1, -3, 3), (x2, -3, 3), cmap=cmap, alpha=alpha,  show=False)
	if fname is not None:
		img.save(fname)
	img.show()
