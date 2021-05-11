# -*-coding:utf-8-*-
# @ Auth:zhao xy
# @ Time:2021/5/11 12:39
# @ File:user_sql.py

from sqlalchemy.orm import sessionmaker # 用以创建session类
from sqlalchemy import create_engine # 保存数据库连接信息

url = "mysql+mysqlconnector://root:zxy19981013@172.18.0.3:3306/test" # 数据库用户名密码地址端口及库名
engin = create_engine(url,pool_size=5)  # 数据库连接池对象个数
Session = sessionmaker(bind=engin) # 创建session类