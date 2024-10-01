import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static int n;
    public static int m;
    public static int[][] board;
    public static boolean[][] visited;

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        n = Integer.parseInt(inputs[0]);
        m = Integer.parseInt(inputs[1]);

        board = new int[n][m];
        for (int i = 0; i < n; i++){
            inputs = br.readLine().split(" ");
            for (int j = 0; j < m; j++){
                board[i][j] = Integer.parseInt(inputs[j]);
            }
        }

        visited = new boolean[n][m];

        int cnt = 0;
        int max = 0;

        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if(board[i][j] == 1 && !visited[i][j]){
                    max = Math.max(max, bfs(i, j));
                    cnt++;
                }
            }
        }
        bw.write(cnt + "\n" + max);
        bw.flush();
        bw.close();
        br.close();

    }

    static int bfs(int x, int y){
        Queue<int []> q = new LinkedList<>();
        q.add(new int [] {x, y});
        visited[x][y] = true;
        int size = 1;

        while(!q.isEmpty()){
            int[] now = q.poll();
            x = now[0];
            y = now[1];

            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && board[nx][ny] == 1){
                    size++;
                    visited[nx][ny] = true;
                    q.add(new int[] {nx, ny});
                }
            }
        }
        return size;

    }
}