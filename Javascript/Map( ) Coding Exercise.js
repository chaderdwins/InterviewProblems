/*
Write a function called doubleValues which accepts an array and returns a new array with all the values in the array passed to the function doubled

Examples:
    doubleValues([1,2,3]) // [2,4,6]
    doubleValues([1,-2,-3]) // [2,-4,-6]
*/
var sequence = [1,2,3,4];
function doubleValues(arr){
    return arr.map(function(value,index,array){
    	return value * 2;
    });
}
console.log(doubleValues(sequence));

/*
Write a function called valTimesIndex which accepts an array and returns a new array with each value multiplied by the index it is currently at in the array.

Examples:
    valTimesIndex([1,2,3]) // [0,2,6]
    valTimesIndex([1,-2,-3]) // [0,-2,-6]
*/
var sequence = [1,2,3,4];
function valTimesIndex(arr){
	return arr.map(function(value,index,array){
		return value * index;
	});    
}
console.log(valTimesIndex(sequence));
/*
Write a function called extractKey which accepts an array of objects and some key and returns a new array with the value of that key in each object.

Examples:
    extractKey([{name: 'Sofi'}, {name: 'Sara'}, {name: 'Boris'}, {name: 'Chad'}], 'name') // ['Sofi', 'Sara', 'Boris', 'Chad']
*/

function extractKey(arr, key){
    return arr.map(function(val){
      return val[key];
  });
}
console.log(extractKey([{name: 'Chad'}, {name: 'Sara'}, {name: 'Boris'}, {name: 'Sofi'}], 'name'));

/*
Write a function called extractFullName which accepts an array of objects and returns a new array with the value of the key with a name of "first" and the value of a key with the name of  "last" in each object, concatenated together with a space. 

Examples:
    extractFullName([{first: 'Sofi', last:"Schoppik"}, {first: 'Sara', last:"Garcia"}, {first: 'Boris', last:"Lane"}, {first: 'Chad', last:"Steele"}]) // ['Sofi Schoppik', 'Sara Garcia', 'Boris Lane', 'Chad Steele']
*/

function extractFullName(arr){
	return arr.map(function(val){
    return val.first + " " + val.last;
  });
    
}