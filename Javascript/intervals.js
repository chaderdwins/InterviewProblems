//Your goal is to implement a function called countDown.  
//The function will accept 1 parameter which is a time in seconds for the count down.  
//The function should console.log the time remaining every second.  
//Once the timer gets to 0, the timer should be stopped and you should console.log "Ring Ring Ring!!!".

//HINT: You will need to use setInterval() to count down and clearInterval to stop the timer.

Example:

countDown(3) 

Console output

Timer: 2
Timer: 1
Ring Ring Ring!!!

//=======================================
//		Implementation of countDown
//=======================================
function countDown(seconds){
	var intervalId = setInterval(function(){
		seconds--;
		if(seconds>0){
			console.log("Timer: ", seconds);
		} else {
			console.log("RING RING RING!!!");
			clearInterval(intervalId);
		}
	},1000);
}