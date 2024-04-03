import java.util.Scanner;
public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;
    public static final int MAX_N = 100;

    public static int n;
    public static int[] a = new int[MAX_N];
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        for(int i=0;i<n;i++){
            a[i] = sc.nextInt();
        }
        int ans = INT_MAX;
        for(int i=0;i<n;i++){
            int distance=0;
            for(int j=0;j<n;j++){
                distance += a[j] * Math.abs(j-i);
            }
            if(distance<ans){
                ans = distance;
            }
        }
        System.out.print(ans);

    }
}