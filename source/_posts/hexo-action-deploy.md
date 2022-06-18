---
title: "git仓库嵌套导致github actions部署hexo博客失败"
tag:
  - Git
  - Github
  - hexo
categories:
  - [博客]
  - [Git]
mathjax: false
sitemap: true
abbrlink: 1524b8f2
date: 2022-05-29 20:18:42
---

# git submodule

按网上的教程配置github actions, 在 `hexo generate` 的时候无法解析文章里的 tag plugins(标签插件) 而是会报错. 我一开始还以为是插件没装上, 后来才意识到, 我的主题是直接在 `themes` 文件夹里 `git clone` 过来的, actions 中 clone 我的仓库是不包含这个主题的, 所以才报错. git 仓库嵌套使用后, 被嵌套的 git 仓库不能被外层 git 仓库检测到. 百度~~(其实是bing但我说习惯了)~~后发现 git 还有 submodule 这种东西, 刚好可以达到我们的目的.

首先要用 `git rm --cached` 删除原来的内层仓库, 不要直接删除, 否则外层可能会感知不到, 然后输入命令:

```gitbash
git submodule add -b [branch] [repository_url] [path]
```

例如:
```gitbash
git submodule add -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes\butterfly
```

正确运行之后除了拉取到的仓库应该还会在根目录多出一个 `.gitmodules` 文件. 如果出现问题想要删除 submodule 请用 `git submodule deinit [path]` 命令.

这之后直接 `git clone` 实际上并不会拉取到 submodule 中的代码, 应该在 `git clone` 命令中带上参数 `--recurse-submodules` 表示递归拉取所有子模块, 或者执行下面的命令:

```gitbash
git submodule init
git submodule update
```

言归正传, 对于 github actions 来说, 如果你用的是 `actions/checkout`, 只需要在 `with` 里加一行 `submodules: true` 或者 `submodules: recursive` 即可, 否则参照上文如何拉取子模块.

# deploy repo
改完后生成似乎没问题了, 但依然部署不上, 报错:

{% note danger %}
fatal: could not read Username for 'https://github.com'
{% endnote %}

将 `_config.yml` 中 `deploy` 的 `repo` 更换一下就行了([参见](https://github.com/hexojs/hexo/issues/2778)):

```yaml
deploy:
  type: git
  # repo: https://github.com/[yourgitname]/[yourgitname].github.io.git
  repo: git@github.com:[yourgitname]/[yourgitname].github.io.git
  branch: master
```

但在我的win10电脑能部署, github actions 却不行, 或许是 windows 和 Ubuntu linux 的差异吧, 也有可能是别的问题, 不太清楚, ~~反正解决了就行了~~.

# 更新时间错误
因为 `git clone` 后文件的修改时间实际上是 `clone` 的时间, 所以没在 `front-matter` 填写 `updated` 的文章的更新时间全都是 `clone` 的时间. 只要把文件的修改时间变为该文件最后 `commit` 的时间, 在生成之前加一行命令即可:

```bash
find source/_posts -name '*.md' | while read file; do touch -d "$(git log -1 --format="@%ct" "$file")" "$file"; done
```

{% note warning %}
一定要注意, 如果使用的是 `actions/checkout`, 要加上参数 `fetch-depth: 0` 来获取所有历史记录
{% endnote %}

参考链接:
[修复 CI 构建博客造成的更新时间错误](https://mrseawave.github.io/blogs/articles/2021/01/07/ci-hexo-update-time/)