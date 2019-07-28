public class Coding_Challenge_2{
    public static void Narcisistas(int n){
        for(int i=0;i<=n;i++){
            String j = Integer.toString(i);
            int p = j.length();
            int s = 0;
            for(int k=0;k<p;k++){
                char ch = j.charAt(k);
                int d = Character.getNumericValue(ch);
                s += Math.pow(d,p);
            }
            if(s==i){
                System.out.println(s);
            }
        }
    }
}