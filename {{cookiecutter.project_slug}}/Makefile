help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

init:  ## 初始化python环境，并加载测试数据
	python3 -m venv env
	env/bin/python -m pip install -r requirements.txt
	env/bin/python src/manage.py migrate
	env/bin/python src/manage.py loaddata --format yaml fixtures.yaml
	@echo "初始化完成。现在你可以运行：make run 启动后端应用了。"

stop: ## 停止 make prd/ make run 启动的服务
	-lsof -i:{{cookiecutter.port}} | awk 'NR==2{print $$2}' | xargs kill
		
run: stop ## 运行后端服务(front)
	env/bin/python src/manage.py runserver {{cookiecutter.port}}

prd: stop ## 生产环境运行(backend)
	nohup env/bin/python src/manage.py runserver {{cookiecutter.port}} 2>&1 &

upgrade: ## 升级后端服务代码
	env/bin/python -m pip install -r requirements.txt
	env/bin/python src/manage.py migrate
	env/bin/python src/manage.py loaddata --format yaml fixtures.yaml
	env/bin/python src/manage.py collectstatic --noinput

dep: ## 部署服务到supervisor与nginx
	-sudo cp deploy/nginx/{{cookiecutter.project_slug}}_prd.conf /etc/nginx/conf.d/
	-sudo cp deploy/supervisor/{{cookiecutter.project_slug}}_prd.ini /etc/supervisord.d/

crontab: ## 安装 cron 定时任务
	cd src && ../env/bin/python manage.py installtasks

cloc: ## 代码量统计。请提前安装cloc(brew install cloc)
	cloc --exclude-dir="env,docs,logs,include,CMakeFiles,dist,static,theme,build,staticfiles" --exclude-ext="json,xml,yaml,yml,md" .

%:  ## cli命令
	env/bin/python "cli.py" $(MAKECMDGOALS)
