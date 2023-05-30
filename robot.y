%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token UNION MOVE_ACTION MOVE_PARAMETER TURN_ACTION TURN_PARAMETER EOL
%%

sentences: sentence                  {printf("PASS\n");}
 | sentences EOL sentences
 | sentences EOL
 ;

sentence: subject polite_word instructions	
        | polite_word subject instructions
;

instructions: instruction union instructions
 | instruction
;
instruction: MOVE_ACTION MOVE_PARAMETER     { printf("MOVE %d ", $2); }
    | TURN_ACTION TURN_PARAMETER            { printf("TURN %d ", $2); }
;

%%

int main(int argc, char **argv) {
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (yyin == NULL) {
            perror(argv[1]);
            exit(1);
        }
    }
    yyparse();
}

void yyerror(const char *s) {
    printf("FAIL\n");
}