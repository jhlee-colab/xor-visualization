# XOR with Multi-Layer Perceptron

## XOR Gate
> [!Important]
> XOR is one of the digital logic gate pronounced as Exclusive OR. \
> XOR gate gives true output when the number of true inputs is odd.
<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/XOR_ANSI.svg/200px-XOR_ANSI.svg.png" alt="drawing" width="200" height="100"/>
<figcaption>Fig 1. XOR Gate Diagram</figcaption>
</figure>

### Truth Table
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


## XOR Problem with Perceptron
### AND, OR vs XOR
- AND, OR Gate: Linear
- XOR Gate: Non-linear 

2-Dimentional Space
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/456c0a12-eabf-4544-acc6-eb138d711a69" alt="drawing"/>
<figcaption>Fig 2. AND, OR and XOR Gate</figcaption>
</figure>

3-Dimentional Space
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/ffb65304-c7cf-4edf-9988-47db6a6aebf4" alt="drawing"/>
<figcaption>Fig 3. AND Gate</figcaption>
</figure>
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/31474f99-c97e-43c5-99e3-4247d324a2a2" alt="drawing"/>
<figcaption>Fig 4. OR Gate</figcaption>
</figure>
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/f2d13200-f569-4451-8e45-7c4c3470c9ae" alt="drawing"/>
<figcaption>Fig 5. XOR Gate</figcaption>
</figure>

> [!Important]
> XOR Gate is a non-linear problem. \
> To sovle XOR problem, it's key point that MLP and activation function make solve it.

## Nonlinear Activation Function
### Perceptron
- Output: $w_1x_1 + w_2x_2 + b$
- Here, the output equation is represented as a plane like Fig 3 and Fig 4 in 3-dimensional space.
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/21cee7a2-c8db-4717-83be-263f99e24b22" alt="drawing" width="500" height="200"/>
<figcaption>Fig 6. Perceptron</figcaption>
</figure>

### Activation Function
- Sigmoid: Nonlinear
- ReLU: Nonlinear
- Tanh: Nonlinear
- Linear: linear

<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/c0640ede-e7c5-49a3-bad1-4e585b71c8fc" alt="drawing"/>
<figcaption>Fig 7. Activation Functions</figcaption>
</figure>

> [!Important]
> When you apply an activation function into perceptron,  \
> the output equation has nonlinearity.

### Perceptron with Activation Function
- Ouput \
  $\Huge{\frac{1}{1+e^{-(w_1x_1+w_2x_2 + b)}}}$
- Therefore, the output equation has nonlinearity through exponential function like Fig 9.


<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/81f0594c-9ddc-4b52-852a-8c9cb7a17c67" alt="drawing" width="500" height="200"/>
<figcaption>Fig 8. Perceptron with Sigmoid</figcaption>
</figure>


<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/465aaea2-665b-4f00-b28d-3feea99297bb" alt="drawing"/>
<figcaption>Fig 9. AND Gate with Sigmoid </figcaption>
</figure>

## XOR with MLP
### MLP
### MLP with Activation Function



