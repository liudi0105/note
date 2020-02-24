# conda source list

```text
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes

channels:   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/   - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ ssl_verify: true
channels:   - https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main/   - https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/free/   - https://mirrors.sjtug.sjtu.edu.cn/anaconda/cloud/conda-forge/ ssl_verify: true
channels:   - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/   - https://mirrors.ustc.edu.cn/anaconda/pkgs/free/   - https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/ ssl_verify: true
```

## set python package source list

```text
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/

linux
~/.pip/pip.conf

[global]
index-url = https://pypi.douban.com/simple/
[install]
trusted-host=pypi.douban.com

windows
~/pip/pip.ini
%APPDATA%/pip/pip.ini

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
