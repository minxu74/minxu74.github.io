$$
\operatorname{ker} f=\{g\in G:f(g)=e_{H}\}{\mbox{.}}
$$

The well known Pythagorean theorem $x^2 + y^2 = z^2$ was
proved to be invalid for other exponents.
Meaning the next equation has no integer solutions:

$$
x^n + y^n = z^n 
$$


$$
\frac{\partial s}{\partial W}
= \frac{\partial \sum_{i=1}^{n} (y_i -(W\cdot x_i+b))^2}
                    {\partial W} \\
= \sum_{i=1}^{n} 2(y_i -W\cdot x_i-b)\cdot(-x_i))
 = 2\cdot \sum_{i=1}^{n} (-y_i\cdot x_i + W\cdot x_i^2 + b\cdot x_i )  
   \stackrel{!}{=} 0    \nonumber\\ \nonumber\\
\Longleftrightarrow W\cdot(\sum_{i=1}^{n} x_i^2) + b\cdot(\sum_{i=1}^{n}x_i) 
 = \sum_{i=1}^{n}x_i\cdot y_i \\
\frac{\partial s}{\partial b}
= \frac{\partial \sum_{i=1}^{n} (y_i -(W\cdot x_i+b))^2}
                    {\partial b} \nonumber \\
= \sum_{i=1}^{n} 2(y_i -W\cdot x_i-b)\cdot(-1))
 = 2\cdot \sum_{i=1}^{n} (-y_i\cdot+ W\cdot x_i+ b)  
   \stackrel{!}{=} 0    \nonumber \\ \nonumber \\
\Longleftrightarrow W\cdot(\sum_{i=1}^{n} x_i) +\sum_{i=1}^{n}b 
 = \sum_{i=1}^{n} y_i \nonumber \\
\Longleftrightarrow W\cdot(\sum_{i=1}^{n}x_i) + n\cdot b 
 = \sum_{i=1}^{n} y_i
$$


\begin{align}
\frac{\partial s}{\partial W}
&= \frac{\partial \sum_{i=1}^{n} (y_i -(W\cdot x_i+b))^2}
                    {\partial W} \nonumber \\
&= \sum_{i=1}^{n} 2(y_i -W\cdot x_i-b)\cdot(-x_i))
 = 2\cdot \sum_{i=1}^{n} (-y_i\cdot x_i + W\cdot x_i^2 + b\cdot x_i )  
   \stackrel{!}{=} 0    \nonumber\\ \nonumber\\
&\Longleftrightarrow W\cdot(\sum_{i=1}^{n} x_i^2) + b\cdot(\sum_{i=1}^{n}x_i) 
 = \sum_{i=1}^{n}x_i\cdot y_i  \\
\frac{\partial s}{\partial b}
&= \frac{\partial \sum_{i=1}^{n} (y_i -(W\cdot x_i+b))^2}
                    {\partial b} \nonumber \\
&= \sum_{i=1}^{n} 2(y_i -W\cdot x_i-b)\cdot(-1))
 = 2\cdot \sum_{i=1}^{n} (-y_i\cdot+ W\cdot x_i+ b)  
   \stackrel{!}{=} 0    \nonumber \\ \nonumber \\
&\Longleftrightarrow W\cdot(\sum_{i=1}^{n} x_i) +\sum_{i=1}^{n}b 
 = \sum_{i=1}^{n} y_i \nonumber \\
&\Longleftrightarrow W\cdot(\sum_{i=1}^{n}x_i) + n\cdot b 
 = \sum_{i=1}^{n} y_i 
\end{align}

