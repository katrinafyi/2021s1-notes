## Question 2
$$
\begin{aligned}
(\lambda x . \lambda y. x \, y)(\lambda z . z) w &\to
(\lambda x . \lambda y. x \, y)\ (z)[z:=w] \\ 
&=(\lambda x . \lambda y. x \, y)\ w \\ 
&\to (\lambda y. x \, y)[x:=w] \\ 
&= \lambda y. w \, y \\ 
\end{aligned}
$$