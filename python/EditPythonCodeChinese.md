# EditPythonCodeChinese

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# 如何编辑Python代码 How To Edit Python Code 

Python uses an indentation-based syntax for grouping statements into blocks. For example:

Python基于语法缩进将语句组合成块。例如

    if some_condition and some_other_condition
        do_something()
    do_this_anyway()

However, beginners to Python programming are sometimes worried about this aspect of the language, asking questions like\...

然而，Python编程初学者有时会担心它的这个特点，提出以下类似疑问：

- How should I add space at the beginning of a line? (In other words, how should I indent text?)
- 我如何在行首添加空格？（换句话说，如何进行文本缩进？）
- How can I be sure that Python won\'t change its mind about the space I\'ve added?
- 我如何确认对我已添加的空格Python不会理解错误？
- What happens if someone edits my code and mixes in tabs and spaces?
- 如果其它人编辑我的代码并混合使用Tab和空格键会导致什么问题？
- Isn\'t Python susceptible to problems I\'ve had with Makefiles?
- 生成文件时产生的问题不会对Python造成影响吗？

This leads us to introduce the golden rule\...

鉴于上述疑问，我们来介绍Python的黄金规则...

------------------------------------------------------------------------

## 不要混合使用Tab和空格! Do Not Mix Tabs and Spaces! 

Now, this doesn\'t mean that you can\'t use the `Tab`{.backtick} key on your keyboard: it just means that your editor has to be set up properly so that tab characters aren\'t mixed in with space characters. Tab characters often appear as very wide spaces in text, typically making the cursor jump to a position further across in the editor window or terminal.

当然，这并不意味着你不能使用键盘上的Tab键：只是说需要恰当配置你的编辑器以使Tab字符不至于与空格字符混在一块儿。Tab字符通常在文本中以较宽的空格显示，代表性的是使光标在编辑器窗口或终端命令行窗口中跳至一个较远的位置。

This leads us to a simple choice:

这引导我们做一个简单的选择：

- **Either** your editor should *always* add spaces when you press the `Tab`{.backtick} key\...

- **要么** 在按下\'Tab\'键时你的编辑器**总是**添加空格；

- **Or** your editor should *always* add tabs when you press the `Tab`{.backtick} key, and you should yourself *always* use tabs when indenting.

- **要么** 在按下\'Tab\'键时你的编辑器**总是**添加Tab字符，并且你**总是**使用Tab字符进行缩进。

Many people recommend the first choice since you can use the `Tab`{.backtick} key as much as you like, and it does no harm to add spaces manually, although your indentation must always be consistent.

许多人推荐选择第一项，因为可以尽可能多的使用\'Tab\'键，而且不会对手动添加空格带来有危害，然而你的缩进方法自始至终必须保持一致。

------------------------------------------------------------------------

Whilst there is always a risk that someone with a badly behaved editor will start mixing tabs and spaces, potentially confusing Python, it should be remembered that such editing habits will probably confuse *programmers* working with such code in any language, as is shown by the following classic example in C-like languages:

当一个人使用不恰当的编辑器导致Tab和空格混合使用时总是会存在风险，给Python带来潜在的困扰，应当谨记：这些坏的编码习惯有可能给使用其它编程语言的程序员带来困惑，它通常在类似C语言中显示为如下典型例子：

    if (some_condition && some_other_condition)
        do_something();
        do_this_anyway();

Although a C or C++ compiler will accept something like this, there may be a clear mismatch between what the programmer intended and the behaviour of the resulting code. Clearly, \"sloppy\" editing habits have an impact regardless of the role of indentation in a language\'s syntax.

虽然C或C++编译器可以接受类似的格式，但是程序员的缩进与最终代码的行为明显不匹配。显然，不管缩进在编程语言语法中扮演何种角色，不\"整洁\"的编辑习惯都是有危害的。

## 文本编辑器的选择 Choosing a Text Editor 

You may have a favourite text editor which you want to use to edit Python code. Hopefully, this editor will be slightly more sophisticated than the Notepad editor (on Windows) and will let you change its settings so that Python code can be edited effectively. Many text editors have support for syntax highlighting (so that different aspects of the text have different colours - keywords might be yellow, strings might be purple, and so on), and such things can be worthwhile benefits which can lure you away from more primitive (if more familiar) programs. A list of Python-compatible editors can be found on the [PythonEditors](PythonEditors) page.

也许你已经有一个喜爱的编辑器想用来进行Python代码编辑。希望这款编辑器比Notepad记事本编辑器(Windows系统中)更高级一些，可以通过更改设置使编辑Python代码更有效率。许多文本编辑器支持语法加亮（因此文本的不同部分可以用不同颜色来显示-关键字可显为黄色，字符串可显为紫色，等等），以及有一些吸引你抛弃原有的编辑器（可能是你熟悉的）的特性。你可以在[PythonEditors](PythonEditors)页面找到与Python兼容的编辑器列表。

## 配置文本编辑器Configuring a Text Editor 

Now that you\'ve made a choice from the [PythonEditors](PythonEditors) list, you\'ll want to make sure that it is set up properly. Below you\'ll find a guide for a number of different editors dealing with important Python issues such as indentation (tabs and spaces) as well as other more general issues like encodings and syntax highlighting/colouring.

当你在[PythonEditors](PythonEditors)页面列表中选好编辑器，接下来你想确认它是否已被合理配置。就如何处理Python关键问题如缩进（Tab和空格），常规问题如语言编码、高亮/多颜色显示等，以下提供的编辑器指南供参考：

- [Vim](Vim) and related editors

## 编者注释Editorial Note 

Feel free to add entries about other editors in the section above. Try to arrange the entries in ascending alphabetical order.

您可在以上部分自由添加其它编辑器的条目。添加时注意按字母前后顺序罗列条目位置。

# 其它资源Other Resources 

- [PEP 8 - Style Guide for Python Code](http://www.python.org/dev/peps/pep-0008/)

------------------------------------------------------------------------

[CategoryEditors](CategoryEditors)
