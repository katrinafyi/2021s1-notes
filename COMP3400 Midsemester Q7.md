## Question 7
```haskell
import Data.Maybe ( isJust )

ordered :: (Bounded a, Ord a) => [a] -> Bool
ordered = isJust . foldr go (Just maxBound)
  where
    go :: Ord a => a -> Maybe a -> Maybe a
    go a1 (Just a2) | a1 < a2 = Just a1
    go _ _ = Nothing
```