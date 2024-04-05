import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] arr2d = new int[n][3];

        for(int i=0;i<n;i++){
            for(int j=0;j<2;j++){
                arr2d[i][j] = sc.nextInt();
            }
        }

        // Integer[] arr = new Integer[n];
        // for(int i=0;i<n;i++){
        //     arr[i] = arr2d[i][1]/arr2d[i][0];
        // }

        for(int i=0;i<n;i++){
            arr2d[i][2] = arr2d[i][1]/arr2d[i][0];
        }

        Arrays.sort(arr2d, (o1,o2) -> o2[2]-o1[2]);
        
        double bag = 0.0;
        double price = 0.0;

        // for(int i=0;i<n;i++){
        //         bag += arr2d[i][0];
        //         price += arr2d[i][1];
        //         if(bag>m){
        //             bag -= arr2d[i][0];
        //             price -= arr2d[i][1];
        //             double remain;
        //             remain = m - bag;
        //             bag += remain/arr2d[i][0];
        //             price += (remain/arr2d[i][0])*arr2d[i][1];
        //             break;
        //     }

        for(int i=0;i<n;i++){
            if((bag+arr2d[i][0])<=m){
                bag += arr2d[i][0];
                price += arr2d[i][1];
            }
            else{
                double remain;
                remain = m-bag;
                bag += remain/arr2d[i][0];
                price += (remain/arr2d[i][0])*arr2d[i][1];
                break;
            }
        }
            

        
        System.out.printf("%.3f",price);

    }
}