1.1
The functionality of the function 'f' is to determine and return true if any element in list 'x' is 0; false otherwise or if 'x' has no elements.

1.4
function f(x: List[Integer]){
  var anyzero: Boolean = false
  var n: Integer = Length(x)
  if(n >= 1){
    for(var i = 0; i < n; ++i){
      if(x[i] == 0){
        anyzero = true
        break
      }
    }
  }
  return anyzero
}

2.1
1 byte/char * 100 chars/string * 1,000,000 strings = 100,000,000 bytes ~ 95.367 megabytes

3.1
1 byte/char * 100 chars/string * 100,000,000 strings = 10,000,000,000 bytes ~ 9.313 gigabytes
