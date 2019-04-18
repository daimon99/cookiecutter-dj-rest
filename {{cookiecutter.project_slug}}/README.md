# {{cookiecutter.project_slug}}

## 安装条件

* xxx

## 安装说明

* 构建运行环境

```
make init
```

* 代码升级

```
make upgrade
```

* 启动服务

```
make run
```


## FAQ

1. pycharm debug 失败

注意跟下代码。一般来讲如果代码中引入：eventlet.monkey_patch()，就会导致不能debug。
如 nameko 的 testing/pytest.py 中就有相应代码。注释掉后，pycharm 的 debug 就正常了。