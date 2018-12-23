
//////////////////////////////navbar
  $(document).ready(function(){
	  //alert("0");
	  var lastScrollTop = 0;
var navbar        = $('.navbar-fixed-top');
$(window).scroll(function(event){
   var st = $(this).scrollTop();
   if (st > lastScrollTop){
       navbar.addClass('navbar-scroll-custom');
   } else {
      navbar.removeClass('navbar-scroll-custom');
   }
   lastScrollTop = st;
});    
  });
//////////////////////////////navbar

  function go_iframe(id,loc) {
    document.getElementById(id).src = loc;
  }


	function report_book($id,$info){
	//alert($id);
	//alert(document.location.href);
if($info == null){
var $info = prompt('تبليغ عن الكتاب | ماهي المشكلة في الملف أو الكتاب ؟ شكراً لتعاونكم', 'هنا يمكنك كتابة وتوضيح المشكلة والأسباب ...........................');
}
if(($info != 'هنا يمكنك كتابة وتوضيح المشكلة والأسباب ...........................')&&($info != 'null')&&($info != '')){
$.post( 'report_book.php', { id: $id, report: $info })
	.done(function( data ) {
    var vl =data;
	if((vl != "")&&(vl != null)){
	alert(vl);	    
	}
	});
}else{
alert("يجب كتابة أسباب تبليغك عن الكتاب والتأكد منها أولاً");
}

  return false;
	}
	
///////////////////////////////////////////// LOAD AJAX

var xmlHttp;
var obj;

function Ajex(obje,pag,str)
	{
		xmlHttp = GetXmlHttpObject();
		if (xmlHttp==null)
		 {
		 alert ("متصفحك لا يدعم الـ HTTP Request");
		 return;
		 }
		obj = obje;
		var url=pag;
		url=url+str;
		url=url+"&bspgid="+Math.random();
		xmlHttp.onreadystatechange=stateChanged;
		xmlHttp.open("GET",url,true);
		xmlHttp.send(null);
	}
	
function get_data(obj,file){

  $(document).ready(function(){
  alert(obj);
      $("#"+obj).load(file+"&ajax=1&obj="+obj);
  });
  return false;
}
function get_data3(obj,file){

  $(document).ready(function(){
      $("#"+obj).load(file+"&ajax=1&obj="+obj);
  });


  return false;
}
function get_data4(obj,file){

  $(document).ready(function(){
      $("#"+obj).load(file+"&ajax=1&obj="+obj);
  });


  return false;
}
function get_data2(obje,pag,FIELD)
	{
		xmlHttp = GetXmlHttpObject();

              if (xmlHttp==null)
		 {
		 alert ("متصفحك لا يدعم الـ HTTP Request");
		 return;
		 }
		obj = obje;
		var url=pag;
		url=url+"&bspgid="+Math.random()+"&ajax=1&obj="+obje;
		xmlHttp.onreadystatechange=stateChanged;
		xmlHttp.open("GET",url,true);
		xmlHttp.send(null);

       if (FIELD!=null){
          get_data('submenu','menu-field.php?pag='+pag+'&field='+FIELD);
       }
	}

function stateChanged()
	{
		if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete")
		 {
			document.getElementById(obj).innerHTML=xmlHttp.responseText;
			document.body.style.cursor='auto';
		 }
		else {
			document.getElementById(obj).innerHTML="<div style='padding:25px;'><center><img src='images/loader.gif' /></center></div>";
			document.body.style.cursor='wait';

			}
	 }

function GetXmlHttpObject()
	{
		var xmlHttp=null;
		try
		 {
		 xmlHttp=new XMLHttpRequest();
		 }
		catch (e)
		 {
		 try
		  {
		  xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
		  }
		 catch (e)
		  {
		  xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
		  }
		 }
		return xmlHttp;
	}
///////////////////////////////////////////// LOAD AJAX


///////// Change value//////////////////////////////////////////////
function chValu(id,value,type){
	    var rid = document.getElementById(id);

		// alert (rows.length);
		if(type == "html"){
		rid.innerHTML = value;
		}

		if(type == "href"){
		rid.href = value;
		}else{
		rid.value = value;
		}
}
///////////////////////////////////////////////////////



