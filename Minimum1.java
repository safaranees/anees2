import java.util.*;
public class Minimum1
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        int a[]=new int[10];
        for(int i=0;i<10;i++)
        {
            a[i]=s.nextInt();
        }
        int minimum=a[0];
        for(int i=0;i<10;i++)
        {
            if(a[i]<minimum)
            {
                minimum=a[i];
            }
        }
        System.out.println(minimum);
    }
}
