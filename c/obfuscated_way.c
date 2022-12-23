#include <stdio.h>
#include <ctype.h>

char l[512];i,m,e,s,t,d;c(char*f){i=0,m=0;while(d=
tolower(l[i++])){e=tolower(f[m]);if(!e)return 1;if
(d==e){if(!f[m+++1])return 1;}else m=0;}return 0;}
main(){FILE*f=fopen("../invoices.txt","rb");while(
fgets(l,512,f))++t&&(c("suspicious")||c("unauthor"
"ized")||c("+1")||c("geek squad")||c(" call"))&&++
s;printf("%d / %d\n",s,t);}
