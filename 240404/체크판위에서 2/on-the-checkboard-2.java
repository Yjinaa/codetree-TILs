import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        
        int r = sc.nextInt();
        int c = sc.nextInt();

        char [][] arr2d = new char[r][c];

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                arr2d[i][j] = sc.next().charAt(0);
            }
        }
        //첫번째 칸과 색이 달라야 함
        //i랑 j에 +1 해주고 거기부터 완전탐색해가며 색이 다르면 점프 아니면 대기

        // int x = 1;
        // int y = 1;

        // char color;
        // color = arr2d[x][y];

        // for(int i=x+1;i<r;i++){
        //     for(int j=y+1;j<c;j++){
        //         if (arr2d[i][j] != color){
        //             x = i;
        //             y = j;
        //             color = arr2d[i][j];
        //         }
        //     }
        // }

        //경우의 수는 어떻게 구해줄 수 있지? n.n을 찍고 다시 돌아가야하나? 그 지점은 어떻게 기억하지?
        //그냥 사각형을 다 잡아봄....for문으로 여러 사각형을 다 잡는다
        int cnt = 0;
        for(int i=1;i<r;i++){
            for(int j=1;j<c;j++){
                for(int k=i+1;k<r-1;k++){
                    for(int l=j+1;l<c-1;l++){
                        if((arr2d[0][0] != arr2d[i][j])&&
                        (arr2d[i][j] != arr2d[k][l])&&
                        (arr2d[k][l] != arr2d[r-1][c-1])){
                            cnt++;
                        }
                    }
                }
            }
        }

     System.out.print(cnt);
    }
}