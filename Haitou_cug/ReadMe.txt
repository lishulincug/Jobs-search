#各文件的用途
	check_everyday.sh  适用于Linux环境下建立一个crontab任务定时的发送邮件
	email.log	发送邮件后的状态命令行信息会保存至此
	haitou.py	主程序文件源码
	
	
#小贴士
	如果感觉每次要输入太复杂，可以将以下信息填充完毕
	# username = 'xxxxxxxxxx@126.com'#input("请输入账号:")
	# password = 'xxxxxxxxxx'#input("请输入密码:")
	# sender = username
	# receiver = []# 'xxxxxxxxxx@qq.com','xxxxxxxxxx@126.com'
	# smtpserver = 'smtp.126.com'
	
	
这个还有很多Bug和要完善的地方，欢迎大家给我发邮件和我讨论
mailto:wangyijieonline@126.com
	

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><![endif]-->
<meta property="wb:webmaster" content="bde7f8a9153c79cb" />
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<script type="text/javascript" src="/static/js/jquery.js"></script>
<link rel="stylesheet" type="text/css" href="/assets/efc9bb6c/artdialog/skins/blue.css" />
<link rel="stylesheet" type="text/css" href="/assets/efc9bb6c/selector/selector.css" />
<link rel="stylesheet" type="text/css" href="/assets/5f254fb/pager.css" />
<script type="text/javascript" src="/assets/efc9bb6c/artdialog/jquery.artDialog.js?skin=blue"></script>
<script type="text/javascript">
/*<![CDATA[*/
var JSPATH='/static/js/data/';
/*]]>*/
</script>
<title>招聘公告 - 中国地质大学</title>
<link rel="stylesheet" type="text/css" href="/static/common/c/common.css"/>
<!-- <link rel="stylesheet" type="text/css" href="/static/style2/common.css"/> -->
<link rel="stylesheet" type="text/css" href="/static/color/orange.css"/>

<!-- <link rel="stylesheet" type="text/css" href="/static/style2/form.css"/> -->
<script type="text/javascript" src="/static/js/jui.min.js"></script>
<script type="text/javascript" src="/static/js/jquery.myslide.js"></script>
<script type="text/javascript" src="/static/js/jquery.jdate.js"></script>
<script type="text/javascript" src="/static/js/jquery.inputhints.min.js"></script>
<script type="text/javascript" src="/static/js/j.core.js"></script>



</head>
<body><script type="text/javascript" src="/assets/efc9bb6c/selector/selector.js"></script>

<div class="css-wrapper">
	<div class="wp">
    <div class="header">
	<div id="logo" class="logo"> <a href="http://cug.91wllm.com">
				<img src="/attachment/university/98/dc/0912c8ec8e19d7ac1799ea507855844a.png" />
				</a> </div>
</div>
        <div id="nav">
        <!-- 主页-->
        <ul class="nav">
                                                                        <li><a href="http://www.cug.edu.cn/new/" target="_blank">学校首页</a></li>
                                                                                                <li><a href="/" target="_self">本站首页</a></li>
                                                                                                                        <li><a href="http://cug.91wllm.com/news/view/tag/zxjs" target="_self">关于我们</a></li>
                                                                                                                    <li><a href="http://cug.91wllm.com/link/page/id/8351" target="_self">学生导航</a></li>
                                                                                                                    <li><a href="http://cug.91wllm.com/link/page/id/8385" target="_self">雇主导航</a></li>
                                                                                                                    <li><a href="http://cug.91wllm.com/link/page/id/8398" target="_self">校友导航</a></li>
                                                                                                                                                                                                                                        <li><a href="http://cug.ncss.org.cn/login" target="_blank">就业一站式服务</a></li>
                                                                                                                        <li><a href="http://cug.91wllm.com/admin" target="_self">管理登录</a></li>
                                        </ul>
        <!-- 2级导航-->

                <div class="container css-common-subnav">
            <ul class="subNav">
                                                                                                                        <li class="curr"><a href="/campus">招聘公告</a></li>
                                                                                                                                                                                                                <li><a href="/jobfair">大型双选会</a></li>
                                                                                                                                                                                                                <li><a href="/teachin">专场宣讲会</a></li>
                                                                                                                                                                                                                <li >
                                    <a href="/job/search/d_category%5B0%5D/0/d_category%5B1%5D/100">招聘信息</a></li>
                                                                                                                                                                                                        <li >
                                    <a href="/job/search/d_category%5B0%5D/0/d_category%5B1%5D/101/d_category%5B2%5D/102">实习信息</a></li>
                                                                                                                                                                                                        <li><a href="/news/index/tag/mrzp">明日招聘</a></li>
                                                                                                                    </ul>
        <!-- 快捷菜单 -->
        <!-- 快捷菜单 -->
<div class="quickMenu" id="quickMenu">
    </div>
