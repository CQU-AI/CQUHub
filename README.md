# CQUHub

本项目是我们开发小组的django练手项目，基本实现了论坛的功能，并仍存在一些可以优化的地方．

本项目旨在为重庆大学的师生提供一个聊天交友、信息发布、学术交流的在线Web平台，可附带商业营销、广告宣传等功能，其定位为一个重庆大学的校园论坛，基本上涵盖有市面上常见论坛的常用功能，例如登录已有账号或注册为新用户、发布帖子和回复帖子等。重庆大学以致其他学校的广大师生，以及校园内部或周边的商业人员均能注册为该论坛的用户，并通过该论坛实现自己聊天交友、发布信息、学术交流等学习和生活需求，以及商业营销、广告宣传等商业需求。此外，本项目还添加了一些社会性论坛所不具有的附加功能，旨在提升论坛的多样性和趣味性，能更好地满足高校师生和商业人员的需求，提高用户友好性。

## 使用方式
### 测试
我们在本项目中通常使用脚本来快速启动
 - linux/macos: 在终端中运行`chmod +x go && ./go`
 - windows: 在终端或cmd中运行`./wgo.bat`　

**注意**:　在`DEBUG=True`时，注册时不会发送验证邮件，而会在终端显示验证码

### 生产
直接使用于生产时，请按照以下步骤来完成部署:
1. 修改论坛标题和背景（可以通过搜索"cqu"来批量替换标题，背景则位于`staticfiles\main.css`）
1. 修改`user\sender.py`中的`        sender_mail`,`receiver`,`mail_title`,`  mail_content`等验证邮件的相关配置，并将邮箱密码写入`my_project\settings.py`中的`MAIL_PSW`．
1. 修改`my_project\settings.py`中的`SECRET_KEY`,`MAIL_PSW`,`ALLOWED_HOSTS`,并将`DEBUG`置为False．
1. 根据服务器具体情况，参考`.\go`中的指令来启动网站

## 贡献者
- [0xSeanll](https://github.com/0xSeanll)
- [1hunter0](https://github.com/1hunter0)
- [Micheal-Hu](https://github.com/Micheal-Hu)
- [Musenming](https://github.com/Musenming)
- [Starfish666](https://github.com/Starfish666)
- [hzj]()
- [iiint](https://github.com/iiint)
- [jbw]()
- [loopyme](https://github.com/loopyme)
- [reBiocoder](https://github.com/reBiocoder)
- [tanrenxuan](https://github.com/tanrenxuan)
- [zl]()
- [zrb1234](https://github.com/zrb1234)

需要特别指出的是: **排名不分先后**，部分贡献者没有Github贡献记录或帐号(已在commit message中指出)，其中reBiocoder大佬在本项目开发前期完成了大量的工作，后期loopyme，0xSeanll，1hunter0，iiint分别对项目整体,用户,删发帖,帖子的组织相关功能负责．

## 协议
本项目开源遵循[MIT](https://github.com/loopyme/CQUHub/blob/master/LICENSE)协议，欢迎fork或提issue
