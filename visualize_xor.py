import torch
import argparse
import sys
from xor.models import XOR
from xor.polynomials import sigmoid, tanh, softplus, silu
from xor.plots import surface_plot, surface_plot_sym
from xor.constants import *

def parse_args():
	desc = 'Plot the output of XOR trained by DNN'
	parser = argparse.ArgumentParser(description=desc)
	parser.add_argument('--hidden_layers', type=str, default='[2]', help='the hidden layers, default [2]')
	parser.add_argument('--activation', type=str, default='sigmoid', help='the type of a activation function, default sigmoid')
	parser.add_argument('--optimizer', type=str, default='adam', help='optimizer, default Adam')
	parser.add_argument('--loss', type=str, default='mse', help='loss function, default mse')
	parser.add_argument('--learning_rate', type=float, default=0.001, help='learning rate')
	parser.add_argument('--epochs', type=int, default=10000, help='a number of epoch')
	parser.add_argument('--save_filename', type=str, default='xor_output.png', help='image filename')
	return check_args(parser.parse_args())

def check_args(args):
    # check hidden layers
    try:
        args.hidden_layers = eval(args.hidden_layers)
        assert type(args.hidden_layers) == list
    except:
        print(f'warning, hidden_layers should be a list. ex) [4, 2]')
        print(f'hidden_layers is set to default value, {args.hidden_layers}.')

    # check activation
    try:
        args.activation = args.activation.lower()
        assert args.activation in ('sigmoid', 'tanh', 'silu', 'softplus', 'relu')
    except:
        print(f'warning, activation should be a text. ex) tanh')
        print(f'activation is set to default value, {args.activation}.')
    args.activation = activation_fuctions[args.activation]

    # check optimizer
    try:
        args.optimizer = args.optimizer.lower()
        assert args.optimizer in ('adam', 'sgd', 'rmsprop', 'adadelta', 'adamax', 'adagrad', 'nadam')
    except:
        print(f'warning, optimizer should be a test. ex) sgd')
        print(f'optimizer is set to default value, {args.optimizer}.')
    args.optimizer = optimizers[args.optimizer]

    # check loss
    try:
        args.loss = args.loss.lower()
        assert args.loss in ('mse', 'bce')
    except:
        print(f'warning, loss should be a test. ex) bce')
        print(f'loss is set to default value, {args.loss}.')
    args.loss =loss_fuctions[args.loss]

    # check learning rate
    try:
        assert type(args.learning_rate) == float or type(args.learning_rate) == int
    except:
        print(f'warning, loss should be a integer or float. ex) 0.01')
        print(f'learning_rate is set to default value, {args.learning_rate}.')

    # check epochs
    try:
        assert args.epochs >= 1
    except:
        print(f'warning, epochs should be a integer(>=1)t. ex) 10')
        print(f'epochs is set to default value, {args.epochs}.')
    return args

def main(args):
    print('-'*20)
    print(f'arguments: {args}')
    print()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # X, y
    X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float).to(device)
    y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float).to(device)

    # training until accuracy is 100%
    while True:
        # build model
        xor_model = XOR(hidden_layers=args.hidden_layers, activation_fn=args.activation, optimizer_fn=args.optimizer, loss=args.loss, learning_rate=args.learning_rate, epochs=args.epochs, device=device)
        xor_model.fit(X, y, print_every=1000)

        if all(xor_model.predict(X) == y):
            break

    # activation function
    if args.activation == 'Sigmoid':
        act_fn = sigmoid
    elif args.activation == 'Tanh':
        act_fn = tanh
    elif args.activation == 'Softplus':
        act_fn = softplus
    elif args.activation == 'SiLU':
        act_fn = silu

    # plot surface
#    surface_plot_sym(xor_model, act_fn, fname=args.save_filename)
    surface_plot(xor_model, fname=args.save_filename)



if __name__ == '__main__':
    args = parse_args()

    main(args)
