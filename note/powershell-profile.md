# Powershell 配置文件

vim \$PROFILE

```powershell
if (!(Test-Path -Path $PROFILE )) {
  New-Item -Type File -Path $PROFILE -Force
}

Set-PSReadlineOption -EditMode Emacs

function go() {
  if ($args.Count -eq 1) {
    switch ($args.Get(0)) {
      128 { ssh root@129.28.148.128 }
      67 { ssh root@47.100.254.67 }
      Default {
        "未识别的地址"
      }
    }
  } else {
    "请输入地址"
  }
}
```
