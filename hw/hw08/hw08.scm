(define (ascending? s) 
(if (or (null? s) (null? (cdr s))) #t
    (let ((a (car s))
          (b (car(cdr s ))))
        (if (> a b ) 
            #f
        (ascending? (cdr s))))))

(define (my-filter pred s) 
    (cond
    ((null? s) '())
    ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
    (else (my-filter pred (cdr s))))
)

(define (interleave lst1 lst2)
    (cond
    ((and (null? lst1) (null? lst2)) '())
    ((null? lst1) lst2)
    ((null? lst2) lst1)
    (else (cons(car lst1) (cons(car lst2) (interleave (cdr lst1) (cdr lst2))))))
    )

(define (no-repeats s)
    (if (null? s)
             s
        (cons (car s) 
        (no-repeats 
        (filter (lambda (x) (not (= x (car s)))) (cdr s))))
    )
)