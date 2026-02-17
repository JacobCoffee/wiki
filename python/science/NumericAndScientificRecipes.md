# NumericAndScientificRecipes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    """
    sinc(x) = sin(\pi x) / (\pi x),  if x != 0
            = 1,  if x = 0
    """
    def sinc(x):
        from math import pi, sin
        try:
            x = pi * x
            return sin(x) / x
        except ZeroDivisionError:   # sinc(0) = 1
            return 1.0


    """
    cbrt(x) = x^{1/3},  if x >= 0
            = -|x|^{1/3},  if x < 0
    """
    def cbrt(x):
        if x >= 0:
            return x ** (1.0/3.0)
        else:
            return - abs(x) ** (1.0/3.0)


    """
    Convert from polar (r,w) to rectangular (x,y)
        x = r cos(w)
        y = r sin(w)
    """
    def rect(r, w, deg=False):          # radian if deg=False; degree if deg=True
        from math import cos, sin, radians
        if deg:
            w = radians(w)
        return r * cos(w), r * sin(w)
    """
    Convert from rectangular (x,y) to polar (r,w)
        r = sqrt(x^2 + y^2)
        w = arctan(y/x) = [-\pi,\pi] = [-180,180]
    """
    def polar(x, y, deg=False):         # radian if deg=False; degree if deg=True
        from math import hypot, atan2, degrees
        if deg:
            return hypot(x, y), degrees(atan2(y, x))
        else:
            return hypot(x, y), atan2(y, x)

       Normally, rect() and polar() uses radian for angle; but, if deg=True
       specified, degree is used instead.

    """
    p(x) = polyeval(a, x)
         = a[0] + a[1]x + a[2]x^2 +...+ a[n-1]x^{n-1} + a[n]x^n
         = a[0] + x(a[1] + x(a[2] +...+ x(a[n-1] + a[n]x)...)
    """
    def polyeval(a, x):
        p = 0
        for coef in a[::-1]:
            p = p * x + coef
        return p


    """
    p'(x) = polyderiv(a)
          = b[0] + b[1]x + b[2]x^2 +...+ b[n-2]x^{n-2} + b[n-1]x^{n-1}
    where
        b[i] = (i+1)a[i+1]
    """
    def polyderiv(a):
        b = [i * x for i,x in enumerate(a)][1:]
        return b


    """
    Given x = r is a root of n'th degree polynomial p(x) = (x-r)q(x),
    divide p(x) by linear factor (x-r) using the same algorithm as
    polynomial evaluation.  Then, return the (n-1)'th degree quotient
    q(x) = polyreduce(a, r)
         = c[0] + c[1]x + c[2]x^2 +...+ c[n-2]x^{n-2} + c[n-1]x^{n-1}
    """
    def polyreduce(a, root):
        c, p = [], 0
        a.reverse()
        for coef in a:
            p = p * root + coef
            c.append(p)
        a.reverse()
        c.reverse()
        return c[1:]


    """
    x^2 + ax + b = 0  (or ax^2 + bx + c = 0)
    By substituting x = y-t and t = a/2, the equation reduces to
        y^2 + (b-t^2) = 0
    which has easy solution
        y = +/- sqrt(t^2-b)
    """
    def quadratic(a, b, c=None):
        import math, cmath
        if c:               # (ax^2 + bx + c = 0)
            a, b = b / float(a), c / float(a)
        t = a / 2.0
        r = t**2 - b
        if r >= 0:          # real roots
            y1 = math.sqrt(r)
        else:               # complex roots
            y1 = cmath.sqrt(r)
        y2 = -y1
        return y1 - t, y2 - t

    """
    x^3 + ax^2 + bx + c = 0  (or ax^3 + bx^2 + cx + d = 0)
    With substitution x = y-t and t = a/3, the cubic equation reduces to
        y^3 + py + q = 0,
    where p = b-3t^2 and q = c-bt+2t^3.  Then, one real root y1 = u+v can
    be determined by solving
        w^2 + qw - (p/3)^3 = 0
    where w = u^3, v^3.  From Vieta's theorem,
        y1 + y2 + y3 = 0
        y1 y2 + y1 y3 + y2 y3 = p
        y1 y2 y3 = -q,
    the other two (real or complex) roots can be obtained by solving
        y^2 + (y1)y + (p+y1^2) = 0
    """
    def cubic(a, b, c, d=None):
        from math import cos
        if d:                       # (ax^3 + bx^2 + cx + d = 0)
            a, b, c = b / float(a), c / float(a), d / float(a)
        t = a / 3.0
        p, q = b - 3 * t**2, c - b * t + 2 * t**3
        u, v = quadratic(q, -(p/3.0)**3)
        if type(u) is complex:     # complex cubic root
            r, w = polar(u.real, u.imag)
            y1 = 2 * cbrt(r) * cos(w / 3.0)
        else:                       # real root
            y1 = cbrt(u) + cbrt(v)
        y2, y3 = quadratic(y1, p + y1**2)
        return y1 - t, y2 - t, y3 - t


    """
    Ubiquitous Newton-Raphson algorithm for solving
        f(x) = 0
    where a root is repeatedly estimated by
        x = x - f(x)/f'(x)
    until |dx|/(1+|x|) < TOL is achieved.  This termination condition is a
    compromise between
        |dx| < TOL,  if x is small
        |dx|/|x| < TOL,  if x is large
    """
    def newton(func, funcd, x, TOL=1e-6):   # f(x)=func(x), f'(x)=funcd(x)
        f, fd = func(x), funcd(x)
        count = 0
        while True:
            dx = f / float(fd)
            if abs(dx) < TOL * (1 + abs(x)): return x - dx
            x -= dx
            f, fd = func(x), funcd(x)
            count += 1
            print "newton(%d): x=%s, f(x)=%s" % (count, x, f)


    """
    Similar to Newton's method, but the derivative is estimated by divided
    difference using only function calls.  A root is estimated by
        x = x - f(x) (x - oldx)/(f(x) - f(oldx))
    where oldx = x[i-1] and x = x[i].
    """
    def secant(func, oldx, x, TOL=1e-6):    # f(x)=func(x)
        oldf, f = func(oldx), func(x)
        if abs(f) > abs(oldf):            # swap so that f(x) is closer to 0
            oldx, x = x, oldx
            oldf, f = f, oldf
        count = 0
        while True:
            dx = f * (x - oldx) / float(f - oldf)
            if abs(dx) < TOL * (1 + abs(x)): return x - dx
            oldx, x = x, x - dx
            oldf, f = f, func(x)
            count += 1
            print "secant(%d): x=%s, f(x)=%s" % (count, x, f)


    """
    Closed Simpson's rule for
        \int_a^b f(x) dx
    Divide [a,b] iteratively into h, h/2, h/4, h/8, ... step sizes; and,
    for each step size, evaluate f(x) at a+h, a+3h, a+5h, a+7h, ..., b-3h,
    b-h, noting that other points have already been sampled.

    At each iteration step, data are sampled only where necessary so that
    the total data is represented by adding sampled points from all
    previous steps:
        step 1:     h       a---------------b
        step 2:     h/2     a-------^-------b
        step 3:     h/4     a---^-------^---b
        step 4:     h/8     a-^---^---^---^-b
        total:              a-^-^-^-^-^-^-^-b
    So, for step size of h/n, there are n intervals, and the data are
    sampled at the boundaries including the 2 end points.

    If old = Trapezoid formula for an old step size 2h, then Trapezoid
    formula for the new step size h is obtained by
        new = old/2 + h{f(a+h) + f(a+3h) + f(a+5h) + f(a+7h) +...+ f(b-3h)
            + f(b-h)}
    Also, Simpson formula for the new step size h is given by
        simpson = (4 new - old)/3
    """
    def closedpoints(func, a, b, TOL=1e-6):         # f(x)=func(x)
        h = b - a
        old2 = old = h * (func(a) + func(b)) / 2.0
        count = 0
        while True:
            h /= 2.0
            x, sum = a + h, 0
            while x < b:
                sum += func(x)
                x += 2 * h
            new = old / 2.0 + h * sum
            new2 = (4 * new - old) / 3.0
            if abs(new2 - old2) < TOL * (1 + abs(old2)): return new2
            old = new       # Trapezoid
            old2 = new2     # Simpson
            count += 1
            print 'closedpoints(%d): Trapezoid=%s, Simpson=%s' % (count, new, new2)


    """
    Open Simpson's rule (excluding end points) for
        \int_a^b f(x) dx
    Divide [a,b] iteratively into h, h/3, h/9, h/27, ... step sizes; and,
    for each step size, evaluate f(x) at a+h/2, a+2h+h/2, a+3h+h/2,
    a+5h+h/2, a+6h+h/2, ... , b-3h-h/2, b-2h-h/2, b-h/2, noting that other
    points have already been sampled.

    At each iteration step, data are sampled only where necessary so that
    the total data is represented by adding sampled points from all
    previous steps:
        step 1:     h       a-----------------^-----------------b
        step 2:     h/3     a-----^-----------------------^-----b
        step 3:     h/9     a-^-------^---^-------^---^-------^-b
        total:              a-^---^---^---^---^---^---^---^---^-b
    So, for step size of h/n, there are n intervals, and the data are
    sampled at the midpoints.

    If old = Trapezoid formula for an old step size 3h, then Trapezoid
    formula for the new step size h is obtained by
        new = old/3 + h{f(a+h/2) + f(a+2h+h/2) + f(a+3h+h/2) + f(a+5h+h/2)
            + f(a+6h+h/2) +...+ f(b-3h-h/2) + f(b-2h-h/2) + f(b-h/2)}
    Also, Simpson formula for the new step size h is given by
        simpson = (9 new - old)/8
    """
    def openpoints(func, a, b, TOL=1e-6):           # f(x)=func(x)
        h = b - a
        old2 = old = h * func((a + b) / 2.0)
        count = 0
        while True:
            h /= 3.0
            x, sum = a + 0.5 * h, 0
            while x < b:
                sum += func(x) + func(x + 2 * h)
                x += 3 * h
            new = old / 3.0 + h * sum
            new2 = (9 * new - old) / 8.0
            if abs(new2 - old2) < TOL * (1 + abs(old2)): return new2
            old = new       # Trapezoid
            old2 = new2     # Simpson
            count += 1
            print 'openpoints(%d): Trapezoid=%s, Simpson=%s' % (count, new, new2)


    """
    Find 2^n that is equal to or greater than.
    """
    def nextpow2(i):
        n = 1
        while n < i: n *= 2
        return n

       This is internal function used by fft(), because the FFT routine
       requires that the data size be a power of 2.


    """
    Return bit-reversed list, whose length is assumed to be 2^n:
    eg. 0111 <--> 1110 for N=2^4.
    """
    def bitrev(x):
        N, x = len(x), x[:]
        if N != nextpow2(N): raise ValueError, 'N is not power of 2'
        for i in range(N):
            k, b, a = 0, N>>1, 1
            while b >= a:
                if b & i: k |= a
                if a & i: k |= b
                b >>= 1
                a <<= 1
            if i < k:               # important not to swap back
                x[i], x[k] = x[k], x[i]
        return x


    """
    FFT using Cooley-Tukey algorithm where N = 2^n.  The choice of
    e^{-j2\pi/N} or e^{j2\pi/N} is made by 'sign=-1' or 'sign=1'
    respectively.  Since I prefer Engineering convention, I chose
    'sign=-1' as the default.

    FFT is performed as follows:
    1. bit-reverse the array.
    2. partition the data into group of m = 2, 4, 8, ..., N data points.
    3. for each group with m data points,
        1. divide into upper half (section A) and lower half (section B),
            each containing m/2 data points.
        2. divide unit circle by m.
        3. apply "butterfly" operation
                |a| = |1  w||a|     or      a, b = a+w*b, a-w*b
                |b|   |1 -w||b|
            where a and b are data points of section A and B starting from
            the top of each section, and w is data points along the unit
            circle starting from z = 1+0j.
    FFT ends after applying "butterfly" operation on the entire data array
    as whole, when m = N.
    """
    def fft(x, sign=-1):
        from cmath import pi, exp
        N = len(x)
        W = [exp(sign * 2j * pi * i / N)
              for i in range(N)]          # exp(-j...) is default
        x = bitrev(x)
        m = 2
        while m <= N:
            for s in range(0, N, m):
                for i in range(m/2):
                    n = i * N / m
                    a, b = s + i, s + i + m/2
                    x[a], x[b] = x[a] + W[n % N] * x[b], x[a] - W[n % N] * x[b]
            m *= 2
        return x
    """
    Inverse FFT with normalization by N, so that x == ifft(fft(x)) within
    round-off errors.
    """
    def ifft(X):
        N, x = len(X), fft(X, sign=1)       # e^{j2\pi/N}
        for i in range(N):
            x[i] /= float(N)
        return x


    """
    DFT using discrete summation
       X(n) = \sum_k W^{nk} x(k),  W = e^{-j2\pi/N}
    where N need not be power of 2.  The choice of e^{-j2\pi/N} or
    e^{j2\pi/N} is made by "sign=-1" or "sign=1" respectively.
    """
    def dft(x, sign=-1):
        from cmath import pi, exp
        N = len(x)
        W = [exp(sign * 2j * pi * i / N)
              for i in range(N)]          # exp(-j...) is default
        X = [sum(W[n * k % N] * x[k] for k in range(N))
              for n in range(N)]
        return X
    """
    Inverse DFT with normalization by N, so that x == idft(dft(x)) within
    round-off errors.
    """
    def idft(X):
        N, x = len(X), dft(X, sign=1)       # e^{j2\pi/N}
        for i in range(N):
            x[i] /= float(N)
        return x


    """
    Convolution of 2 causal signals, x(t<0) = y(t<0) = 0, using discrete
    summation.
        x*y(t) = \int_^t x(u) y(t-u) du = y*x(t)
    where the size of x[], y[], x*y[] are P, Q, N=P+Q-1 respectively.
    """
    def conv(x, y):
        P, Q, N = len(x), len(y), len(x)+len(y)-1
        z = []
        for k in range(N):
            lower, upper = max(0, k-(Q-1)), min(P-1, k)
            z.append(sum(x[i] * y[k-i]
                          for i in range(lower, upper+1)))
        return z
    """
    Correlation of 2 causal signals, x(t<0) = y(t<0) = 0, using discrete
    summation.
        Rxy(t) = \int_^{\infty} x(u) y(t+u) du = Ryx(-t)
    where the size of x[], y[], Rxy[] are P, Q, N=P+Q-1 respectively.

    The Rxy[i] data is not shifted, so relationship with the continuous
    Rxy(t) is preserved.  For example, Rxy(0) = Rxy[0], Rxy(t) = Rxy[i],
    and Rxy(-t) = Rxy[-i].  The data are ordered as follows:
        t:  -(P-1),  -(P-2),  ..., -3,  -2,  -1,  0, 1, 2, 3, ..., Q-2, Q-1
        i:  N-(P-1), N-(P-2), ..., N-3, N-2, N-1, 0, 1, 2, 3, ..., Q-2, Q-1
    """
    def corr(x, y):
        P, Q, N = len(x), len(y), len(x)+len(y)-1
        z1=[]
        for k in range(Q):
            lower, upper = 0, min(P-1, Q-1-k)
            z1.append(sum(x[i] * y[i+k]
                           for i in range(lower, upper+1)))            # 0, 1, 2, ..., Q-1
        z2=[]
        for k in range(1,P):
            lower, upper = k, min(P-1, Q-1+k)
            z2.append(sum(x[i] * y[i-k]
                           for i in range(lower, upper+1)))            # N-1, N-2, ..., N-(P-2), N-(P-1)
        z2.reverse()
        return z1 + z2


    """
    FFT convolution using relation
        x*y <==> XY
    where x[] and y[] have been zero-padded to length N, such that N >=
    P+Q-1 and N = 2^n.
    """
    def fftconv(x, y):
        X, Y = fft(x), fft(y)
        return ifft([a * b for a,b in zip(X,Y)])
    """
    FFT correlation using relation
        Rxy <==> X'Y
    where x[] and y[] have been zero-padded to length N, such that N >=
    P+Q-1 and N = 2^n.
    """
    def fftcorr(x, y):
        X, Y = len(x), fft(x), fft(y)
        return ifft([a.conjugate() * b for a,b in zip(X,Y)])


    """
    vdot(x, y) = <x|y> = \sum_i x_i y_i
    """
    def vdot(x, y):
        if len(x) != len(y): raise ValueError, 'unequal length'
        return sum(a * b for a, b in zip(x, y))


    """
    Various vector norms of x[]:
        ||x||1 = \sum_i |x_i|
        ||x||2 = sqrt(\sum_i x_i^2) = sqrt(<x|x>)
        ||x||oo = \max |x_i|
    """
    def vnorm(x, normtype=2):
        from math import sqrt
        if normtype == 1:           # ||x||1
            return sum(abs(a) for a in x)
        elif normtype == 2:         # ||x||2 is default
            return sqrt(vdot(x, x))
        elif normtype == 'oo':      # ||x||oo
            return max( abs(min(x)), abs(max(x)) )
        else:
            raise ValueError, 'unknown option'


    """
    Calculate mean and standard deviation of data x[]:
        mean = {\sum_i x_i \over n}
        std = sqrt(\sum_i (x_i - mean)^2 \over n-1)
    """
    def meanstdv(x):
        from math import sqrt
        n = len(x)
        mean = sum(x) / float(n)
        std = sqrt(sum((a - mean)**2 for a in x) / float(n-1))
        return mean, std


    """
    Read 1 number/line using eval() from <stdin> or 'file' if specified.
    If the first non-whitespace is not valid number characters
    '(+-.0123456789', then the line will be skipped.
    """
    def getv(s=''):
        import sys
        if s == '':
            f = sys.stdin
        else:
            f = open(s, 'r')
        x = []
        for a in f:
            a = a.strip()
            if a != '' and a[0] in '(+-.0123456789':
                x.append(eval(a))
        return x
    """
    Read 2 numbers/line using eval() from <stdin> or 'file' if specified.
    If the first non-whitespace is not valid number characters
    '(+-.0123456789', then the line will be skipped.
    """
    def getv2(s=''):
        import sys
        if s == '':
            f = sys.stdin
        else:
            f = open(s, 'r')
        x, y = [], []
        for a in f:
            a = a.strip()
            if a != '' and a[0] in '(+-.0123456789':
                b = a.split()
                x.append(eval(b[0]))
                y.append(eval(b[1]))
        return x, y


    """
    Write 1 number/line to <stdout> or 'file' if specified.
    """
    def printv(x, s=''):
        import sys
        out = ''
        for a in x:
            out += repr(a) + '\n'
        if s == '':
            sys.stdout.write(out)
        else:
            open(s, 'w').write(out)


    """
    Returns coefficients to the regression line "y=ax+b" from x[] and
    y[].  Basically, it solves
        Sxx a + Sx b = Sxy
         Sx a +  N b = Sy
    where Sxy = \sum_i x_i y_i, Sx = \sum_i x_i, and Sy = \sum_i y_i.  The
    solution is
        a = (Sxy N - Sy Sx)/det
        b = (Sxx Sy - Sx Sxy)/det
    where det = Sxx N - Sx^2.  In addition,
        Var|a| = s^2 |Sxx Sx|^-1 = s^2 | N  -Sx| / det
           |b|       |Sx  N |          |-Sx Sxx|
        s^2 = {\sum_i (y_i - \hat{y_i})^2 \over N-2}
            = {\sum_i (y_i - ax_i - b)^2 \over N-2}
            = residual / (N-2)
        R^2 = 1 - {\sum_i (y_i - \hat{y_i})^2 \over \sum_i (y_i - \mean{y})^2}
            = 1 - residual/meanerror

    It also prints to <stdout> few other data,
        N, a, b, R^2, s^2,
    which are useful in assessing the confidence of estimation.
    """
    def linreg(X, Y):
        from math import sqrt
        if len(X) != len(Y):  raise ValueError, 'unequal length'

        N = len(X)
        Sx = Sy = Sxx = Syy = Sxy = 0.0
        for x, y in zip(X, Y):
            Sx += x
            Sy += y
            Sxx += x*x
            Syy += y*y
            Sxy += x*y
        det = Sxx * N - Sx * Sx
        a, b = (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det

        meanerror = residual = 0.0
        for x, y in zip(X, Y):
            meanerror += (y - Sy/N)**2
            residual += (y - a * x - b)**2
        RR = 1 - residual/meanerror
        ss = residual / (N-2)
        Var_a, Var_b = ss * N / det, ss * Sxx / det

        print "y=ax+b"
        print "N= %d" % N
        print "a= %g \\pm t_{%d;\\alpha/2} %g" % (a, N-2, sqrt(Var_a))
        print "b= %g \\pm t_{%d;\\alpha/2} %g" % (b, N-2, sqrt(Var_b))
        print "R^2= %g" % RR
        print "s^2= %g" % ss

        return a, b
