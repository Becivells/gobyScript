# goby EXP 辅助工具



`goby-cmd` 的图形界面测试太麻烦，命令行测试poc的参数太长，也太麻烦，提交的时候需要按照一定的格式。附带测试的案例。此工具提供了代码格式化(需要安装[go](https://studygolang.com/dl) 并且设置环境变量)，代码检查(需要安装[golangci](https://golangci-lint.run/usage/install/#local-installation)), 还有测试。

## 示例

### 最简模式

目录下只有一个go文件。文件末尾带有目标

```
├── pocfile.yaml
├── pocfile.go
├── README.md
```

`pocfile.go`

```
.
.
.
			}
			return expResult
		},
	))
}

// http://target:port
```

#### 测试poc

```shell
gobyexp --poc
```

#### 测试exp

```shell
gobyexp --exp
```

目录下多个文件可以使用 `-t` 参数指定其中一个

### 普通模式

#### 生成 `cve` poc

`goby-cmd`

```
goby-cmd -mode genpoc -CVEID CVE-2020-15505 -exportFile test.go
```

`gobyexp`

```
 gobyexp -g -c CVE_2020-13167 -e Netsweeper_webAdmin_RCE_CVE_2020-13167.go
```

#### 测试 poc

`goby-cmd`

```shell
goby-cmd -mode runpoc -target http://target:port -pocFile pocfile.go -operation scan
```

`gobyexp`

```shell
gobyexp -u http://target:port -t pocfile.go --poc 
```

#### 测试 exp

`goby-cmd`

```shell
goby-cmd -mode runpoc -target http://target:port -pocFile pocfile.go -params {"cmd":"whoami"} -operation exploit
```

`gobyexp`

```shell
gobyexp -u http://target:port -t pocfile.go --poc
```

#### 打印相关命令

```
gobyexp -u http://target:port -t pocfile.go  --poc --test
gobyexp -u http://target:port -t pocfile.go  --exp --test
```

### 格式化代码和检查

```
gobyexp -u http://target:port -t pocfile.go  --poc --test
```

如果不需要代码检查和格式化可以使用 `--nolint --nofmt ` 

## 环境变量

如果有环境变量则按照环境变量来

```
godserver   # 暂无用途
goby_params # 用于exp执行的时候传值
goby_proxy  # 用于获取cve信息时候的代理地址
```

## 注意事项
编写时请加入`//nolint`
```shell script
ExpManager.AddExploit(NewExploit( //nolint
```


```shell script
usage: gobyexp.py [-h] [--nolint] [--nofmt] [--poc | --exp] [--test] [-u URL] [-t TEMPLATE] [-p PARAMS] [-g] [-c CVEID] [-e EXPORTFILE] [--proxy PROXY]

goby-cmd poc fast test you can set env export goby_params='{"cmd":"whoami"}' or export goby_proxy="http://127.0.0.1:8080"

optional arguments:
  -h, --help            show this help message and exit
  --nolint              golangci-lint check default true
  --nofmt               gofmt code

genpoc:
  genpoc template from cveid

  -g, --genpoc          genpoc
  -c CVEID, --cveid CVEID
                        test url
  -e EXPORTFILE, --exportFile EXPORTFILE
                        test url
  --proxy PROXY         proxy with cve search default None

poc/exp:
  test poc or exp

  --poc                 poc mode
  --exp                 exp mode
  --test                only print command and not execute
  -u URL, --url URL     test target
  -t TEMPLATE, --template TEMPLATE
                        goby exp template
  -p PARAMS, --params PARAMS
                        default '{"cmd":"whoami"}'

```