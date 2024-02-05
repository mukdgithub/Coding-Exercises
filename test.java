import java.util.*;

class pat1{
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        int i,j,n;
        System.out.println(" enter the length ");
        n=sc.nextInt();
        
        for(i=0;i<n;i++){
            for(j=0;j<=i;j++){
                System.out.print(" * ");    
            }
            System.out.println();
        }
    }
}
