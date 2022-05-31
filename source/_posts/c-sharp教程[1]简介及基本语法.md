---
title: 'C#基础教程[1] 简介及基本语法'
tags:
  - c#
categories:
  - [电子电路社]
  - [c#, c#教程]
cover: 'https://s6.jpg.cm/2021/11/28/LLO4yG.jpg'
mathjax: true
abbrlink: 38394
date: 2021-11-23 00:00:00
---

# 前言

本系列教程是为了我在学校社团课使用而写的，我尽量在简单起见的情况下保证严谨一些，但可能仍有些随意或不严谨的地方，更严谨的说法请去看微软官方文档。因为学校高一的信息课会学习 python，因此会与 python 的语法作一些对比，不过不懂也没关系。

感谢 [zbx1425](https://github.com/zbx1425) 大佬对于本系列教程的帮助

## 可能有用的网址

### 教程/文档：

[菜鸟教程](https://www.runoob.com/csharp/csharp-tutorial.html) 

[微软官网教程](https://docs.microsoft.com/zh-cn/learn/paths/csharp-first-steps/)

[微软官方文档](https://docs.microsoft.com/zh-CN/dotnet/csharp/)(如果有问题或者说的不清楚建议看英文原版)

### IDE：

IDE 即集成开发环境, 可以不严谨的理解为编写并运行代码所用的软件

[Visual Studio](https://visualstudio.microsoft.com/zh-hans/downloads/)：如果可以的话 `VS` 对于写 C# 必然是首选，不过体积较大，可能要占好几个GB

[Sharp Develop](https://sourceforge.net/projects/sharpdevelop/)：`VS` 中很多功能对于初学者没有必要，所以也可以用 `Sharp Devlop`，安装包仅十几MB

如果使用手机或者因为各种原因没安装 IDE 可以使用在线工具例如[这个]( http://www.dooccn.com/csharp/)

# 简介

{% note flat %}
以下内容来自[维基百科](https://zh.wikipedia.org/wiki/C%E2%99%AF), 随便看看就好
{% endnote %}

> C#是微软推出的一种基于.NET框架的、面向对象的高级编程语言。C#是一种由C和C++派生出来的面向对象的编程语言。它在继承C和C++强大功能的同时去掉了一些它们的复杂特性，使其成为C语言家族中的一种高效强大的编程语言。C#以.NET框架类库作为基础，拥有类似Visual Basic的快速开发能力。C#由安德斯·海尔斯伯格主持开发，微软在2000年发布了这种语言，希望借助这种语言来取代Java。

---

# 第一个 C# 程序

各位同学可能在课内学习过一点 python。以输出 `"hello world"` 作为初学者的第一个程序是计算机界的传统，这是一个能打印出 `"hello world"` 的 python 程序：

```python
print("hello world")
```

在真正上手写 C# 之前，我们先来看一个能实现同样功能的 C# 程序，来大致了解一下 C# 语言是怎样的：

{% note info flat %}
`//` 代表开始单行注释, `//` 后面的内容都是解释代码意思的文字, 与程序的运行无关
{% endnote %}

```csharp
using System;

namespace ConsoleApp // ConsoleApp命名空间(namespace)
{
    class Program // Program类(class)
    {
        static void Main(string[] args) // Main函数
        {
            Console.WriteLine("Hello World!"); // 输出语句
        }
    }
}
```

## 程序结构

先不要被这么多代码吓到, 我们来分析一下:
- 比起功能相同的 python 程序，内容多多了
- 不过真正进行"打印文字"这一操作的代码也只有一行(含有 `WriteLine` 的那行)
- 代码似乎被大括号分成了很多块

大括号的包含关系是 C# 的一个特点。上面的代码有一个命名空间(`namespace`)，里面包含着一个类（`class`），类里面又包含着一个"主函数[^1]"（`Main`），主函数里装着真正的用来打印文字的代码。作为初学者，各位暂时不需要理解什么是函数、类、命名空间，先把它当作模板照着写就好了，下面简单介绍一下他们的关系。

举个例子来说，就像这样：

```中文
学校 南开中学
{
    学生 小明
    {
        参加考试(考试地点) {
            考试过程
        }
    }
}
```

你可能只想描述小明考试的过程，但是 C# 里就得一笔带过地稍微描述下小明这人和它的学校。之所以这么麻烦，是因为 C# 规定，执行的内容必须得被包含在函数里，函数必须得被包含在类里，类又必须得被包含在命名空间里...所以咱的代码就给包成了个三明治，不像 python 直接开始写就行。大家可能会觉得，这样比功能相同的 python 代码要繁琐很多，这样的设计看似没有必要，但实际上在大点的项目里便能展现出它的优势

不过还是那句话，外面的包装是我们初学者不需太关心的，大家目前只需要注意一下`Main` 函数里的内容。我们的程序总会从 `Main` 函数开始执行。所以我们来集中精力看这一行实际干活的代码。

在语句 `Console.WriteLine("Hello World!");` 中，`Console` 其实也是一个类，而 `WriteLine()` 则为 `Console` 类中的一个函数，中间的 `.` 表示访问 `Console` 类中的成员[^2]，此处访问的即为该类中的 `WriteLine()` 函数。

`Console`是控制台的意思，也就是运行程序时看到的那个黑窗口；而 "Console" "." "WriteLine" 就是调用 "控制台" "里面的" 叫做 "写一行字" 的函数。大家目前只需要对类的事情稍微留一些印象即可，不用过多关注。

{% note warning %}
函数的后面必须有括号，即使它没有参数。例如调用 `Console.WriteLine();` 会输出空行
{% endnote %}

因为我们目前只看主函数部分，所以后面会省略主函数之外的内容, 将上面那段代码写成如下的形式[^3]：

```csharp
Console.WriteLine("Hello World!"); // 输出语句
```

如果你把上面的 `Console` 改为 `console`, 你会在“输出”区域看到一条错误消息：

{% note danger %}
error CS0103: The name 'console' does not exist in the current context
{% endnote %}

翻译一下就是 `console` 在当前上下文中不存在, 也就是说, 编译器不认识 `console`, 只认识 `Console`

{% note warning %}
不要把单词拼错（英语不好的同学可能有些困难，但是请尽量），拼错单词英语考试里会没分，C# 里会编译失败

C# 是区分大小写的！请注意各个单词的大小写，大小写搞错也会导致编译错误。一般来说`namespace`, `class`等“关键字”是全小写，函数是各单词首字母大写。
{% endnote %}

 - 一些 IDE 会替你查找潜在错误, 然后在出错的地方加上红色波浪线, 你可以将鼠标光标移上去来查看详细信息(有时候出现的红色波浪线只是因为你代码没打完)
 - 没有红色波浪线的时候, 将光标移到函数或类上可以查看它的定义和注释来快速理解它的用法(函数和类的定义以后会讲)~~可惜SharpDevelop只有定义没有注释~~

# 基本语法

## 数据类型

在学习初期我们会见到的值类型如下:

| 类型   | 描述                | 范围              | 默认值  |
| ------ | ------------------- | ----------------- | ------- |
| bool   | 布尔值             | `True` 或 `False` | `False` |
| double | 浮点型   | 非常大            | 0.0D    |
| int    | 整型 | 约±20亿           | 0       |
| string | 字符串 (文本)      | -                | 空(null)  |

 - `bool` 即布尔值, 参与逻辑运算, 值只能是 `True` 或 `False` 的其中一个
 - `int` 即整数, 一般表示整数用 `int` 即可
 - `double` 类型可以不严谨的认为是小数
 - 字符串(`string` 类型)其实我们已经用过了, 用双引号括起来的便是字符串, 例如 `"Hello World!"` (注意不能是单引号)

请大家注意 `string` 类型的 `"25"` 和 `int` 类型的 `25` 的区别: 前者是一个字符串, 与 `"abc"` 本质上没有区别, 因此 `"25"` 无法参与实数运算, 也就是不能写 `"25" * 10`, 如果需要则先转换成 `int` 类型

将其他三种类型转换为`double`的代码: `Convert.ToDouble(x)`, 其返回值的类型为 `Double`, 其中的x为调用`ToDouble`函数的参数; 而返回值顾名思义, 就是调用的函数运行后返回的结果, `WriteLine` 没有返回值. 与 `ToDouble()` 同理:
- 转换为 `string` 的代码为: `Convert.ToString(x)`
- 转换为 `int` 的代码为: `Convert.ToInt32(x)` (只有这个需要写为 `Int32` 比较特殊, 不过并不需要特殊记忆, 因为 IDE 的代码补全会有提示)

类型转换的用法例如: (代码中的 `string a` `int b` 等的用法会在下面介绍)

```csharp
string a = "55";
int b = Convert.ToInt32(a);
Console.WriteLine(b * 10);
```

输出结果为:
{% note default flat %}
550
{% endnote %}

{% note info %}
在初学阶段, 即使你已经看明白了代码的意思, 也建议不看文章手动输入一遍本文中的例子. 一是为了加深记忆, 二是有时看懂了可能只是有些问题没有发现
{% endnote %}

大家可能会疑惑 `a = "55"` 等地方为什么要加空格. 只是为了规范, 这些空格并不会影响程序的运行, 只是为了读起来方便. 实际上所有那种不影响语义的空格和换行都可以去掉, 把上面的代码写成这样:

```csharp
string a="55";int b=Convert.ToInt32(a);Console.WriteLine(b*10);
```

但这样看起来就很难懂了, 建议别这么写. 注意 `int` 和 `b` 之间的空格不能省略成`intb`(显然把两个词连成一个词会影响语义)

对于多数IDE(快捷键可能有些许不同), 当你在输入内容的时候, 你很可能会看到代码补全的候选列表:
 - 在显示候选列表时：按Tab可以采纳选中的建议，按↑↓可以浏览不同的建议，如果不想要这些建议可以按Esc退出候选列表
 - 在没有显示候选列表时：按 `Tab` 可以插入四个空格，按 `Shift+Tab` 可以去掉四个空格

## 变量的声明和定义

如果需要处理代码里没有的数据，就需要声明一个变量。刚刚其实已经用过变量了。一个"变量"是在其生存期内可以更改其值的数据项。可以使用变量来临时存储稍后要在代码中使用的值。

在 python 中, 声明变量前不需说明类型, 例如:

```python
a = 5
abc = "abc"
```

但在 C# 中需要显示指明类型应写为这样:

```csharp
int a = 5;
string abc = "apple";
```

你可以用逗号来声明多个相同类型的变量:
```csharp
int a = 5, b = 10, c = 20;
```

C# 中一个变量的类型在声明时已经固定, 不能赋其他类型的值, 在 python 中, 这样的代码是合法的:

```python
a = 5
a = "abc" // 注意是给同一个变量 a 赋值
```

但在 C# 中会报错:

```csharp
int a = 5;
a = "55";
```

{% note danger flat %}
错误	CS0029	无法将类型“string”隐式转换为“int”
{% endnote %}

"隐式类型转换"指的是你没有显式说明, 而是自动进行的类型转换. 一般来说, 只有转换之后 {% emp 肯定不会 %} 造成数据损失或者错误的类型之间才能进行隐式类型转换(注意, 是所有这类型的数据都不会出现问题才能隐式转换, 举特例是不行的). 例如:
 - `string` {% emp 不能 %} 隐式转换为 `int`, 因为有像 `"abc"` 这类字符串; 
 - `int` 可以隐式转换为 `string`
 - `double` {% emp 不能 %} 隐式转换为 `int`, 因为会丢失小数部分
 - `int` 可以隐式转换为 `double`

为了将上面的 `string` 类型的 `"55"` 转换为 `int` 类型的 `55`, 可以考虑使用上面提过的 `Convert.ToInt32()` 函数, 例如:

```csharp
int a = Convert.ToInt32("55");
Console.WriteLine(a);
```

关于类型转换的更多内容可以参考我的另一篇文章[c#中的数据类型转换](https://satorimarch.github.io/posts/19004/)

## 标准输入输出

C# 中的函数名一般比较直观易懂，~~不像某语言中乍一看不知所云的 `atoi`~~。例如：

```csharp
Console.Write("hello "); // 输出到控制台(无换行)
Console.WriteLine("world"); // 输出到控制台(有换行)
```

上面的代码输出如下:
{% note default flat %}
hello world
{% endnote %}

与 `WriteLine()` 相对应, 从标准输入流读入下一行字符并存储为字符串的函数叫 `ReadLine()`

```csharp
string a;
a = Console.ReadLine();
Console.WriteLine(a);
```

函数的嵌套：

```csharp
int a = Convert.ToInt32(Console.ReadLine());
```

类比数学中的复合函数 $f(g(x))$, 嵌套函数的应从内往外开始运行, 也就是先执行 `Console.ReadLine()`, 再把该函数的返回值代入到 `Convert.ToInt32()` 中

### WriteLine()的格式化 (format)
如果想要依次输出 abc 的值, 并在前面输出变量名和等号, 例如 `a=1`, 以我们之前学的内容应该这么写:
```csharp
int a = 5, b = 15, c = 10;
Console.WriteLine("a=" + a + " b=" + b + " c=" + c); 
```

上面的代码中 abc 分别被隐式转换成字符串然后进行字符串串联. 这样很是麻烦还不方便阅读, 有没有更简单的方法呢?~~既然我这么说了~~, 当然是有的:

```csharp
int a = 1, b = 2, c = 3;
Console.WriteLine("a={0} b={1} c={2}", a, b, c);
```

其中 `{n}` 表示字符串后面的第 `n` 个对象(从 `0` 开始计数)
我们管 `{n}` 叫做占位符, 你可以理解为它把对应的值的位置给占了, 而在运行的时候会把后面的值放到占位符的位置上

从 `C#6.0` 开始还有一种更方便阅读的语法, 在字符串前面加上 `$` 就可以直接在大括号里写变量名:
```csharp
Console.WriteLine($"a={a} b={b} c={c}");
```

不过 SharpDevelop 只支持到 `C#5.0`(

## 运算符
C# 中的赋值/算术/比较运算符与 python 基本相同, 但也仍有很多差别。

### 赋值运算符

大家看到 `a = 5` 的时候可能并不会想太多, `a` 等于 `5` 感觉很合理. 但实际上, `=` 并不是等于的意思, 例如 `a = a + 1;` 语句看起来在数学上恒不成立, 但在代码中是合法的. 这是因为 `=` 的学名叫做赋值运算符, 他表达的意思实际上是"计算出右侧的值, 然后把右侧的值赋给左边的变量". 假如 `int` 变量 `a` 原本为 `5`, 在 `a = a + 1` 中, 会先计算出右边的数值 `a + 1` 即为 `6`, 然后将 `6` 赋给左边的变量 `a`, 故该语句运行之后 `a` 的值为 `6`  

```csharp
int a = 5;
a = a + 10;
Console.WriteLine(a); // 输出15
```

由于 `a = a + ?` 的使用率很高, 所以又有了一种运算符为 `+=`, `a += 5` 相当于 `a = a + 5`, 同理还有 `-=` 等运算符

另外, C# 中还有 `++` 运算符, `a++` 基本相当于 `a += 1` 也就是 `a = a + 1`, `--`运算符同理. 你也可以把 `++` 写到前面如 `++a`. 但是`a++` 与 `++a` 作为复合表达式的时候有些区别, 因此在没弄清楚前不要写诸如 `b = a++;` 这种式子

### 算术运算符

```csharp
int a = 5, b = 10;
Console.WriteLine(a + b); // 输出 15
Console.WriteLine(a - b); // 输出 -5
Console.WriteLine(a * b); // 输出 50
Console.WriteLine(a / b); // 输出 0
```

大家请注意最后 `a/b` 的结果: `5/10` 返回的结果竟然是 `0`

那让我们再试一下这段代码：
```csharp
int a = 5;
double b = 10.0;

Console.WriteLine(a / b); // 输出 0.5
```

这样写输出的结果就变成了 `0.5`

{% note danger flat %}
C# 中的 `/` 在两个操作数中至少有一个是浮点数时才会为实数除法, 否则会向 `0` 取整, 例如: `-5/2` 的结果是 `-2`, `-5/2.0` 的结果是 `-2.5`
{% endnote %}

### 例 1-1 (a+b)×c (洛谷B2008)

读入 3 个整数 a,b,c, 输出表达式 $(a+b) \times c$  的值。

示例代码:

```csharp
int a = Convert.ToInt32(Console.ReadLine());
int b = Convert.ToInt32(Console.ReadLine());
int c = Convert.ToInt32(Console.ReadLine());
int answer = (a + b) * c;
Console.WriteLine(answer);
```

前三行的读入看起来有些繁琐, 第四节会学到简单点的写法. 另外, 多数 IDE 会有复制当前行的快捷键, 可以去设置里找一下. 你也可以省略中间变量 `answer`, 将最后两行合并写成:

```csharp
Console.WriteLine((a + b) * c);
```

`string` 类型也可以进行 `+` 操作, 例如 `"abc" + "def"` 会得到 `"abcdef"`

### 比较运算符

```csharp
int a = 5, b = 10;
Console.WriteLine(a == b); //输出 False
Console.WriteLine(a != b); //输出 True
Console.WriteLine(a >= b); //输出 False
Console.WriteLine(a <= b); //输出 True
Console.WriteLine(a > b);  //输出 False
Console.WriteLine(a < b);  //输出 True
```

那让我们试试下面的代码:

```csharp
Console.WriteLine(7 < 5 < 10);
```

与我们的预期相反, 这段代码报错了:
{% note danger flat %}
CS0019	运算符“<”无法应用于“bool”和“int”类型的操作数
{% endnote %}

这是因为编译器会把表达式 `7 < 5 < 10` 理解为 `(7 < 5) < 5`, 而`7 < 5` 会返回 `bool` 类型的 `False`, 而在 C# 中 `bool` 类型不能直接与 `int` 类型进行比较, 也不能隐式转换成 `int` 类型, 因此这个表达式会报错

{% note danger flat %}
不能把表达式写成形如 `a <= x <= b` 的形式, 应该写为 `a <= x && x <= b` （ `&&` 表示 "并且", 将在后面的逻辑运算符进行讲解）
{% endnote %}

另外, C# 中没有 python 中的 `**` 等运算符, 如果想求出 $a^b$, 请使用 `Math.Pow(a, b);` 函数

### 逻辑运算符

C# 中的逻辑运算符如下(已知 A = true, B = false):

| 运算符       | 描述                                                         | 实例                      | python |
| :----- | :----------------------------------------------------------- | :---------------- | ------ |
| &&           | 称为逻辑与运算符。如果两个操作数都非零，则条件为真。         | (A && B) 为假。           | and    |
| &#124;&#124; | 称为逻辑或运算符。如果两个操作数中有任意一个非零，则条件为真。 | (A &#124;&#124; B) 为真。 | or     |
| !            | 称为逻辑非运算符。用来逆转操作数的逻辑状态。如果条件为真则变为假。 | !(A && B) 为真。          | not    |

```csharp
bool a = true, b = true, c = false;
Console.WriteLine(a && b); //输出 True
Console.WriteLine(a && c); //输出 False
Console.WriteLine(a || b); //输出 True
Console.WriteLine(a || c); //输出 True
Console.WriteLine(!a);     //输出 False
Console.WriteLine(!c);     //输出 True
```

## `if()`语句

`if()` 语句的条件要在小括号里, 如果条件表达式为 `true` 的时候执行的语句在大括号里(或者说大括号包裹的部分为一个代码块, 执行整个代码块), 例如:

```csharp
int score = 0;
if(score == 0) {
    Console.WriteLine("我爆零了");
}
```

`else` 中的语句只有在对应的 `if` 的条件不满足的时候才会执行, 例如:

```csharp
int score = 0;
if(score == 0) {
    Console.WriteLine("我爆零了");
} 
else { // 有些人会习惯把 else 和上一行的 } 写到一行
    Console.WriteLine("我没爆零");
}
```

注意体会下面两段代码的区别:

1. 代码1, 这段代码相当于三选一:

```csharp
if(a) {
    // a 为 true 时运行
} 
else if(b) { // 注意这行多一个else
    // a 为 false 且 b 为 true 时运行
} 
else {
    // a,b 都为 false 时运行
}
```

2. 代码2, 注意这时后两个分支与 `a` 无关

```csharp
if(a) {
    // a 为 true 时运行
}  
// 实际运用时这行可以加个空行防止误解
if(b) {
    // b 为 true 时运行, 与 a 无关
} 
else {
    // b 为 false 时运行, 与 a 无关
}
```


### 例题 1-2 判断数正负(洛谷B2035)

给定一个整数 `N`，判断其正负。如果 $N>0$, 输出 `positive` ; 如果 $N=0$, 输出 `zero` ; 如果 $N<0$, 输出 `negative`。

```csharp
int n = Convert.ToInt32(Console.ReadLine());
if(n > 0) {
    Console.WriteLine("positive");
}
else if(n == 0) {
    Console.WriteLine("zero");
}
if(n < 0) {
    Console.WriteLine("negative");
}
```

因为 `n` 的三种取值是互斥的所以这里也可以这么写(不推荐):

```csharp
int n = Convert.ToInt32(Console.ReadLine());
if(n > 0) {
    Console.WriteLine("positive");
} 
if(n == 0) {
    Console.WriteLine("zero");
} 
else {
    Console.WriteLine("negative");
}
```

# 练习:
如果你觉得读入麻烦那么改成声明变量时初始化(如`int a = 5;`)也可以, 但请确保你会读入一行字符串并转换为整数

## 1-1 圆柱体的表面积

给出圆柱体的底面半径 $r$ 和 高 $h$, 分两行依次输出该圆柱体的侧面积和底面面积

## 1-2 直角三角形

已知三条边的长度(分三行给出), 判断是否能围成直角三角形, 若是则输出 `yes`, 否则输出 `no`

### 1-2-2

判断条件改为: 若为直角三角形输出 `yes`, 否则若能够构成三角形输出 `no`, 不能构成三角形输出 `not a triangle`

## 1-3 三排序

输入三个整数, 按从小到大排序后输出

### 挑战：
本题只使用3个 `if` 语句便可完成任务

## 1-4 一元二次方程
依次给出一元二次方程的a,b,c(均为整数, $a\neq 0$), 利用求根公式求一元二次方程实数根, 保留两位小数。有两实根时先输出更小的，一实根时输出那一个根，无实根时输出 `"No Answer"`

提示: 

- 使用 `Console.WriteLine("{0:F2}", 0.125);` 来对 `0.125` 保留 `2` 位小数, 其中 `F2` 的 `2` 表示两位
- 使用 `Math.Sqrt(a)` 来 求出 $\sqrt a$

---
# 练习参考代码
## 1-1 圆柱体的表面积
```csharp
int r = Convert.ToInt32(Console.ReadLine());
int h = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(Math.PI * r * r);
Console.WriteLine(2 * Math.PI * r * h);
```

## 1-2 直角三角形
```csharp
int a = Convert.ToInt32(Console.ReadLine());
int b = Convert.ToInt32(Console.ReadLine());
int c = Convert.ToInt32(Console.ReadLine());

if(a*a == b*b + c*c || b*b == a*a + c*c || c*c == a*a + b*b) {
    Console.WriteLine("yes");
} 
else {
    Console.WriteLine("no");
}
```

{% note info flat %}
如果你不知道哪个运算符的优先级比较高, 那就多加括号
{% endnote %}

### 1-2-2

```csharp
// 省略输入
if (a + b <= c || a + c <= b || b + c <= a) {
    Console.WriteLine("not a triangle");
} 
else {
    if (a*a == b*b + c*c || b*b == a*a + c*c || c*c == a*a + b*b) {
        Console.WriteLine("yes");
    }
    else {
        Console.WriteLine("no");
    }
}	
```

## 1-3 三排序

```csharp
// 省略输入

if(a > b){
    int temp = a;
    a = b;
    b = temp;
}
if(a > c){
    int temp = a;
    a = c;
    c = temp;
}
if(b > c){
    int temp = b;
    b = c;
    c = temp;
}

Console.WriteLine("{0}\n{1}\n{2}", a, b, c);
```

## 1-4 一元二次方程

```csharp
// 省略输入
double delta = b * b - 4 * a * c;

if(delta < 0) {
Console.WriteLine("No Answer");
}
else {
Console.WriteLine("{0:F2}", (- b - Math.Sqrt(delta))/2/a);
}

if(delta > 0) {
Console.WriteLine("{0:F2}", (- b + Math.Sqrt(delta))/2/a);
}
```

---

[^1]: C# 中的函数称作方法, 但出于简单起见以后全部称为函数
[^2]: 其学名为成员访问运算符
[^3]: 实际上这么写在 C#10 或者前面加上 `using System;` 在 C#9.0 中是合法的, 但不推荐初学者这么写
