## Question 9
```haskell
data Suit = Hearts | Clubs | Diamonds | Spades deriving Eq
data Rank = Numeric Int | Jack | Queens | King | Ace deriving Eq
data Card = NormalCard Rank Suit | Joker deriving Eq
```

```haskell
isAce :: Card -> Bool
isAce (NormalCard Ace _) = True
isAce _ = False

isJoker :: Card -> Bool
isJoker Joker = True
isJoker _ = False

countAces :: [Card] -> Int
countAces = length . filter ((||) <$> isAce <*> isJoker)
```