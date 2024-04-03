import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int maxVal = Integer.MIN_VALUE;

        int[][] arr2d = new int[n][n];

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                arr2d[i][j] = sc.nextInt();
            }
        }
        int num;
        for(int i=0;i<n;i++){
            for(int j=0;j<n-2;j++){
                num = arr2d[i][j] + arr2d[i][j+1] + arr2d[i][j+2];
                if(num > maxVal){
                    maxVal = num;
                }

            }

        }
        System.out.print(maxVal);



    }
}