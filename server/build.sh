#!/bin/sh
set -e

APP_NAME="demoapp"
APP_PATH="/home/work/app/pythonapp"
#拷贝代码文件
cp -r ../server/* ${APP_PATH}/${APP_NAME}
cd ${APP_PATH}/${APP_NAME}

python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements1.txt
chmod 775 supervisor.conf
supervisorctl shutdown
supervisord -c supervisor.conf
echo "finished"
