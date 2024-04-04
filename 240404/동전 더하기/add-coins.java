import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int amt = sc.nextInt();
        int[] arr = new int[n];

        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        int coins = 0;
        int num = 0;
        for(int i=n-1;i>=0;i--){
            num = amt/arr[i];
            amt = amt%arr[i];
            coins += num;
        }
        System.out.print(coins);
    }
}