<!-- 快捷菜单完 -->
        <!-- 快捷菜单完 -->
        </div>


    </div>
        <div class="container cl">
	<div class="mn z view view2" id="mn">
		<div class="schBox">
			<form name="campus" method="get" action="">
				<div class="schItem keyWordItem wz">
					<div class="schTit">关键词</div>
					<div class="schIpt">
						<input type="text" name="keyword" value="" class="keyWord" />
					</div>
				</div>
				<div class="schItem">
					<div class="schTit">范围</div>
					<div class="schIpt" id="schRange">
						<i>请选择</i>
						<input type="hidden" name="range" value="" />
					</div>
				</div>
				<div class="schItem">
					<div class="schTit">工作城市</div>
					<div class="schIpt" id="schCity">
						<i>请选择</i>
						<input type="hidden" name="city" value="" />
					</div>
				</div>
				<div class="schItem">
					<div class="schTit">发布时间</div>
					<div class="schIpt" id="schTime">
						<i>请选择</i>
						<input type="hidden" name="time" value="" />
					</div>
				</div>
				<div class="schBtn">
					<button type="submit" class="btnnor">搜索</button>
				</div>
				<input type="hidden" name="page" value="11" />
			</form>
		</div>
		<div class="infoBox mt10">
			<ul class="infoTit">
				<li class="span7" style="width:500px">招聘公告</li>
				<li class="span1" style="width:240px">工作城市</li>
				<li class="span4" style="width:150px">发布时间</li>
			</ul>

										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477399" target="_blank">东方财富2018届校园招聘简章</a></li>
				<li class="span1" style="width:240px">上海市</li>
				<li class="span4" style="width:150px">2017-09-14 15:03:22</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477402" target="_blank">2018洋丰集团百人计划校园招聘(新的世界 洋丰起航）</a></li>
				<li class="span1" style="width:240px">荆门市</li>
				<li class="span4" style="width:150px">2017-09-14 15:03:09</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477279" target="_blank">中国移动湖北公司2018校园招聘公告</a></li>
				<li class="span1" style="width:240px">湖北省</li>
				<li class="span4" style="width:150px">2017-09-14 11:09:10</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477268" target="_blank">武汉珈和科技招聘公告—遥感类</a></li>
				<li class="span1" style="width:240px">武汉市</li>
				<li class="span4" style="width:150px">2017-09-14 11:08:48</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477187" target="_blank">华新水泥股份有限公司校园招聘公告</a></li>
				<li class="span1" style="width:240px">湖北省,其他</li>
				<li class="span4" style="width:150px">2017-09-14 10:47:49</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477205" target="_blank">广州普邦园林股份有限公司武汉分公司2017校园招聘</a></li>
				<li class="span1" style="width:240px">湖北省,河南省,江西省,湖南省,江苏省</li>
				<li class="span4" style="width:150px">2017-09-14 10:47:41</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477264" target="_blank">广州数鹏通科技有限公司 JAVA招聘简章</a></li>
				<li class="span1" style="width:240px">广州市</li>
				<li class="span4" style="width:150px">2017-09-14 10:47:32</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477219" target="_blank">2018年安踏湖北分公司校园招聘</a></li>
				<li class="span1" style="width:240px">武汉市</li>
				<li class="span4" style="width:150px">2017-09-14 10:47:25</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477224" target="_blank">中国铁建大桥工程局集团有限公司</a></li>
				<li class="span1" style="width:240px">天津市,湖北省,湖南省,广东省,吉林省</li>
				<li class="span4" style="width:150px">2017-09-14 10:47:04</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477225" target="_blank">武汉市中潮互联网教育有限公司招聘公告</a></li>
				<li class="span1" style="width:240px">湖北省</li>
				<li class="span4" style="width:150px">2017-09-14 10:46:49</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477236" target="_blank">北京亚控科技发展有限公司2018校园招聘</a></li>
				<li class="span1" style="width:240px">北京市</li>
				<li class="span4" style="width:150px">2017-09-14 10:46:18</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477238" target="_blank">太平洋建设楚商集团（湖南一水）  2018校园招聘简章</a></li>
				<li class="span1" style="width:240px">湖南省,云南省,山西省,新疆,湖北省</li>
				<li class="span4" style="width:150px">2017-09-14 10:46:04</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477241" target="_blank">实施顾问实习生</a></li>
				<li class="span1" style="width:240px">湖北省</li>
				<li class="span4" style="width:150px">2017-09-14 10:45:56</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477245" target="_blank">上海隧道工程有限公司2018校园招聘</a></l
				<li class="span7"style="width:500px"><a href="/campus/view/id/477257" target="_blank">浙江省计量科学研究院/浙江省方正校准有限公司 2017年度招聘公告</a></li>
				<li class="span1" style="width:240px">浙江省</li>i>
				<li class="span1" style="width:240px">江苏省,浙江省,上海市,天津市,湖北省</li>
				<li class="span4" style="width:150px">2017-09-14 10:45:45</li>
			</ul>
										<ul class="infoList">
				<li class="span4" style="width:150px">2017-09-14 10:45:36</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477249" target="_blank">中国移动云南公司2018年校园招聘公告</a></li>
				<li class="span1" style="width:240px">云南省</li>
				<li class="span4" style="width:150px">2017-09-14 10:45:10</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477173" target="_blank">广东东鹏控股股份有限公司2018届校园招聘</a></li>
				<li class="span1" style="width:240px">佛山市,清远市,宜春市</li>
				<li class="span4" style="width:150px">2017-09-14 10:39:35</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477171" target="_blank">济南市勘察测绘研究院</a></li>
				<li class="span1" style="width:240px">山东省,济南市</li>
				<li class="span4" style="width:150px">2017-09-14 10:39:21</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477113" target="_blank">厦门市斯巴特进出口有限公司2018校园招聘</a></li>
				<li class="span1" style="width:240px">福建省,上海市</li>
				<li class="span4" style="width:150px">2017-09-14 08:10:44</li>
			</ul>
										<ul class="infoList">
				<li class="span7"style="width:500px"><a href="/campus/view/id/477151" target="_blank">2018金蝶天燕校园招聘计划书</a></li>
				<li class="span1" style="width:240px">深圳市</li>
				<li class="span4" style="width:150px">2017-09-14 08:10:28</li>
			</ul>
						<div class="ctl">
				<div class="pages y">
				<div class="pageinfo">共<span class="orange">717</span>页</div><ul class="page" id="yw0"><li class="first"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=">&lt;&lt;</a></li>