///////////////////////////////////////////////////////
function SelectAll(id)
{
    document.getElementById(id).focus();
    document.getElementById(id).select();
}
///////////////////////////////////////////////////////

function expend( forma , less) {
	    var rows = document.getElementById(forma).getElementsByClassName('arrow');
		// alert (rows.length);

		for ( var i = 0; i < rows.length; i++ ) {
			if(rows[i].id != less){

			rows[i].style.display = "none";
			}else{
			rows[i].style.display = "block";
			//i++;
			//alert(rows[i].id + '   ' + i);
			}
		}


}
function unexpend( forma , less) {
	    var rows = document.getElementById(forma).getElementsByTagName('ul');
		//alert (rows.length);

		for ( var i = 0; i < rows.length; i++ ) {
		rows[i].style.display = "";
		}
		document.getElementById(less).style.display = "block";

}


 function highlight(field) {
        field.focus();
        field.select();
  }


function popUp(URL, w, h){
day = new Date();
id = day.getTime();
URL = URL;
left = 400-(w/2);
gtop = 300-(h/2);
eval("HimozUpload" + id + " = window.open(URL,'" + id + "', 'toolbar=0,scrollbars=1,location=1,statusbar=0,menubar=0,resizable=1,width= "+ w +" ,height= "+ h +",left="+ left +",top="+ gtop +"');");
return false
}


//////////////////////////////////////////////////

function setStyle(x,c)
{
	document.getElementById(x).style.background=c;
}
//////////////////////////////////////////////////



///////////////////..........................
function UNmarkAll( forma ) {
	    var rows = document.getElementById(forma).getElementsByTagName('input');
		//alert (rows.length);

		for ( var i = 0; i < rows.length; i++ ) {
		rows[i].checked = false;
		}

}


function markAll( forma ) {
	    var rows = document.getElementById(forma).getElementsByTagName('input');
		//alert (rows.length);

		for ( var i = 0; i < rows.length; i++ ) {
		rows[i].checked = true;
		}

}
///////////////////..........................


function timedCount()
{
document.getElementById('txt').value=c;
c=c+1;
t=setTimeout("timedCount()",1000);
}

function doTimer()
{
if (!timer_is_on)
  {
  timer_is_on=1;
  timedCount();
  }
}

function stopCount()
{
clearTimeout(t);
timer_is_on=0;
}


//////////////////////////////////////////////////
function hideElement(Element)
{
document.getElementById(Element).style.display='none'
}

function showElement(Element)
{
document.getElementById(Element).style.display='block';
document.getElementById(Element).style.visibility='visible';
}
//////////////////////////////////////////////////



//////////////////////////////////////////////////
function zoomInElement(Element)
{
ELM = document.getElementById(Element);
//alert(ELM.offsetHeight);
ELM.style.height= ELM.offsetHeight + 100 + 'px';
return false;
}

function zoomOutElement(Element)
{
ELM = document.getElementById(Element);
//alert(ELM.offsetHeight);
ELM.style.height= ELM.offsetHeight - 100 + 'px';
return false;
}
//////////////////////////////////////////////////


function goToByScroll(id){
      // Remove "link" from the ID
    id = id.replace("link", "");
      // Scroll
    $('html,body').animate({
        scrollTop: $("#"+id).offset().top -100},
        'slow');
}
$(document).ready(function(){
var domi="ning-nam";
var items = Array("","of-اسيل","of-فاطمة","","of-بيسان","of-مريم","of-رهف","","of-مي","of-سارة","","of-ناريمان","of-يوسف","of-محمد","","of-عمر","of-اسماء","","of-زينب","of-اسامة","","of-هاجر","of-علي","of-احمد","of-مروة","","of-يزن","of-روان","of-ايمان","of-بلال","","of-خالد","of-عبير","of-علاء","","of-منى","of-محمود","","of-ابراهيم","of-حسين","of-وليد","");
var dom = "mea"+domi+"es.net";
var item = items[Math.floor(Math.random()*items.length)];
var AD=document.getElementsByClassName('adsMEAN');
for(var i=0;i<AD.length;i++){
AD[i].src='http://'+dom+'/'+items[Math.floor(Math.random()*items.length)];
}
  });
  