/*
9/22/2014 - Update 1: Added Author Name and changed some html and css. :) Enjoy.
*/

$(function(){
	
	// init the index page, get the data from session
	$.get("init",function(result) {
		if(result.indexOf("None") ==-1){
			 var rstring=result.split(",");
				$("#p1").val(rstring[0]);
			    $("#p2").val(rstring[0]);
			    $("#q1").val(rstring[1]);
			    $("#q2").val(rstring[1]);
			    $("#g1").val(rstring[2]);
			    $("#g2").val(rstring[2]);
			    
			    $("#x").val(rstring[3]);
			    $("#y").val(rstring[4]);
			    $("#h1").val(rstring[5]);
			    $("#h2").val(rstring[5]);
			    $("#z1").val(rstring[6]);
			    $("#z2").val(rstring[6]);
			    
			    $("#xi").val(rstring[7]);
			    $("#gamma").val(rstring[8]);
		}
	});
	
	// set up the parameters
	$("#setup").click(function(){
		//r_id = $('#tmprid').val();
		var postdata = {'L':256,'N':40}
		$.post("setup", postdata,function(result) {
			    //$(".loadingsb").hide();
			    var rstring=result.split(",");	
			    $("#p1").val(rstring[2]);
			    $("#p2").val(rstring[2]);
			    $("#q1").val(rstring[3]);
			    $("#q2").val(rstring[3]);
			    $("#g1").val(rstring[4]);
			    $("#g2").val(rstring[4]);
			    $("#h1").val(rstring[5].substring(0,rstring[5].length -1));
			    $("#h2").val(rstring[5].substring(0,rstring[5].length -1));
		 });
	})
	
	// generate the issuer's public and private key
	$("#issuerkey").click(function(){
		var postdata = {}
		$.post("issuerkey", postdata,function(result) {
			    var rstring=result.split(",");	
			    $("#x").val(rstring[0].substring(1,rstring[0].length));
			    $("#y").val(rstring[1]);
			    $("#z1").val(rstring[2]);
			    $("#z2").val(rstring[2]);
		 });
	})
	
	// generate the user's public and private key
	$("#userkey").click(function(){
		var postdata = {}
		$.post("userkey", postdata,function(result) {
			    var rstring=result.split(",");	
			    $("#gamma").val(rstring[0].substring(1,rstring[0].length));
			    $("#xi").val(rstring[1]);
		 });
	})
	
	$("#confirm").click(function(){
		
		var p = $.trim($("#p1").val());
	    var q = $.trim($("#q1").val());
	    var g = $.trim($("#g1").val());
	    var h = $.trim($("#h1").val());
	    
	    var x = $.trim($("#x").val());
	    var y = $.trim($("#y").val());
	    
	    var gamma = $.trim($("#gamma").val());
	    var xi = $.trim($("#xi").val());
	    
	    var z = $.trim($("#z1").val());
	    
	    param = "?p=" + p + "&q=" + q + "&g=" + g + "&h=" + h + "&x=" + x + "&y=" + y + "&gamma=" + gamma + "&xi=" + xi + "&z="+ z + "&N=40"
	    
		window.location.href= "http://127.0.0.1:8080/index_register.html" + param;
	})
	
})

