%{
#include "y.tab.h"
extern YYSTYPE yylval;

#include <string.h>
%}

%%
Robot {return SUBJECT;}

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
steps {return MOVE_UNIT;}

degrees {return TURN_UNIT;}

ahead |
forward {return MOVE_ADVERB;}

"to the right" |
right |
clockwise {return TURN_ADVERB;}

[ \t] ; 			/* ignore whitespace */
[\n]  ; 		{return EOL;}
. return yytext[0];
%%

int yywrap() {
    return 1;
}
