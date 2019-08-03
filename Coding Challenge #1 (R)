coding_challenge1 = function(x){
  y = c(); s = c(); n = length(x);
  print("Secuencias")
  for(i in 1:(n-1)){
    if(x[i]<x[i+1]){
      y = c(y,x[i]);
      if(i==(n-1)){
        y=c(y,x[i+1]);
        s=c(s,sum(y));
        print(y)
      }
      next;
    }
    else if(x[i]>=x[i+1] && x[i] >x[i-1]){
      y=c(y,x[i]);
      s=c(s,sum(y));
      print(y)
      y = c();
    }
  }
  print("Sumas de las secuencias")
  for(i in 1:length(s)){
    print(s[i])
  }
  print("Suma máxima")
  print(max(s))
}
