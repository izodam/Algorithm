import java.io.*;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        String[] chList = new String[n];

        for (int i = 0; i < n; i++){
            chList[i] = br.readLine();
        }

        int k1 = 0;  // KBS1 찾기 용
        int k2 = 0;  // KBS2 찾기 용
        String temp = "";

        while (!chList[0].equals("KBS1")) {
            if (!chList[k1].equals("KBS1")){
                bw.write("1");
                k1++;
            } else {
                bw.write("4");
                temp = chList[k1];
                chList[k1] = chList[k1 - 1];
                chList[k1-1] = temp;
                k1--;
            }
        }

        while (!chList[1].equals("KBS2")) {
            if (!chList[k2].equals("KBS2")){
                bw.write("1");
                k2++;
            } else {
                bw.write("4");
                temp = chList[k2];
                chList[k2] = chList[k2 - 1];
                chList[k2-1] = temp;
                k2--;
            }
        }

        bw.flush();
    }
}