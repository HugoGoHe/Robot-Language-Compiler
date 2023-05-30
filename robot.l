%{
#include "y.tab.h"
%}
%%
"and"|"and then"|","|",and"|",then"|",and then"			 return UNION; 
"move"|"advance"|"travel"|"go"|"proceed"				 return MOVE_ACTION; 
"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"		 return NUMBER; 
"turn"|"rotate"|"spin"|"pivot"|"twist"|"shift" 	 return TURN_ACTION; 
"90 degrees"|"180 degrees"|"270 degrees"|"360 degrees" return TURN_PARAMETER;

[ \t] ; 			/* ignore whitespace */
[\n]  ; 		return EOL;
. return yytext[0];
%%