//This is the example of how to read and process input.

import java.util.*;
import java.lang.*;

class Main
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner( System.in );
        String input = scanner.nextLine();
        String replaceString = input.replaceAll("[^0-9a-zA-Z]", "?");
        String replaceString1 = replaceString.replaceAll("[0-9]", "*");
        String replaceString2 = replaceString1.replaceAll("[a-zA-Z]", "-");
        System.out.print(replaceString2);
    }
}