<li class="previous"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=10">&lt;</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=6">6</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=7">7</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=8">8</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=9">9</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=10">10</a></li>
<li class="page selected"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=11">11</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=12">12</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=13">13</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=14">14</a></li>
<li class="page"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=15">15</a></li>
<li class="next"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=12">&gt;</a></li>
<li class="last"><a href="/campus/index?keyword=&amp;range=&amp;city=&amp;time=&amp;page=717">&gt;&gt;</a></li></ul>				</div>
			</div>
		</div>
	</div>
	<!--
	<div class="sd y b" id="sd">
		<div class="sTit">热点实习</div>
		<ul class="sdList">
			<li><span>[顶]</span><a href="#">老卡上的上课啦记得</a></li>
			<li><span>[顶]</span><a href="#">老卡上的上课啦记得</a></li>
			<li><span>[顶]</span><a href="#">老卡上的上课啦记得</a></li>
			<li><span>[顶]</span><a href="#">老卡上的上课啦记得</a></li>
			<li><span>[顶]</span><a href="#">老卡上的上课啦记得</a></li>
		</ul>
	</div>
	-->
</div>
<script type="text/javascript">
$(function(){
	$('#schRange').MySelector({
		js:["\u5168\u90e8","\u6821\u5185\u53d1\u5e03","\u6821\u5916\u53d1\u5e03"],
		Max:1,
		title:'范围'
	});
	$('#schCity').MySelector({
		js:'DataDistrict',
		Max:5,
		type:2,
		title:'工作城市'
	});
	$('#schTime').MySelector({
		js:{"0":"\u6240\u6709","1":"\u8fd11\u5929","3":"\u8fd13\u5929","7":"\u8fd11\u5468","14":"\u8fd12\u5468","30":"\u8fd11\u6708","60":"\u8fd12\u6708"},
		Max:1,
		title:'发布时间'
	});

});
</script>        <div style="clear:both;"></div>
	<div class="footer cl">
		<div class="flink">
                                <select onchange="javascript:this.value!=''?window.open(this.value):'';" style="width: 100px;">
				<option value="">教育就业</option>
                                <option value="http://gj.ncss.org.cn/?from=groupmessage&isappinstalled=0">高校毕业生到国际组织实习任职信息服务平台</option>
                                <option value="http://xj.ncss.org.cn/index.html">新疆籍毕业生就业创业信息平台</option>
                			</select>
                                <select onchange="javascript:this.value!=''?window.open(this.value):'';" style="width: 100px;">
				<option value="">校内链接</option>
                			</select>
                                <select onchange="javascript:this.value!=''?window.open(this.value):'';" style="width: 100px;">
				<option value="">人才中心</option>
                			</select>
                                <select onchange="javascript:this.value!=''?window.open(this.value):'';" style="width: 100px;">
				<option value="">兄弟院校</option>
                			</select>
            		</div>
		<div class="finfo">
            <p></p>
            <p>
            <script language="javascript" type="text/javascript" src="http://js.users.51.la/18961395.js"></script>
<noscript><a href="http://www.51.la/?18961395" target="_blank"><img alt="我要啦免费统计" src="http://img.users.51.la/18961395.asp" style="border:none" /></a></noscript><script language="javascript" type="text/javascript" src="http://quote.51.la/?id=18961395&mb=3"></script></br>
地址：湖北省武汉市洪山区鲁磨路388号 邮编430074
                Copyright &copy; cug.91wllm.com All Right reserved 鄂ICP备13011617号-3 技术支持:<a href="http://www.jysd.com" target="_blank">才立方就业</a></p>
		</div>
	</div>
</div>
</div>
</body>
</html>
