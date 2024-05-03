# XOR with Multi-Layer Perceptron

## XOR Gate
> [!Important]
> XOR is one of the digital logic gate pronounced as Exclusive OR. \
> XOR gate gives true output when the number of true inputs is odd.
<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/XOR_ANSI.svg/200px-XOR_ANSI.svg.png" alt="drawing" width="200" height="100"/>
<figcaption>XOR Gate Diagram</figcaption>
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
<figcaption>AND, OR and XOR Gate</figcaption>
</figure>

3-Dimentional Space
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/ffb65304-c7cf-4edf-9988-47db6a6aebf4" alt="drawing"/>
<figcaption>AND Gate</figcaption>
</figure>
<figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/31474f99-c97e-43c5-99e3-4247d324a2a2" alt="drawing"/>
<figcaption>OR Gate</figcaption>
</figure>
<img src="https://github.com/jhlee-colab/xor-visualization/assets/158408101/f2d13200-f569-4451-8e45-7c4c3470c9ae" alt="drawing"/>
<figcaption>XOR Gate</figcaption>
</figure>

> [!Important]
> XOR Gate is a non-linear problem. \
> To sovle XOR problem, it's key point that MLP and activation function make solve it.




