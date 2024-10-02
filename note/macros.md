# Macros
programs as data 
``` scheme
(define a (list 'quotient 1 2 3))
(eval a)
(list ' + 1 (+ 2 3))
'(1 2 3)
```
quote '
quasiquote `

``` scheme
(list ' +1 (+ 2 3))
(list '(+ 1 (+ 2 3)))
```

a classic procedure is
``` scheme
(begin
(define p)
(p ...))
```

generating code:
```
`(lambda (, (cards), car))
```

macro =1. quote 2 eval

在 Scheme 中，当使用反引号（`）构造表达式时，逗号（,）用于插入并求值表达式。每个逗号仅作用于它后面的单个表达式，因此你需要为每个需要求值的部分添加逗号。


`(1 (,x) 3)
`(1 ,(* x y) y)

``` scheme
(let((x 1))())
((lambda ()()) ()) ; let and lambda both can have multiple expression
((lambda(x)(+ x 5)(+ x 10))8) ; only get 18
```
``` SQL
SELECT n > 1, count(*) from numbers group by n > 1;

haiku 俳句