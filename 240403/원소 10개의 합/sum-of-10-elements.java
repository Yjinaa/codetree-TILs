import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int sum, num;
        sum=0;
        for(int i=0;i<10;i++){
            num = sc.nextInt();
            sum += num;}
            System.out.print(sum);
        
    }
}