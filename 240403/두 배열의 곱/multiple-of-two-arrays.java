import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int[][] arr2d_1 = new int[3][3];
        int[][] arr2d_2 = new int[3][3];

        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                arr2d_1[i][j] = sc.nextInt();
            }

        }
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                arr2d_2[i][j] = sc.nextInt();
            }
        }
        
        int[][] sum2d = new int[3][3];

        int num;
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                num = arr2d_1[i][j] * arr2d_2[i][j];
                sum2d[i][j] = num;
            }
        }

        
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.print(sum2d[i][j]+" ");
            }
        System.out.println();}

    }
}