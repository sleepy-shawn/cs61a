(define (over-or-under num1 num2) 
    (cond 
      ((> num1 num2) 1)
      ((> num2 num1) (- 1))
      ((= num2 num1) 0)
      ))

(define (make-adder num)
    (lambda (x) (+ num x)))

(define (composed f g) 
    (lambda (x) (f(g x))))

(define (repeat f n) 
(if (= n 1) f
  (composed f (repeat f (- n 1)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
(let ((x (max a b))
      (y (min a b)))
      (if (zero? (modulo x y))
          y
        (gcd y (modulo x y)))))
