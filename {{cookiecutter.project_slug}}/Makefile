help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

init:  ## 初始化python环境，并加载测试数据
	python3 -m venv env
	env/bin/python3 -m pip install -r requirements.txt
	env/bin/python3 src/manage.py migrate
	env/bin/python3 src/manage.py loaddata --format yaml fixtures.yaml
	@echo "初始化完成。现在你可以运行：make run 启动后端应用了。"

run: ## 运行后端服务
	env/bin/python3 src/manage.py runserver {{cookiecutter.port}}

prd: ## 生产环境运行
	nohup env/bin/python3 src/manage.py runserver {{cookiecutter.port}} 2>&1 &

upgrade: ## 升级后端服务代码
	env/bin/python3 -m pip install -r requirements.txt
	env/bin/python3 src/manage.py migrate
	env/bin/python3 src/manage.py loaddata --format yaml fixtures.yaml
	env/bin/python3 src/manage.py collectstatic --noinput

%:  ## cli命令
	env/bin/python3 "cli.py" $(MAKECMDGOALS)
