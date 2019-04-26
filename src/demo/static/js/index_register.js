/*
04/22/2019 - Update 1: Rujia Li
*/

$(function(){
	
	function initParam(){
		var url = window.location.href;
		var arrObj = url.split("?");
		var arr = arrObj[1].split("=");
		var value = arr[1];
		var rstring = value.split("#");
		
		$("#p1").val(rstring[0]);
	    $("#p2").val(rstring[0]);
	    $("#q1").val(rstring[1]);
	    $("#q2").val(rstring[1]);
	    $("#g1").val(rstring[2]);
	    $("#g2").val(rstring[2]);
	    $("#h1").val(rstring[3]);
	    $("#h2").val(rstring[3]);
	    
	    $("#x").val(rstring[4]);
	    $("#y").val(rstring[5]);

	    $("#gamma").val(rstring[6]);	
	    $("#xi").val(rstring[7]);
	    
	    $("#z1").val(rstring[8]);
	    $("#z2").val(rstring[8]);
	}
	
	initParam();
	
})

