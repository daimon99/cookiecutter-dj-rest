# {{cookiecutter.project_name}}

## 开发环境构建 与 系统设计说明

参考 

* docs/DESIGN.rst
* docs/CONTRIBUTING.rst

## FAQ

1. pycharm debug 失败

注意跟下代码。一般来讲如果代码中引入：eventlet.monkey_patch()，就会导致不能debug。
如 nameko 的 testing/pytest.py 中就有相应代码。注释掉后，pycharm 的 debug 就正常了。

2. 创建数据库

	* `postgres`

```sql
CREATE USER {{cookiecutter.project_slug}}_prd WITH PASSWORD '<password>'; 
CREATE DATABASE {{cookiecutter.project_slug}}_prd OWNER {{cookiecutter.project_slug}}_prd; 
```
