---
title: test
categories:
  - 博客
mathjax: true
abbrlink: 63534
date: 2021-11-28 00:00:00
sitemap: false
---

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题

> 提示块标签
>
>> 嵌套提示块
>>

- 无序列表1
- 无序列表2

1. 有序列表1
2. 有序列表2

__加粗__，*斜体*，~~删除线~~，<u>下划线</u>。


```c++
printf("hello world");
```

```c++
cout << "hello world";
```

```java
System.out.println("hello world");
```

```csharp
Console.WriteLine("hello world");
```

$$
(\bigcup_{n}S_{n}) ^{c} =\bigcap_{n}S^{c}_{n}
$$

$$
\begin{equation}
  x = a_0 + \cfrac{1}{a_1 
          + \cfrac{1}{a_2 
          + \cfrac{1}{a_3 + \cfrac{1}{a_4} } } }
\end{equation}
$$

试试行内公式 $e^{ix} = \cos x + i \cdot \sin x$

[^这是脚注]

这也是脚注[^1]

| title                | an English long long title                               | 一个中文长长长长标题~                  |
| -------------------- | :------------------------------------------------------- | -------------------------------------- |
| content              | Lorem ipsum dolor sit amet, consectetur adipisicing elit | 中文内容                               |
| **markdown**~~测试~~ | 公式测试: $(a+b)^2=a^2+2ab+b^2$                          | 使用HTML 转义字符如: &#124; (`&#124;`) |




