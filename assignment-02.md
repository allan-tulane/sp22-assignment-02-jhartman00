# CMPS 2200 Assignment 2

**Name:** Jamie Hartman

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py`.. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.

    - Master Theorem
        - T(n) = aT(n/b) + f(n)
        - a>= 1, b > 1
        - f(n) = O(n^k log^p n)
     
        - Case 1: log_b a > k then O(n^log_b a)
        - Case 2: log_b a = k
            - if p > -1 then O(n^k log^p+1 n)
            - if p = -1 then O(n^k log(log(n)))
            - if p < -1 then O(n^k)
        - Case 3: log_b a < k:
            - if p >= 0 then O(n^k log^p n)
            - if p < 0 then O(n^k)
   
  * $W(n)=2W(n/3)+1$

    - log_b a = log_3 2 = 0.63092975357
    - k = 0
    - Case 1
    - O(n) = O(n^log_3 2) = O(n^.63092975357)  


  * $W(n)=5W(n/4)+n$

    - log_b a = log_4 5 = 1.1609640474
    - k = 1
    - Case 1
    - O(n) = O(n^1.1609640474)


  * $W(n)=7W(n/7)+n$

    - log_b a = log_7 7 = 1
    - k = 1
    - case 2
    - p = 0
    - O(n) = O(n * logn)
      


  * $W(n)=9W(n/3)+n^2$

    - log_b a = 2
    - k = 2
    - case 2
    - p = 0
    - O(n) = O(n^2 * logn)


  * $W(n)=8W(n/2)+n^3$

    - log_b a = 3
    - k = 3
    - case 2
    - p = 0
    - O(n) = O(n^3 + logn)


  * $W(n)=49W(n/25)+n^{3/2}\log n$

    - log_25 49 = 1.2090619551
    - k = 3/2 = 1.5
    - case 3
    - O(n) = O(n^3/2 * log*n)


  * $W(n)=W(n-1)+2$

    - T(n) = T(n-1) + 2
    - T(n-1) = T(n-2) + 2
    - T(n) = (T(n-2) + 2) + 2
    - T(n) = T(n-2) + 4
    - T(n) = T(n-k) + 2k
    - T(0) = 2
    - If n-k = 0 then n = k
    - T(n) = T(n-n) + n
    - T(n) = T(0) + 2n
    - O(n) = O(2n + 2)
    - O(n) = O(n)
    

  * $W(n)= W(n-1)+n^c$, with $c\geq 1$

    - T(n) = T(n-1) + n^c
    - T(n-1) = T(n-2) + (n-1)^c
    - T(n) = T(n-2) + n^c + (n-1)^c
    - T(n-2) = T(n-3) + (n-2)^c
    - T(n) = T(n-3) + n^c + (n-1)^c + (n-2)^c
    - T(n) = T(n-k) + (n-k+ 1)^c + (n-k+2)^c + ... + (n-1)^c  + n^c
    - if k = n then
    - T(n) = T(n-n) + (n-n+1)^c + ... + (n-1)^c + n^c
    - T(n) = T(0) + 1^c + 2^c + 3^c + ... + n^c
    - T(n) = 1^c + 2^c + 3^c + ... + n^c <= n^c + n^c + ... + n^c = n^(c+1)
    - O(n) = O(n^(c))

  

  * $W(n)=W(\sqrt{n})+1$

    - T(n) = T(sqrt(n) + 1) = T(n^(1/2))
    - T(n) = T(n^(1/(2^2)) + 2
    - T(n) = T(n^(1/(2^3)) + 3
    - T(n) = T(n^(1/(2^k))) + k
    - Assume n = 2^m
    - T(2^m) = T(2^(m/2k)) + k
    - Assume T(2^(m/2k)) = T(2) = 1
    - Then m/2k = 1
    - m = 2^k and k = log_2 m
    - Since n = 2^m and m = log_2 m then
    - k = log(log_2(n))
    - O(log(log_2(n)))


2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.

    - a = 5
    - b = 2
    - f(n) = 1
    - T(n) = 5T(n/2) + 1
    - log_b a = 2.32192809489
    - k = 0
    - Case 1
    - O(n^2.32192809489)


  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.

    - a = 2
    - b = (n-1)
    - f(n) = 1
    - T(n) = 2T(n-1) + 1
    - T(n-1) = 2T(n-2) + 1
    - T(n) = 2 * (2T(n-2) + 1) + 1
    - T(n) = 2^2 * T(n-2) + 2
    - T(n-2) = 2T(n-3) + 1
    - T(n) = 2^2 * 2T(n-3) + 2 + 1
    - T(n) = 2^3 * T(n-3) + 3
    - T(n) = 2^k * (n-k) + k
    - if n-k = 0 then n = k
    - T(n) = 2^n * T(n-n) + n
    - T(n) = 2^n * T(0) + n
    - T(n) = 2^n * 1 + n
    - T(n) = 2^n + n
    - O(n) = O(2^n)
   

    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    - a = 9
    - b = 3
    - f(n) = n^2
    - T(n) = 9T(n/3) + n^2
    - k = 2
    - log_b a = 2
    - O(n) = O(n^2)
    

* What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?

    - The work for the below answers are done above
    - The first problem has a recurence function of  T(n) = 5T(n/2) + 1 and an asymptotic run time of O(n^2.32192809489)
    - The second problem has a recurence function of T(n) = 2T(n-1) + 1 and an asymptotic run time of O(2^n)
    - The third problem has a recurence function of T(n) = 9T(n/3) + n^2 and an asymptotic run time of O(n^2)
    - O(n^2) < O(n^2.3) < O(2^n) therefore I would choose algorithm 3


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
     - I compared the sub quadratic function to the quadratic function from recitation three and got a table you can print out if you run the main file.  I was going to add the table here but it does not format right in the rendered markdown
     - the table clearly shows the subquadratic function increasing in time (in ms) at a slower rate than the quadratic function
     - I tested the two functions with different powers of 5 as the x and the y values.  At 5^12, the subquadratic algorithm ran in 2.8 ms whereas the quadratic ran in 6.2 (note these numbers may vary slightly but are subquadratic is consistently less than quadratic)
     - Since the problem states that the sub_quadratic function should run in sub quadratic time and the sub_quadratic functions times are much lower than the quadratic functions times I would say that the code scales in the manner described by the asymptotic run times.
