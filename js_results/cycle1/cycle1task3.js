//This is the example of how to read and process input.

var inputLine;
while (inputLine = readline()) {
    print(processLine(inputLine));
}

function processLine(inputLine) {
    //Enter your code here
    var str = inputLine;

    var charReplace = str.replace(/\W/g, '?');
    var numReplace = charReplace.replace(/\d/g, '*');
    var alphaReplace = numReplace.replace(/[A-Za-z]/g, '-');

    return alphaReplace;
}
