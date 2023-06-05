%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}

%token SUBJECT
POLITE_WORD
COMMA
AND
THEN
NUMBER
DEGREES
MOVE_ACTION
TURN_ACTION
MOVE_UNIT
TURN_UNIT
MOVE_ADVERB
TURN_ADVERB
EOL
%%

sentences: sentence                 
 | sentences EOL sentences
 | sentences EOL
 ;

sentence: SUBJECT POLITE_WORD instructions	
        | POLITE_WORD SUBJECT instructions
;

instructions: instruction 
 | instruction union instructions
;

union: COMMA AND THEN 
 | COMMA AND
 | COMMA THEN
 | COMMA
 | AND THEN
 | THEN
 | AND


instruction: MOVE_ACTION lenght MOVE_UNIT MOVE_ADVERB     { printf("MOV,%d\n", $2); }
    | MOVE_ACTION lenght MOVE_UNIT                      { printf("MOV,%d\n", $2); }
    | TURN_ACTION lenght TURN_UNIT TURN_ADVERB          { printf("TURN,%d\n", $2); }
    | TURN_ACTION lenght TURN_UNIT                      { printf("TURN,%d\n", $2); }
;

lenght: NUMBER { $$ = $1; }
    | DEGREES { $$ = $1; }
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