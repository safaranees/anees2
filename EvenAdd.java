import java.util.*;
public class EvenAdd
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int m=s.nextInt();
        int add=n+m;
        if(add%2==0)
        { 
             System.out.println("even");
        }
        else
        {
             System.out.println("odd");
        }
      
    }
}
