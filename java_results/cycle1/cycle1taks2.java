import java.util.*;
import java.lang.*;

public class Main {
  public static void main(String[] args)
    {
      Scanner scanner = new Scanner( System.in );
      String input = scanner.nextLine();
      String lower = input.toLowerCase();
      String original = lower.replaceAll("[^a-zA-Z]", "");
      char[] chars = original.toCharArray();
      Arrays.sort(chars);
      String str = new String(chars);
      int count[] = new int[256];
      int len = str.length();
      for (int i = 0; i < len; i++)
          count[str.charAt(i)]++;
      char ch[] = new char[str.length()];
      for (int i = 0; i < len; i++) {
          ch[i] = str.charAt(i);
          int find = 0;
          for (int j = 0; j <= i; j++) {
              if (str.charAt(i) == ch[j])
                  find++;
          }
          if (find == 1)
              System.out.println(str.charAt(i) + ":" + count[str.charAt(i)]);
      }
    }
}
