import java.util.*;
 
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
 
        int n = scan.nextInt();
        int t = scan.nextInt();
 
        Node[] node = new Node[n + 1]; //단원
        for(int i = 1; i <= n; i++) {
            int k = scan.nextInt(); //최소 공부 시간
            int s = scan.nextInt(); //배점
            node[i] = new Node(k, s);
        }
 
        //dp
        int[][] dp = new int[n + 1][t + 1];
        for(int i = 1; i <= n; i++) {
            for(int j = 0; j <= t; j++) {
                if(node[i].k <= j){
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - node[i].k] + node[i].s);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        System.out.println(dp[n][t]);
    }
 
    public static class Node {
        int k;
        int s;
 
        public Node(int k, int s) {
            this.k = k;
            this.s = s;
        }
    }
}