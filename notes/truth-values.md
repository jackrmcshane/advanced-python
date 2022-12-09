
# Python Truth Values

Any object can be tested for a boolean truth value.

The values that evaluate to boolean 0:
* `False` and `None`
* Numeric zero values: 0, 0.0, 0j
* Decimal(0), Fraction(0,x)
* Empty sequences/collections: '', (), [], {}
* set(), range(0)

Custom objects are `True` by default unless they:
* override the `__bool__` function and return a `False` value, or
* override the `__len__` function and return a length of `0`.


### Boolean Operations
---

| Boolean Operation | Result |
| --- | --- |
| X *and* Y | true if X and Y are both true |
| X *or* Y | true if either X or Y are true |
| *not* X | if X is false, then true, else false |

_**Note:**_ These are short circuit operators!

