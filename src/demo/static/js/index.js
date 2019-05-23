$(function(){
	
	// init the index page, get the data from session
	$.get("init",function(result) {
		if(result.indexOf("None") ==-1){
			var rstring=result.split("#");	
			
			$("#p1").val(rstring[0]);
			$("#p2").val(rstring[0]);
			
			$("#a1").val(rstring[1]);
			$("#a2").val(rstring[1]);
			
			$("#b1").val(rstring[2]);
			$("#b2").val(rstring[2]);
			
			$("#n1").val(rstring[3]);
			$("#n2").val(rstring[3]);
			
			$("#g1").val(rstring[4]);
			$("#g2").val(rstring[4]);
			
			$("#h1").val(rstring[5]);
			$("#h2").val(rstring[5]);
			
			secp = rstring[6]
			
			$("#x").val(rstring[7]);
			$("#y").val(rstring[8]);
			$("#z1").val(rstring[9]);
			$("#z2").val(rstring[9]);
			$("#gamma").val(rstring[10]);
			$("#xi").val(rstring[11]);
			
			
			//$("#selectParam").find("option:contains('"+secp+"')").attr("selected",true);
			
			//$('input:radio').find("id:contains('"+secp+"')").attr('checked', 'true');
			$("#"+secp).attr('checked', true);
			$("#i"+secp).css('display',''); 
			
		}
	});
	
	
	$('input[type=radio]').click(function() {
        //var selectParam = $(this).children("option:selected").val();
        var selectParam = $("input[type=radio]:checked").val();
		var postdata = {'secp':selectParam}
		
		$("#isecp256k1").css('display','none'); 
		$("#isecp192k1").css('display','none'); 
		
		$("#i"+selectParam).css('display',''); 
		
		$.post("setup", postdata,function(result) {
				
				var rstring=result.split("#");	
				$("#p1").val(rstring[0]);
				$("#p2").val(rstring[0]);
				
				$("#a1").val(rstring[1]);
				$("#a2").val(rstring[1]);
				
				$("#b1").val(rstring[2]);
				$("#b2").val(rstring[2]);
				
				$("#n1").val(rstring[3]);
				$("#n2").val(rstring[3]);
				
				$("#g1").val(rstring[4]);
				$("#g2").val(rstring[4]);
				
				$("#h1").val(rstring[5]);
				$("#h2").val(rstring[5]);
		 });  
    });
	
	// generate the issuer's public and private key
	$("#issuerkey").click(function(){
		var postdata = {}
		$.post("issuerkey", postdata,function(result) {
			    var rstring=result.split("#");	
			    $("#x").val(rstring[0]);
			    $("#y").val(rstring[1]);
			    $("#z1").val(rstring[2]);
			    $("#z2").val(rstring[2]);
		 });
	})
	
	// generate the user's public and private key
	$("#userkey").click(function(){
		var postdata = {}
		$.post("userkey", postdata,function(result) {
			    var rstring=result.split("#");	
			    $("#gamma").val(rstring[0]);
			    $("#xi").val(rstring[1]);
		 });
	})
	
	$("#confirm").click(function(){
		
		var a = $.trim($("#a1").val());
	    var b = $.trim($("#b1").val());
		var p = $.trim($("#p1").val());
		var n = $.trim($("#n1").val());
	    var g = $.trim($("#g1").val());
	    var h = $.trim($("#h1").val());
	    
	    
	    var x = $.trim($("#x").val());
	    var y = $.trim($("#y").val());
	    
	    var gamma = $.trim($("#gamma").val());
	    var xi = $.trim($("#xi").val());
	    
	    var z = $.trim($("#z1").val());
	    
	    param = "?p=" + p + "&n=" + n + "&g=" + g + "&h=" + h + "&x=" + x + "&y=" + y + "&gamma=" + gamma + "&xi=" + xi + "&z="+ z + "&a="+ a + "&b="+ b
	    
		window.location.href= "http://127.0.0.1:8080/index_register.html" + param;
	})
	
})

