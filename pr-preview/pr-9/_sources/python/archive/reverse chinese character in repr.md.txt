# reverse chinese character in repr

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    # This program reverses the hex code in the repr of any value back into chinese character.
    # If you find any problem, please tell me.
    # author: Simeon Chaos simeon.chaos@gmail.com
    # version 0.1.0 2007-6-24
    # license: In public domain. You can freely use, modify, redistribute this file in any ways. Keep the text about the authon is appreciated.
    # Warranty: THERE IS NO ANY WARRANTY FOR THE PROGRAM. The software is provided "as-is," without any express or implied warranty. In no event shall the author be held liable for any damages arising from the use of the software.
    # Tested at Windows, python 2.4.4

    # Chinese
    # 本程序将任意对象中汉字的十六进制码表示(所谓乱码)重新转换回汉字。
    # 如果有任何问题，请告诉我。
    # 作者: 曹星明 simeon.chaos@gmail.com
    # 版本 0.1.0 2007-6-24
    # 使用证书：公用许可。允许以任何方式自由使用，修改，分发本文件。欢迎保留这些关于作者的文字。
    # 免责声明：作者对本文件的使用不作任何担保。
    # 在Windows, python 2.4.4上运行通过。
    '''
    This program reverses the hex code in the repr of any value back into chinese character.
    将任意对象中汉字的十六进制码表示(所谓乱码)重新转换回汉字
    '''
    def myrepr(x):
      '''可以将任意对象中汉字的十六进制码表示(所谓乱码)重新转换回汉字'''
      re_hzrepr = re.compile(r'\\x[a-f0-9][a-f0-9]\\x[a-f0-9][a-f0-9]')
      r = repr(x);  s = ''
      i = 0; j = 0  
      while i < len(r):
        if re_hzrepr.match(r[i:]) and int(r[i+2:i+4], 16)>127:
          s += chr(int(r[i+2:i+4], 16)) + chr(int(r[i+6:i+8], 16)) 
          i += 8 
        elif r[i]=='\\' and r[i+1]=='n': s += '\n'; i += 2
        elif r[i]=='\\' and r[i+1]=='\'': i += 2
        elif r[i]=='\\' and r[i+1]=='\"': i += 2
        else: s += r[i]; i += 1;
      if len(s)>1 and s[0]=="'": s = s[1:-1]
      return s
     
    def printhz(*x1):
      '''打印带全角或汉字的myrepr结果字符串
    >>> repr('我')
    "'\\xce\\xd2'"
    >>> print ['我']
    ['\\xce\\xd2']
    >>> printhz(['我'])
    ['我']
    '''
      for x in x1:
        print myrepr(x),

    def printhznl(*x1):
      '''打印带全角或汉字的myrepr结果字符串并换行
    >>> repr('我')
    "'\\xce\\xd2'"
    >>> print ['我']
    ['\\xce\\xd2']
    >>> printhz(['我'])
    ['我']
    '''
      for x in x1:
        print myrepr(x),
      print

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
