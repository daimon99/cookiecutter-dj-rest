help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

init:  ## 初始化python环境，并加载测试数据
	python3 -m venv env
	env/bin/python3 -m pip install -r requirements.txt
	env/bin/python3 src/manage.py migrate
	env/bin/python3 src/manage.py loaddata --format yaml fixtures.yaml
	@echo "初始化完成。现在你可以运行：make run 启动后端应用了。"

stop: ## 停止 make prd/ make run 启动的服务
	-lsof -i:9074 | awk 'NR==2{print $$2}' | xargs kill
		
run: stop ## 运行后端服务(front)
	env/bin/python3 src/manage.py runserver {{cookiecutter.port}}

prd: stop ## 生产环境运行(backend)
	nohup env/bin/python3 src/manage.py runserver {{cookiecutter.port}} 2>&1 &

upgrade: ## 升级后端服务代码
	env/bin/python3 -m pip install -r requirements.txt
	env/bin/python3 src/manage.py migrate
	env/bin/python3 src/manage.py loaddata --format yaml fixtures.yaml
	env/bin/python3 src/manage.py collectstatic --noinput

%:  ## cli命令
	env/bin/python3 "cli.py" $(MAKECMDGOALS)
