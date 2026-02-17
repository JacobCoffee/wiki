# Wiki沙箱

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

你可以在這裡盡情嘗試 wiki 的各項功能, 但是別把四個減號上面的說明改掉了\...(就是本段!) 還有, 請 **\*不要\*** 只是因為想試試看, 就新增沒有內容/意義的頁面.

**提示:** 按住 Shift 鍵再點選 \"[HelpOnEditing](HelpOnEditing)\" 就可以在另一個視窗裡打開編輯說明. IE 用戶請在 \"[HelpOnEditing](HelpOnEditing)\" 上點右鍵, 選「在新視窗開啟」. Firefox 或 Mozilla 用戶可以試試用滑鼠中鍵, 在新的分頁中開啟.

------------------------------------------------------------------------

## 文字格式 

*斜體* **粗體** `非調和字`

`倒單引號帶出的非調和字`{.backtick} (這個功能可能會關掉)

放大 [縮小]

    預先排好格式的段落

    def syntax(highlight):
        print "on"
        return None

## 連結 

[HelpOnEditing](HelpOnEditing) [InterWiki](http://moinmoin.wikiwikiweb.de/InterWiki "MoinMoin") [中文的MoinMoin](./(e4b8ade69687e79a84)MoinMoin.html)

[http://purl.net/wiki/moin/](http://purl.net/wiki/moin/) [Python](http://www.python.org/)

[someone@the.inter.net](mailto:someone@the.inter.net)

### 圖片連結 

![](http://c2.com/sig/wiki.gif "http://c2.com/sig/wiki.gif")

## 清單 

### 圓點 

- 第一點
  1.  帶編號的巢狀清單
  2.  編號會一直往上加
- 第二點
- 第三點
  - 又見面了!

  縮排
  - 再縮排

### 辭彙 

專有名詞
:   定義

### 畫圖 

[![\[ATTACH\]](/wiki/modernized/img/attach.png "[ATTACH]")]( "Create new drawing "mytest.tdraw (opens in new window)"")

# 標題 1 

## 標題 2 

### 標題 3 

#### 標題 4 

##### 特別的大小 

[ПростоТест](./(d09fd180d0bed181d182d0bed0a2d0b5d181d182).html)

# IRC 對話記錄測試 

    (23:18) <     jroes> ah
    (23:19) <     jroes> hm, i like the way {{{ works, but i was hoping the lines would wrap
    (23:21) -!- gpciceri [~gpciceri@host181-130.pool8248.interbusiness.it] has quit [Read error: 110 (Connection timed out)]
    (23:36) < ThomasWal> you could also write a parser or processor
    (23:38) <     jroes> i could?
    (23:38) <     jroes> would that require modification on the moin end though?
    (23:38) <     jroes> i cant change the wiki myself :x
    (23:39) < ThomasWal> parsers and processors are plugable
    (23:39) < ThomasWal> so you dont need to change the core code
    (23:40) < ThomasWal> you need to copy it to the wiki data directory though
    (23:40) <     jroes> well, what i meant to say was that i dont have access to the box running the wiki
    (23:40) < ThomasWal> then this is no option awdsd asdasd sa asdasd sad asdadasds adasd asd asd asd asd asd a dadad ad adad ad asd asd adad asdasd asd adad as d
    (23:40) <     jroes> yeah :/

[![\[ATTACH\]](/wiki/modernized/img/attach.png "[ATTACH]")]( "Create new drawing "mytest2.tdraw (opens in new window)"")

Spanning rows and columns::

- ::: {}
  +:----------:+------------------------------------------------------------------------------------------------------------------:+
  | 2 rows     | row 1                                                                                                             |
  |            +-------------------------------------------------------------------------------------------------------------------+
  |            | row 2 hh hfdsh hfsh jhsdkfh shf jhkvjh xh vjcxh vhcxxvcfdgfdhkh hkhf skjhkjdhfkhdkf hdhkf kjfk jdhskfh df dfhs fs |
  +------------+-------------------------------------------------------------------------------------------------------------------+
  | row 3 over 2 columns                                                                                                           |
  +--------------------------------------------------------------------------------------------------------------------------------+
  :::
