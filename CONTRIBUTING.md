# 贡献指南

项目采用(缩短周期的)敏捷开发模式，依赖于pull-request-review机制实现，大致贡献流程如下：
1. 快速构建起一个可运行的空框架
2. 分为三个组同时对三个app(功能模块进行开发)，功能需求都组内自己提出，自己实现．
3. 每天进行多次Intergration(集成)，由各组的分支向master分支提PR，review时对无法修复的更新直接回滚．
4. 每天晚上进行一次release(发布)，review后由master分支merge到stable分支．

## 各项目角色的职责及操作指南

### 组长
组长主要负责代码仓库下某一分支(以下称为`B`)的开发与维护，操作流程为：
1. 提出功能需求，并在组内协作实现该需求．
2. 将组内代码`git commit`,`git push`到`B`分支.
3. 确认某一功能需求已实现后，发起一个从`B`分支到`Master`分支的PR
4. 在Code-reviewer通知整个项目已顺利完成一次Intergration后，发起一个从`Master`分支到`B`分支的PR,并直接选择`Ｍerage`,接下来将最新版本的代码分发给所有小组成员
5. 每天早上(即一次release后)，重复步骤4．

**注意**：
1. 组长对分支`B`负责，但应避免向`Master`或其他组的分支做任何写操作，不应向`Stable`分支做任何写操作
2. 由于Intergration会消耗一定时间，在该时间段组内的commit可能会在步骤4中产生conflict,参考解决方法：
 - 在Intergration期间不要开发，休息一会儿~~~
 - 手动解决conflict：Discard不必要的项目更改(i.e:`db.sqlite3`),然后在conflict处进行手动调整．
3. 参考组员注意事项

### 组员
组员主要参与代码仓库下某一分支(以下称为`B`)的开发，由组内协调开发方式

**注意**：
1. 组员不应向`Master`或其他组的分支做任何写操作，不应向`Stable`分支做任何写操作
2. 提交commit时，应关闭`python manage.py runserver`所创建的进程
3. 提交commit或PR时，应注明代码内容或实现的功能．如果该功能完全解决某个issue,请在commit message或PR message中tag这个issue，并关闭issue．如果只能部分修复某个issue，请在issue下指出你已完成的工作．
4. 提交commit时，不应全部提交，需要确认`db.sqlite3`,`*.pyc`,`001*.py`等文件保持ignore
5. 从master(或其他任何分支)下载好最新代码后，应运行
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
以部署生产环境和测试运行

6. 若部署生产环境时显示数据库中有table缺失，请使用
``` sh
python manage.py migrate --run-syncdb
```
来更新数据库
