var issue_domain = "http://" + window.location.host
var trace_domain =  issue_domain + ":8080"



$(function(){
	$("#a_index").attr("href",issue_domain);
	$("#a_issuing").attr("href",issue_domain + "/issuing");
	$("#a_verifying").attr("href",issue_domain + "/verifying");
	$("#a_tracing").attr("href",trace_domain + "/tracing.html");
})