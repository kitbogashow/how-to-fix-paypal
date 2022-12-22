#include <stdio.h>
#include <ctype.h>

char l[512];int c(char f[]){int i=0,m=0,c;while(c=tolower(l[i++])){char
e=tolower(f[m]);if(!e)return 1;else if(c==e){if(f[m+++1]=='\0')return 1
;}else m=0;}return 0;}int main(){int s=0,t=0;FILE*fh=fopen("../invoice"
"s.txt","rb");while(fgets(l,512,fh))++t&&(c("suspicious")||c("unauthor"
"ized")||c("+1")||c("geek squad")||c(" call"))&&s++;printf("%d / %d\n",
s,t);}
