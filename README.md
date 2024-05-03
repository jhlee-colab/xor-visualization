### Requirements
- torch
- matplotlib
- sympy
- numpy

### Arguments
- hidden_layers: the hidden layers, default [2]
- activation: the type of a activation function, default sigmoid
  - Sigmoid
  - ReLU
  - Tanh
  - Softplus
  - SiLU
- optimizer: optimizer function, default Adam
  - SGD
  - Adam
  - Nadam
  - RMSProp
  - AdaDelta
  - AdaMax
  - AdaGrad
- loss: loss function, default mse
  - MSE
  - BCE
- learning_rate: learning rate, default 0.001
- epochs: epochs, default 10,000
- save_filename: image filename, default xor_output.png

### Usage
```shell
python visualize_xor.py \
--hidden_layer "[4, 3, 2]" \
--activation relu \
--optimizer nadam \
--loss bce \
--learning_rate 0.01 \
--epochs 2000
--save_filename 'xor_output.png'
```
![xor_output](https://github.com/jhlee-colab/xor-visualization/assets/158408101/cdc94cf2-bc8b-46a1-a896-4eefca08e6f3)

