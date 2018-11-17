
**Key points:**

- Our goal is to maximasing the probability and minimising the cross-entropy. Cross-entropy is inversely proportional to the total probability of an outcome.
- Multi-class cross-entropy formula
- Error Function formula

<img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" title="\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" />

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)

<img src="http://yuml.me/diagram/scruffy/class/[note: You can stick notes on diagrams too!{bg:cornsilk}],[Customer]<>1-orders 0..*>[Order], [Order]++*-*>[LineItem], [Order]-1>[DeliveryMethod], [Order]*-*>[Product], [Category]<->[Product], [DeliveryMethod]^[National], [DeliveryMethod]^[International]" >

<img src="http://latex.codecogs.com/gif.latex?%5Csum%20%28a&plus;b%29%21" >

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/May/5910e6c6_codecogseqn-49/codecogseqn-49.gif">

Gradient Calculation
In the last few videos, we learned that in order to minimize the error function, we need to take some derivatives. So let's get our hands dirty and actually compute the derivative of the error function. The first thing to notice is that the sigmoid function has a really nice derivative. Namely,

\sigma'(x) = \sigma(x) (1-\sigma(x))σ 
′
 (x)=σ(x)(1−σ(x))

The reason for this is the following, we can calculate it using the quotient formula:


And now, let's recall that if we have mm points labelled x^{(1)}, x^{(2)}, \ldots, x^{(m)},x 
(1)
 ,x 
(2)
 ,…,x 
(m)
 , the error formula is:

E = -\frac{1}{m} \sum_{i=1}^m \left( y_i \ln(\hat{y_i}) + (1-y_i) \ln (1-\hat{y_i}) \right)E=− 
m
1
​	 ∑ 
i=1
m
​	 (y 
i
​	 ln( 
y 
i
​	 
^
​	 )+(1−y 
i
​	 )ln(1− 
y 
i
​	 
^
​	 ))

where the prediction is given by \hat{y_i} = \sigma(Wx^{(i)} + b). 
y 
i
​	 
^
​	 =σ(Wx 
(i)
 +b).

Our goal is to calculate the gradient of E,E, at a point x = (x_1, \ldots, x_n),x=(x 
1
​	 ,…,x 
n
​	 ), given by the partial derivatives

\nabla E =\left(\frac{\partial}{\partial w_1}E, \cdots, \frac{\partial}{\partial w_n}E, \frac{\partial}{\partial b}E \right)∇E=( 
∂w 
1
​	 
∂
​	 E,⋯, 
∂w 
n
​	 
∂
​	 E, 
∂b
∂
​	 E)

To simplify our calculations, we'll actually think of the error that each point produces, and calculate the derivative of this error. The total error, then, is the average of the errors at all the points. The error produced by each point is, simply,

E = - y \ln(\hat{y}) - (1-y) \ln (1-\hat{y})E=−yln( 
y
^
​	 )−(1−y)ln(1− 
y
^
​	 )

In order to calculate the derivative of this error with respect to the weights, we'll first calculate \frac{\partial}{\partial w_j} \hat{y}. 
∂w 
j
​	 
∂
​	  
y
^
​	 . Recall that \hat{y} = \sigma(Wx+b), 
y
^
​	 =σ(Wx+b), so:


The last equality is because the only term in the sum which is not a constant with respect to w_jw 
j
​	  is precisely w_j x_j,w 
j
​	 x 
j
​	 , which clearly has derivative x_j.x 
j
​	 .

Now, we can go ahead and calculate the derivative of the error EE at a point x,x, with respect to the weight w_j.w 
j
​	 .


A similar calculation will show us that


This actually tells us something very important. For a point with coordinates (x_1, \ldots, x_n),(x 
1
​	 ,…,x 
n
​	 ), label y,y, and prediction \hat{y}, 
y
^
​	 , the gradient of the error function at that point is \left(-(y - \hat{y})x_1, \cdots, -(y - \hat{y})x_n, -(y - \hat{y}) \right).(−(y− 
y
^
​	 )x 
1
​	 ,⋯,−(y− 
y
^
​	 )x 
n
​	 ,−(y− 
y
^
​	 )). In summary, the gradient is

\nabla E = -(y - \hat{y}) (x_1, \ldots, x_n, 1).∇E=−(y− 
y
^
​	 )(x 
1
​	 ,…,x 
n
​	 ,1).
