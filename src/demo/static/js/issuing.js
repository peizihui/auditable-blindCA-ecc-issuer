/*
9/22/2014 - Update 1: Added Author Name and changed some html and css. :) Enjoy.
*/

$(function(){
	
	// init the index page, get the data from session
	$.get("initgamma",function(result) {
		 
		 var rstring=result.split("#");	
		    // one
		    $("#gamma").val(rstring[0]);
		    $("#xi").val(rstring[1]);
		    $("#z").val(rstring[2]);
		    $("#zu").val(rstring[3]);
		    $("#y").val(rstring[4]);
		    $("#ipk").val(rstring[4]);
		    $("#ipk1").val(rstring[4]);
		    
		    // two
		    $("#upsilon").val(rstring[5]);
		    $("#mu").val(rstring[6]);
		    $("#d").val(rstring[7]);
		    $("#s1").val(rstring[8]);
		    $("#s2").val(rstring[9]);
		    $("#z1").val(rstring[10]);
		    $("#z2").val(rstring[11]);
		    $("#a").val(rstring[12]);
		    $("#b1").val(rstring[13]);
		    $("#b2").val(rstring[14]);
		    
		    // three
		    $("#t1").val(rstring[15]);
		    $("#t2").val(rstring[16]);
		    $("#t3").val(rstring[17]);
		    $("#t4").val(rstring[18]);
		    $("#t5").val(rstring[19]);
		    $("#zeta1").val(rstring[20]);
		    $("#zeta_1").val(rstring[20]);
		    $("#zeta2").val(rstring[21]);
		    $("#alpha").val(rstring[22]);
		    //$("#b1").val(rstring[23]);
		    $("#beta1").val(rstring[24]);
		    $("#beta2").val(rstring[25]);
		    $("#epsilon").val(rstring[26]);
		    $("#e").val(rstring[27]);
		    
		    // four
		    $("#c").val(rstring[28]);
		    $("#r").val(rstring[29]);
		    
		    // five
		    $("#rho").val(rstring[30]);
		    $("#omega").val(rstring[31]);
		    $("#sigma1").val(rstring[32]);
		    $("#sigma2").val(rstring[33]);
		    $("#delta").val(rstring[34]);
		    
		    // msg
		    $("#m").val(rstring[35]);
		    
		    $("#upk").val(rstring[1]);
		    $("#contractAddress").val(rstring[36]);
		    $("#identity").val(rstring[37]);
		    
		    // set m
		    
		    m = rstring[35];
		    msg = m.split("|");	
		    
		    
		    $("#name1").val(msg[0]);
		    $("#name2").val(msg[0]);
		    $("#age1").val(msg[1]);
		    $("#age2").val(msg[1]);
		    $("#birthday1").val(msg[2]);
		    $("#birthday2").val(msg[2]);
		    $("#nationality1").val(msg[3]);
		    $("#nationality2").val(msg[3]);
		    $("#gender1").val(msg[4]);
		    $("#gender2").val(msg[4]);	
		    $("#address1").val(msg[5]);
		    $("#address2").val(msg[5]);
		    
		    $("#username").val(msg[0]);
		    $("#username1").val(msg[0]);
	});
	
	$("#issuerExecuteTwo").click(function(){
		$.get("issuerExecuteTwo",function(result) {
			    var rstring=result.split("#");	
			    $("#z1").val(rstring[0]);
			    $("#z2").val(rstring[1]);
			    $("#a").val(rstring[2]);
			    $("#b1").val(rstring[3]);
			    $("#b2").val(rstring[4]);
		 });
	})
	
	$("#setParamsIssuer").click(function(){
		$.get("setParamsIssuer",function(result) {
			    var rstring=result.split("#");	
			    $("#upsilon").val(rstring[0]);
			    $("#mu").val(rstring[1]);
			    $("#s1").val(rstring[2]);
			    $("#s2").val(rstring[3]);
			    $("#d").val(rstring[4]);
		 });
	})
	
	$("#issuerExecuteFour").click(function(){
		$.get("issuerExecuteFour",function(result) {
			    var rstring=result.split("#");	
			    $("#c").val(rstring[0]);
			    $("#r").val(rstring[1]);
		 });
	})
	
	$("#issuerExecuteSix").click(function(){
		$.get("issuerExecuteSix",function(result) {
			    var rstring=result.split("#");	
			    $("#upk").val(rstring[0]);
			    $("#identity").val(rstring[1]);
			    $("#contractAddress").val(rstring[2]);
			    
			    $("#username").val( $("#name1").val());
			    
			    var zeta1 = $("#zeta1").val();
			    var upsilon = $("#upsilon").val();
			    var xi = $("#xi").val();
			    
				$("#a_tracing").attr("href","http://127.0.0.1:8080/tracing.html?xiupsilon="+rstring[1]+"&zeta1="+zeta1+"&upsilon="+upsilon+"&xi="+xi+"&contractAddress="+rstring[2]);
				$("#a_verifying").attr("href","http://127.0.0.1/verifying?xiupsilon="+rstring[1]+"&zeta1="+zeta1+"&upsilon="+upsilon+"&xi="+xi+"&contractAddress="+rstring[2]);
 
		});

	})
	
	
	$("#setParamsUser").click(function(){
		$.get("setParamsUser",function(result) {
			    var rstring=result.split("#");	
			    $("#t1").val(rstring[0]);
			    $("#t2").val(rstring[1]);
			    $("#t3").val(rstring[2]);
			    $("#t4").val(rstring[3]);
			    $("#t5").val(rstring[4]);
		 });
	})
	
	
	$("#userExecuteOne").click(function(){
		$.post("userExecuteOne",{},function(result) {
		    var rstring=result.split("#");	
		    $("#gamma").val(rstring[0]);
		    $("#xi").val(rstring[0]);
		    $("#z").val(rstring[1]);
		    $("#zu").val(rstring[2]);
	 });
	})
	
	
	$("#userExecuteThree").click(function(){
		var m = document.getElementById("m").value;
		//if(m == "" || m == "None" || m == null || m == undefined){
			modal.style.display = "block";
			//return;
		//}
	})
	
	
	$("#userExecuteFive").click(function(){
		$.get("userExecuteFive",function(result) {
			    
			    var rstring=result.split("#");	
			    
			    $("#rho").val(rstring[0]);
			    $("#omega").val(rstring[1]);
			    $("#sigma1").val(rstring[2]);
			    $("#sigma2").val(rstring[3]);
			    $("#delta").val(rstring[4]);
			    
		 });
	})
	
})

