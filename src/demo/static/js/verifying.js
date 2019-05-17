/*
9/22/2014 - Update 1: Added Author Name and changed some html and css. :) Enjoy.
*/

$(function(){
	
	// init the index page, get the data from session
	$.get("getCred",function(result) {
		 var rstring=result.split("#");	
		    $("#y1").val(rstring[0]);
		    $("#y2").val(rstring[0]);
		    
		    $("#zeta1").val(rstring[1]);
		    $("#rho").val(rstring[2]);
		    $("#omega").val(rstring[3]);
		    $("#sigma1").val(rstring[4]);
		    $("#sigma2").val(rstring[5]);
		    $("#delta").val(rstring[6]);
		    $("#m").val(rstring[7]);
		    
		    m = rstring[7];
		    msg = m.split("|");	
		    
		    $("#name2").val(msg[0]);
		    $("#age2").val(msg[1]);
		    $("#birthday2").val(msg[2]);
		    $("#nationality2").val(msg[3]);
		    $("#gender2").val(msg[4]);	
		    $("#address2").val(msg[5]);
		    
		    $("#ipk").val(rstring[0]);
		    
		    var param = window.location.search;
			$("#a_tracing").attr("href",$("#a_tracing").attr("href")  +param);
	});
	
	
	
	$("#verifyCred").click(function(){
		$.get("verifyCred",function(result) {
			    var rstring=result.split(",");	
			    $("#omegadelta").val(rstring[0]);
			    $("#hashresult").val(rstring[1]);
			    $("#res").html("&#969; + &#948;  = hashresult. <br> The credential is verified successfully.");
		 });
	})
	
	modal2 = document.getElementById("ca-popup-2");
	
	$("#button2").click(function(){
		modal2.style.display = "block";
	})
	
	 function hide() {
        modal2.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target === modal2) {
            hide();
        }
    }
    close1 = document.getElementsByClassName("ca-exout")[0];
    close1.onclick = function () {
        hide();
    }
	
	
})

