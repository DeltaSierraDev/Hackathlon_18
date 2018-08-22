//This is the example of how to read and process input.

var inputLine;
while (inputLine = readline()) {
    print(processLine(inputLine));
}

function processLine(inputLine) {
    //Enter your code here
    var str1 = inputLine;
    var str2 = str1.toLowerCase();
    var str = str2.replace(/[^a-z]/g, '')

    var res = str.toLowerCase();
    arr = res.split("");
    arr.sort();
    var count = 1;
    var results = "";
    for (var i = 0; i < arr.length; i++)
    {
        if (arr[i] == arr[i+1])
        {
          count +=1;
        }
        else
        {
            results += arr[i] + ":" + count + "\n" ;
            count=1;
        }
    }
    return results;
}
