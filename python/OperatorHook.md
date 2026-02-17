# OperatorHook

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    # This program demos overloading operator and some builtin function's hook。It can be used as a tutorial. 
    # If you find any problem, please tell me.
    # author: Simeon Chaos simeon.chaos@gmail.com
    # version 0.1.0 2007-6-24
    # license: In public domain. You can freely use, modify, redistribute this file in any ways. Keep the text about the author is appreciated.
    # Warranty: THERE IS NO ANY WARRANTY FOR THE PROGRAM. The software is provided "as-is," without any express or implied warranty. In no event shall the author be held liable for any damages arising from the use of the software.
    # Tested at Windows, python 2.4.4

    #from __future__ import division #when imported，__truediv__ is called, output is as below:
    # op/1: __truediv__      1/op: __rtruediv__      op /= 1: __itruediv__
    #else __div__ is called, output is as below:
    # op/1: __div__      1/op: __rdiv__      op /= 1: __idiv__

    # Chinese
    # 本程序演示重载操作符和某些内置函数的钩子，用于学习和演示。
    # 如果有任何问题，请告诉我。
    # 作者: 曹星明 simeon.chaos@gmail.com
    # 版本 0.1.0 2007-6-24
    # 使用证书：公用许可。允许以任何方式自由使用，修改，分发本文件。欢迎保留这些关于作者的文字。
    # 免责声明：作者对本文件的使用不作任何担保。
    # 在Windows, python 2.4.4上运行通过。

    #from __future__ import division #如果导入，将调用__truediv__，因此将有如下输出
    # op/1: __truediv__      1/op: __rtruediv__      op /= 1: __itruediv__
    #否则，将调用__div__,因此将有如下输出
    # op/1: __div__      1/op: __rdiv__      op /= 1: __idiv__

    #result(run on Windows, python 2.4.4, boa constructor 0.4.4)
    '''
    op.__doc__: Operation  __doc__
    Demo the relation between some operators / builtin function and their hook method.
    演示各种操作符以及内建函数与钩子函数之间的对应关系
    op+1: __add__      1+op: __radd__      op += 1: __iadd__
    op-1: __sub__      1-op: __rsub__      op -= 1: __isub__
    op*1: __mul__      1*op: __rmul__      op *= 1: __imul__
    op/1: __div__      1/op: __rdiv__      op /= 1: __idiv__
    op%1: __xmod__      1%op: __rmod__      op %= 1: __imod__
    op//1: __floordiv__      1//op: __rfloordiv__      op //= 1: __ifloordiv__
    op^1: __xor__      1^op: __rxor__      op ^= 1: __ixor__
    ~op: __invert__
    -op: __neg__
    +op: __pos__
    abs(op): __abs__
    op==1: __eq__       1==op: __eq__
    op!=1: __ne__       1!=op: __ne__
    op<1: __lt__       1<op: __gt__
    op<=1: __le__       1<=op: __ge__
    op>=1: __ge__       1>=op: __le__
    op>1: __gt__       1>op: __lt__
    cmp(op,1): __eq__ __lt__ __gt__ __cmp__       cmp(1,op): __eq__ __gt__ __lt__ __cmp__
    op>=1: __ge__       1>=op: __le__
    divmod(op,1): __divmod__      divmod(1,op): __rdivmod__
    pow(op,1): __pow__      pow(1,op): __rpow__
    int(op): __int__
    long(op): __long__
    float(op): __float__
    oct(op): __oct__
    hex(op): __hex__
    op or 1: __nonzero__
    op(): __call__
    op[1]=1 __setitem__
    op[1] __getitem__
    op[:]=[] __setslice__
    op[:] __getslice__
    del op[:] __delslice__
    1 in op __contains__
    [x for x in op] __iter__
    op.a: __getattr__
    op.a = 1: __setattr__
    op.a:
    del op.a: __delattr__

    len(op) __len__
    str(op) __str__
    repr(op) __repr__

    coerce(op,1): __coerce__ number coercion failed
    op+1: __coerce__
    '''

    class Operation:
      '''Operation  __doc__
    Demo the relation between some operators / builtin function and their hook method.
    演示各种操作符以及内建函数与钩子函数之间的对应关系'''
      def __add__(self, other): print '__add__',
      def __radd__(self, other): print '__radd__',
      def __iadd__(self, other): print '__iadd__',; return self 

      def __sub__(self, other): print '__sub__',
      def __rsub__(self, other): print '__rsub__',
      def __isub__(self, other): print '__isub__',; return self 

      def __mul__(self, other): print '__mul__',
      def __rmul__(self, other): print '__rmul__',
      def __imul__(self, other): print '__imul__',; return self 

      def __div__(self, other): print '__div__',
      def __rdiv__(self, other): print '__rdiv__',
      def __idiv__(self, other): print '__idiv__',; return self 

      def __xor__(self, other): print '__xor__',
      def __rxor__(self, other): print '__rxor__',
      def __ixor__(self, other): print '__ixor__',; return self 

      def __mod__(self, other): print '__xmod__',
      def __rmod__(self, other): print '__rmod__',
      def __imod__(self, other): print '__imod__',; return self 

      def __floordiv__(self, other): print '__floordiv__',
      def __rfloordiv__(self, other): print '__rfloordiv__',
      def __ifloordiv__(self, other): print '__ifloordiv__',; return self 

      def __truediv__(self, other): print '__truediv__',
      def __rtruediv__(self, other): print '__rtruediv__',
      def __itruediv__(self, other): print '__itruediv__',; return self 

      def __or__(self, other): print '__or__',
      def __ror__(self, other): print '__ror__',
      def __ior__(self, other): print '__ior__',; return self 

      def __and__(self, other): print '__and__',
      def __rand__(self, other): print '__rand__',
      def __iand__(self, other): print '__iand__',; return self 

      def __lshift__(self, other): print '__lshift__',
      def __rlshift__(self, other): print '__rlshift__',
      def __ilshift__(self, other): print '__ilshift__',; return self 

      def __rshift__(self, other): print '__rshift__',
      def __rrlshift__(self, other): print '__rrshift__',
      def __irlshift__(self, other): print '__irshift__',; return self 

      def __invert__(self): print '__invert__'; return 0
      def __neg__(self): print '__neg__'; return -1
      def __pos__(self): print '__pos__'; return +1

      def __divmod__(self, other): print '__divmod__',
      def __rdivmod__(self, other): print '__rdivmod__',

      def __pow__(self, other): print '__pow__',
      def __rpow__(self, other): print '__rpow__',

      def __abs__(self): print '__abs__',
      def __nonzero__(self): print '__nonzero__'; return True
      
      def __call__(self): print '__call__',;

      def __eq__(self, other): print '__eq__',; return 0
      def __ne__(self, other): print '__ne__',; return 0
      def __lt__(self, other): print '__lt__',; return 0
      def __le__(self, other): print '__le__',; return 0
      def __ge__(self, other): print '__ge__',; return 0
      def __gt__(self, other): print '__gt__',; return 0
      def __cmp__(self, other): print '__cmp__',; return 0
      
      def __coerce__(self, other): return None
      
      def __getitem__(self, i): print '__getitem__'; return None
      def __setitem__(self, i, value): print '__setitem__'; return self

      def __getslice__( self, i, j): print '__getslice__'; return self
        #Deprecated since release 2.0. Support slice objects as parameters to the __getitem__() method.

      def __setslice__( self, i, j, sequence): print '__setslice__'; return self 
        #This method is deprecated. 

      def __delslice__( self, i, j): print '__delslice__'  
      def __contains__( self, item): print '__contains__' 
      def __iter__( self): print '__iter__'; return iter([]) 
     

      def __getattribute__(self, attr): print '__getattribute__'; return None
      #def __setattribute__(self, attr, value): print '__setattribute__'; self.__dict__[attr] = value; return None
      #__setattribute__只对new style class起作用
      def __getattr__(self, attr): print '__getattr__',; return None
      def __setattr__(self, attr, value): print '__setattr__'; self.__dict__[attr] = value; return None
      def __delattr__(self, attr): print '__delattr__'; return None
      
      def __float__(self): print '__float__'; return 0.0
      def __int__(self): print '__int__'; return 0
      def __long__(self): print '__long__'; return 0
      def __oct__(self): print '__oct__'; return '12'
      def __hex__(self): print '__hex__'; return '0xf5'
      def __len__(self): print '__len__'; return 0
      def __repr__(self): print '__repr__'; return ''
      def __str__(self): print '__str__'; return ''
      

    op = Operation()
    print 'op.__doc__:', op.__doc__

    print 'op+1:',; op+1; print '     1+op:',; 1+op; print '     op += 1:',; op += 1; print
    print 'op-1:',; op-1; print '     1-op:',; 1-op; print '     op -= 1:',; op -= 1; print
    print 'op*1:',; op*1; print '     1*op:',; 1*op; print '     op *= 1:',; op *= 1; print
    print 'op/1:',; op/1; print '     1/op:',; 1/op; print '     op /= 1:',; op /= 1; print
    print 'op%1:',; op%1; print '     1%op:',; 1%op; print '     op %= 1:',; op %= 1; print
    print 'op//1:',; op//op; print '     1//op:',; 1//op; print '     op //= 1:',; op //= 1; print
    print 'op^1:',; op^1; print '     1^op:',; 1^op; print '     op ^= 1:',; op ^= 1; print

    print '~op:',; ~op
    print '-op:',; -op
    print '+op:',; +op

    print 'abs(op):',; abs(op);print
    print 'op==1:',; op==1; print '      1==op:',; 1==op; print
    print 'op!=1:',; op!=1; print '      1!=op:',; 1!=op; print
    print 'op<1:',; op<1; print '      1<op:',; 1<op; print
    print 'op<=1:',; op<=1; print '      1<=op:',; 1<=op; print
    print 'op>=1:',; op>=1; print '      1>=op:',; 1>=op; print
    print 'op>1:',; op>1; print '      1>op:',; 1>op; print
    print 'cmp(op,1):',; cmp(op,1); print '      cmp(1,op):',; cmp(1,op);print
    print 'op>=1:',; op>=1; print '      1>=op:',; 1>=op;print
    print 'divmod(op,1):',;divmod(op,1);print '     divmod(1,op):',; divmod(1,op); print 
    print 'pow(op,1):',;pow(op,1);print '     pow(1,op):',; pow(1,op); print 


    print 'int(op):',; int(op)
    print 'long(op):',; long(op)
    print 'float(op):',; float(op)
    print 'oct(op):',; oct(op)
    print 'hex(op):',; hex(op)

    print 'op or 1:',; op or 1
    print 'op():',; op(); print

    print 'op[1]=1',; op[1]=1
    print 'op[1]',; op[1]
    print 'op[:]=[]',; op[:]=[]
    print 'op[:]',; op[:]
    print 'del op[:]',; del op[:]
    print '1 in op',; 1 in op
    print '[x for x in op]',;[x for x in op]
    print 'op.a:',; op.a; print
    print 'op.a = 1:',; op.a = 1
    print 'op.a:',; op.a; print
    print 'del op.a:',; del op.a; print
    print 'len(op)',; len(op);
    print 'str(op)',; str(op)
    print 'repr(op)', repr(op)
     
    class Operation:
      '''complement:If __coerce__ is put above, it is disturbed to run the other method, 
    so __coerce__ is put here alone. You can try it yourself.
    补充:因为__coerce__放在上面的类定义中将干扰其它方法的执行，因此单独列出。读者可以自己试一下。'''
      def __add__(self, other): pass
      def __coerce__(self, other): print '__coerce__',; return None

    op = Operation()
    try: print 'coerce(op,1):',; coerce(op,1); 
    except TypeError, e: print e
    try: print 'op+1:',; op+1; 
    except TypeError, e: print e
