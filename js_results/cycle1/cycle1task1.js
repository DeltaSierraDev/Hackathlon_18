//This is the example of how to read and process input.

var inputLine;
while (inputLine = readline()) {
    print(processLine(inputLine));
}

function processLine(inputLine) {
    //Enter your code here
    var str = inputLine;
    var x = str.charAt(0);
    var res = x;
    var i;
    for (i = 1; i < str.length; i++) {
    	if (x == str.charAt(i)) {
        	res = res + "*";
        	}
        else {
        	res = res + str.charAt(i);
        }
        }

    return res;
}
