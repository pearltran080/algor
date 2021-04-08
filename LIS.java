// Pearleen Tran
// CSC 321
// longest increasing subsequence

public class LIS {

  public static int FastLIS(int[] A){
    A[0] = Integer.MIN_VALUE;
    int[][] LISbigger = new int [A.length][A.length+1];

    for (int j = A.length-1; j > 0; j--){
      for (int i = 0; i < j; i++) {
        int keep = 1 + LISbigger[j][j+1];
        int skip = LISbigger[i][j+1];
        if (A[i] >= A[j]) {
          LISbigger[i][j] = skip;
        } else {
          if (skip > keep) LISbigger[i][j] = skip;
          else LISbigger[i][j] = keep;
        }
      }
    }
    return (LISbigger[0][1]);
  }

  public static void main(String args[]) {
    // 1
    int[] A = {0, 60, 10, 70, 20, 80, 30, 90, 50, 100, 60, 110, 70, 120, 80, 90};
    // 2
    int answer = FastLIS(A);
    // 3
    System.out.printf("The length of the longest increasing subsequence is %d.", answer);
  }

}
