narcisistas = function(n){
  for(i in 0:n){
    j = as.character(i);
    p = nchar(j);
    s = 0;
    for(k in 1:p){
      ch = substr(j,k,k);
      d = strtoi(ch);
      s = s+d^p;
    }
    if(s==i){
      print(i)
    }
  }
}
