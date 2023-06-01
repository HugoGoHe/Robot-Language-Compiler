%{
#include "y.tab.h"
extern YYSTYPE yylval;

#include <string.h>
%}

%%
Robot |
Rob |
Turtle {return SUBJECT;}

please |
kindly {return POLITE_WORD;}

,            { return COMMA; }
and          { return AND; }
then         { return THEN; }


[0-9]    {  yylval = atoi(yytext); return NUMBER; }
(90|180|270|360)    {  yylval = atoi(yytext); return DEGREES; }

move |
advance |
travel |
go |
proceed				{ return MOVE_ACTION; }

turn |
rotate |
spin |
pivot |
twist |
shift 	{return TURN_ACTION; }

blocks |
block |
steps |
step |
units |
unit |
paces |
pace |
strides |
stride {return MOVE_UNIT;}

degrees {return TURN_UNIT;}

ahead |
forward |
onward |
straight {return MOVE_ADVERB;}

"to the right" |
right |
clockwise |
"to the east" |
"toward the right" {return TURN_ADVERB;}

[ \t] ; 			/* ignore whitespace */
[\n]  ; 		{return EOL;}
. return yytext[0];
%%

int yywrap() {
    return 1;
}
