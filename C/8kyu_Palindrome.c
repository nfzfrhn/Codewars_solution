#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool is_palindrome(const char *str_in) {

    //  <----  hajime!
  if(str_in==NULL){return false;}
  
  size_t str_len = strlen(str_in);
  
  for(int i=0;i<(int)str_len;i++){
    if(tolower(str_in[i]) == tolower(str_in[str_len-1-i])){
      continue;
    }
    else
      return false;  
  }
  return true;
}