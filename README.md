# SEU-Health-system-auto-filling
东南大学一键填报每日健康系统。

利用python的selenium库，使用前，请安装Firefox和geckodriver，后者请放在path系统路径。
运行时，请在同一目录下新建文本文件"user.ini"，第一行设定用户名（一卡通号），第二行是密码（同一身份认证密码）。

理论上一些其他可做的工作：
- 定时自动填报
- 多人批量填报
- UI
- 更强的错误检测能力

但是考虑到其实作用并不大，所以没做。
考虑到开发者可能利用此程序窃取密码，所以给出源码不给exe，避免这种质疑的出现。