---
# butterfly主题自带 tag plugins
> 以下部分的[来源和详细使用方法](https://butterfly.js.org/posts/4aa8abbe/#%E6%A8%99%E7%B1%A4%E5%A4%96%E6%8E%9B%EF%BC%88Tag-Plugins%EF%BC%89)

## label

{% label 这是红色 red %}

{% label 这是粉色 pink %}

{% label 这是橙色 orange %}

{% label 这是黄色 yellow %}

{% label 这是蓝色 blue %}

{% label 这是绿色 green %}

{% label 这是紫色 purple %}

{% label 这是灰色 %}

---

## note

{% note 'fab fa-cc-visa' flat %}
你是刷 Visa 还是 UnionPay
{% endnote %}
{% note blue 'fas fa-bullhorn' flat %}
2021年快到了....
{% endnote %}
{% note pink 'fas fa-car-crash' flat %}
小心开车 安全至上
{% endnote %}
{% note red 'fas fa-fan' flat%}
这是三片呢？还是四片？
{% endnote %}
{% note orange 'fas fa-battery-half' flat %}
你是刷 Visa 还是 UnionPay
{% endnote %}
{% note purple 'far fa-hand-scissors' flat %}
剪刀石头布
{% endnote %}
{% note green 'fab fa-internet-explorer' flat %}
前端最讨厌的浏览器
{% endnote %}

---

{% note flat %}
默认 提示块标签
{% endnote %}

{% note default flat %}
default 提示块标签
{% endnote %}

{% note primary flat %}
primary 提示块标签
{% endnote %}

{% note success flat %}
success 提示块标签
{% endnote %}

{% note info flat %}
info 提示块标签
{% endnote %}

{% note warning flat %}
warning 提示块标签
{% endnote %}

{% note danger flat %}
danger 提示块标签
{% endnote %}

---

## button

{% btn 'https://butterfly.js.org/',Butterfly,far fa-hand-point-right,larger %}
{% btn 'https://butterfly.js.org/',Butterfly,far fa-hand-point-right,blue larger %}
{% btn 'https://butterfly.js.org/',Butterfly,far fa-hand-point-right,pink larger %}
{% btn 'https://butterfly.js.org/',Butterfly,far fa-hand-point-right,red larger %}
{% btn 'https://butterfly.js.org/',Butterfly,far fa-hand-point-right,purple larger %}
{% btn 'https://butterfly.js.org/',Butterfly,far fa-hand-point-right,orange larger %}
{% btn 'https://butterfly.js.org/',Butterfly,far fa-hand-point-right,green larger %}

## tab

{% tabs test1 %}
<!-- tab -->
**This is Tab 1.**
<!-- endtab -->

<!-- tab -->
**This is Tab 2.**
<!-- endtab -->

<!-- tab -->
**This is Tab 3.**
<!-- endtab -->
{% endtabs %}

{% tabs test4 %}
<!-- tab 第一個Tab -->
**tab名字為第一個Tab**
<!-- endtab -->

<!-- tab @fab fa-apple-pay -->
**只有圖標 沒有Tab名字**
<!-- endtab -->

<!-- tab 炸彈@fas fa-bomb -->
**名字+icon**
<!-- endtab -->
{% endtabs %}

---

## hide toggle

{% hideToggle Butterfly安裝方法 %}
在你的博客根目錄裏

git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/Butterfly

如果想要安裝比較新的dev分支，可以

git clone -b dev https://github.com/jerryc127/hexo-theme-butterfly.git themes/Butterfly

{% endhideToggle %}

---

## timeline

{% timeline 2022 %}
<!-- timeline 01-02 -->
测试1
<!-- endtimeline -->
<!-- timeline 02-03 -->
测试2
<!-- endtimeline -->
{% endtimeline %}

---

{% timeline 2022,orange %}
<!-- timeline 01-02 -->
這是測試頁面
<!-- endtimeline -->
{% endtimeline %}

## flink
{% flink %}
- class_name: 網站
  class_desc: 值得推薦的網站
  link_list:
    - name: Youtube
      link: https://www.youtube.com/
      avatar: https://i.loli.net/2020/05/14/9ZkGg8v3azHJfM1.png
      descr: 視頻網站
    - name: Twitter
      link: https://twitter.com/
      avatar: https://i.loli.net/2020/05/14/5VyHPQqR6LWF39a.png
      descr: 社交分享平台
{% endflink %}

---

# html 用法

> 以下文本和修改自这个人的 `typora` 主题的[demo](https://typora-dyzj-theme.vercel.app/#ref-footnote-1)

<kbd>ctrl</kbd>键

可以通过设置 `background-color`属性控制背景色，如：`<font style="background-color:#8bc34a">`绿色小标签`</font>`

[跳转](#二级标题)至指定标题（锚点），也可以在任意位置通过 `<a name="锚点名" alt="none"> </a>`（为了方便编辑，typora会显示空标签或 `style="display:none"`的标签，但填充一个空格就可以被隐藏，在导出为HTML文件时，由于该款超链接样式有一个padding宽度，所以空链接还是会显示下划线，`alt="none"`用于避免该问题，如果自定义的锚点有文字说明，则不要使用 `alt="none"`）设定锚点，示例：[求点个赞呗](#star)

<a href="#" alt="null">无样式链接</a>，主要用于图片超链接，如：<a href="#" alt="null"><img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github"><img src="https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white"></a>

<ruby>Base<rp> (</rp><rt>top</rt><rp>) </rp></ruby>、<ruby>佐天泪子<rp> (</rp><rt>xiān qún kuáng mó</rt><rp>) </rp></ruby>、<ruby>超電磁砲<rp> (</rp><rt>レールガン</rt><rp>) </rp></ruby>


<audio controls="controls">
  <source src="/music/parsley.mp3" type="audio/mp3" />
</audio>

> 可以将 `<audio>`音频包裹在 `<center></center>`中居中显示

插入网易云的外链播放器（`<iframe>`，可嵌入油管等平台视频）：

<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="https://music.163.com/outchain/player?type=2&id=1836421270&auto=1&height=66"></iframe>

<details>
    <summary>折叠标签</summary>
    青青子衿，悠悠我心
</details>

[Emoji表情符号](https://www.webfx.com/tools/emoji-cheat-sheet/)：😄（`:smile:`），Decimal NCRs或Hexadecimal NCRs^[2]^编码也是受支持的，譬如“笑哭”：&#128514;（`&#128514;`）或&#x1F602;（`&#x1F602;`）

---

<video src="\video\club.mp4" controls="controls" style="max-width: 100%; display: block; margin-left: auto; margin-right: auto;">
your browser does not support the video tag
</video>

---

# Tag Plugins Plus

## link 
插件作者:
{% link Akilar, https://akilar.top/posts/615e2dec, https://npm.elemecdn.com/akilar-candyassets/image/siteicon/favicon.ico %}

## 行内文本样式 text
{% emp 着重号 %}
{% wavy 波浪线 %}

## 复选列表 checkbox
{% checkbox 纯文本测试 %}
{% checkbox checked, 支持简单的 [markdown](https://guides.github.com/features/mastering-markdown/) 语法 %}
{% checkbox red, 支持自定义颜色 %}
{% checkbox green checked, 绿色 + 默认选中 %}
{% checkbox yellow checked, 黄色 + 默认选中 %}
{% checkbox cyan checked, 青色 + 默认选中 %}
{% checkbox blue checked, 蓝色 + 默认选中 %}
{% checkbox plus green checked, 增加 %}
{% checkbox minus yellow checked, 减少 %}
{% checkbox times red checked, 叉 %}

## 单选列表 radio
{% radio 纯文本测试 %}
{% radio checked, 支持简单的 [markdown](https://guides.github.com/features/mastering-markdown/) 语法 %}
{% radio red, 支持自定义颜色 %}
{% radio green, 绿色 %}
{% radio yellow, 黄色 %}
{% radio cyan, 青色 %}
{% radio blue, 蓝色 %}

## audio / video
{% audio /music/parsley.mp3 %}

{% videos, 2 %}
{% video \video\club.mp4 %}
{% video \video\club.mp4 %}
{% video \video\club.mp4 %}
{% video \video\club.mp4 %}
{% endvideos %}

## sites
{% sitegroup %}
{% site satori_march, url=https://satorimarch.github.io, screenshot=\img\koishi1.jpg, avatar=\img\avatar1.jpg, description=这是说明1 %}
{% site satori_march, url=https://satorimarch.github.io, screenshot=\img\koishi1.jpg, avatar=\img\avatar1.jpg, description=这是说明2 %}
{% site satori_march, url=https://satorimarch.github.io, screenshot=\img\koishi1.jpg, avatar=\img\avatar1.jpg, description=这是说明3 %}

{% endsitegroup %}

---

[^1]: 这是脚注1

[^这是脚注]: 我是一个脚注
