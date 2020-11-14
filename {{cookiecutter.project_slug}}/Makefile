help:           ## Show this help.
	# @fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'


init:  ## 初始化python环境，并加载测试数据
	python -m pip install -r requirements.txt
	python src/manage.py migrate
	python src/manage.py loaddata --format yaml fixtures.yaml
	@echo "初始化完成。现在你可以运行：make run 启动后端应用了。"

stop: ## 停止 make prd/ make run 启动的服务
	-lsof -i:{{cookiecutter.port}} | awk 'NR==2{print $$2}' | xargs kill

run: stop ## 运行后端服务(front)
	python src/manage.py runserver {{cookiecutter.port}}

prd: stop ## 生产环境运行(backend)
	nohup python src/manage.py runserver {{cookiecutter.port}} 2>&1 &

upgrade: ## 升级后端服务代码
	python -m pip install -r requirements.txt
	python src/manage.py migrate
	python src/manage.py loaddata --format yaml fixtures.yaml
	python src/manage.py collectstatic --noinput

dep: ## 部署服务到supervisor与nginx
	-sudo cp deploy/nginx/{{cookiecutter.project_slug}}_prd.conf /etc/nginx/conf.d/
	-sudo cp deploy/supervisor/{{cookiecutter.project_slug}}_prd.ini /etc/supervisord.d/

crontab: ## 安装 cron 定时任务
	cd src && python manage.py installtasks

cloc: ## 代码量统计。请提前安装cloc(brew install cloc)
	cloc --exclude-dir="env,docs,logs,include,CMakeFiles,dist,static,theme,build,staticfiles" --exclude-ext="json,xml,yaml,yml,md" .

docker-build: ## docker build
	docker build -f docker/Dockerfile -t ccr.ccs.tencentyun.com/tjhb/{{cookiecutter.project_name}}:latest .

docker-run: ## docker run
	if [ -f .env ]; then docker run --env-file=.env --rm -it -p {{cookiecutter.port}}:{{cookiecutter.port}} ccr.ccs.tencentyun.com/tjhb/{{cookiecutter.project_name}} ${CMD} ; \
	else docker run --rm -it -p {{cookiecutter.port}}:{{cookiecutter.port}} ccr.ccs.tencentyun.com/tjhb/{{cookiecutter.project_name}} ${CMD} ; fi

docker-release: test docker-test ## merge master to docker
	bumpversion patch
	git checkout -b docker origin/docker
	git merge master
	git checkout master

test: ## Smoke Test suit
	PYTHONPATH=./src pytest -m "smoke"

docker-test: ## test docker
	docker build -f ./docker/Dockerfile -t ccr.ccs.tencentyun.com/tjhb/{{cookiecutter.project_name}}:latest .

doc: ## 构建 doc 文档, 并查看
	cd docs && make open

epub: ## 构建 epub 模式文档
	cd docs && make epub && open -a finder _build/epub

pdf: ## 构建 pdf 文档
	cd docs && make pdf

doc-clean: ## 清理 doc 构建数据
	cd docs && make clean

CODE_DIR ?= .
test: ## test docker
	CODE_DIR=$(CODE_DIR) ./docker-entrypoint.sh runserver

%:  ## cli命令
	python "cli.py" $(MAKECMDGOALS)
