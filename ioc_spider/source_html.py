# -*- coding: utf-8 -*-
# @Time    : 2019-06-17 22:46
# @Author  : zyh
# @File    : source_html.py
# @Software: PyCharm

html = """<html><head id="head">
<title>SEA LEVEL STATION MONITORING FACILITY</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<link rel="stylesheet" type="text/css" href="/css/style.css?1">
<link rel="stylesheet" type="text/css" href="/css/tooltip.css">
<meta http-equiv="refresh" content="300">

<script language="javascript" type="text/javascript" src="js/tooltip.js"></script><script type="text/javascript">
function showexpert(val)
{
 var ref = window.location.href;
 if(!val) val='exp';
 if(ref.indexOf('?',0)>0) ref=ref+'&audience='+val;
 else ref=ref+'?audience=exp';
 window.location.href=ref;
}

function openwindow(lnk){
var monitorwindow= window.open(lnk,'monitorwindow','width=800,toolbar=0,location=0,resizable=1,scrollbars=1');
monitorwindow.focus();
}

/* used in station.php */
function showinfo(s){
 confirm(s);
}

function newgraph(cmd){
 if(document.graph) document.graph.src='images/button_loading.png';
 if(cmd=='30')document.station.period.value=30;
 else if(cmd=='7')document.station.period.value=7;
 else if(cmd=='1')document.station.period.value=1;
 else if(cmd=='0.5')document.station.period.value=0.5;
 else if(cmd=='exp') document.station.audience.value='exp';
 else if(cmd=='simple') document.station.audience.value='simple';
 else if(cmd=='raw') document.station.displaylevel.value='raw';
 else if(cmd=='rl') document.station.displaylevel.value='rl';
 else if(cmd=='offset') document.station.displaylevel.value='offset';
 else if(cmd=='battery') document.station.displaylevel.value='battery';
 else if(cmd=='sw') document.station.displaylevel.value='sw';
 else if(cmd=='filter') document.station.usefilter.checked = (document.station.usefilter.checked ? false : true);
 if(document.station.code.value) document.station.action='station.php?code='+document.station.code.value;
 document.station.submit();
}
</script>
</head><body id="body" style="margin-top:0px;">	<table id="maintable">
    <tbody><tr><td align="center">

        <table border="0" cellpadding="0" cellspacing="0" width="980" bgcolor="#FFFFFF">
        <tbody><tr><td>
			<table cellspacing="0" cellpadding="0" width="100%">
			<tbody><tr><td><img hspace="10" vspace="5" src="images/unescoiocsmall.png"></td>
				<td align="center"><div class="title">SEA LEVEL STATION MONITORING FACILITY</div></td></tr>
			</tbody></table>
		</td></tr>
		<tr><td align="center">
		</td></tr>
		<tr><td>
			<table cellspacing="0" cellpadding="0" border="0" width="100%" align="center">
			<tbody><tr><td><table width="100%" border="0" cellspacing="0" celpadding="0"><tbody><tr><td class="A_navigatie" width="14%"><a href="index.php">Intro</a></td><td class="A_navigatie" width="14%"><a href="map.php">Map</a></td><td class="A_navigatie_current" width="14%"><a href="list.php">Station lists</a></td><td class="A_navigatie" width="14%"><a href="station.php">Station details</a></td><td class="A_navigatie" width="14%"><a href="service.php">Services &amp; FAQ</a></td><td class="A_navigatie" width="14%"><a href="gloss.php">GLOSS</a></td><td class="A_navigatie" width="14%"><a href="ssc.php">Catalog</a></td></tr></tbody></table></td></tr></tbody></table></td></tr>
 <tr><td><div class="maincontent">
  <table align="center">
 <tbody><tr valign="top"><td align="left"> 
<form action="#"><input type="hidden" name="operator" value="">
<table width="100%" class="nice" cellspacing="1" cellpadding="1">

			<tbody><tr><th colspan="17" class="field">
			
				Status at 2019-06-17 14:43 GMT : 878 stations listed ordered by code </th>

			</tr><tr class="field" valign="middle">
			<td colspan="17" align="left">
			<table>

			<tbody><tr valign="center"><td valign="top">Show:
			<select onchange="submit()" ;="" name="showall">
				<option value="a" selected="">Active stations</option>
				<option value="g">Stations from GLOSS network</option>
				<option value="all">All known stations</option>
				<option value="gts">Stations on GTS network</option>
				<option value="ftp">Stations on FTP connection</option>
				<option value="web">Stations on webservice connection</option>
				<option value="bgan">Stations on BGAN network or web pushing connection</option>
				<option value="email">Stations on Email connection</option>
				<option value="socket">Stations on socket connection</option>

			</select>
			</td>
			<td valign="top">Info:
			<select onchange="submit()" ;="" name="output">
			<option value="general" selected="">General information</option>
			<option value="contacts">Contact information</option>
			<option value="performance">Performance statistics</option>

			</select></td></tr></tbody></table></td></tr>

			
			<tr valign="bottom" class="field">
			<td><a href="list.php?showall=a&amp;output=general&amp;order=code&amp;dir=desc">Code</a></td>
			<td><a href="list.php?showall=a&amp;output=general&amp;order=glossid&amp;dir=asc">GLOSS ID</a></td>
			<!-- td>Operator</td -->
			<td><a href="list.php?showall=a&amp;output=general&amp;order=country&amp;dir=asc">Country</a></td>
			<td><a href="list.php?showall=a&amp;output=general&amp;order=location&amp;dir=asc">Location</a></td>
			<td><a href="list.php?showall=a&amp;output=general&amp;order=connect&amp;dir=asc">Connection</a></td>
			<td>DCP ID</td>
			<td colspan="2">Last observation<br>
				<span align="left">Level</span>
				<span align="center"><a href="list.php?showall=a&amp;output=general&amp;order=lasttime&amp;dir=asc">&nbsp;&nbsp;&nbsp;Time in GMT</a></span></td>
			<td><a href="list.php?showall=a&amp;output=general&amp;order=delay&amp;dir=asc">Delay</a></td>
			<td><a href="list.php?showall=a&amp;output=general&amp;order=interval&amp;dir=asc">Transmit<br>Interval</a></td>
			<td align="center">View </td></tr>
			<tr>
		<td class="nice"><a href="station.php?code=abas">abas</a></td>
		<td class="nice">327</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Abashiri </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">ABASHIRI</td>
		<td class="nice">2.41</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=abas">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=abed">abed</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Aberdeen </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=abed">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=abur">abur</a></td>
		<td class="nice">82</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Aburatsu </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">ABURATSU</td>
		<td class="nice">2.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=abur">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=acaj">acaj</a></td>
		<td class="nice">182</td>
		<td class="nice">El Salvador</td>
		<td class="nice" nowrap="">Acajutla </td>
		<td class="nice" nowrap="">SEMS40</td>
		<td class="nice" nowrap="">50313520</td>
		<td class="nice">2.41</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=acaj">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=acap2">acap2</a></td>
		<td class="nice">267</td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Acapulco2 </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">0100D7CA</td>
		<td class="nice">4.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=acap2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=acnj">acnj</a></td>
		<td class="nice">220</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Atlantic City </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3367B730</td>
		<td class="nice">1.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=acnj">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=acnj2">acnj2</a></td>
		<td class="nice">220</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Atlantic City </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3367B730</td>
		<td class="nice">-7.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=acnj2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=acya">acya</a></td>
		<td class="nice">267</td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Acapulco Club de Yates </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.96</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=acya">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=adak">adak</a></td>
		<td class="nice">302</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Adak </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3360F60E</td>
		<td class="nice">0.91</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=adak">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=adak2">adak2</a></td>
		<td class="nice">302</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Adak </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3360F60E</td>
		<td class="nice">-2.33</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=adak2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=agal">agal</a></td>
		<td class="nice"></td>
		<td class="nice">Mauritius</td>
		<td class="nice" nowrap="">Agalega </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">3246B586</td>
		<td class="nice">7.37</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 03:16</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=agal">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=aigi">aigi</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Aigio </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=aigi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ajac">ajac</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ajaccio </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.49</td>
		<td class="nice" align="center" nowrap="">
			<small>08:47</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>6h</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ajac">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ajac2">ajac2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ajaccio2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR300</td>
		<td class="nice">0.32</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ajac2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alak">alak</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Alitak </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3363341E</td>
		<td class="nice">1.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=alak">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alak2">alak2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Alitak </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3363341E</td>
		<td class="nice">-3.96</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=alak2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alam">alam</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Alameda </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3362E08C</td>
		<td class="nice">-0.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=alam">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=albu">albu</a></td>
		<td class="nice"></td>
		<td class="nice">Portugal</td>
		<td class="nice" nowrap="">Albufeira </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">ALBU</td>
		<td class="nice">2.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=albu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alcu">alcu</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Alcudia </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=alcu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alex1">alex1</a></td>
		<td class="nice"></td>
		<td class="nice">Egypt</td>
		<td class="nice" nowrap="">Alexandria </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">ALEX1</td>
		<td class="nice">-4.19</td>
		<td class="nice" align="center" nowrap="">
			<small>14:41</small></td>
		<td bgcolor="white" nowrap=""><small>3'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=alex1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alge">alge</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Algeciras </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=alge">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alme">alme</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Almeria </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.42</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=alme">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alofi">alofi</a></td>
		<td class="nice"></td>
		<td class="nice">Niue</td>
		<td class="nice" nowrap="">Alofi Niue </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">66570</td>
		<td class="nice">0.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=alofi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=alva">alva</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Alvarado </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=alva">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=amal">amal</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Charlotte-Amalie </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3364A348</td>
		<td class="nice">4.41</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-08-08 12:16</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>313d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=amal">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=amal2">amal2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Charlotte-Amalie </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3364A348</td>
		<td class="nice">-4.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=amal2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ambon">ambon</a></td>
		<td class="nice">68</td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Ambon </td>
		<td class="nice" nowrap="">SZID40</td>
		<td class="nice" nowrap="">06503AC6</td>
		<td class="nice">5.01</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-14 03:48</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>3d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ambon">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=AN15">AN15</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Ancona </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=AN15">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=anch">anch</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Anchorage </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3363B20A</td>
		<td class="nice">8.55</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=anch">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=anch2">anch2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Anchorage </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3363B20A</td>
		<td class="nice">-3.55</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=anch2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ancu">ancu</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Ancud </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC12228</td>
		<td class="nice">5.56</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=ancu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ancu2">ancu2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Ancud </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=ancu2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ande">ande</a></td>
		<td class="nice">322</td>
		<td class="nice">Norway</td>
		<td class="nice" nowrap="">Andenes </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.36</td>
		<td class="nice" align="center" nowrap="">
			<small>16:20</small></td>
		<td bgcolor="white" nowrap=""><small>-96'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=ande">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=anto">anto</a></td>
		<td class="nice">174</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Antofagasta </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC0F6BA</td>
		<td class="nice">5.95</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=anto">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=anto2">anto2</a></td>
		<td class="nice">174</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Antofagasta </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=anto2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=apfl">apfl</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Apalachicola </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3346C2B4</td>
		<td class="nice">0.62</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=apfl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=apfl2">apfl2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Apalachicola </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3346C2B4</td>
		<td class="nice">-6.17</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:12</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=apfl2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=apla">apla</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Lawma, Amerada Pass, LA </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">334773C0</td>
		<td class="nice">3.4</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-02-01 07:09</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>136d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=apla">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=apla2">apla2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Lawma, Amerada Pass, LA </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">334773C0</td>
		<td class="nice">-7.91</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=apla2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=arac">arac</a></td>
		<td class="nice"></td>
		<td class="nice">Puerto Rico</td>
		<td class="nice" nowrap="">Arecibo </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.19</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=arac">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=aracS">aracS</a></td>
		<td class="nice"></td>
		<td class="nice">Puerto Rico</td>
		<td class="nice" nowrap="">Arecibo (GTS) </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3366454E</td>
		<td class="nice">-3.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=aracS">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=arca">arca</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Arcachon Eyrac </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.23</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-15 04:42</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>2d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=arca">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=arca2">arca2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Arcachon Eyrac 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR190</td>
		<td class="nice">3.22</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-15 04:43</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>2d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=arca2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=aren">aren</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Arena Cove </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3368115A</td>
		<td class="nice">-0.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=aren">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=aren2">aren2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Arena Cove </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336AF75C</td>
		<td class="nice">-9.44</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=aren2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=aric">aric</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Arica </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC0D056</td>
		<td class="nice">4.97</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=aric">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=aric2">aric2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Arica </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.44</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=aric2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=arrc">arrc</a></td>
		<td class="nice"></td>
		<td class="nice">Brasil</td>
		<td class="nice" nowrap="">Arraial do Cabo </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">B5B007D4</td>
		<td class="nice">2.1</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-08 09:57</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>9d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=arrc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=arre">arre</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Arrecife </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=arre">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=arri">arri</a></td>
		<td class="nice"></td>
		<td class="nice">Portugal</td>
		<td class="nice" nowrap="">Arrifana </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">ARRI</td>
		<td class="nice">1.21</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=arri">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ashd1">ashd1</a></td>
		<td class="nice"></td>
		<td class="nice">Israel</td>
		<td class="nice" nowrap="">Ashdod Marina </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">ASHD1</td>
		<td class="nice">-0.06</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-09 00:01</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>9d</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ashd1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ashk">ashk</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Ashkhara </td>
		<td class="nice" nowrap="">SXOM33</td>
		<td class="nice" nowrap="">18E447FC</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-16 13:31</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>1d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ashk">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=asto">asto</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Astoria </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335086EE</td>
		<td class="nice">-0.22</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=asto">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=asto2">asto2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Astoria </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335086EE</td>
		<td class="nice">-6.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=asto2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=atka">atka</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Atka, AK </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=atka">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=auct">auct</a></td>
		<td class="nice">127</td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Auckland </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">AUCT</td>
		<td class="nice">4.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=auct">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=audi">audi</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Audierne </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=audi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=audi2">audi2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Audierne 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR6305</td>
		<td class="nice">4.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=audi2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=avon">avon</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Avonmouth Portbury </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=avon">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=AZ42">AZ42</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Anzio </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.21</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=AZ42">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=BA05">BA05</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Bari </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=BA05">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ball">ball</a></td>
		<td class="nice"></td>
		<td class="nice">Ireland</td>
		<td class="nice" nowrap="">Ballyglass pier, Belmullet </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=ball">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=balt">balt</a></td>
		<td class="nice">169</td>
		<td class="nice">Ecuador</td>
		<td class="nice" nowrap="">Baltra,Galapagos </td>
		<td class="nice" nowrap="">SEEQ40</td>
		<td class="nice" nowrap="">932040EE</td>
		<td class="nice">3.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=balt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bamd">bamd</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Baltimore </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336577DA</td>
		<td class="nice">0.42</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bamd">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bamd2">bamd2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Baltimore </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336577DA</td>
		<td class="nice">-4.09</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bamd2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bame">bame</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Bar Harbor </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336747B4</td>
		<td class="nice">3.03</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bame">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bame2">bame2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Bar Harbor </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336747B4</td>
		<td class="nice">-3.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bame2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bamf">bamf</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Bamfield </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.69</td>
		<td class="nice" align="center" nowrap="">
			<small>09:45</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>5h</small></td>
		<td class="nice" nowrap="" align="center"><small>6h</small></td>
		<td class="nice"><a href="station.php?code=bamf">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bang">bang</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Bangor </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.03</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=bang">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bapj">bapj</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Battery Point </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">61221</td>
		<td class="nice">0.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=bapj">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bara">bara</a></td>
		<td class="nice"></td>
		<td class="nice">Dominican Republic</td>
		<td class="nice" nowrap="">Barahona </td>
		<td class="nice" nowrap="">SXDR40</td>
		<td class="nice" nowrap="">04401622</td>
		<td class="nice">0.62</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bara">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=barb">barb</a></td>
		<td class="nice"></td>
		<td class="nice">Antigua</td>
		<td class="nice" nowrap="">Barbuda </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">334550D8</td>
		<td class="nice">-0.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=barb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=barb2">barb2</a></td>
		<td class="nice"></td>
		<td class="nice">Antigua</td>
		<td class="nice" nowrap="">Barbuda </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">334550D8</td>
		<td class="nice">-1.22</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=barb2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=barc">barc</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Barcelona </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=barc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=barm">barm</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Barmouth </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.28</td>
		<td class="nice" align="center" nowrap="">
			<small>14:00</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>44'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=barm">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=barn">barn</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Burnie Tasmania </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">60910</td>
		<td class="nice">3.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=barn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bass">bass</a></td>
		<td class="nice"></td>
		<td class="nice">St. Kitts &amp; Nevis</td>
		<td class="nice" nowrap="">Basseterre (Coast Guard Base) </td>
		<td class="nice" nowrap="">SOAT10</td>
		<td class="nice" nowrap="">FA8005BC</td>
		<td class="nice"></td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-15 12:03</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>2d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bass">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=batr">batr</a></td>
		<td class="nice"></td>
		<td class="nice">Lebanon</td>
		<td class="nice" nowrap="">Batroun </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">BATR</td>
		<td class="nice">4.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:41</small></td>
		<td bgcolor="white" nowrap=""><small>3'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=batr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bbbc">bbbc</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Bella Bella </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">CD401E4C</td>
		<td class="nice">0.58</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bbbc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bdto">bdto</a></td>
		<td class="nice"></td>
		<td class="nice">Panamá</td>
		<td class="nice" nowrap="">Bocas Del Toro </td>
		<td class="nice" nowrap="">SOPM10</td>
		<td class="nice" nowrap="">F230215A</td>
		<td class="nice">-2.74</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bdto">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=benc">benc</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Beaufort </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3364C6AE</td>
		<td class="nice">0.77</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-07 16:28</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>41d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=benc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=benc2">benc2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Beaufort </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3364C6AE</td>
		<td class="nice">-3.85</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:08</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=benc2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=beno">beno</a></td>
		<td class="nice">49</td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Benoa </td>
		<td class="nice" nowrap="">SZID43</td>
		<td class="nice" nowrap="">06508948</td>
		<td class="nice">-1.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=beno">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bgct">bgct</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Bridgeport </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.68</td>
		<td class="nice" align="center" nowrap="">
			<small>14:18</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>26'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bgct">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bgct2">bgct2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Bridgeport </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3372E712</td>
		<td class="nice">-4.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bgct2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bil3">bil3</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Bilbao3 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.96</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=bil3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bitu">bitu</a></td>
		<td class="nice">69</td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Bitung </td>
		<td class="nice" nowrap="">SZID42</td>
		<td class="nice" nowrap="">06504284</td>
		<td class="nice">5.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=bitu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=blow">blow</a></td>
		<td class="nice"></td>
		<td class="nice">Anguilla</td>
		<td class="nice" nowrap="">Blowing Point </td>
		<td class="nice" nowrap="">SOAT10</td>
		<td class="nice" nowrap="">A84006AC</td>
		<td class="nice"></td>
		<td class="nice" align="center" nowrap="">
			<small>2018-12-06 00:21</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>194d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=blow">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=blueb">blueb</a></td>
		<td class="nice"></td>
		<td class="nice">Mauritius</td>
		<td class="nice" nowrap="">Blue Bay </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">22BF90A6</td>
		<td class="nice">2.87</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=blueb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bmda">bmda</a></td>
		<td class="nice">221</td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Bermuda </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33573754</td>
		<td class="nice">0.68</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=bmda">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bmsa">bmsa</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Bahia Mansa </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">14063458</td>
		<td class="nice">5.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bmsa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bmsa2">bmsa2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Bahia Mansa </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bmsa2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=boma">boma</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Boston </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335E54EE</td>
		<td class="nice">2.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:18</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>26'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=boma">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bon2">bon2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Bonanza2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=bon2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bork">bork</a></td>
		<td class="nice"></td>
		<td class="nice">Germany</td>
		<td class="nice" nowrap="">Borkum Fischerbalje </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bork">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bouc">bouc</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Boucau-Bayonne </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bouc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bouc2">bouc2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Boucau-Bayonne 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR094</td>
		<td class="nice">4.02</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-16 15:01</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>32d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=bouc2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=boul">boul</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Boulogne-Sur-Mer </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.83</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=boul">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=boul2">boul2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Boulogne-Sur-Mer 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR111</td>
		<td class="nice">4.86</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=boul2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bour">bour</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Bournemouth </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=bour">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bres">bres</a></td>
		<td class="nice">242</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Brest </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">6.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bres">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=brid">brid</a></td>
		<td class="nice"></td>
		<td class="nice">Barbados</td>
		<td class="nice" nowrap="">Bridgetown Port </td>
		<td class="nice" nowrap="">SOBR10</td>
		<td class="nice" nowrap="">14004206</td>
		<td class="nice">0.45</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-02-01 06:43</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>501d</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=brid">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=brom">brom</a></td>
		<td class="nice">40</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Broome </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">62650</td>
		<td class="nice">8.51</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=brom">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=brpt">brpt</a></td>
		<td class="nice"></td>
		<td class="nice">Hawaii</td>
		<td class="nice" nowrap="">Barbers Point </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">35403732</td>
		<td class="nice">3.46</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=brpt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=brsk">brsk</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Breskens Handelshaven </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.68</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=brsk">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=btny">btny</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Battery The </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336670D4</td>
		<td class="nice">1.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=btny">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=btny2">btny2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Battery The </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336670D4</td>
		<td class="nice">-2.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=btny2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=buca">buca</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Bucalemu </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC203CA</td>
		<td class="nice">4.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=buca">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=buca3">buca3</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Bucalemu </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.87</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=buca3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=bull">bull</a></td>
		<td class="nice"></td>
		<td class="nice">Curaçao</td>
		<td class="nice" nowrap="">Bullen Bay </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3541C54C</td>
		<td class="nice">2.23</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=bull">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=busa">busa</a></td>
		<td class="nice">84</td>
		<td class="nice">Korea</td>
		<td class="nice" nowrap="">Busan </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.97</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=busa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=buve">buve</a></td>
		<td class="nice">170</td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Buenaventura </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:13</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>31'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=buve">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=buve2">buve2</a></td>
		<td class="nice">170</td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Buenaventura </td>
		<td class="nice" nowrap="">SXCO41</td>
		<td class="nice" nowrap="">15AA92C8</td>
		<td class="nice">0.78</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-06 23:01</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>11d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=buve2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=CA02">CA02</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Cagliari </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=CA02">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cabc">cabc</a></td>
		<td class="nice"></td>
		<td class="nice">Belize</td>
		<td class="nice" nowrap="">Carrie Bow Cay </td>
		<td class="nice" nowrap="">SOBH10</td>
		<td class="nice" nowrap="">777022C4</td>
		<td class="nice">1.38</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 23:50</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cabc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cadi">cadi</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Cadiz </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">CADI</td>
		<td class="nice">3.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:41</small></td>
		<td bgcolor="white" nowrap=""><small>3'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=cadi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cala">cala</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Calais </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cala">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cald">cald</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Caldera </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC104C4</td>
		<td class="nice">5.26</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cald">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cald2">cald2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Caldera </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.78</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cald2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=call">call</a></td>
		<td class="nice">173</td>
		<td class="nice">Perú</td>
		<td class="nice" nowrap="">Callao,La-Punta </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">354165B4</td>
		<td class="nice">6.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=call">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=camt">camt</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Lerma Campeche </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=camt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=caph">caph</a></td>
		<td class="nice"></td>
		<td class="nice">Haïti</td>
		<td class="nice" nowrap="">Cap-Haïtien </td>
		<td class="nice" nowrap="">SEHA10</td>
		<td class="nice" nowrap="">3540C7B6</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:03</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=caph">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=carb">carb</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Carboneras </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=carb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=carg">carg</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Cartagena </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">CARG</td>
		<td class="nice">0.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=carg">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=casc">casc</a></td>
		<td class="nice">246</td>
		<td class="nice">Portugal</td>
		<td class="nice" nowrap="">Cascais </td>
		<td class="nice" nowrap="">socket</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>1'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.0833'</small></td>
		<td class="nice"><a href="station.php?code=casc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cast">cast</a></td>
		<td class="nice">330</td>
		<td class="nice">Ireland</td>
		<td class="nice" nowrap="">Castletownbere </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.49</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-10-16 17:25</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>244d</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=cast">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cbmd">cbmd</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cambridge </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3366E5B6</td>
		<td class="nice">0.16</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cbmd">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ccar">ccar</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Ciudad del Carmen, Camp. </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.38</td>
		<td class="nice" align="center" nowrap="">
			<small>14:17</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>27'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=ccar">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cctx">cctx</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Corpus Christi, TX </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336943DC</td>
		<td class="nice">0.85</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cctx">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cctx2">cctx2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Corpus Christi, TX </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336943DC</td>
		<td class="nice">-8.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cctx2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cent">cent</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Centuri </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.41</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-10 19:09</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>7d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cent">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cent2">cent2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Centuri2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR807</td>
		<td class="nice">0.33</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=cent2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ceut">ceut</a></td>
		<td class="nice">249</td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Ceuta </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.77</td>
		<td class="nice" align="center" nowrap="">
			<small>04:59</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>10h</small></td>
		<td class="nice" nowrap="" align="center"><small>1d</small></td>
		<td class="nice"><a href="station.php?code=ceut">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ceut1">ceut1</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Ceuta </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">CEUT1</td>
		<td class="nice">0.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ceut1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=CF06">CF06</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Carloforte </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=CF06">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chab">chab</a></td>
		<td class="nice">337</td>
		<td class="nice">Iran</td>
		<td class="nice" nowrap="">Chabahar </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">366C76AC</td>
		<td class="nice"></td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-15 10:54</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>2d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=chab">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=char">char</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Charleston, OR </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336874BC</td>
		<td class="nice">-0.48</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=char">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=char2">char2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Charleston, OR </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336874BC</td>
		<td class="nice">-4.53</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:09</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=char2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cher">cher</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Cherbourg </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cher">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cher2">cher2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Cherbourg 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR013</td>
		<td class="nice">1.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=cher2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chia">chia</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Puerto Chiapas/Madero </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">0100A15A</td>
		<td class="nice">9.67</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-06 16:07</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>11d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=chia">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chij">chij</a></td>
		<td class="nice">103</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Chichijima </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">CHICHIJIMA</td>
		<td class="nice">1.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=chij">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chit">chit</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Owenga, Chatham Island </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">CHIT</td>
		<td class="nice">2.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=chit">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chnr">chnr</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Chañaral </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC296A8</td>
		<td class="nice">4.63</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=chnr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chnr2">chnr2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Chañaral </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.1</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=chnr2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chrp">chrp</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cherry Point </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336BB6AC</td>
		<td class="nice">1.62</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=chrp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chrp2">chrp2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cherry Point </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336BB6AC</td>
		<td class="nice">-7.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=chrp2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chrs">chrs</a></td>
		<td class="nice">47</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Christmas Island </td>
		<td class="nice" nowrap="">SZIO01</td>
		<td class="nice" nowrap="">46290</td>
		<td class="nice">0.93</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=chrs">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=chtt">chtt</a></td>
		<td class="nice">36</td>
		<td class="nice">Bangladesh</td>
		<td class="nice" nowrap="">Chittagong </td>
		<td class="nice" nowrap="">SZBW40</td>
		<td class="nice" nowrap="">065079CC</td>
		<td class="nice">4.21</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=chtt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=CI20">CI20</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Civitavecchia </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=CI20">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cili">cili</a></td>
		<td class="nice">291</td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Cilacap </td>
		<td class="nice" nowrap="">SZID49</td>
		<td class="nice" nowrap="">0650FFD8</td>
		<td class="nice">6.65</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=cili">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ciut">ciut</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Ciutadella </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">CIUT</td>
		<td class="nice">-0.16</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ciut">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=clst">clst</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Celestun, Yuc. </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.76</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=clst">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cmet">cmet</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Caleta Meteoro </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">140204F8</td>
		<td class="nice">1.6</td>
		<td class="nice" align="center" nowrap="">
			<small>14:14</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>30'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=cmet">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cmet3">cmet3</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Caleta Meteoro </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=cmet3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cmnj">cmnj</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cape May </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335D53E0</td>
		<td class="nice">1.45</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cmnj">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cmnj2">cmnj2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cape May </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335D53E0</td>
		<td class="nice">-3.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cmnj2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cocb">cocb</a></td>
		<td class="nice">46</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Cocos Island </td>
		<td class="nice" nowrap="">SZIO01</td>
		<td class="nice" nowrap="">46280</td>
		<td class="nice">0.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=cocb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=coch">coch</a></td>
		<td class="nice">32</td>
		<td class="nice">India</td>
		<td class="nice" nowrap="">Cochin </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap="">43357</td>
		<td class="nice">0.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=coch">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cocos">cocos</a></td>
		<td class="nice"></td>
		<td class="nice">Costa Rica</td>
		<td class="nice" nowrap="">Cocos Island </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3542E4AE</td>
		<td class="nice">2.73</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cocos">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cois">cois</a></td>
		<td class="nice"></td>
		<td class="nice">Nicaragua</td>
		<td class="nice" nowrap="">Corn Island </td>
		<td class="nice" nowrap="">SXXX50</td>
		<td class="nice" nowrap="">22178120</td>
		<td class="nice">2.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:09</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>35'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=cois">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=coli">coli</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Coliumo </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC210BC</td>
		<td class="nice">5.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=coli">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=colo">colo</a></td>
		<td class="nice">33</td>
		<td class="nice">Sri Lanka</td>
		<td class="nice" nowrap="">Colombo </td>
		<td class="nice" nowrap="">SWIO40</td>
		<td class="nice" nowrap="">0650018E</td>
		<td class="nice">1.19</td>
		<td class="nice" align="center" nowrap="">
			<small>10:45</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>4h</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=colo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=como">como</a></td>
		<td class="nice"></td>
		<td class="nice">Comores</td>
		<td class="nice" nowrap="">Comores </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">166AC436</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-30 10:23</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>48d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=como">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=conc">conc</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Concarneau </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.66</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-14 20:50</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>3d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=conc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=conc2">conc2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Concarneau 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR160</td>
		<td class="nice">4.64</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=conc2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cons2">cons2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Constitucion </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cons2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=const">const</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Constitucion </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC154B8</td>
		<td class="nice">6.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=const">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=coqu">coqu</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Coquimbo </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC117B2</td>
		<td class="nice">4.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=coqu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=coqu2">coqu2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Coquimbo </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.41</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=coqu2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cor2">cor2</a></td>
		<td class="nice">243</td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Acoruna </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=cor2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cord">cord</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cordova </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335FA690</td>
		<td class="nice">0.5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cord">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cord2">cord2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cordova </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335FA690</td>
		<td class="nice">-7.39</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cord2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=corf">corf</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Kerkyra, Corfu </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.32</td>
		<td class="nice" align="center" nowrap="">
			<small>14:40</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=corf">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cori">cori</a></td>
		<td class="nice"></td>
		<td class="nice">Nicaragua</td>
		<td class="nice" nowrap="">Puerto Corinto </td>
		<td class="nice" nowrap="">SXXX50</td>
		<td class="nice" nowrap="">050284CA</td>
		<td class="nice">0.26</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-11 19:47</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>6d</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=cori">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=corn">corn</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Corinth </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">CORN</td>
		<td class="nice">0.38</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=corn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=corr">corr</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Corral </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">14066424</td>
		<td class="nice">5.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=corr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=corr2">corr2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Corral </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.42</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=corr2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=coru">coru</a></td>
		<td class="nice">243</td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">La Coruña </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.51</td>
		<td class="nice" align="center" nowrap="">
			<small>07:51</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>7h</small></td>
		<td class="nice" nowrap="" align="center"><small>1d</small></td>
		<td class="nice"><a href="station.php?code=coru">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cove">cove</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Coveñas </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice"></td>
		<td class="nice" align="center" nowrap="">
			<small>11:10</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>4h</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=cove">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cpit">cpit</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Castlepoint </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">CPIT</td>
		<td class="nice">3.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=cpit">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cpla">cpla</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Calcasieu Pass, LA </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3368C732</td>
		<td class="nice">0.84</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cpla">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=CR08">CR08</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Crotone </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=CR08">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=crbc">crbc</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Campbell River </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">CD402BD6</td>
		<td class="nice">2.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=crbc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cres">cres</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Crescent City </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33622592</td>
		<td class="nice">-0.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cres">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cres2">cres2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Crescent City </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33622592</td>
		<td class="nice">-4.09</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cres2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=crnl">crnl</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Coronel </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC1C1DA</td>
		<td class="nice">5.58</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=crnl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=crnl2">crnl2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Coronel </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=crnl2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=crom">crom</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Cromer </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=crom">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=csta">csta</a></td>
		<td class="nice"></td>
		<td class="nice">Romania</td>
		<td class="nice" nowrap="">Constanta </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">48.38</td>
		<td class="nice" align="center" nowrap="">
			<small>11:50</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>3h</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=csta">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=csta2">csta2</a></td>
		<td class="nice"></td>
		<td class="nice">Romania</td>
		<td class="nice" nowrap="">Constanta </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">CSTA2</td>
		<td class="nice">-7.39</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=csta2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cstr">cstr</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Castro </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC1315E</td>
		<td class="nice">5.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=cstr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cstr2">cstr2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Castro </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.67</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=cstr2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=CT03">CT03</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Catania </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=CT03">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cule">cule</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Culebra Is </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335CB2E8</td>
		<td class="nice">0.09</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=cule">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cule2">cule2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Culebra Is </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335CB2E8</td>
		<td class="nice">-3.57</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=cule2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=curri">curri</a></td>
		<td class="nice"></td>
		<td class="nice">Philippines</td>
		<td class="nice" nowrap="">Currimao </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">12D7050E</td>
		<td class="nice">4.25</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=curri">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cuvie">cuvie</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Cape Cuvier Wharf </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">62385</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=cuvie">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cuxh">cuxh</a></td>
		<td class="nice">284</td>
		<td class="nice">Germany</td>
		<td class="nice" nowrap="">Cuxhaven </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cuxh">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cwfl">cwfl</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Clearwater Beach </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3358C142</td>
		<td class="nice">1.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cwfl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cwfl2">cwfl2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Clearwater Beach </td>
		<td class="nice" nowrap="">SXXX50</td>
		<td class="nice" nowrap="">3358C142</td>
		<td class="nice">-4.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cwfl2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cwme">cwme</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cutler Farris Wharf, ME </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33672252</td>
		<td class="nice">3.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cwme">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=cwme2">cwme2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Cutler Farris Wharf, ME </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33672252</td>
		<td class="nice">-3.58</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:07</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=cwme2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dakar">dakar</a></td>
		<td class="nice">253</td>
		<td class="nice">Sénégal</td>
		<td class="nice" nowrap="">Dakar </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">360916B8</td>
		<td class="nice">5.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=dakar">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=darw">darw</a></td>
		<td class="nice">62</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Darwin </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">63230</td>
		<td class="nice">0.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=darw">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=davo">davo</a></td>
		<td class="nice">71</td>
		<td class="nice">Philippines</td>
		<td class="nice" nowrap="">Davao </td>
		<td class="nice" nowrap="">SWPH41</td>
		<td class="nice" nowrap="">06505F20</td>
		<td class="nice">6.87</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-24 05:50</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>24d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=davo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=deke">deke</a></td>
		<td class="nice">115</td>
		<td class="nice">Micronesia</td>
		<td class="nice" nowrap="">Dekehtik,Pohnpei </td>
		<td class="nice" nowrap="">SZPA01</td>
		<td class="nice" nowrap="">67950</td>
		<td class="nice">1.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=deke">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=delf">delf</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Delfzijl </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=delf">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=denh">denh</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Den Helder </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=denh">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dese">dese</a></td>
		<td class="nice">190</td>
		<td class="nice">Argentina</td>
		<td class="nice" nowrap="">Puerto Deseado </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">33912088</td>
		<td class="nice">4.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=dese">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=desh">desh</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Deshaies, Guadeloupe </td>
		<td class="nice" nowrap="">SXMF40</td>
		<td class="nice" nowrap="">12A0419C</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=desh">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=desi">desi</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">La Desirade Island, Guadeloupe </td>
		<td class="nice" nowrap="">SXMF40</td>
		<td class="nice" nowrap="">12A00296</td>
		<td class="nice">0.32</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=desi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dial">dial</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Dauphin Island </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335752B2</td>
		<td class="nice">0.49</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-10-06 03:05</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>254d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=dial">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=diba">diba</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Diba </td>
		<td class="nice" nowrap="">SXOM33</td>
		<td class="nice" nowrap="">18EE7334</td>
		<td class="nice">0.11</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-03-14 16:33</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>95d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=diba">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=diel">diel</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Dielette </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.54</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=diel">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=diel2">diel2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Dielette 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR628</td>
		<td class="nice">2.55</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=diel2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=diep">diep</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Dieppe </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.95</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=diep">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=diep2">diep2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Dieppe 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR024</td>
		<td class="nice">3.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=diep2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dlpr">dlpr</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Deal Pier </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.99</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-28 23:59</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>20d</small></td>
		<td class="nice" nowrap="" align="center"><small>0.1666'</small></td>
		<td class="nice"><a href="station.php?code=dlpr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dove">dove</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Dover </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=dove">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dpnc">dpnc</a></td>
		<td class="nice">219</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Duck Pier </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335DD5F4</td>
		<td class="nice">0.03</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-01-22 08:40</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>146d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=dpnc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dumo">dumo</a></td>
		<td class="nice">131</td>
		<td class="nice">Antarctica</td>
		<td class="nice" nowrap="">Dumont d'Urville </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-18 15:00</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>60d</small></td>
		<td class="nice" nowrap="" align="center"><small>4h</small></td>
		<td class="nice"><a href="station.php?code=dumo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dunk">dunk</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Dunkerque </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=dunk">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dunk2">dunk2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Dunkerque 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR002</td>
		<td class="nice">4.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=dunk2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=duqm">duqm</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Duqm </td>
		<td class="nice" nowrap="">SXOM33</td>
		<td class="nice" nowrap="">18EB74F4</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-07 21:46</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>41d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=duqm">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dutc">dutc</a></td>
		<td class="nice">102</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Dutch Hbr Unalaska </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3360A672</td>
		<td class="nice">0.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=dutc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dutc2">dutc2</a></td>
		<td class="nice">102</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Dutch Hbr Unalaska </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3360A672</td>
		<td class="nice">-5.2</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-12-25 07:04</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>174d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=dutc2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dzao">dzao</a></td>
		<td class="nice">96</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Dzaoudzi (Mayotte) </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.74</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=dzao">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=dzao2">dzao2</a></td>
		<td class="nice">96</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Dzaoudzi (Mayotte) 2 </td>
		<td class="nice" nowrap="">SZIO01</td>
		<td class="nice" nowrap="">FR030</td>
		<td class="nice">3.9</td>
		<td class="nice" align="center" nowrap="">
			<small>13:42</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>1h</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=dzao2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=east">east</a></td>
		<td class="nice">137</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Easter </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">93202BDA</td>
		<td class="nice">3.47</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=east">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=east2">east2</a></td>
		<td class="nice">137</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Easter </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=east2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=elak">elak</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Elfin Cove </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33604580</td>
		<td class="nice">-0.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=elak">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=elak2">elak2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Elfin Cove </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33604580</td>
		<td class="nice">-1.83</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=elak2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=elpo">elpo</a></td>
		<td class="nice"></td>
		<td class="nice">Panamá</td>
		<td class="nice" nowrap="">El Porvenir </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">354084BC</td>
		<td class="nice">6.48</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=elpo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=epme">epme</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">East Port </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3365875E</td>
		<td class="nice">0.28</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-02-27 04:27</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>110d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=epme">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=epme2">epme2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">East Port </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3365875E</td>
		<td class="nice">-4.38</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:10</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=epme2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=erdem">erdem</a></td>
		<td class="nice"></td>
		<td class="nice">Turkey</td>
		<td class="nice" nowrap="">Erdemli </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:40</small></td>
		<td bgcolor="white" nowrap=""><small>3'</small></td>
		<td class="nice" nowrap="" align="center"><small>2'</small></td>
		<td class="nice"><a href="station.php?code=erdem">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=espe">espe</a></td>
		<td class="nice">54</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Esperance </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">62080</td>
		<td class="nice">0.55</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=espe">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=euro">euro</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Europlatform </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.61</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=euro">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fbfl">fbfl</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Fernadina Beach </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336782AA</td>
		<td class="nice">1.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fbfl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fbfl2">fbfl2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Fernadina Beach </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336782AA</td>
		<td class="nice">-2.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fbfl2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fer1">fer1</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Ferrol1 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.71</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=fer1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fer2">fer2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Ferrol2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.67</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=fer2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ferg">ferg</a></td>
		<td class="nice">60</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Cape Ferguson </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">59260</td>
		<td class="nice">2.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=ferg">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=feth">feth</a></td>
		<td class="nice"></td>
		<td class="nice">Turkey</td>
		<td class="nice" nowrap="">Fethiye </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">FETH</td>
		<td class="nice">1.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:43</small></td>
		<td bgcolor="white" nowrap=""><small>1'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=feth">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ffcj">ffcj</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Flying Fish Cove Jetty Christmas Is </td>
		<td class="nice" nowrap="">SZIO01</td>
		<td class="nice" nowrap="">46291</td>
		<td class="nice">1.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=ffcj">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=figu">figu</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">La Figueirette </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=figu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=figu2">figu2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">La Figueirette2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR0846</td>
		<td class="nice">0.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=figu2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fish">fish</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Fishguard </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=fish">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fmfl">fmfl</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Fort Myers </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336754C2</td>
		<td class="nice">0.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fmfl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fmfl2">fmfl2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Fort Myers </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336754C2</td>
		<td class="nice">-2.89</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fmfl2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fong">fong</a></td>
		<td class="nice">121</td>
		<td class="nice">Tuvalu Islands</td>
		<td class="nice" nowrap="">Fongafale </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">67440</td>
		<td class="nice">2.32</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=fong">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=form">form</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Formentera </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=form">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fort">fort</a></td>
		<td class="nice">336</td>
		<td class="nice">Brasil</td>
		<td class="nice" nowrap="">Fortaleza </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3542D134</td>
		<td class="nice">3.87</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fort">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fosm">fosm</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Fos-sur-Mer </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fosm">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fosm2">fosm2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Fos-sur-Mer2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR0719</td>
		<td class="nice">0.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=fosm2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fpga">fpga</a></td>
		<td class="nice">289</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Fort Pulaski </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335F151E</td>
		<td class="nice">1.89</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fpga">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fpga2">fpga2</a></td>
		<td class="nice">289</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Fort Pulaski </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335F151E</td>
		<td class="nice">-3.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fpga2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fpnt">fpnt</a></td>
		<td class="nice">158</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Ft Point,San Fran </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336172E0</td>
		<td class="nice">-0.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fpnt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fpnt2">fpnt2</a></td>
		<td class="nice">158</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Ft Point,San Fran </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336172E0</td>
		<td class="nice">-2.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fpnt2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fren">fren</a></td>
		<td class="nice">107</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Tern,Fr. Frigate </td>
		<td class="nice" nowrap="">SXHW11</td>
		<td class="nice" nowrap="">15D58280</td>
		<td class="nice">6.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=fren">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=frtr">frtr</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Frontera </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.46</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-13 16:54</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>4d</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=frtr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ftfr">ftfr</a></td>
		<td class="nice">338</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Fort-de-France, Martinique </td>
		<td class="nice" nowrap="">SZCA01</td>
		<td class="nice" nowrap="">FR126</td>
		<td class="nice">0.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ftfr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ftfr2">ftfr2</a></td>
		<td class="nice">338</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Fort-de-France, Martinique2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ftfr2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fue2">fue2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Fuerteventura </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=fue2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=fuka">fuka</a></td>
		<td class="nice"></td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Fukaura </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">FUKAURA</td>
		<td class="nice">2.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=fuka">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=futu">futu</a></td>
		<td class="nice">353</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Leava (Futuna Island, Wallis &amp; Futuna) </td>
		<td class="nice" nowrap="">SZFW40</td>
		<td class="nice" nowrap="">065219DE</td>
		<td class="nice">1.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=futu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=GA37">GA37</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Gaeta </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=GA37">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gamb">gamb</a></td>
		<td class="nice">138</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Rikitea (French Polynesia, Gambier, Mangareva) </td>
		<td class="nice" nowrap="">SEHI40</td>
		<td class="nice" nowrap="">FAA0542E</td>
		<td class="nice">0.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:03</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>41'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=gamb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gand">gand</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Gandia </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=gand">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ganm">ganm</a></td>
		<td class="nice">27</td>
		<td class="nice">Maldive Islands</td>
		<td class="nice" nowrap="">Gan </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">32D8A2BE</td>
		<td class="nice">7.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ganm">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=garc">garc</a></td>
		<td class="nice">26</td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Diego Garcia </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">18963134</td>
		<td class="nice">7.19</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=garc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gbit">gbit</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Great Barrier </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">GBIT</td>
		<td class="nice">5.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=gbit">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gcsb">gcsb</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Gold Coast Sand Bypass Jetty </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">60053</td>
		<td class="nice">0.61</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=gcsb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=GE25">GE25</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Genova </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=GE25">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=geor">geor</a></td>
		<td class="nice"></td>
		<td class="nice">Cayman Islands</td>
		<td class="nice" nowrap="">George Town </td>
		<td class="nice" nowrap="">SOGC10</td>
		<td class="nice" nowrap="">1320048C</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=geor">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=GI20">GI20</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Ginostra (Isola di Stromboli) </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.45</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=GI20">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gibr3">gibr3</a></td>
		<td class="nice">248</td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Gibraltar </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">1852F574</td>
		<td class="nice">1.68</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=gibr3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gij2">gij2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Gijon </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=gij2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gila">gila</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Grand Isle, LA </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335DA364</td>
		<td class="nice">0.51</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=gila">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gist">gist</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Gisborne </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">GIST</td>
		<td class="nice">3.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=gist">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gokc">gokc</a></td>
		<td class="nice"></td>
		<td class="nice">Turkey</td>
		<td class="nice" nowrap="">Gokceada </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.92</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-04 16:00</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>74d</small></td>
		<td class="nice" nowrap="" align="center"><small>2'</small></td>
		<td class="nice"><a href="station.php?code=gokc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=goto">goto</a></td>
		<td class="nice">233</td>
		<td class="nice">Sweden</td>
		<td class="nice" nowrap="">GoteborgTorshamnen </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">9.93</td>
		<td class="nice" align="center" nowrap="">
			<small>13:55</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>49'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=goto">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=goug">goug</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Gough Island </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">18D74682</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=goug">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gpab">gpab</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Geraldton </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">62290</td>
		<td class="nice">0.71</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=gpab">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gptx">gptx</a></td>
		<td class="nice">217</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Galveston Pier </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336AB456</td>
		<td class="nice">0.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=gptx">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=greg">greg</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Bahia Gregorio </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC1B74A</td>
		<td class="nice">7.86</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=greg">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=greg2">greg2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Bahia Gregorio </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">7.39</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=greg2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=groo">groo</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Groote Eylandt </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">63511</td>
		<td class="nice">0.54</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=groo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=guam">guam</a></td>
		<td class="nice">149</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Guam (Apra Harbor) </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.67</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=guam">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=gwda">gwda</a></td>
		<td class="nice">295</td>
		<td class="nice">Pakistan</td>
		<td class="nice" nowrap="">Gwadar </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">1851B170</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=gwda">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hade2">hade2</a></td>
		<td class="nice"></td>
		<td class="nice">Israel</td>
		<td class="nice" nowrap="">Hadera Port </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">HADE2</td>
		<td class="nice">0.11</td>
		<td class="nice" align="center" nowrap="">
			<small>14:44</small></td>
		<td bgcolor="white" nowrap=""><small>-0'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=hade2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=haif">haif</a></td>
		<td class="nice"></td>
		<td class="nice">Israel</td>
		<td class="nice" nowrap="">Haifa </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">HAIF</td>
		<td class="nice">0.1</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=haif">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hain">hain</a></td>
		<td class="nice"></td>
		<td class="nice">Myanmar</td>
		<td class="nice" nowrap="">Haing Gyi Kyun </td>
		<td class="nice" nowrap="">SZBM45</td>
		<td class="nice" nowrap="">48000</td>
		<td class="nice">2.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=hain">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hako">hako</a></td>
		<td class="nice">88</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Hakodate </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">HAKODATE</td>
		<td class="nice">1.89</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=hako">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hana">hana</a></td>
		<td class="nice"></td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Hanasaki </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">HANASAKI</td>
		<td class="nice">1.47</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=hana">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hani">hani</a></td>
		<td class="nice"></td>
		<td class="nice">Maldive Islands</td>
		<td class="nice" nowrap="">Hanimadhoo </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">26CB10AC</td>
		<td class="nice">6.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=hani">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=harl">harl</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Harlingen </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=harl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=harv">harv</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Oil Platform Harvest, CA </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.22</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=harv">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=harw">harw</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Harwich </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=harw">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hbay">hbay</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Herne Bay </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.57</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.1666'</small></td>
		<td class="nice"><a href="station.php?code=hbay">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=helg">helg</a></td>
		<td class="nice"></td>
		<td class="nice">Germany</td>
		<td class="nice" nowrap="">Helgoland Binnenhafen </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.52</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=helg">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hens">hens</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Henslung Cove </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=hens">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=herb">herb</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">L'Herbaudière </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.45</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=herb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=herb2">herb2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">L'Herbaudière 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR198</td>
		<td class="nice">5.43</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=herb2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=heys">heys</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Heysham </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.22</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=heys">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hie2">hie2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">ElHierro </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=hie2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hien">hien</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Hienghene (New Caledonia) </td>
		<td class="nice" nowrap="">SZNC42</td>
		<td class="nice" nowrap="">xxxxxxx</td>
		<td class="nice">0.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=hien">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hill">hill</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Hillarys Harbor </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">62237</td>
		<td class="nice">0.59</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=hill">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hilo">hilo</a></td>
		<td class="nice">287</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Hilo,Hawaii </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.38</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=hilo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hilo2">hilo2</a></td>
		<td class="nice">287</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Hilo, Hawaii </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">334934A2</td>
		<td class="nice">-3.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=hilo2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hink">hink</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Hinkley Point </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=hink">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hirt">hirt</a></td>
		<td class="nice"></td>
		<td class="nice">Denmark</td>
		<td class="nice" nowrap="">Hirtshals </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=hirt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hiva">hiva</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Hiva Oa (Marquesas, French Polynesia) </td>
		<td class="nice" nowrap="">SEHI40</td>
		<td class="nice" nowrap="">9322451A</td>
		<td class="nice">2.66</td>
		<td class="nice" align="center" nowrap="">
			<small>14:17</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>27'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=hiva">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hmda">hmda</a></td>
		<td class="nice">326</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Hamada </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">HAMADA</td>
		<td class="nice">2.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=hmda">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hoek">hoek</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Hoek van Holland </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=hoek">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=holy2">holy2</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Holyhead2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.1</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=holy2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=honn">honn</a></td>
		<td class="nice"></td>
		<td class="nice">Norway</td>
		<td class="nice" nowrap="">Honningsvåg </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.51</td>
		<td class="nice" align="center" nowrap="">
			<small>16:20</small></td>
		<td bgcolor="white" nowrap=""><small>-96'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=honn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hono">hono</a></td>
		<td class="nice">108</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Honolulu,Oahu </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.21</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=hono">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=horn">horn</a></td>
		<td class="nice"></td>
		<td class="nice">Germany</td>
		<td class="nice" nowrap="">Hörnum </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.53</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=horn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=hrak">hrak</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Hrakleio </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.11</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=hrak">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=huahi">huahi</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Huahine island (Society Islands, French Polynesia) </td>
		<td class="nice" nowrap="">SEHI40</td>
		<td class="nice" nowrap="">B1F0371A</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:01</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>43'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=huahi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=huas2">huas2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Huasco </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=huas2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=huas3">huas3</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Huasco </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.89</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=huas3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=huat">huat</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Huatulco </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">01010358</td>
		<td class="nice">1.07</td>
		<td class="nice" align="center" nowrap="">
			<small>13:57</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>47'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=huat">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=huat2">huat2</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Huatulco </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:13</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>31'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=huat2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=huel">huel</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Huelva5 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=huel">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=iaix">iaix</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ile d'Aix </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=iaix">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ibiz">ibiz</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Ibiza2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.35</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=ibiz">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=iclr">iclr</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Isla Clarion </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">FB03E75A</td>
		<td class="nice">0.66</td>
		<td class="nice" align="center" nowrap="">
			<small>12:26</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>2h</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=iclr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=iera">iera</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Ierapetra </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:41</small></td>
		<td bgcolor="white" nowrap=""><small>3'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=iera">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=iler">iler</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ile Royale, Kourou, French Guiana </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=iler">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=iler2">iler2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ile Royale, Kourou, French Guiana 2 </td>
		<td class="nice" nowrap="">SZCA01</td>
		<td class="nice" nowrap="">FR749</td>
		<td class="nice">1.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=iler2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ilfa">ilfa</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Ilfracombe </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.53</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ilfa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=IM01">IM01</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Imperia </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=IM01">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=im02">im02</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Imperia 2 </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">IM02</td>
		<td class="nice">-0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=im02">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=immi">immi</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Immingham </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:00</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>44'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=immi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=imuj">imuj</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Isla Mujeres, Q. R. </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:16</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>28'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=imuj">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=inav">inav</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Isla Naval </td>
		<td class="nice" nowrap="">SXCO41</td>
		<td class="nice" nowrap="">15A05856</td>
		<td class="nice">0.63</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=inav">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=inav2">inav2</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Isla Naval </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.62</td>
		<td class="nice" align="center" nowrap="">
			<small>14:16</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>28'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=inav2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=iqui">iqui</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Iquique </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC1F440</td>
		<td class="nice">5.96</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=iqui">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=iqui2">iqui2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Iquique </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=iqui2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=isab">isab</a></td>
		<td class="nice"></td>
		<td class="nice">Puerto Rico</td>
		<td class="nice" nowrap="">Isabel Segunda </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3366D02C</td>
		<td class="nice">-2.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=isab">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ishig">ishig</a></td>
		<td class="nice"></td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Ishigakijima </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">ISHIGAKIJIMA</td>
		<td class="nice">2.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=ishig">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=iske">iske</a></td>
		<td class="nice"></td>
		<td class="nice">Turkey</td>
		<td class="nice" nowrap="">Iskenderun </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2</td>
		<td class="nice" align="center" nowrap="">
			<small>08:27</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>6h</small></td>
		<td class="nice" nowrap="" align="center"><small>2'</small></td>
		<td class="nice"><a href="station.php?code=iske">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=IT45">IT45</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Isole Tremiti </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.1</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=IT45">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=itea">itea</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Itea </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=itea">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=jack">jack</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Jackson Bay </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">65180</td>
		<td class="nice">1.73</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=jack">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=jers">jers</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Jersey </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=jers">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=john">john</a></td>
		<td class="nice">109</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Johnston </td>
		<td class="nice" nowrap="">SXHW11</td>
		<td class="nice" nowrap="">15D142A4</td>
		<td class="nice">7.28</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=john">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=juan">juan</a></td>
		<td class="nice">176</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Juan Fernandez </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC0B5B0</td>
		<td class="nice">5.67</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=juan">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=juan2">juan2</a></td>
		<td class="nice">176</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Juan Fernandez </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.16</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=juan2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kahu">kahu</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Kahului, Maui </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=kahu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kahu2">kahu2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Kahului, Maui </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33518414</td>
		<td class="nice">-3.95</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=kahu2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kait">kait</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Kaikoura </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">KAIT</td>
		<td class="nice">2.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=kait">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kala">kala</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Kalamata </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">18.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=kala">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kalt">kalt</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Kalathos </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.38</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-05 16:01</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>12d</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=kalt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kant">kant</a></td>
		<td class="nice">145</td>
		<td class="nice">Kiribati</td>
		<td class="nice" nowrap="">Kanton </td>
		<td class="nice" nowrap="">SEPA40</td>
		<td class="nice" nowrap="">354305A6</td>
		<td class="nice">5.05</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:00</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=kant">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kapi">kapi</a></td>
		<td class="nice">117</td>
		<td class="nice">Micronesia</td>
		<td class="nice" nowrap="">Kapingamarangi </td>
		<td class="nice" nowrap="">SEPA40</td>
		<td class="nice" nowrap="">3541D63A</td>
		<td class="nice">4.33</td>
		<td class="nice" align="center" nowrap="">
			<small>01:49</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>13h</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=kapi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kara">kara</a></td>
		<td class="nice">30</td>
		<td class="nice">Pakistan</td>
		<td class="nice" nowrap="">Karachi </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">120D7136</td>
		<td class="nice">0.74</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=kara">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kata">kata</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Katakolo </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:00</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>44'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=kata">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kawa">kawa</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Kawaihae, Hawaii </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.27</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=kawa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kawa2">kawa2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Kawaihae, Hawaii </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3351527C</td>
		<td class="nice">-2.73</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=kawa2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=keba">keba</a></td>
		<td class="nice"></td>
		<td class="nice">Pakistan</td>
		<td class="nice" nowrap="">Keti Bandar </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">32CC9580</td>
		<td class="nice"></td>
		<td class="nice" align="center" nowrap="">
			<small>2018-10-15 04:52</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>245d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=keba">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kepo">kepo</a></td>
		<td class="nice">187</td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">King Edward Point </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=kepo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kerg2">kerg2</a></td>
		<td class="nice">23</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Kerguelen Island </td>
		<td class="nice" nowrap="">SZIO01</td>
		<td class="nice" nowrap="">FR023</td>
		<td class="nice">0.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=kerg2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kiel">kiel</a></td>
		<td class="nice"></td>
		<td class="nice">Germany</td>
		<td class="nice" nowrap="">LT Kiel </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.95</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=kiel">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kinl">kinl</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Kinlochbervie </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.25</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=kinl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kjni">kjni</a></td>
		<td class="nice"></td>
		<td class="nice">Norfolk Island</td>
		<td class="nice" nowrap="">Kingston Jetty Norfolk </td>
		<td class="nice" nowrap="">SZPA01</td>
		<td class="nice" nowrap="">57700</td>
		<td class="nice">0.64</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=kjni">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kodi">kodi</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Kodiak Island, AK </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33626698</td>
		<td class="nice">0.7</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=kodi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kodi2">kodi2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Kodiak Island, AK </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3341730E</td>
		<td class="nice">-6.43</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=kodi2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=koli">koli</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Kolinamil, Jakarta Port </td>
		<td class="nice" nowrap="">SZID52</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">7.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=koli">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=koli2">koli2</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Kolinamil 2, Jakarta Port </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.44</td>
		<td class="nice" align="center" nowrap="">
			<small>08:16</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>6h</small></td>
		<td class="nice" nowrap="" align="center"><small>8h</small></td>
		<td class="nice"><a href="station.php?code=koli2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kors">kors</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Korsakov </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.62</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-03-06 12:44</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>468d</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=kors">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kos1">kos1</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Kos </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">KOS1</td>
		<td class="nice">0.27</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=kos1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kush">kush</a></td>
		<td class="nice">89</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Kushiro </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">KUSHIRO</td>
		<td class="nice">2.27</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=kush">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kusm">kusm</a></td>
		<td class="nice">85</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Kushimoto </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">KUSHIMOTO</td>
		<td class="nice">2.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=kusm">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kwaj">kwaj</a></td>
		<td class="nice">111</td>
		<td class="nice">Marshall Islands</td>
		<td class="nice" nowrap="">Kwajalein </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336131EA</td>
		<td class="nice">1.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=kwaj">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kwfl">kwfl</a></td>
		<td class="nice">216</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Key West </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336717C8</td>
		<td class="nice">0.73</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=kwfl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=kypa">kypa</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Kyparissia </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.1</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=kypa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=LA23">LA23</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Lampedusa </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=LA23">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=LA38">LA38</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">La Spezia </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=LA38">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lago">lago</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">LaGomera </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=lago">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lajo">lajo</a></td>
		<td class="nice">159</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">La Jolla </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3362A386</td>
		<td class="nice">0.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lajo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lajo2">lajo2</a></td>
		<td class="nice">159</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">La Jolla </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3362A386</td>
		<td class="nice">-2.48</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lajo2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lalb">lalb</a></td>
		<td class="nice"></td>
		<td class="nice">El Salvador</td>
		<td class="nice" nowrap="">La Libertad </td>
		<td class="nice" nowrap="">SOES10</td>
		<td class="nice" nowrap="">5030C75E</td>
		<td class="nice">0.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lalb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lali">lali</a></td>
		<td class="nice">172</td>
		<td class="nice">Ecuador</td>
		<td class="nice" nowrap="">La Libertad </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3540B126</td>
		<td class="nice">4.63</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lali">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lame">lame</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">LameshurBayStJohnVI </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335D10EA</td>
		<td class="nice">0.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lame">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lame2">lame2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">LameshurBayStJohnVI </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335D10EA</td>
		<td class="nice">-2.47</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lame2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lamu">lamu</a></td>
		<td class="nice"></td>
		<td class="nice">Kenya</td>
		<td class="nice" nowrap="">Lamu </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">16287190</td>
		<td class="nice">8.99</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=lamu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lang">lang</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Langosteira </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.72</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=lang">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lank">lank</a></td>
		<td class="nice"></td>
		<td class="nice">Malaysia</td>
		<td class="nice" nowrap="">Langkawi </td>
		<td class="nice" nowrap="">SZMS40</td>
		<td class="nice" nowrap="">06509A3E</td>
		<td class="nice">8.36</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:14</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lank">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lapa">lapa</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">LaPalma </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=lapa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=larp">larp</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">La Rochelle-Pallice </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.71</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=larp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=larp2">larp2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">La Rochelle-Pallice 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR034</td>
		<td class="nice">5.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=larp2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=laru2">laru2</a></td>
		<td class="nice">339</td>
		<td class="nice">Seychelles</td>
		<td class="nice" nowrap="">Pt.LaRue </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">12FD90D0</td>
		<td class="nice">6.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=laru2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lasp">lasp</a></td>
		<td class="nice">251</td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">LasPalmas2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=lasp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lata">lata</a></td>
		<td class="nice"></td>
		<td class="nice">Solomon Islands</td>
		<td class="nice" nowrap="">Lata Wharf </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">57131</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=lata">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=laun">laun</a></td>
		<td class="nice"></td>
		<td class="nice">El Salvador</td>
		<td class="nice" nowrap="">La Union </td>
		<td class="nice" nowrap="">SEMS40</td>
		<td class="nice" nowrap="">3354C0DE</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=laun">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=laza">laza</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Lazaro Cardenas </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">6.11</td>
		<td class="nice" align="center" nowrap="">
			<small>14:13</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>31'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=laza">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lcst">lcst</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Le Castella </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">LCST</td>
		<td class="nice">-1.94</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-10 04:49</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>38d</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=lcst">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lebu">lebu</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Lebu </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC16122</td>
		<td class="nice">4.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lebu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lebu2">lebu2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Lebu </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.48</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lebu2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=leco">leco</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Le Conquet </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=leco">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=leco2">leco2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Le Conquet 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR152</td>
		<td class="nice">5.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=leco2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lecy">lecy</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Le Crouesty </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lecy">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lega">lega</a></td>
		<td class="nice">72</td>
		<td class="nice">Philippines</td>
		<td class="nice" nowrap="">Legaspi </td>
		<td class="nice" nowrap="">SWPA42</td>
		<td class="nice" nowrap="">06501C2A</td>
		<td class="nice">2.32</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lega">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=leha">leha</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Le Havre </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.85</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=leha">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=leha2">leha2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Le Havre 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR004</td>
		<td class="nice">2.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=leha2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=leit">leit</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Leith </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.32</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=leit">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lemba">lemba</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Lembar </td>
		<td class="nice" nowrap="">SZID44</td>
		<td class="nice" nowrap="">0650A176</td>
		<td class="nice">5.56</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lemba">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lena">lena</a></td>
		<td class="nice"></td>
		<td class="nice">Vanuatu</td>
		<td class="nice" nowrap="">Lenakel, Tanna </td>
		<td class="nice" nowrap="">SZNV41</td>
		<td class="nice" nowrap="">91566</td>
		<td class="nice">4.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lena">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lero">lero</a></td>
		<td class="nice"></td>
		<td class="nice">Martinique</td>
		<td class="nice" nowrap="">Le Robert </td>
		<td class="nice" nowrap="">SOMR10</td>
		<td class="nice" nowrap="">12A052EA</td>
		<td class="nice">0.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lero">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lerw2">lerw2</a></td>
		<td class="nice">236</td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Lerwick2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=lerw2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=leso">leso</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Les Sables d'Olonne </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=leso">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=leso2">leso2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Les Sables d'Olonne 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR062</td>
		<td class="nice">4.89</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=leso2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=levu">levu</a></td>
		<td class="nice"></td>
		<td class="nice">Fiji Islands</td>
		<td class="nice" nowrap="">Lautoka </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">67070</td>
		<td class="nice">1.11</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=levu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lgos">lgos</a></td>
		<td class="nice"></td>
		<td class="nice">Portugal</td>
		<td class="nice" nowrap="">Lagos </td>
		<td class="nice" nowrap="">socket</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.53</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>1'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.0833'</small></td>
		<td class="nice"><a href="station.php?code=lgos">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=LI11">LI11</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Livorno </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.21</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=LI11">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lifo">lifo</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Lifou </td>
		<td class="nice" nowrap="">SZNC40</td>
		<td class="nice" nowrap="">0652047A</td>
		<td class="nice">0.76</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lifo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lime">lime</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Limetree </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3364B03E</td>
		<td class="nice">0.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lime">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lime2">lime2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Limetree </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3364B03E</td>
		<td class="nice">-3.83</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=lime2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=limon">limon</a></td>
		<td class="nice"></td>
		<td class="nice">Costa Rica</td>
		<td class="nice" nowrap="">Limon </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">354011DE</td>
		<td class="nice">6.33</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=limon">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lirf">lirf</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Lihou Reef </td>
		<td class="nice" nowrap="">SZPA01</td>
		<td class="nice" nowrap="">57829</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=lirf">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=litz">litz</a></td>
		<td class="nice"></td>
		<td class="nice">Vanuatu</td>
		<td class="nice" nowrap="">Litzlitz, Malekula </td>
		<td class="nice" nowrap="">SZNV40</td>
		<td class="nice" nowrap="">91556</td>
		<td class="nice">4.59</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=litz">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=live">live</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Liverpool </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=live">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=llan">llan</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Llandudno </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=llan">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lmma">lmma</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">La Mola de Mahon </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">LMMA</td>
		<td class="nice">-0.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=lmma">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lomb">lomb</a></td>
		<td class="nice">331</td>
		<td class="nice">Papua New Guinea</td>
		<td class="nice" nowrap="">Lombrum Manus Is </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">56130</td>
		<td class="nice">1.09</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=lomb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=losa">losa</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Los Angeles </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336AF75C</td>
		<td class="nice">0.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=losa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=losa2">losa2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Los Angeles </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336AF75C</td>
		<td class="nice">-7.66</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-01-28 11:12</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>140d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=losa2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lott">lott</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">East Cape </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">LOTT</td>
		<td class="nice">2.95</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=lott">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lowe">lowe</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Lowestoft </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=lowe">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lpbc">lpbc</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Langara Point BC (Henslung Cove) </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">15C396A6</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=lpbc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=luba">luba</a></td>
		<td class="nice"></td>
		<td class="nice">Philippines</td>
		<td class="nice" nowrap="">Lubang </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">221F4098</td>
		<td class="nice">5.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=luba">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=luga">luga</a></td>
		<td class="nice"></td>
		<td class="nice">Vanuatu</td>
		<td class="nice" nowrap="">Luganville </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">57210</td>
		<td class="nice">0.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=luga">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=lymg">lymg</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Lymington </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.1666'</small></td>
		<td class="nice"><a href="station.php?code=lymg">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=made">made</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Puerto Madero, Chis. </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">6.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:13</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>31'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=made">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=madry">madry</a></td>
		<td class="nice">191</td>
		<td class="nice">Argentina</td>
		<td class="nice" nowrap="">Puerto Madryn </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">335665D2</td>
		<td class="nice">5.21</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=madry">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=maer">maer</a></td>
		<td class="nice"></td>
		<td class="nice">Turkey</td>
		<td class="nice" nowrap="">Marmara Ereglisi </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>2'</small></td>
		<td class="nice"><a href="station.php?code=maer">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=magi">magi</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Magueyes Island </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3364E042</td>
		<td class="nice">-0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=magi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=magi2">magi2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Magueyes Island </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3364E042</td>
		<td class="nice">-2.66</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=magi2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=maho">maho</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Mahon </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=maho">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mais">mais</a></td>
		<td class="nice">20</td>
		<td class="nice">South-Africa</td>
		<td class="nice" nowrap="">Marion Island </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">16AF741C</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:17</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>27'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=mais">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mais2">mais2</a></td>
		<td class="nice"></td>
		<td class="nice">South-Africa</td>
		<td class="nice" nowrap="">Marion Island </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">9.09</td>
		<td class="nice" align="center" nowrap="">
			<small>00:26</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>14h</small></td>
		<td class="nice" nowrap="" align="center"><small>8h</small></td>
		<td class="nice"><a href="station.php?code=mais2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=maji">maji</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Majis </td>
		<td class="nice" nowrap="">SXOM33</td>
		<td class="nice" nowrap="">180D62C6</td>
		<td class="nice">0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=maji">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=maju">maju</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Marina Jambu </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">MAJU</td>
		<td class="nice">0.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=maju">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=make">make</a></td>
		<td class="nice">354</td>
		<td class="nice">Polynésie Française </td>
		<td class="nice" nowrap="">Makemo (Polynésie française, Tuamotu) </td>
		<td class="nice" nowrap="">SEHI40</td>
		<td class="nice" nowrap="">FAA04758</td>
		<td class="nice">0.94</td>
		<td class="nice" align="center" nowrap="">
			<small>13:45</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>59'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=make">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mal3">mal3</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Malaga </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=mal3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mala">mala</a></td>
		<td class="nice">120</td>
		<td class="nice">Palau Islands</td>
		<td class="nice" nowrap="">Malakal </td>
		<td class="nice" nowrap="">SWPA40</td>
		<td class="nice" nowrap="">xxxxxxxx</td>
		<td class="nice">2.97</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=mala">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=male">male</a></td>
		<td class="nice">28</td>
		<td class="nice">Maldive Islands</td>
		<td class="nice" nowrap="">Male </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">16289262</td>
		<td class="nice">2.39</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=male">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mali">mali</a></td>
		<td class="nice">239</td>
		<td class="nice">Ireland</td>
		<td class="nice" nowrap="">Malin Head Peninsular </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.53</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=mali">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=malo">malo</a></td>
		<td class="nice"></td>
		<td class="nice">Norway</td>
		<td class="nice" nowrap="">Måløy </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.62</td>
		<td class="nice" align="center" nowrap="">
			<small>16:20</small></td>
		<td bgcolor="white" nowrap=""><small>-96'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=malo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=malp">malp</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Malpelo </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:14</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>30'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=malp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=malp2">malp2</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Malpelo </td>
		<td class="nice" nowrap="">SXCO41</td>
		<td class="nice" nowrap="">15AAB424</td>
		<td class="nice">13.41</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=malp2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mang">mang</a></td>
		<td class="nice"></td>
		<td class="nice">Romania</td>
		<td class="nice" nowrap="">Mangalia </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">MANG</td>
		<td class="nice">-7.42</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=mang">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mani">mani</a></td>
		<td class="nice">73</td>
		<td class="nice">Philippines</td>
		<td class="nice" nowrap="">Manila </td>
		<td class="nice" nowrap="">SWPH40</td>
		<td class="nice" nowrap="">xxxxxxxx</td>
		<td class="nice">1.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=mani">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mare">mare</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Maré (New Caledonia, Loyalty Islands) </td>
		<td class="nice" nowrap="">SZNC41</td>
		<td class="nice" nowrap="">06520AA8</td>
		<td class="nice">0.72</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=mare">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mari">mari</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Marin </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.51</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=mari">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=marm">marm</a></td>
		<td class="nice">281</td>
		<td class="nice">India</td>
		<td class="nice" nowrap="">Marmagao </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap="">43195</td>
		<td class="nice">1.56</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=marm">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mars">mars</a></td>
		<td class="nice">205</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Marseille </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.39</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-01-22 02:32</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>146d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=mars">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=marsh">marsh</a></td>
		<td class="nice">112</td>
		<td class="nice">Marshall Islands</td>
		<td class="nice" nowrap="">Majuro </td>
		<td class="nice" nowrap="">SZPA01</td>
		<td class="nice" nowrap="">67680</td>
		<td class="nice">0.72</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-17 07:23</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>61d</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=marsh">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=masi">masi</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Masirah </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">16288114</td>
		<td class="nice">1.99</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-06 12:07</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>72d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=masi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mata">mata</a></td>
		<td class="nice"></td>
		<td class="nice">Perú</td>
		<td class="nice" nowrap="">Matarani </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">354176C2</td>
		<td class="nice">5.63</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=mata">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=matel">matel</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Marina di Teulada </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">MATEL</td>
		<td class="nice">0.27</td>
		<td class="nice" align="center" nowrap="">
			<small>11:57</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>3h</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=matel">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=maya">maya</a></td>
		<td class="nice"></td>
		<td class="nice">Puerto Rico</td>
		<td class="nice" nowrap="">Mayaguez </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336633DE</td>
		<td class="nice">-2.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=maya">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=maza">maza</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Mazatlan </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:13</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>31'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=maza">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=MC41">MC41</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Marina Di Campo </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=MC41">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ME13">ME13</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Messina </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ME13">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=meji">meji</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Mejillones </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">01032040</td>
		<td class="nice">4.48</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=meji">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=meji2">meji2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Mejillones </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=meji2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=meli">meli</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Melilla </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.45</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=meli">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mera">mera</a></td>
		<td class="nice">86</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Mera </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">MERA</td>
		<td class="nice">2.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=mera">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mhav">mhav</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Milford Haven </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.46</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=mhav">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=midx">midx</a></td>
		<td class="nice">106</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Midway </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3363A17C</td>
		<td class="nice">0.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=midx">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=midx2">midx2</a></td>
		<td class="nice">106</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Midway </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3363A17C</td>
		<td class="nice">-3.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=midx2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mill">mill</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Millport </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.59</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=mill">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mimz">mimz</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Mimizan </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.09</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=mimz">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mimz2">mimz2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Mimizan 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR0614</td>
		<td class="nice">4.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=mimz2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mins">mins</a></td>
		<td class="nice">104</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Minami-Tori-Shima </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">MINAMITORISHIMA</td>
		<td class="nice">2.53</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=mins">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mnkt">mnkt</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Manukau </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">MNKT</td>
		<td class="nice">2.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=mnkt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=momb">momb</a></td>
		<td class="nice">8</td>
		<td class="nice">Kenya</td>
		<td class="nice" nowrap="">Mombasa </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">22ADF72A</td>
		<td class="nice">6.46</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=momb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mona">mona</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Mona Island </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3365E2B8</td>
		<td class="nice">0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-01 15:58</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>16d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=mona">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mona2">mona2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Mona Island </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3365E2B8</td>
		<td class="nice">-1.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=mona2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=monc">monc</a></td>
		<td class="nice"></td>
		<td class="nice">Monaco</td>
		<td class="nice" nowrap="">Monaco, Fontvieille harbour </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.33</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=monc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=monc2">monc2</a></td>
		<td class="nice"></td>
		<td class="nice">Monaco</td>
		<td class="nice" nowrap="">Monaco2, Fontvieille harbour </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR022</td>
		<td class="nice">0.33</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=monc2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mont">mont</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Monterey </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33630184</td>
		<td class="nice">0.09</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=mont">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mont2">mont2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Monterey </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33630184</td>
		<td class="nice">-4.24</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 17:36</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=mont2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mony">mony</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Montauk, NY </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33401412</td>
		<td class="nice">0.72</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=mony">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mony2">mony2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Montauk, NY </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33401412</td>
		<td class="nice">-3.56</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=mony2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=motr">motr</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Motril2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.78</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=motr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=moul">moul</a></td>
		<td class="nice">141</td>
		<td class="nice">Myanmar</td>
		<td class="nice" nowrap="">Moulmein </td>
		<td class="nice" nowrap="">SZBM40</td>
		<td class="nice" nowrap="">0650AFA4</td>
		<td class="nice">3.27</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=moul">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ms001">ms001</a></td>
		<td class="nice"></td>
		<td class="nice">Malaysia</td>
		<td class="nice" nowrap="">Porto Malai, Langkawi </td>
		<td class="nice" nowrap="">SZMS01</td>
		<td class="nice" nowrap="">MS001</td>
		<td class="nice">1.58</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ms001">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ms002">ms002</a></td>
		<td class="nice"></td>
		<td class="nice">Malaysia</td>
		<td class="nice" nowrap="">Kerachut, Penang </td>
		<td class="nice" nowrap="">SZMS01</td>
		<td class="nice" nowrap="">MS002</td>
		<td class="nice">-2.47</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-14 08:23</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>3d</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ms002">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ms004">ms004</a></td>
		<td class="nice"></td>
		<td class="nice">Malaysia</td>
		<td class="nice" nowrap="">Pulau Perhentian </td>
		<td class="nice" nowrap="">SZMS01</td>
		<td class="nice" nowrap="">MS004</td>
		<td class="nice">0.97</td>
		<td class="nice" align="center" nowrap="">
			<small>14:40</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ms004">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ms005">ms005</a></td>
		<td class="nice"></td>
		<td class="nice">Malaysia</td>
		<td class="nice" nowrap="">Kudat, Sabah </td>
		<td class="nice" nowrap="">SZMS01</td>
		<td class="nice" nowrap="">MS005</td>
		<td class="nice">1.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ms005">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ms006">ms006</a></td>
		<td class="nice"></td>
		<td class="nice">Malaysia</td>
		<td class="nice" nowrap="">Lahad Datu, Sabah </td>
		<td class="nice" nowrap="">SZMS01</td>
		<td class="nice" nowrap="">MS006</td>
		<td class="nice">2.91</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ms006">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mtwa">mtwa</a></td>
		<td class="nice">9</td>
		<td class="nice">Tanzania</td>
		<td class="nice" nowrap="">Mtwara </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">26313506</td>
		<td class="nice">-8.36</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-13 16:25</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>65d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=mtwa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mumb">mumb</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Mumbles </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=mumb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=mus2">mus2</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Muscat (BGAN) </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">OM-MUSC-00</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>13:30</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>1h</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=mus2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=musc">musc</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Muscat </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">262D700E</td>
		<td class="nice">5.35</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-02-10 11:00</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>127d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=musc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=naga">naga</a></td>
		<td class="nice">83</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Nagasaki </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">NAGASAKI</td>
		<td class="nice">2.64</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=naga">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=naha">naha</a></td>
		<td class="nice">81</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Naha </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">NAHA</td>
		<td class="nice">2.19</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=naha">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=naho">naho</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Nahodka </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=naho">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nain">nain</a></td>
		<td class="nice">224</td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Nain </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.04</td>
		<td class="nice" align="center" nowrap="">
			<small>10:01</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>5h</small></td>
		<td class="nice" nowrap="" align="center"><small>6h</small></td>
		<td class="nice"><a href="station.php?code=nain">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nanc">nanc</a></td>
		<td class="nice"></td>
		<td class="nice">India</td>
		<td class="nice" nowrap="">Nancowry </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap="">43383</td>
		<td class="nice">0.04</td>
		<td class="nice" align="center" nowrap="">
			<small>10:39</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>4h</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=nanc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=napt">napt</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Port Napier </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">NAPT</td>
		<td class="nice">2.71</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=napt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nauu">nauu</a></td>
		<td class="nice"></td>
		<td class="nice">Nauru</td>
		<td class="nice" nowrap="">Nauru </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">67640</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=nauu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nawi">nawi</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Nawiliwili, Kauai </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.27</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=nawi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ncpt">ncpt</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">North Cape </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">NCPT</td>
		<td class="nice">3.35</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=ncpt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=newl2">newl2</a></td>
		<td class="nice">241</td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Newlyn2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.63</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=newl2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nhav">nhav</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Newhaven </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.54</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=nhav">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nhte">nhte</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Nehuentue </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC240C0</td>
		<td class="nice">2.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=nhte">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nice">nice</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Nice </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.35</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=nice">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nice2">nice2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Nice2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR0339</td>
		<td class="nice">0.35</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=nice2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nkfa">nkfa</a></td>
		<td class="nice">125</td>
		<td class="nice">Tonga Island</td>
		<td class="nice" nowrap="">Nukualofa </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">66600</td>
		<td class="nice">0.77</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=nkfa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nksk">nksk</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Nikol'skoe </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.73</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=nksk">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=noct">noct</a></td>
		<td class="nice"></td>
		<td class="nice">Mauritania</td>
		<td class="nice" nowrap="">Nouakchott </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">366E2324</td>
		<td class="nice">13.93</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=noct">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nome">nome</a></td>
		<td class="nice">74</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Nome </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3360809E</td>
		<td class="nice">0.5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=nome">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nome2">nome2</a></td>
		<td class="nice">74</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Nome </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3360809E</td>
		<td class="nice">-5.4</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:10</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=nome2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=noto">noto</a></td>
		<td class="nice"></td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Noto </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">NOTO</td>
		<td class="nice">2.25</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=noto">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=noua">noua</a></td>
		<td class="nice"></td>
		<td class="nice">Mauritania</td>
		<td class="nice" nowrap="">Nouadhibou </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap="">18ABD7D0</td>
		<td class="nice">0.08</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-08-10 21:05</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>311d</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=noua">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=npor">npor</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Newport </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.54</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=npor">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nshi">nshi</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">North Shields </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=nshi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nspi">nspi</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">North Spit, Humboldt </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336837B6</td>
		<td class="nice">-0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=nspi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nspi2">nspi2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">North Spit, Humboldt </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3354D3A8</td>
		<td class="nice">-5.65</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=nspi2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ntue">ntue</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Nehuentue </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC240C0</td>
		<td class="nice">2.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ntue">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ntue2">ntue2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Nehuentue </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.86</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ntue2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nuku">nuku</a></td>
		<td class="nice">142</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Nuku Hiva (Marquesas, French Polynesia) </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3540D4C0</td>
		<td class="nice">6.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=nuku">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=numbo">numbo</a></td>
		<td class="nice">123</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Nouméa - Numbo (New Caledonia) </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=numbo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nuuk">nuuk</a></td>
		<td class="nice">225</td>
		<td class="nice">Denmark</td>
		<td class="nice" nowrap="">Nuuk harbor </td>
		<td class="nice" nowrap="">email</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-2.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=nuuk">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=nyal">nyal</a></td>
		<td class="nice">345</td>
		<td class="nice">Norway</td>
		<td class="nice" nowrap="">Ny Ålesund </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.09</td>
		<td class="nice" align="center" nowrap="">
			<small>16:20</small></td>
		<td bgcolor="white" nowrap=""><small>-96'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=nyal">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ofun">ofun</a></td>
		<td class="nice">87</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Ofunato </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">OFUNATO</td>
		<td class="nice">2.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=ofun">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=omae">omae</a></td>
		<td class="nice"></td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Omaezaki </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">OMAEZAKI</td>
		<td class="nice">2.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=omae">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=OR24">OR24</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Ortona </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=OR24">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=oran">oran</a></td>
		<td class="nice"></td>
		<td class="nice">Aruba</td>
		<td class="nice" nowrap="">Oranjestad </td>
		<td class="nice" nowrap="">SONU10</td>
		<td class="nice" nowrap="">AA300044</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=oran">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=orma">orma</a></td>
		<td class="nice"></td>
		<td class="nice">Pakistan</td>
		<td class="nice" nowrap="">Ormara </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">262AD2C2</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=orma">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=oste">oste</a></td>
		<td class="nice"></td>
		<td class="nice">Belgium</td>
		<td class="nice" nowrap="">Ostend </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.48</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=oste">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=OT15">OT15</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Otranto </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.34</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-15 05:48</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>2d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=OT15">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=otat">otat</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Dunedin </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">OTAT</td>
		<td class="nice">5.16</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=otat">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ouin">ouin</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ouinne, New Caledonia </td>
		<td class="nice" nowrap="">SZNC43</td>
		<td class="nice" nowrap="">06522C44</td>
		<td class="nice">0.77</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ouin">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ouis">ouis</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ouistreham </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.52</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ouis">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ouis2">ouis2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ouistreham 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR311</td>
		<td class="nice">2.5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ouis2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ouve">ouve</a></td>
		<td class="nice"></td>
		<td class="nice">New Caledonia</td>
		<td class="nice" nowrap="">Ouvea </td>
		<td class="nice" nowrap="">SZNC45</td>
		<td class="nice" nowrap="">06523F32</td>
		<td class="nice">0.68</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 03:50</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ouve">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=PA07">PA07</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Palermo </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=PA07">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pada">pada</a></td>
		<td class="nice">45</td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Padang </td>
		<td class="nice" nowrap="">SZID50</td>
		<td class="nice" nowrap="">06510374 </td>
		<td class="nice">6.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=pada">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pagb">pagb</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Pago Bay, Guam </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.54</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=pagb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pago">pago</a></td>
		<td class="nice">144</td>
		<td class="nice">Samoa</td>
		<td class="nice" nowrap="">Pago Pago </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336015FC</td>
		<td class="nice">0.47</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=pago">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pagx">pagx</a></td>
		<td class="nice">144</td>
		<td class="nice">Samoa</td>
		<td class="nice" nowrap="">Pago Pago </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336312F2</td>
		<td class="nice">-2.57</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=pagx">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=palb">palb</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Port Alberni </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">15C3B04A</td>
		<td class="nice">-0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=palb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=palm">palm</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">PalmadeMallorca </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=palm">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=palm1">palm1</a></td>
		<td class="nice">329</td>
		<td class="nice">Cabo Verde</td>
		<td class="nice" nowrap="">Palmeira </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">26D6F7A6</td>
		<td class="nice">5.96</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=palm1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pano">pano</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Panormos </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">PANO</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-13 09:00</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>4d</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=pano">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pant">pant</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Pantelleria </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">PANT</td>
		<td class="nice">-0.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=pant">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pape">pape</a></td>
		<td class="nice">140</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Papeete (Tahiti, French Polynesia) </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3341D3F6</td>
		<td class="nice">6.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pape">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=papo">papo</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Paposo </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC285DE</td>
		<td class="nice">4.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=papo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=papo2">papo2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Paposo </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.02</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-16 07:00</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>1d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=papo2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=parh">parh</a></td>
		<td class="nice"></td>
		<td class="nice">Antigua</td>
		<td class="nice" nowrap="">Parham (Camp Blizard), Antigua </td>
		<td class="nice" nowrap="">SOAT10</td>
		<td class="nice" nowrap="">14022214</td>
		<td class="nice">0.3</td>
		<td class="nice" align="center" nowrap="">
			<small>13:43</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>1h</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=parh">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pata">pata</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Patache </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC22526</td>
		<td class="nice">4.42</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pata">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pata2">pata2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Patache </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pata2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pcha">pcha</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Chacabuco </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">1403B58C</td>
		<td class="nice">6.28</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=pcha">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pcha2">pcha2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Chacabuco </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.99</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=pcha2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pcor">pcor</a></td>
		<td class="nice"></td>
		<td class="nice">Honduras</td>
		<td class="nice" nowrap="">Puerto Cortes </td>
		<td class="nice" nowrap="">SOHO10</td>
		<td class="nice" nowrap="">50C44664</td>
		<td class="nice">9.31</td>
		<td class="nice" align="center" nowrap="">
			<small>14:00</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>44'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=pcor">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pdas">pdas</a></td>
		<td class="nice">245</td>
		<td class="nice">Portugal</td>
		<td class="nice" nowrap="">Ponta Delgada Azor </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">354271CC</td>
		<td class="nice">5.87</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pdas">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=PE09">PE09</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Porto empedocle </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.1</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=PE09">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pedn">pedn</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Eden </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">1400B282</td>
		<td class="nice">5.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=pedn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pedn2">pedn2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Eden </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.67</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=pedn2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=peir">peir</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Peiraias </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=peir">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=penr">penr</a></td>
		<td class="nice">143</td>
		<td class="nice">Cook Islands</td>
		<td class="nice" nowrap="">Penrhyn </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3541A0AA</td>
		<td class="nice">5.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=penr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=petr">petr</a></td>
		<td class="nice">93</td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Petropavlovsk </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.62</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=petr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=phbc">phbc</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Port Hardy </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">CD4038A0</td>
		<td class="nice">0.53</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=phbc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=phcp">phcp</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Port Hedland </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">62585</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=phcp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pich">pich</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Pichidangui </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">35402444</td>
		<td class="nice">5.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pich">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pich2">pich2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Pichidangui </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.76</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pich2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pich3">pich3</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Pichidangui </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.02</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-15 16:19</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>63d</small></td>
		<td class="nice" nowrap="" align="center"><small>2'</small></td>
		<td class="nice"><a href="station.php?code=pich3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pisa">pisa</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Pisagua </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC17254</td>
		<td class="nice">5.03</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pisa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pisa2">pisa2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Pisagua </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.44</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pisa2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pkem">pkem</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Port Kembla </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">60420</td>
		<td class="nice">0.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=pkem">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=PL14">PL14</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Palinuro </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.25</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=PL14">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=plat2">plat2</a></td>
		<td class="nice">192</td>
		<td class="nice">Argentina</td>
		<td class="nice" nowrap="">Mar del Plata </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3542B4D2</td>
		<td class="nice">9.46</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=plat2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=plmy">plmy</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Palmyra Island </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3541E3A0</td>
		<td class="nice">6.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=plmy">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pluz">pluz</a></td>
		<td class="nice">251</td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Puerto de la Luz </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.62</td>
		<td class="nice" align="center" nowrap="">
			<small>05:59</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>9h</small></td>
		<td class="nice" nowrap="" align="center"><small>1d</small></td>
		<td class="nice"><a href="station.php?code=pluz">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=plym">plym</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Plymouth </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=plym">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pmel">pmel</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Melinka </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">14000FDE</td>
		<td class="nice">5.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pmel">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pmel2">pmel2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Melinka </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pmel2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pmon">pmon</a></td>
		<td class="nice">178</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Montt </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">140642C8</td>
		<td class="nice">6.43</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=pmon">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pmon2">pmon2</a></td>
		<td class="nice">178</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Montt </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">6.56</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=pmon2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pmur">pmur</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">PtMurat </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">62430</td>
		<td class="nice">1.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=pmur">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pnfl">pnfl</a></td>
		<td class="nice">288</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Pensacola </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33A02AD0</td>
		<td class="nice">0.64</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pnfl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pnfl2">pnfl2</a></td>
		<td class="nice">288</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Pensacola </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33A02AD0</td>
		<td class="nice">-3.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pnfl2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=PO40">PO40</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Ponza </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=PO40">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pobe">pobe</a></td>
		<td class="nice"></td>
		<td class="nice">Belize</td>
		<td class="nice" nowrap="">Port of Belize </td>
		<td class="nice" nowrap="">SOBH10</td>
		<td class="nice" nowrap="">6B001EEE</td>
		<td class="nice">2.31</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pobe">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=porl">porl</a></td>
		<td class="nice">55</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Portland </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">61410</td>
		<td class="nice">0.67</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=porl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=porp">porp</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Portpatrick </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.47</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=porp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=port">port</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port-Bloc </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.6</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=port">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=port2">port2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port-Bloc2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR015</td>
		<td class="nice">4.55</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=port2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=posa">posa</a></td>
		<td class="nice"></td>
		<td class="nice">Portugal</td>
		<td class="nice" nowrap="">Porto Santo </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">POSA</td>
		<td class="nice">2.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=posa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=posi">posi</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Pos'et </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=posi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ppcp">ppcp</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Portopalo di Capo Passero </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">PPCP</td>
		<td class="nice">0.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ppcp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prai">prai</a></td>
		<td class="nice"></td>
		<td class="nice">Cabo Verde</td>
		<td class="nice" nowrap="">Praia </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap="">18F7C178</td>
		<td class="nice">0.69</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-07-10 19:15</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>342d</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=prai">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prat">prat</a></td>
		<td class="nice">189</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Antarctica Base Prat </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC191A6</td>
		<td class="nice">1.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=prat">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prat3">prat3</a></td>
		<td class="nice">189</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Antarctica Base Prat </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.78</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=prat3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prba">prba</a></td>
		<td class="nice"></td>
		<td class="nice">Guatemala</td>
		<td class="nice" nowrap="">Puerto Barrios </td>
		<td class="nice" nowrap="">SOGU40</td>
		<td class="nice" nowrap="">96500162</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=prba">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prec">prec</a></td>
		<td class="nice"></td>
		<td class="nice">Martinique</td>
		<td class="nice" nowrap="">Le Prêcheur </td>
		<td class="nice" nowrap="">SOMR10</td>
		<td class="nice" nowrap="">12A011E0</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=prec">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=preo">preo</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Preobrazheniye </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.19</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=preo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pric">pric</a></td>
		<td class="nice"></td>
		<td class="nice">Grenada</td>
		<td class="nice" nowrap="">Prickly Bay, Grenada </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3541B3DC</td>
		<td class="nice">5.16</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pric">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prig">prig</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Prigi </td>
		<td class="nice" nowrap="">SZID48</td>
		<td class="nice" nowrap="">0650F10A</td>
		<td class="nice">6.74</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=prig">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prin">prin</a></td>
		<td class="nice">155</td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Prince Rupert </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">6.45</td>
		<td class="nice" align="center" nowrap="">
			<small>09:45</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>5h</small></td>
		<td class="nice" nowrap="" align="center"><small>6h</small></td>
		<td class="nice"><a href="station.php?code=prin">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prin2">prin2</a></td>
		<td class="nice">155</td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Prince Rupert </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.76</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=prin2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prog">prog</a></td>
		<td class="nice">213</td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Progreso, Yuc </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.85</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=prog">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prog2">prog2</a></td>
		<td class="nice">213</td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Progreso, Yuc </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">01029134</td>
		<td class="nice">0.22</td>
		<td class="nice" align="center" nowrap="">
			<small>14:14</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>30'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=prog2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prud">prud</a></td>
		<td class="nice">151</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Prudhoe Bay </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33611706</td>
		<td class="nice">0.19</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=prud">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prud2">prud2</a></td>
		<td class="nice">151</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Prudhoe Bay </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33611706</td>
		<td class="nice">-4.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=prud2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=prus">prus</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Portrush </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=prus">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=psdn">psdn</a></td>
		<td class="nice"></td>
		<td class="nice">Nicaragua</td>
		<td class="nice" nowrap="">Puerto Sandino </td>
		<td class="nice" nowrap="">SXXX50</td>
		<td class="nice" nowrap="">0500F7AE</td>
		<td class="nice">0.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=psdn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=psla">psla</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Pilots Station East, SW Pass, LA </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.77</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=psla">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=psla2">psla2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Pilots Station East, SW Pass, LA </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">337363FC</td>
		<td class="nice">-3.32</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-12-05 18:15</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>194d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=psla2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pslu">pslu</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Port San Luis </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336A07D8</td>
		<td class="nice">0.25</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=pslu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pslu2">pslu2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Port San Luis </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336A07D8</td>
		<td class="nice">-5.32</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=pslu2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=PT17">PT17</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Porto Torres </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=PT17">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptal">ptal</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Aldea </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC1D2AC</td>
		<td class="nice">4.87</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptal">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptal2">ptal2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Aldea </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptal2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptan">ptan</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Puerto Angel </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">0100F126</td>
		<td class="nice">4.52</td>
		<td class="nice" align="center" nowrap="">
			<small>14:12</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>32'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ptan">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptan2">ptan2</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Puerto Angel </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.54</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ptan2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptar">ptar</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Punta Arenas </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">140064EA</td>
		<td class="nice">5.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ptar">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptar2">ptar2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Punta Arenas </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.85</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ptar2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptbl">ptbl</a></td>
		<td class="nice">38</td>
		<td class="nice">India</td>
		<td class="nice" nowrap="">Port Blair </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap="">43332</td>
		<td class="nice">1.93</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=ptbl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptca">ptca</a></td>
		<td class="nice"></td>
		<td class="nice">Dominican Republic</td>
		<td class="nice" nowrap="">Punta Cana </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">354041A2</td>
		<td class="nice">5.45</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptca">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptfe">ptfe</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port Ferréol </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.38</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptfe">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptfe2">ptfe2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port Ferréol 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR0847</td>
		<td class="nice">0.39</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ptfe2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptis">ptis</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Port Isaac </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.69</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.1666'</small></td>
		<td class="nice"><a href="station.php?code=ptis">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptln">ptln</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port-La-Nouvelle </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.46</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptln">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptln2">ptln2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port-la-Nouvelle 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR803</td>
		<td class="nice">0.46</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ptln2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptlu">ptlu</a></td>
		<td class="nice">18</td>
		<td class="nice">Mauritius</td>
		<td class="nice" nowrap="">Pt.Louis </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">165B3038</td>
		<td class="nice">1.67</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ptlu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptma">ptma</a></td>
		<td class="nice"></td>
		<td class="nice">Malta</td>
		<td class="nice" nowrap="">Portomaso </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:37</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=ptma">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptmd2">ptmd2</a></td>
		<td class="nice"></td>
		<td class="nice">Dominica island</td>
		<td class="nice" nowrap="">Portsmouth, Dominica </td>
		<td class="nice" nowrap="">SODO10</td>
		<td class="nice" nowrap="">6B0025A6</td>
		<td class="nice">3.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptmd2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptme">ptme</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Portland </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335F0668</td>
		<td class="nice">-3.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ptme">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptmt">ptmt</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Portsmouth </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.23</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ptmt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptos">ptos</a></td>
		<td class="nice"></td>
		<td class="nice">Brasil</td>
		<td class="nice" nowrap="">Porto de Santana </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">B5B00906</td>
		<td class="nice">3.09</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-02-01 05:42</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>136d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptos">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptpl">ptpl</a></td>
		<td class="nice"></td>
		<td class="nice">Dominican Republic</td>
		<td class="nice" nowrap="">Puerto Plata </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">35407438</td>
		<td class="nice">5.23</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptpl">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptpt">ptpt</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Pointe à Pitre, Guadeloupe </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptpt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptpt2">ptpt2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Pointe à Pitre, Guadeloupe 2 </td>
		<td class="nice" nowrap="">SZCA01</td>
		<td class="nice" nowrap="">FR125</td>
		<td class="nice">0.28</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ptpt2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptro">ptro</a></td>
		<td class="nice">210</td>
		<td class="nice">Jamaica</td>
		<td class="nice" nowrap="">Port Royal </td>
		<td class="nice" nowrap="">SOJM10</td>
		<td class="nice" nowrap="">92405008</td>
		<td class="nice"></td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptro">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptsc">ptsc</a></td>
		<td class="nice"></td>
		<td class="nice">Barbados</td>
		<td class="nice" nowrap="">Port St. Charles </td>
		<td class="nice" nowrap="">SOBR10</td>
		<td class="nice" nowrap="">BAB00078</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-09 22:46</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>8d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptsc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptsp">ptsp</a></td>
		<td class="nice">203</td>
		<td class="nice">Trinidad &amp; Tobago</td>
		<td class="nice" nowrap="">Port of Spain </td>
		<td class="nice" nowrap="">SOTD10</td>
		<td class="nice" nowrap="">A9C000B6</td>
		<td class="nice">3.72</td>
		<td class="nice" align="center" nowrap="">
			<small>13:32</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>1h</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=ptsp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptve">ptve</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port-Vendres </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=ptve">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ptve2">ptve2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port-Vendres2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR075</td>
		<td class="nice">0.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=ptve2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=puert">puert</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Puerto Vallarta </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">27.6</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=puert">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pumo">pumo</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Puerto Morelos, Q. R. </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=pumo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pumo2">pumo2</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Puerto Morelos </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">010F1446</td>
		<td class="nice">-0.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=pumo2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=puyt">puyt</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Puysegur Welcome Bay </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">PUYT</td>
		<td class="nice">6.33</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=puyt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pwil">pwil</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Williams </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC147CE</td>
		<td class="nice">3.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:18</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>26'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=pwil">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=pwil2">pwil2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Puerto Williams </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.35</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=pwil2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=qaqo">qaqo</a></td>
		<td class="nice">344</td>
		<td class="nice">Denmark</td>
		<td class="nice" nowrap="">Qaqortoq, Julianehab </td>
		<td class="nice" nowrap="">email</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-1.28</td>
		<td class="nice" align="center" nowrap="">
			<small>13:51</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>52'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=qaqo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=qcbc">qcbc</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Queen Charlotte </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">CD404E30</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-16 19:43</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>19h</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=qcbc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=qing">qing</a></td>
		<td class="nice"></td>
		<td class="nice">China</td>
		<td class="nice" nowrap="">Qinglan </td>
		<td class="nice" nowrap="">SZCI01</td>
		<td class="nice" nowrap="">11742</td>
		<td class="nice">0.97</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=qing">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=qtro">qtro</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Quintero </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC2662C</td>
		<td class="nice">4.86</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=qtro">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=qtro2">qtro2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Quintero </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=qtro2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=quar">quar</a></td>
		<td class="nice">77</td>
		<td class="nice">Hong Kong - China</td>
		<td class="nice" nowrap="">Quarry Bay </td>
		<td class="nice" nowrap="">SEHK40</td>
		<td class="nice" nowrap="">QUARYBAY</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=quar">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=quel">quel</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Queule </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC1E736</td>
		<td class="nice">4.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=quel">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=quel2">quel2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Queule </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.68</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=quel2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=quepo">quepo</a></td>
		<td class="nice">167</td>
		<td class="nice">Costa Rica</td>
		<td class="nice" nowrap="">Quepos </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3540A250</td>
		<td class="nice">4.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=quepo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=quin">quin</a></td>
		<td class="nice">75</td>
		<td class="nice">Viet Nam</td>
		<td class="nice" nowrap="">Qui Nhon </td>
		<td class="nice" nowrap="">SZVS40</td>
		<td class="nice" nowrap="">0650771E</td>
		<td class="nice">2.9</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=quin">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=quir">quir</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Quiriquina </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC2755A</td>
		<td class="nice">5.61</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=quir">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=quir2">quir2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Quiriquina </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=quir2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=qura">qura</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Qurayat </td>
		<td class="nice" nowrap="">SXOM33</td>
		<td class="nice" nowrap="">1842C770</td>
		<td class="nice">0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=qura">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=RA10">RA10</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Ravenna </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=RA10">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rangi">rangi</a></td>
		<td class="nice">355</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Rangiroa Atoll (Tuamotu, French Polynesia) </td>
		<td class="nice" nowrap="">SEHI40</td>
		<td class="nice" nowrap="">B1F00280</td>
		<td class="nice">0.6</td>
		<td class="nice" align="center" nowrap="">
			<small>14:00</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>44'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=rangi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=raro">raro</a></td>
		<td class="nice">139</td>
		<td class="nice">Cook Islands</td>
		<td class="nice" nowrap="">Rarotonga </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">65980</td>
		<td class="nice">0.45</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=raro">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rbct">rbct</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Raoul Island Boat Cove </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">RBCT</td>
		<td class="nice">5.67</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=rbct">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=RC09">RC09</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Reggio Calabria </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=RC09">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=reun">reun</a></td>
		<td class="nice">17</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Pointe des Galets (Reunion Island) </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.4</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=reun">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=reun2">reun2</a></td>
		<td class="nice">17</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Pointe des Galets (Reunion Island) 2 </td>
		<td class="nice" nowrap="">SZIO02</td>
		<td class="nice" nowrap="">FR110</td>
		<td class="nice">0.39</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=reun2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=reyk">reyk</a></td>
		<td class="nice">229</td>
		<td class="nice">Iceland</td>
		<td class="nice" nowrap="">Reykjavik </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.6</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=reyk">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rfrt">rfrt</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Raoul Island Fishing Rock </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">RFRT</td>
		<td class="nice">3.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=rfrt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=riki">riki</a></td>
		<td class="nice">138</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Rikitea (Gambier, French Polynesia) </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3541F0D6</td>
		<td class="nice">6.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=riki">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rodr">rodr</a></td>
		<td class="nice">19</td>
		<td class="nice">Mauritius</td>
		<td class="nice" nowrap="">Rodrigues </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">16590056</td>
		<td class="nice">1.87</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=rodr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rorv">rorv</a></td>
		<td class="nice">234</td>
		<td class="nice">Norway</td>
		<td class="nice" nowrap="">Rørvik </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.05</td>
		<td class="nice" align="center" nowrap="">
			<small>16:20</small></td>
		<td bgcolor="white" nowrap=""><small>-96'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=rorv">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rosc">rosc</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Roscoff </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=rosc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rosc2">rosc2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Roscoff 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR054</td>
		<td class="nice">5.97</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=rosc2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rose">rose</a></td>
		<td class="nice"></td>
		<td class="nice">Dominica island</td>
		<td class="nice" nowrap="">Roseau </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">354097CA</td>
		<td class="nice">5.59</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=rose">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ross">ross</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Rosslyn Bay </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">59670</td>
		<td class="nice">2.77</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=ross">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rothe">rothe</a></td>
		<td class="nice">342</td>
		<td class="nice">Antarctica</td>
		<td class="nice" nowrap="">Rothera </td>
		<td class="nice" nowrap="">SEMS40</td>
		<td class="nice" nowrap="">6B000D98</td>
		<td class="nice">2.78</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=rothe">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rous">rous</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ile Rousse </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=rous">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rous2">rous2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Ile Rousse2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR802</td>
		<td class="nice">0.33</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=rous2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rtas">rtas</a></td>
		<td class="nice"></td>
		<td class="nice">Honduras</td>
		<td class="nice" nowrap="">Roatan Island Punta Gorda Harbor </td>
		<td class="nice" nowrap="">SOHO10</td>
		<td class="nice" nowrap="">50CF45CC</td>
		<td class="nice">1.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:00</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>44'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=rtas">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=rudn">rudn</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Rudnaya Pristan </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=rudn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=SA16">SA16</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Salerno </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.31</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=SA16">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=saba">saba</a></td>
		<td class="nice">347</td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Sabang </td>
		<td class="nice" nowrap="">SZID45</td>
		<td class="nice" nowrap="">0650B200</td>
		<td class="nice">2.21</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=saba">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sado">sado</a></td>
		<td class="nice"></td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Sado </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">SADO</td>
		<td class="nice">1.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=sado">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sagr">sagr</a></td>
		<td class="nice"></td>
		<td class="nice">Portugal</td>
		<td class="nice" nowrap="">Sagres </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">SAGR</td>
		<td class="nice">1.35</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=sagr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sagu">sagu</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Sagunto </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.11</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=sagu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=said">said</a></td>
		<td class="nice"></td>
		<td class="nice">Morocco</td>
		<td class="nice" nowrap="">Saidia Marina </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">SAID</td>
		<td class="nice">1.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=said">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=saig">saig</a></td>
		<td class="nice"></td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Saigo </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">SAIGO</td>
		<td class="nice">2.02</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=saig">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sain">sain</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Saint-Nazaire </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.44</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sain">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sain2">sain2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Saint-Nazaire 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR037</td>
		<td class="nice">5.41</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sain2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=saip">saip</a></td>
		<td class="nice">118</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Saipan </td>
		<td class="nice" nowrap="">SWMY40</td>
		<td class="nice" nowrap="">06506468</td>
		<td class="nice">7.33</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=saip">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sali">sali</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Salina Cruz, Oax. </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.74</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=sali">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sali2">sali2</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Salina Cruz, Oax. </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">0103703C</td>
		<td class="nice">0.72</td>
		<td class="nice" align="center" nowrap="">
			<small>14:17</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>27'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sali2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=salv">salv</a></td>
		<td class="nice">334</td>
		<td class="nice">Brasil</td>
		<td class="nice" nowrap="">Salvador (Capitania dos Portos da Bahia) </td>
		<td class="nice" nowrap="">SEPA40</td>
		<td class="nice" nowrap="">354052D4</td>
		<td class="nice">6.83</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=salv">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sama">sama</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Santa Marta </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">35419530</td>
		<td class="nice">6.16</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sama">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=san2">san2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Santander </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.42</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=san2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sana">sana</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">San Andres </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">35418646</td>
		<td class="nice">5.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sana">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sand">sand</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">San Diego </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336275EE</td>
		<td class="nice">-3.47</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sand">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sanf">sanf</a></td>
		<td class="nice">177</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">San Felix </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC0A6C6</td>
		<td class="nice">5.88</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sanf">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sanf3">sanf3</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">San Felix </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.91</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-22 04:07</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>26d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sanf3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sanj">sanj</a></td>
		<td class="nice">206</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">San Juan </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335CA19E</td>
		<td class="nice">0.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sanj">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sanj2">sanj2</a></td>
		<td class="nice">206</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">San Juan </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335CA19E</td>
		<td class="nice">-2.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sanj2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sano">sano</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">San Antonio </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">1401F372</td>
		<td class="nice">5.6</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sano">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sano2">sano2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">San Antonio </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.05</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sano2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sanp">sanp</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">San Pedro </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC1A43C</td>
		<td class="nice">2.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sanp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sant">sant</a></td>
		<td class="nice"></td>
		<td class="nice">Ecuador</td>
		<td class="nice" nowrap="">SantaCruz,Galapagos </td>
		<td class="nice" nowrap="">SEEQ40</td>
		<td class="nice" nowrap="">932085F0</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-21 22:36</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>27d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sant">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sapz">sapz</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Sapzurro </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.95</td>
		<td class="nice" align="center" nowrap="">
			<small>14:17</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>27'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sapz">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sapz2">sapz2</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Sapzurro </td>
		<td class="nice" nowrap="">SXCO41</td>
		<td class="nice" nowrap="">15A045F2</td>
		<td class="nice">0.99</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sapz2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sass">sass</a></td>
		<td class="nice"></td>
		<td class="nice">Germany</td>
		<td class="nice" nowrap="">Sassnitz </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.91</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sass">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=saum">saum</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Saumlaki </td>
		<td class="nice" nowrap="">SZID41</td>
		<td class="nice" nowrap="">06503414</td>
		<td class="nice">5.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=saum">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=SB36">SB36</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">S.Benedetto Del Tronto </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=SB36">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sbea">sbea</a></td>
		<td class="nice">157</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">South Beach </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3368974E</td>
		<td class="nice">1.58</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-11-02 18:45</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>227d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sbea">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sbea2">sbea2</a></td>
		<td class="nice">157</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">South Beach </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3368974E</td>
		<td class="nice">-6.37</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sbea2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=SC43">SC43</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Sciacca </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=SC43">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=scar">scar</a></td>
		<td class="nice"></td>
		<td class="nice">Trinidad &amp; Tobago</td>
		<td class="nice" nowrap="">Scarborough </td>
		<td class="nice" nowrap="">SOTD10</td>
		<td class="nice" nowrap="">A9C0352C</td>
		<td class="nice">3.12</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 13:33</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=scar">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sche">sche</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Scheveningen </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:10</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>34'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=sche">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=scoa">scoa</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Socoa </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.1</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=scoa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=scoa2">scoa2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Socoa2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR095</td>
		<td class="nice">4.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=scoa2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=scor">scor</a></td>
		<td class="nice">315</td>
		<td class="nice">Denmark</td>
		<td class="nice" nowrap="">Ittoqqortoormiit, Scoresbysund </td>
		<td class="nice" nowrap="">email</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.26</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=scor">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sdpr">sdpr</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Sandown Pier </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.1666'</small></td>
		<td class="nice"><a href="station.php?code=sdpr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sdpt">sdpt</a></td>
		<td class="nice">100</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Sand Point </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33602066</td>
		<td class="nice">0.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sdpt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sdpt2">sdpt2</a></td>
		<td class="nice">100</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Sand Point </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33602066</td>
		<td class="nice">-4.68</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sdpt2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sebe">sebe</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Sebesi Island </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">SEBE</td>
		<td class="nice">0.91</td>
		<td class="nice" align="center" nowrap="">
			<small>14:40</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=sebe">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sema">sema</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Semarang </td>
		<td class="nice" nowrap="">SZID53</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.68</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=sema">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sete">sete</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Sète </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.36</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sete">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sete2">sete2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Sete 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR250</td>
		<td class="nice">0.35</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sete2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=setp1">setp1</a></td>
		<td class="nice">211</td>
		<td class="nice">Bahamas</td>
		<td class="nice" nowrap="">Settlement pt </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">3543234A</td>
		<td class="nice">3.47</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=setp1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=setu">setu</a></td>
		<td class="nice"></td>
		<td class="nice">Portugal</td>
		<td class="nice" nowrap="">Setubal </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">SETU</td>
		<td class="nice">-1.39</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=setu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sev2">sev2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Sevilla </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.42</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=sev2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sewa">sewa</a></td>
		<td class="nice">150</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Seward </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3362856A</td>
		<td class="nice">0.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sewa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sewa2">sewa2</a></td>
		<td class="nice">150</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Seward </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3362856A</td>
		<td class="nice">-7.71</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sewa2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=shee">shee</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Sheerness </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.27</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=shee">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=shek">shek</a></td>
		<td class="nice"></td>
		<td class="nice">Hong Kong - China</td>
		<td class="nice" nowrap="">Shek Pik </td>
		<td class="nice" nowrap="">SEHK40</td>
		<td class="nice" nowrap="">SHEK_PIK</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:35</small></td>
		<td bgcolor="white" nowrap=""><small>9'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=shek">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=shen">shen</a></td>
		<td class="nice"></td>
		<td class="nice">China</td>
		<td class="nice" nowrap="">Shenzhen </td>
		<td class="nice" nowrap="">SZCI01</td>
		<td class="nice" nowrap="">09733</td>
		<td class="nice">2.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=shen">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sian">sian</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Sian Ka'an </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:03</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>41'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=sian">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sibo">sibo</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Sibolga </td>
		<td class="nice" nowrap="">SZID46</td>
		<td class="nice" nowrap="">0650BCD2 </td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sibo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sino">sino</a></td>
		<td class="nice"></td>
		<td class="nice">Turkey</td>
		<td class="nice" nowrap="">Sinop </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.57</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>2'</small></td>
		<td class="nice"><a href="station.php?code=sino">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sisa">sisa</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Sisal </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.73</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-14 21:20</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>3d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=sisa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sitk">sitk</a></td>
		<td class="nice">154</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Sitka </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33625302</td>
		<td class="nice">-0.28</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sitk">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sitk2">sitk2</a></td>
		<td class="nice">154</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Sitka </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336056F6</td>
		<td class="nice">-7.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sitk2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sitt">sitt</a></td>
		<td class="nice">37</td>
		<td class="nice">Myanmar</td>
		<td class="nice" nowrap="">Sittwe </td>
		<td class="nice" nowrap="">SZBM41</td>
		<td class="nice" nowrap="">0650C490</td>
		<td class="nice">6.21</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sitt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=smag">smag</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Sanchez Magallanes </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=smag">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=smar2">smar2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Sainte Marie (Reunion island) 2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.54</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-05-14 03:03</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>34d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=smar2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=smog">smog</a></td>
		<td class="nice"></td>
		<td class="nice">Sweden</td>
		<td class="nice" nowrap="">Smogen </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.74</td>
		<td class="nice" align="center" nowrap="">
			<small>13:50</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>54'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=smog">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sobr">sobr</a></td>
		<td class="nice"></td>
		<td class="nice">Croatia</td>
		<td class="nice" nowrap="">Sobra </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.2</td>
		<td class="nice" align="center" nowrap="">
			<small>14:40</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=sobr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sole">sole</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Solenzara </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.42</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=sole">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sole2">sole2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Solenzara2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR710</td>
		<td class="nice">0.41</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=sole2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=solo">solo</a></td>
		<td class="nice">66</td>
		<td class="nice">Solomon Islands</td>
		<td class="nice" nowrap="">Honiara </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">56670</td>
		<td class="nice">0.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=solo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sosu">sosu</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Sosunovo </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.22</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=sosu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sove">sove</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Sovetskaja Gavan' </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=sove">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=spjy">spjy</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Southport Jetty </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">61240</td>
		<td class="nice">0.53</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=spjy">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=spmi">spmi</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Saint Pierre et Miquelon, Canada </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=spmi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sprg">sprg</a></td>
		<td class="nice">56</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Spring Bay </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">61170</td>
		<td class="nice">1.09</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=sprg">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sscr">sscr</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Second Severn Crossing </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-4.5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.1666'</small></td>
		<td class="nice"><a href="station.php?code=sscr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stan">stan</a></td>
		<td class="nice">305</td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Stanley </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">269375AE</td>
		<td class="nice">0.97</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=stan">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stari">stari</a></td>
		<td class="nice"></td>
		<td class="nice">Croatia</td>
		<td class="nice" nowrap="">Stari Grad </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.16</td>
		<td class="nice" align="center" nowrap="">
			<small>14:40</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=stari">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stcr">stcr</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">St Croix </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3365B2C4</td>
		<td class="nice">0.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=stcr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stcr2">stcr2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">St Croix </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3365B2C4</td>
		<td class="nice">-3.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=stcr2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sthl2">sthl2</a></td>
		<td class="nice">264</td>
		<td class="nice">Saint-Helena</td>
		<td class="nice" nowrap="">Saint Helena UK Ruperts Bay </td>
		<td class="nice" nowrap="">SXXX32</td>
		<td class="nice" nowrap="">18BC4718</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=sthl2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sthm">sthm</a></td>
		<td class="nice">341</td>
		<td class="nice">Sweden</td>
		<td class="nice" nowrap="">Stockholm </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">6.68</td>
		<td class="nice" align="center" nowrap="">
			<small>13:55</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>49'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=sthm">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stjo">stjo</a></td>
		<td class="nice">223</td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">St. Johns </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.99</td>
		<td class="nice" align="center" nowrap="">
			<small>10:00</small></td>
		<td style="color:white;background-color:#FF0000" nowrap=""><small>5h</small></td>
		<td class="nice" nowrap="" align="center"><small>6h</small></td>
		<td class="nice"><a href="station.php?code=stjo">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stlo2">stlo2</a></td>
		<td class="nice"></td>
		<td class="nice">Sénégal</td>
		<td class="nice" nowrap="">StLouis </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">10.47</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-03-09 09:45</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>465d</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=stlo2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stlu">stlu</a></td>
		<td class="nice"></td>
		<td class="nice">Saint Lucia</td>
		<td class="nice" nowrap="">Ganter's Bay </td>
		<td class="nice" nowrap="">SOLC10</td>
		<td class="nice" nowrap="">6B00103C</td>
		<td class="nice">2.34</td>
		<td class="nice" align="center" nowrap="">
			<small>14:26</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>18'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=stlu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stma">stma</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Saint-Malo </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=stma">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stma2">stma2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Saint-Malo 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR410</td>
		<td class="nice">3.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:31</small></td>
		<td bgcolor="white" nowrap=""><small>13'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=stma2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stmr">stmr</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">St Marys </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.66</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=stmr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stmt">stmt</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Saint Martin Island </td>
		<td class="nice" nowrap="">SXMF40</td>
		<td class="nice" nowrap="">12A01F32</td>
		<td class="nice">-0.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:11</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>33'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=stmt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stor">stor</a></td>
		<td class="nice">238</td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Stornoway </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.48</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=stor">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stqy">stqy</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Saint-Quay-Portrieux </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.56</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=stqy">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=stqy2">stqy2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Saint-Quay-Portrieux 2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR0506</td>
		<td class="nice">4.58</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=stqy2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=subi">subi</a></td>
		<td class="nice"></td>
		<td class="nice">Philippines</td>
		<td class="nice" nowrap="">Subic Bay </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">3226F4BE</td>
		<td class="nice">5.25</td>
		<td class="nice" align="center" nowrap="">
			<small>14:16</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>28'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=subi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=sura">sura</a></td>
		<td class="nice"></td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Surabaya </td>
		<td class="nice" nowrap="">SZID51</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.38</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=sura">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=suro">suro</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Sur </td>
		<td class="nice" nowrap="">SXOM33</td>
		<td class="nice" nowrap="">188263EC</td>
		<td class="nice">0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=suro">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=swpr">swpr</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Swanage Pier </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.47</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.1666'</small></td>
		<td class="nice"><a href="station.php?code=swpr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=syow">syow</a></td>
		<td class="nice">95</td>
		<td class="nice">Antarctica</td>
		<td class="nice" nowrap="">Syowa </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">8.19</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-03-06 23:55</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>103d</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=syow">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=syro">syro</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Syros </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.66</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=syro">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=TA18">TA18</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Taranto </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=TA18">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tala">tala</a></td>
		<td class="nice"></td>
		<td class="nice">Perú</td>
		<td class="nice" nowrap="">Talara </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">35414358</td>
		<td class="nice">0.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=tala">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=talc">talc</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Talcahuano </td>
		<td class="nice" nowrap="">SXCH40</td>
		<td class="nice" nowrap="">ADC0C320</td>
		<td class="nice">5.65</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=talc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=talc2">talc2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Talcahuano </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.06</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=talc2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=talt2">talt2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Taltal </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">5.63</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>7'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=talt2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tara">tara</a></td>
		<td class="nice">113</td>
		<td class="nice">Kiribati</td>
		<td class="nice" nowrap="">Betio,Tarawa </td>
		<td class="nice" nowrap="">SZPA01</td>
		<td class="nice" nowrap="">67590</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=tara">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tare">tare</a></td>
		<td class="nice"></td>
		<td class="nice">Solomon Islands</td>
		<td class="nice" nowrap="">Tarekukure Wharf </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">56363</td>
		<td class="nice">1.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=tare">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tari">tari</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Tarifa </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.19</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=tari">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tarr">tarr</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Tarragona </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.27</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=tarr">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=taut">taut</a></td>
		<td class="nice"></td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Port of Tauranga </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">TAUT</td>
		<td class="nice">4.54</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=taut">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tbwc">tbwc</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Twofold Bay </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">60531</td>
		<td class="nice">0.85</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=tbwc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=telc">telc</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Telchac </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.47</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-14 19:51</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>3d</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=telc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tene">tene</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Tenerife2 </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.27</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=tene">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ters">ters</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Terschelling Noordzee </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-1.32</td>
		<td class="nice" align="center" nowrap="">
			<small>14:10</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>34'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=ters">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tfbc">tfbc</a></td>
		<td class="nice">156</td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Tofino </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">15C3A33C</td>
		<td class="nice">0.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=tfbc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=thes">thes</a></td>
		<td class="nice"></td>
		<td class="nice">Greece</td>
		<td class="nice" nowrap="">Thessaloniki </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.26</td>
		<td class="nice" align="center" nowrap="">
			<small>14:18</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>26'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=thes">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=thev">thev</a></td>
		<td class="nice">308</td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Thevenard </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">62000</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=thev">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=thio">thio</a></td>
		<td class="nice"></td>
		<td class="nice">New Caledonia</td>
		<td class="nice" nowrap="">Thio </td>
		<td class="nice" nowrap="">SZNC44</td>
		<td class="nice" nowrap="">xxxxxxx</td>
		<td class="nice">0.81</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=thio">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=thul">thul</a></td>
		<td class="nice">343</td>
		<td class="nice">Denmark</td>
		<td class="nice" nowrap="">Thule, Pituffik </td>
		<td class="nice" nowrap="">email</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.18</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=thul">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=toama">toama</a></td>
		<td class="nice"></td>
		<td class="nice">Madagascar</td>
		<td class="nice" nowrap="">Toamasina </td>
		<td class="nice" nowrap="">SZIO03</td>
		<td class="nice" nowrap="">FR041</td>
		<td class="nice">0.75</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=toama">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tobe">tobe</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Tobermory </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=tobe">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=toco2">toco2</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Tocopilla </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.19</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=toco2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=toco3">toco3</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Tocopilla </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.24</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=toco3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tosa">tosa</a></td>
		<td class="nice"></td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Tosashimizu </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">TOSASHIMIZU</td>
		<td class="nice">2.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=tosa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=toul">toul</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Toulon </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=toul">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=toul2">toul2</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Toulon2 </td>
		<td class="nice" nowrap="">SZFR01</td>
		<td class="nice" nowrap="">FR0680</td>
		<td class="nice">0.3</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=toul2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=toya">toya</a></td>
		<td class="nice">325</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Toyama </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">TOYAMA</td>
		<td class="nice">2.16</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=toya">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=TR22">TR22</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Trieste </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.15</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=TR22">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=treg">treg</a></td>
		<td class="nice">321</td>
		<td class="nice">Norway</td>
		<td class="nice" nowrap="">Tregde </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.42</td>
		<td class="nice" align="center" nowrap="">
			<small>16:20</small></td>
		<td bgcolor="white" nowrap=""><small>-96'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=treg">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=trin">trin</a></td>
		<td class="nice"></td>
		<td class="nice">Sri Lanka</td>
		<td class="nice" nowrap="">Trinconmalee </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">322952D4</td>
		<td class="nice">0.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=trin">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=trnz">trnz</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Terneuzen </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.09</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=trnz">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=trst">trst</a></td>
		<td class="nice"></td>
		<td class="nice">Australia</td>
		<td class="nice" nowrap="">Torres Strait </td>
		<td class="nice" nowrap="">SZAU01</td>
		<td class="nice" nowrap="">58170</td>
		<td class="nice">2.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=trst">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tubua">tubua</a></td>
		<td class="nice">356</td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Tubuai (Austral Islands - French Polynesia) </td>
		<td class="nice" nowrap="">SEHI40</td>
		<td class="nice" nowrap="">FFF0073A</td>
		<td class="nice">0.5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=tubua">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tudy">tudy</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Port-Tudy (Groix island) </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.76</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=tudy">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tumc">tumc</a></td>
		<td class="nice"></td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Tumaco </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.82</td>
		<td class="nice" align="center" nowrap="">
			<small>13:48</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>56'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=tumc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tumc2">tumc2</a></td>
		<td class="nice">171</td>
		<td class="nice">Colombia</td>
		<td class="nice" nowrap="">Tumaco </td>
		<td class="nice" nowrap="">SXCO41</td>
		<td class="nice" nowrap="">15AAC2B4</td>
		<td class="nice">30.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=tumc2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=tuxp">tuxp</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Tuxpan </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.41</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=tuxp">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ulla">ulla</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Ullapool </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.61</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ulla">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=upol">upol</a></td>
		<td class="nice"></td>
		<td class="nice">Samoa</td>
		<td class="nice" nowrap="">Apia Upolu </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">66840</td>
		<td class="nice">1.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=upol">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ushu">ushu</a></td>
		<td class="nice">181</td>
		<td class="nice">Argentina</td>
		<td class="nice" nowrap="">Ushuaia </td>
		<td class="nice" nowrap="">SEPO40</td>
		<td class="nice" nowrap="">334CE50A</td>
		<td class="nice">6.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:19</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>25'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ushu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vair">vair</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Vairao (Tahiti Island - French Polynesia) </td>
		<td class="nice" nowrap="">SEHI40</td>
		<td class="nice" nowrap="">FAA022BE</td>
		<td class="nice">0.48</td>
		<td class="nice" align="center" nowrap="">
			<small>13:59</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>45'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=vair">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vale">vale</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Valencia </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.08</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=vale">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=valp2">valp2</a></td>
		<td class="nice">175</td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Valparaiso </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=valp2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=valp3">valp3</a></td>
		<td class="nice"></td>
		<td class="nice">Chile</td>
		<td class="nice" nowrap="">Valparaiso </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>2'</small></td>
		<td class="nice"><a href="station.php?code=valp3">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vanu">vanu</a></td>
		<td class="nice">348</td>
		<td class="nice">Vanuatu</td>
		<td class="nice" nowrap="">Port Villa, Vanuatu </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">57320</td>
		<td class="nice">0.73</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=vanu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vard">vard</a></td>
		<td class="nice">323</td>
		<td class="nice">Norway</td>
		<td class="nice" nowrap="">Vardø </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.61</td>
		<td class="nice" align="center" nowrap="">
			<small>16:20</small></td>
		<td bgcolor="white" nowrap=""><small>-96'</small></td>
		<td class="nice" nowrap="" align="center"><small>1h</small></td>
		<td class="nice"><a href="station.php?code=vard">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vati">vati</a></td>
		<td class="nice"></td>
		<td class="nice">Fiji Islands</td>
		<td class="nice" nowrap="">Vatia, Viti Levu </td>
		<td class="nice" nowrap="">SZFJ40</td>
		<td class="nice" nowrap="">91000</td>
		<td class="nice">1.07</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=vati">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=VE19">VE19</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Venice </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=VE19">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vela">vela</a></td>
		<td class="nice"></td>
		<td class="nice">Croatia</td>
		<td class="nice" nowrap="">Vela Luka </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.12</td>
		<td class="nice" align="center" nowrap="">
			<small>14:40</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=vela">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=ver1">ver1</a></td>
		<td class="nice">188</td>
		<td class="nice">Antarctica</td>
		<td class="nice" nowrap="">Vernadsky - Faraday </td>
		<td class="nice" nowrap="">SEMS40</td>
		<td class="nice" nowrap="">3354E632</td>
		<td class="nice">2.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:09</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>35'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=ver1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vera">vera</a></td>
		<td class="nice">212</td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Veracruz, Ver. </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">27.6</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=vera">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vera2">vera2</a></td>
		<td class="nice">212</td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Veracruz, Ver. </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">0102A4AE</td>
		<td class="nice">1.8</td>
		<td class="nice" align="center" nowrap="">
			<small>14:10</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>34'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=vera2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=verav">verav</a></td>
		<td class="nice">31</td>
		<td class="nice">India</td>
		<td class="nice" nowrap="">Veeraval </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap="">42910</td>
		<td class="nice">2.82</td>
		<td class="nice" align="center" nowrap="">
			<small>14:27</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>17'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=verav">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vern">vern</a></td>
		<td class="nice">188</td>
		<td class="nice">Antarctica</td>
		<td class="nice" nowrap="">Vernadsky - Faraday </td>
		<td class="nice" nowrap="">SEMS40</td>
		<td class="nice" nowrap="">3354E632</td>
		<td class="nice">2.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:09</small></td>
		<td style="color:black;background-color:#FFFF00" nowrap=""><small>35'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=vern">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vhbc">vhbc</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Vancouver Harbor </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">CD400D3A</td>
		<td class="nice">3.52</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=vhbc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=VI12">VI12</a></td>
		<td class="nice"></td>
		<td class="nice">Italy</td>
		<td class="nice" nowrap="">Vieste </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.13</td>
		<td class="nice" align="center" nowrap="">
			<small>14:42</small></td>
		<td bgcolor="white" nowrap=""><small>2'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=VI12">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vibc">vibc</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Victoria Harbor </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">CD405D46</td>
		<td class="nice">1.1</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=vibc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vieq">vieq</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Vieques </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">335CC478</td>
		<td class="nice">-0</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=vieq">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vieq2">vieq2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Vieques </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">335CC478</td>
		<td class="nice">-3.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=vieq2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vig2">vig2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Vigo </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.48</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>5'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=vig2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vil2">vil2</a></td>
		<td class="nice"></td>
		<td class="nice">Spain</td>
		<td class="nice" nowrap="">Villagarcia </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.7</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>4'</small></td>
		<td class="nice"><a href="station.php?code=vil2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vish">vish</a></td>
		<td class="nice">35</td>
		<td class="nice">India</td>
		<td class="nice" nowrap="">Visakhapatnam </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap="">43151</td>
		<td class="nice">1.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:23</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>21'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=vish">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=viti">viti</a></td>
		<td class="nice">122</td>
		<td class="nice">Fiji Islands</td>
		<td class="nice" nowrap="">Suva Viti Levu </td>
		<td class="nice" nowrap="">SZPS01</td>
		<td class="nice" nowrap="">67050</td>
		<td class="nice">0.92</td>
		<td class="nice" align="center" nowrap="">
			<small>14:38</small></td>
		<td bgcolor="white" nowrap=""><small>6'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=viti">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vlad">vlad</a></td>
		<td class="nice"></td>
		<td class="nice">Russia</td>
		<td class="nice" nowrap="">Vladivostok </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.38</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=vlad">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vlis">vlis</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Vlissingen </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">1.71</td>
		<td class="nice" align="center" nowrap="">
			<small>14:20</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>24'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=vlis">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vlrn">vlrn</a></td>
		<td class="nice"></td>
		<td class="nice">Netherlands</td>
		<td class="nice" nowrap="">Vlakte v/d Raan </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">342.8</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-06-04 06:00</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>13d</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=vlrn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=vung">vung</a></td>
		<td class="nice"></td>
		<td class="nice">Viet Nam</td>
		<td class="nice" nowrap="">Vung Tau </td>
		<td class="nice" nowrap="">SZVS41</td>
		<td class="nice" nowrap="">06506ABA</td>
		<td class="nice">0.79</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=vung">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=waik">waik</a></td>
		<td class="nice">346</td>
		<td class="nice">Indonesia</td>
		<td class="nice" nowrap="">Waikelo </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">32A89288</td>
		<td class="nice">-999</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=waik">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=waka">waka</a></td>
		<td class="nice">324</td>
		<td class="nice">Japan</td>
		<td class="nice" nowrap="">Wakkanai </td>
		<td class="nice" nowrap="">SWJP40</td>
		<td class="nice" nowrap="">WAKKANAI</td>
		<td class="nice">1.98</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>10'</small></td>
		<td class="nice"><a href="station.php?code=waka">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wake">wake</a></td>
		<td class="nice">105</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Wake </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3349124E</td>
		<td class="nice">0.89</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=wake">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wake2">wake2</a></td>
		<td class="nice">105</td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Wake </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3349124E</td>
		<td class="nice">-2.89</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-04-07 18:07</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>71d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=wake2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wall">wall</a></td>
		<td class="nice"></td>
		<td class="nice">France</td>
		<td class="nice" nowrap="">Mata-Utu (Wallis island) </td>
		<td class="nice" nowrap="">SZFW41</td>
		<td class="nice" nowrap="">0652170C </td>
		<td class="nice">1.29</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=wall">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=warn">warn</a></td>
		<td class="nice"></td>
		<td class="nice">Germany</td>
		<td class="nice" nowrap="">Warnemünde </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.91</td>
		<td class="nice" align="center" nowrap="">
			<small>14:36</small></td>
		<td bgcolor="white" nowrap=""><small>8'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=warn">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wbhb">wbhb</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">West Bay Harbour </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">-0.31</td>
		<td class="nice" align="center" nowrap="">
			<small>14:39</small></td>
		<td bgcolor="white" nowrap=""><small>4'</small></td>
		<td class="nice" nowrap="" align="center"><small>0.1666'</small></td>
		<td class="nice"><a href="station.php?code=wbhb">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=weym">weym</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Weymouth </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">0.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=weym">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=whbc">whbc</a></td>
		<td class="nice"></td>
		<td class="nice">Canada</td>
		<td class="nice" nowrap="">Winter Harbour </td>
		<td class="nice" nowrap="">SXAK50</td>
		<td class="nice" nowrap="">15C385D0</td>
		<td class="nice">0.14</td>
		<td class="nice" align="center" nowrap="">
			<small>14:30</small></td>
		<td bgcolor="white" nowrap=""><small>14'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=whbc">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=whit">whit</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Whitby </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.68</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=whit">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wick">wick</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Wick Harbour </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">2.01</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=wick">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wlgt">wlgt</a></td>
		<td class="nice">101</td>
		<td class="nice">New Zealand</td>
		<td class="nice" nowrap="">Wellington </td>
		<td class="nice" nowrap="">SZNZ01</td>
		<td class="nice" nowrap="">WLGT</td>
		<td class="nice">3.04</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>3'</small></td>
		<td class="nice"><a href="station.php?code=wlgt">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wlms">wlms</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Bay Waveland Yacht Club, MS </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33456542</td>
		<td class="nice">0.87</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=wlms">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wlms2">wlms2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Bay Waveland Yacht Club, MS </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">33456542</td>
		<td class="nice">-8.55</td>
		<td class="nice" align="center" nowrap="">
			<small>14:22</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>22'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=wlms2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wood">wood</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Woods Hole, MA </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">3340A79C</td>
		<td class="nice">0.49</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=wood">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wood2">wood2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Woods Hole, MA </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3340A79C</td>
		<td class="nice">-3.72</td>
		<td class="nice" align="center" nowrap="">
			<small>14:21</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>23'</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=wood2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=work">work</a></td>
		<td class="nice"></td>
		<td class="nice">UK</td>
		<td class="nice" nowrap="">Workington </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">4.94</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=work">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wpwa">wpwa</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Westport, WA </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">33632768</td>
		<td class="nice">-0.66</td>
		<td class="nice" align="center" nowrap="">
			<small>14:29</small></td>
		<td bgcolor="white" nowrap=""><small>15'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=wpwa">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=wuda">wuda</a></td>
		<td class="nice"></td>
		<td class="nice">Oman</td>
		<td class="nice" nowrap="">Khawr Wudam </td>
		<td class="nice" nowrap="">SXOM33</td>
		<td class="nice" nowrap="">18539268</td>
		<td class="nice">0.14</td>
		<td class="nice" align="center" nowrap="">
			<small>2018-09-29 02:58</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>261d</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=wuda">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=xmas">xmas</a></td>
		<td class="nice">146</td>
		<td class="nice">Kiribati</td>
		<td class="nice" nowrap="">Christmas </td>
		<td class="nice" nowrap="">SEPA40</td>
		<td class="nice" nowrap="">3542F7D8</td>
		<td class="nice">4.31</td>
		<td class="nice" align="center" nowrap="">
			<small>14:15</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>29'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=xmas">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=yabu">yabu</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Yabucoa Harbor, PR </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">3366B5CA</td>
		<td class="nice">-6.17</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=yabu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=yaku">yaku</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Yakutat </td>
		<td class="nice" nowrap="">web</td>
		<td class="nice" nowrap="">336B0522</td>
		<td class="nice">0.03</td>
		<td class="nice" align="center" nowrap="">
			<small>14:25</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>19'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=yaku">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=yaku2">yaku2</a></td>
		<td class="nice"></td>
		<td class="nice">USA</td>
		<td class="nice" nowrap="">Yakutat </td>
		<td class="nice" nowrap="">SXXX03</td>
		<td class="nice" nowrap="">336B0522</td>
		<td class="nice">-9.44</td>
		<td class="nice" align="center" nowrap="">
			<small>14:24</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>20'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=yaku2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=yapi">yapi</a></td>
		<td class="nice">119</td>
		<td class="nice">Micronesia</td>
		<td class="nice" nowrap="">Yap Island </td>
		<td class="nice" nowrap="">SWPA41</td>
		<td class="nice" nowrap="">065012F8</td>
		<td class="nice">1.72</td>
		<td class="nice" align="center" nowrap="">
			<small>14:34</small></td>
		<td bgcolor="white" nowrap=""><small>10'</small></td>
		<td class="nice" nowrap="" align="center"><small>6'</small></td>
		<td class="nice"><a href="station.php?code=yapi">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=zanz">zanz</a></td>
		<td class="nice">297</td>
		<td class="nice">Tanzania</td>
		<td class="nice" nowrap="">Zanzibar </td>
		<td class="nice" nowrap="">SXXX33</td>
		<td class="nice" nowrap="">1605D3E0</td>
		<td class="nice">4.97</td>
		<td class="nice" align="center" nowrap="">
			<small>14:28</small></td>
		<td style="color:black; background-color:#AAFFAA" nowrap=""><small>16'</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=zanz">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=zhap">zhap</a></td>
		<td class="nice">78</td>
		<td class="nice">China</td>
		<td class="nice" nowrap="">Zhapo </td>
		<td class="nice" nowrap="">SZCI01</td>
		<td class="nice" nowrap="">09731</td>
		<td class="nice">2.5</td>
		<td class="nice" align="center" nowrap="">
			<small>14:33</small></td>
		<td bgcolor="white" nowrap=""><small>11'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=zhap">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=zihu">zihu</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Zihuatanejo, Gro </td>
		<td class="nice" nowrap="">ftp</td>
		<td class="nice" nowrap=""></td>
		<td class="nice">3.3</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-02-11 15:13</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>126d</small></td>
		<td class="nice" nowrap="" align="center"><small>15'</small></td>
		<td class="nice"><a href="station.php?code=zihu">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=zihu2">zihu2</a></td>
		<td class="nice"></td>
		<td class="nice">Mexico</td>
		<td class="nice" nowrap="">Zihuatanejo, Gro </td>
		<td class="nice" nowrap="">SOMX10</td>
		<td class="nice" nowrap="">0102D23E</td>
		<td class="nice">3.37</td>
		<td class="nice" align="center" nowrap="">
			<small>2019-02-11 15:08</small></td>
		<td style="color:white;background-color:#000000" nowrap=""><small>126d</small></td>
		<td class="nice" nowrap="" align="center"><small>5'</small></td>
		<td class="nice"><a href="station.php?code=zihu2">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr><tr>
		<td class="nice"><a href="station.php?code=zygi1">zygi1</a></td>
		<td class="nice"></td>
		<td class="nice">Cyprus</td>
		<td class="nice" nowrap="">Zygi </td>
		<td class="nice" nowrap="">bgan</td>
		<td class="nice" nowrap="">ZYGI1</td>
		<td class="nice">0.53</td>
		<td class="nice" align="center" nowrap="">
			<small>14:32</small></td>
		<td bgcolor="white" nowrap=""><small>12'</small></td>
		<td class="nice" nowrap="" align="center"><small>1'</small></td>
		<td class="nice"><a href="station.php?code=zygi1">&nbsp;&nbsp;[open]&nbsp;&nbsp;</a></td>
		</tr></tbody></table> </form></td></tr>
 </tbody></table> </div>
 </td></tr>
 <tr>
  <td>
  <hr>
 	<div class="footer_left">Site developed and maintained by <a href="http://www.vliz.be" target="_blank">VLIZ</a> for <a href="http://www.ioc-unesco.org" target="_blank">UNESCO/IOC</a></div>
 	<div class="footer_right"><a href="disclaimer.php">disclaimer</a> | <a href="mailto:info@ioc-sealevelmonitoring.org">contact</a></div>
  </td>
  </tr>
 </tbody></table>
</td></tr></tbody></table>

</body></html>"""
