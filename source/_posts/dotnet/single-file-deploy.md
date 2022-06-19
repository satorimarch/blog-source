---
title: .NET5以上WPF发布单个文件
tag:
  - c#
  - WPF
  - .NET
categories:
  - .NET
mathjax: false
sitemap: true
abbrlink: 51b37ab1
date: 2022-05-22 01:08:43
---

## 嵌入native libraries

最近要把WPF项目发布成含运行时(部署模式选择"独立")的单个exe, 想当然的在发布选项里勾选了"生成单个文件", 却仍生成了若干dll, 而且删除便无法运行, 似乎是native dlls. 搜索资料发现还需要在发布配置文件(`Properties\PublishProfiles\*.pubxml`)中加入一行代码:

```xml
<IncludeNativeLibrariesForSelfExtract>true</IncludeNativeLibrariesForSelfExtract>
```

加入后, 运行程序时会先提取出本地库到目录, 某种意义上不算真正的单文件

详情见此 -> [微软官方文档](https://docs.microsoft.com/en-us/dotnet/core/deploying/single-file/overview#output-differences-from-net-3x)

勾选生成单个文件已经在开头提过了, 后文再补充一些我能想到的其他未能生成单个文件的原因

## 更改文件保存方式
请在属性选项卡中将图片等文件的"生成操作"(build action)设置为 `资源`, "复制到输出目录"设置为 `不复制`, 代码中以路径或Pack URI来使用资源, ~~也可以用反射读取嵌入的资源~~

一些文本数值或者其他对象可以用 `.resx`, `.settings`, 或者自行实现序列化存到 `Appdata\Local` 或者参见[Configuration](https://docs.microsoft.com/en-us/dotnet/core/extensions/configuration) 等各种方式来存储

## 更改`.pdb` 生成选项
在项目设置中找到"调试符号", 选择"未发出任何符号"或者"嵌入到Dll/exe"
选择前者会导致无法Debug以及 `StackTrace` 无法输出异常的文件位置和行号, 因此不推荐使用
