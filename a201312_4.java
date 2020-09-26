import java.util.*;
public class a201312_4 {
 
	public static final long MOD = 1000000007;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		long[][] states = new long[n+1][6];
		states[1][0] = 1;
		for(int i = 2;i<6;i++)
			states[1][i] = 0;
		
		for(int i = 2;i<=n;i++){
			states[i][0] = 1;
			states[i][1] = (states[i-1][0]+states[i-1][1]*2)%MOD;
			states[i][2] = (states[i-1][0]+states[i-1][2])%MOD;
			states[i][3] = (states[i-1][1]+states[i-1][3]*2)%MOD;
			states[i][4] = (states[i-1][1]+states[i-1][2]+states[i-1][4]*2)%MOD;
			states[i][5] = (states[i-1][3]+states[i-1][4]+states[i-1][5]*2)%MOD;
		}
		System.out.println(states[n][5]);
	}
 
}
