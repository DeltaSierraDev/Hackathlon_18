import java.util.*;
import java.lang.*;

class Main
{
    public static void main(String args[])
    {
        Scanner scanner = new Scanner( System.in );
        String input = scanner.nextLine();

        String[] parts = input.split(" ");
        int start = Integer.parseInt(parts[0]);
        int end = Integer.parseInt(parts[1]);
        int skip = 0;
        int result = 0;

        if(start % 2 == 0 && end % 2 == 1){
          skip++;
          end++;
          }
        if(start % 2 == 1 && end % 2 == 0){
          skip++;
          start++;
        }
        if (end > start){
          result = (end - start) / 2;
        }
        if (end < start){
          result = (start - end) / 2;
        }
        System.out.print(result+skip);
    }
}
