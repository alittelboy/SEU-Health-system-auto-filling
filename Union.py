import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("http://ehall.seu.edu.cn/new/index.html")
with open("user.ini",'r',encoding='gbk') as f1:
    ini = f1.readlines()

#用文本文件"user.ini"设定用户名和密码
user = ini[0]
psw = ini[1]

js_health = """

$('div[data-action="add"]').click();
var flag = false;

var interval = setInterval(() => {
    if(!flag && $('input[name="DZ_JSDTCJTW"]')) {
        flag = true;
        $('input[name="DZ_JSDTCJTW"]').val('36.5');
        $('#save').click();
        $('.bh-dialog-btnContainerBox').children()[0].click()
        clearInterval(interval);
    }
}, 3000);
"""
js_enther = """
$('div[data-action="add"]').click();
var flag = false;
Date.prototype.Format = function(fmt)   
{   
  var o = {   
    "M+" : this.getMonth()+1,                 //月份   
    "d+" : this.getDate(),                    //日   
    "h+" : this.getHours(),                   //小时   
    "m+" : this.getMinutes(),                 //分   
    "s+" : this.getSeconds(),                 //秒   
    "q+" : Math.floor((this.getMonth()+3)/3), //季度   
    "S"  : this.getMilliseconds()             //毫秒   
  };   
  if(/(y+)/.test(fmt))   
    fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));   
  for(var k in o)   
    if(new RegExp("("+ k +")").test(fmt))   
  fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));   
  return fmt;   
}

var interval = setInterval(() => {
    if(!flag && $('div[data-name="SFFHFHYQ"] .jqx-dropdownlist-content')) {

        flag = true;
        var curDate = new Date();
        var date = new Date((curDate/1000+86400)*1000);
        var dateformat = date.Format('yyyy-MM-dd')
        var dateStart = dateformat + " 08:51:00";
        var dateEnd = dateformat + " 21:51:00";

        $('div[data-name="SFFHFHYQ"] .jqx-dropdownlist-content').html('是');
        $('div[data-name="SFFHFHYQ"] input').val('1');

        $('div[data-name="NFZHGRFH"] .jqx-dropdownlist-content').html('是');
        $('div[data-name="NFZHGRFH"] input').val('1');

        $('div[data-name="SFYZNJJJGL"] .jqx-dropdownlist-content').html('是');
        $('div[data-name="SFYZNJJJGL"] input').val('1');

        $('div[data-name="DZ_JRSTZK"] .jqx-dropdownlist-content').html('是');
        $('div[data-name="DZ_JRSTZK"] input').val('1');

        $('div[data-name="CAMPUS"] .jqx-dropdownlist-content').html('<span unselectable="on">四牌楼-校区</span>');
        $('div[data-name="CAMPUS"] input').val('4');

        $('div[data-name="IN_SCHOOL_TIME"] input').val(dateStart);
        $('div[data-name="OFF_SCHOOL_TIME"] input').val(dateEnd);
        $('input[data-name="SDLY"]').val('图书馆');

        $('div[data-name="SQ_REASON"] .jqx-dropdownlist-content').html('到图书馆学习借书');
        $('div[data-name="SQ_REASON"] input').val('4');

        $('.ivu-btn-success').click();
        var timeout = setTimeout(() => {
            $('.bh-dialog-btnContainerBox').children()[0].click();
            clearTimeout(timeout)
        }, 1000);
        clearInterval(interval);
    }
}, 3000);
"""
try:
    time.sleep(2)
    #点击“登录”
    driver.find_element_by_xpath("//*[@id='ampHasNoLogin']/span[1]").click()
    print("点击登录成功")
    time.sleep(2)
    #输入账户和密码
    driver.find_element_by_xpath("//*[@id='username']").send_keys(user)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(psw)
    print("输入账号成功")
    time.sleep(2)

    #接着点击学生服务
    driver.find_element_by_xpath("//*[@id='xsfw']").click()
    print("学生服务成功")
    time.sleep(2)
    driver.get("http://ehall.seu.edu.cn/amp3/index.html#/service")
    time.sleep(5)
    #首先点击每日健康打卡
    driver.find_element_by_xpath("//*[text()='全校师生每日健康申报系统']").click()
    print("点击成功")
    time.sleep(15)
    #获取当前页面所有的句柄
    n=driver.window_handles
    #开始操作每日健康汇报
    # driver.execute_script(js_health)
    print("健康打卡完成")
    #切换到最开始打开的窗口，也就是信息大厅网页
    driver.switch_to.window(n[0])
    print("切换成功")
    time.sleep(2)
    #点击入校申请按钮
    driver.find_element_by_xpath("//*[text()='入校申请审批']").click()
    time.sleep(15)
    #开始操作申请入校
    driver.execute_script(js_enther)
    print("入校申请完成")
except:
    print("失败")
    driver.quit


