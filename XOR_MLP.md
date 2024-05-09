# XOR with Multi-Layer Perceptron

## XOR Gate
> [!Important]
> XOR is one of the digital logic gate pronounced as Exclusive OR. \
> XOR gate gives true output when the number of true inputs is odd.
<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/XOR_ANSI.svg/200px-XOR_ANSI.svg.png" alt="drawing" width="200" height="100"/>
<figcaption><br>Fig 1. XOR Gate Diagram</figcaption>
</figure>
<br>

### Truth Table for XOR gate
<table>
<thead>
<tr>
  <th colspan=2 align="center">Input</th> <th align="center">Output</th>
</tr>
<tr>
  <th align="center">A</th> <th align="center">B</th> <th align="center">A XOR B</th>
</tr>
</thead>
<tr>
  <td align="center">0</td> <td align="center">0</td> <td align="center">0</td></tr>
<tr>
  <td align="center">0</td> <td align="center">1</td> <td align="center">1</td>
</tr>
<tr>
  <td align="center">1</td> <td align="center">0</td> <td align="center">1</td>
</tr>
<tr>
 <td align="center">1</td> <td align="center">1</td> <td align="center">0</td>
</tr>
</table>
<br>

## XOR Problem with Perceptron
### AND, OR vs XOR
- AND, OR Gate: Linear
- XOR Gate: Non-linear 
<br>

2-Dimensional Space
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/456c0a12-eabf-4544-acc6-eb138d711a69" alt="drawing"/>
<figcaption><br>Fig 2. AND, OR and XOR Gate<br></figcaption>
</figure> 

<br>

> [!Important]
> XOR Gate is a non-linear problem. \
> To sovle XOR problem, it's key point that MLP and activation function make solve it.
<br>

## Nonlinear Activation Function
### Perceptron
- Output: $w_1x_1 + w_2x_2 + b$
- Here, the output equation is represented as a plane like Fig 3 and Fig 4 in 3-dimensional space.
<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/21cee7a2-c8db-4717-83be-263f99e24b22" alt="drawing" width="500" height="200"/>
<figcaption><br>Fig 3. Perceptron</figcaption>
</figure>
<br>

### Activation Function
- Sigmoid: Nonlinear
- ReLU: Nonlinear
- Tanh: Nonlinear
- Linear: linear
<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/c0640ede-e7c5-49a3-bad1-4e585b71c8fc" alt="drawing" width="500" height="350"/>
<figcaption><br>Fig 4. Activation Functions<br></figcaption>
</figure>


<br>

> [!Important]
> If you apply an activation function into perceptron,  \
> the output equation has nonlinearity.

<br>

### Perceptron with Activation Function
- Ouput \
  $\Huge{\frac{1}{1+e^{-(w_1x_1+w_2x_2 + b)}}}$
- Therefore, the output equation has nonlinearity through exponential function like Fig 6.

<br>
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/81f0594c-9ddc-4b52-852a-8c9cb7a17c67" alt="drawing" width="500" height="200"/>
<figcaption><br>Fig 5. Perceptron with Sigmoid<br></figcaption>
</figure>

<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/465aaea2-665b-4f00-b28d-3feea99297bb" alt="drawing" width="400" height="400"/>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/ffb65304-c7cf-4edf-9988-47db6a6aebf4" alt="drawing" width="400" height="400"/>
<figcaption><br>Fig 6. the output surface of AND Gate model with Sigmoid and the output plane of AND Gate model with linear<br></figcaption>
</figure>

<br>

## XOR with MLP
### MLP
> [!Important]
> A multilayer perceptron (MLP) is consisting of  hidden layers between input layer and output layer at perceptron. \
> And activation function is also applied for nonlinearity.
<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/b22e9cda-ac3c-42c2-b495-14cff3e2563b" alt="drawing" width="500" height="250"/>
<figcaption><br>Fig 7. Simple MLP<br></figcaption>
</figure>

<br>

- Input Layer: 2 features, $(x_1, x_2)$
- Hidden Layer: 1 hidden layer, its size is 2. 
- Output Layer: $\hat y$, range 0 ~ 1

<br>

### Hidden Layer
- $h_1$ is a perceptron. Therefore, its equation is below:
  - $\Huge{h_1=\frac{1}{1+e^{-(w_1x_1+w_2x_2+b_1)}}}$
<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/9448572d-289c-4d76-b126-c28a2a338f5b" alt="drawing" width="300" height="200"/>
<figcaption><br>Fig 8. Hidden Layer, h1<br></figcaption>
</figure>

<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/e5c74589-ecf1-42ae-83bb-b9fd1945efb6" alt="drawing" width="400" height="400"/>
<figcaption><br>Fig 9. the surface of h1<br></figcaption>
</figure>

<br>

- $h_2$ is also a perceptron. Therefore, its equation is below:
  - $\Huge{h_2=\frac{1}{1+e^{-(w_3x_1+w_4x_2+b_2)}}}$

<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/cfd6e7ca-6a0a-47d7-ba21-5d902a093d77" alt="drawing" width="300" height="200"/>
<figcaption><br>Fig 10. Hidden Layer, h2<br></figcaption>
</figure>

<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/10e9741e-1db8-405c-9aff-5307a69b783f" alt="drawing" width="400" height="400"/>
<figcaption><br>Fig 11. the surface of h2<br></figcaption>
</figure>

<br>

### Output Layer
- The final output is also a perceptron with input, $h_1$ and $h_2$.
  - $\Huge{H=\frac{1}{1+e^{-(w_5h_1+w_6h_2+b_3)}}}$
  - $\Huge{H=\frac{1}{1+e^{-(w_5\frac{1}{1+e^{-(w_1x_1+w_2x_2+b_1)}}+w_6\frac{1}{1+e^{-(w_3x_1+w_4x_2+b_2)}}+b_3)}}}$   

<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/d1b5eb1b-0235-4768-b703-8b68998cad91" alt="drawing" width="280" height="200"/>
<figcaption><br>Fig 12. The final output layer, H<br></figcaption>
</figure>

<br>

> [!Important]
> Finally, MLP XOR model makes the output plane curved surface through activation function and multilayer rather than the plane of linear model. \
> Fig 13. shows curved surface of the output of MLP model.

<br>

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/f2d13200-f569-4451-8e45-7c4c3470c9ae" alt="drawing"/>
<figcaption><br>Fig 13. The output surface of MLP XOR model<br></figcaption>
</figure>