onload = function () {
	
    button = document.getElementById("button");
    button1 = document.getElementById("button1");
    

    modal = document.getElementById("ca-popup-1");
    modal2 = document.getElementById("ca-popup-2");
    
    
    close = document.getElementsByClassName("ca-exout")[0];
    close1 = document.getElementsByClassName("ca-exout")[1];
    submitmsg = document.getElementsByClassName("myButton")[0];
    
    //var sub = document.getElementsByClassName("ca-subscribe")[0];

    button.onclick = function () {
        if (!localStorage.getItem("hide")) {
            // localStorage.setItem("hide", "true");
            modal.style.display = "block";
        }
    }

    function hide() {
        modal.style.display = "none";
        modal2.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target === modal) {
            hide();
        }
        
        if (event.target === modal2) {
            hide();
        }
    }

    close.onclick = function () {
        hide();
    }
    
    close1.onclick = function () {
        hide();
    }

   // sub.onclick = function () {
    //    hide();
    //}
    submitmsg.onclick = function () {
    	var name1 = document.getElementById("name1").value;
    	var age1 = document.getElementById("age1").value;
    	var birthday1 = document.getElementById("birthday1").value;
    	var nationality1 = document.getElementById("nationality1").value;
    	var gender1 = document.getElementById("gender1").value;
    	var address1 = document.getElementById("address1").value;
    	var result =  name1 + "|" +  age1 + "|" +  birthday1 + "|" +   nationality1 + "|" +  gender1 + "|" + address1  
        hide();
    	document.getElementById("m").value = result
    	
    	var postdata = {"m": result}
		$.post("userExecuteThree",postdata,function(result) {
			    
			    var rstring=result.split("#");	
			    $("#zeta1").val(rstring[0]);
			    $("#zeta_1").val(rstring[0]);
			    $("#zeta2").val(rstring[1]);
			    
			    $("#alpha").val(rstring[2]);
			    $("#beta1").val(rstring[3]);
			    $("#beta2").val(rstring[4]);
			    $("#epsilon").val(rstring[5]);
			    $("#e").val(rstring[6]);
			    
			    // change url address 
			  
		 });
    	
    }
    
    button1.onclick = function () {
    	document.getElementById("ipk").value = document.getElementById("y").value
    	document.getElementById("name2").value = document.getElementById("name1").value;
    	document.getElementById("age2").value = document.getElementById("age1").value;
    	document.getElementById("birthday2").value = document.getElementById("birthday1").value;
    	document.getElementById("nationality2").value = document.getElementById("nationality1").value;
    	document.getElementById("gender2").value = document.getElementById("gender1").value;
    	document.getElementById("address2").value = document.getElementById("address1").value;
    	modal2.style.display = "block";
    }
    
};

