var XHR = new XMLHttpRequest();

XHR.onreadystatechange = function(){
	if(XHR.readyState == 4){//check to see if the request has completed
		if(XHR.status == 200){//if it has completed, make sure there are no errors
			console.log(XHR.responseText);
		} else {
			console.log("There is a problem!")//handle error		
		}
	}
}
XHR.open("GET", "https://api.github.com/zen");
XHR.send();