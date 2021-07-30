#!/bin/sh
set -e

APP_NAME="demoapp"
APP_PATH="/home/work/app/pythonapp"
#拷贝代码文件
cp -r server APP_PATH/${APP_NAME}
cd APP_PATH/${APP_NAME}

python -m venv env
source env/bin/activate
pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple
pip3 install -r requirements1.txt
supervisord -c supervisor.conf