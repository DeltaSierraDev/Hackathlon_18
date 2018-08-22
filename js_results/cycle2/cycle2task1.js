//This is the example of how to read and process input.

var inputLine;
while (inputLine = readline()) {
    print(processLine(inputLine));
}

function processLine(inputLine) {
    //Enter your code here
    var str = inputLine;
    var arr = str.split(" ");
    var travStart = parseInt(arr[0]);
    var travEnd = parseInt(arr[1]);
    var skip = 0;
    var result = 0;

    if (travStart % 2 === 0 && travEnd % 2 === 1){
      skip++;
      travEnd++;
    }
    if (travStart % 2 === 1 && travEnd % 2 === 0){
      skip++;
      travStart++;
    }

    if (travEnd > travStart){
      var result = parseInt(((travEnd - travStart) / 2)) + skip;
    }
    if (travEnd < travStart){
      var result = parseInt(((travStart - travEnd) / 2)) + skip;
    }

    return result;
}
