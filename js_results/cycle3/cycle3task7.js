var inputLine;
while (inputLine = readline()) {
    print(processLine(inputLine));
}

function processLine(inputLine) {
    var str = inputLine;
    var arr = str.split(" ");
    var result = "";

    for(var i in arr){
        if (arr[i][0] === "-"){
            result=result+"-";
        }
        else {
            result=result+"+";
        }
    }

    result = result.substring(1);
    return result;

}
