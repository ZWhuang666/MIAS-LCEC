默认情况下，pip使用官方源（PyPI）来下载和安装包。官方源的下载速度较慢的时候就需要替换源。

1. 使用命令行工具更换源

1.1 使用pip config命令：

     打开终端，输入以下命令来设置新的源：

     pip config set global.index-url 新源的url

1.2 使用-i参数：

     在使用pip命令时，可以通过`-i`参数来指定新的源。格式为：pip install -i 新源的url pacakge_name
     例如：
     pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ torchvision==0.16
     这个命令就是替换为中科大源来安装torchvision版本0.16。


2. 常用的pip源

2.1 中科大源（https://pypi.mirrors.ustc.edu.cn/simple/）

   中科大源是中国科学技术大学提供的镜像源，速度快且稳定。有时候速度快到飞起。

2.2 豆瓣源（https://pypi.douban.com/simple/）

   豆瓣源是豆瓣提供的镜像源，速度也比较快。

2.3 清华源（https://pypi.tuna.tsinghua.edu.cn/simple/）

   清华源是清华大学提供的镜像源，速度较快。

2.4 阿里云源（http://mirrors.aliyun.com/pypi/simple/）

   阿里云源是阿里云提供的镜像源，速度也比较快。


