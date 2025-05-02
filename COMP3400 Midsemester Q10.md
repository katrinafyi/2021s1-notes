## Question 10
```haskell
neg :: Expr -> Expr
neg = BinOp Mul (Num (-1))

removeSub :: Expr -> Expr
removeSub (BinOp op x y) =
  case op of
    Subtract -> BinOp Add x' (neg y')
    _        -> BinOp op x' y'
  where
    x' = removeSub x
    y' = removeSub y
removeSub x = x
```