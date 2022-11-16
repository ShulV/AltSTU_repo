#pragma once

#include <iostream>
#include <string>
#include <map>

#define type_int_const 1
#define type_char_const 2
#define type_ident 3

#define type_dot 100
#define type_comma 101
#define type_semicolon 102
#define type_lbracket 103
#define type_rbracket 104
#define type_lparenthesis 105
#define type_rparenthesis 106
#define type_colon 107
#define type_square_lparenthesis 108
#define type_square_rparenthesis 109
#define type_quote 110

#define type_int 200
#define type_short 201
#define type_long 202
#define type_bool 203
#define type_void 204
#define type_return 205
#define type_main 206
#define type_true 207
#define type_false 208
#define type_switch 209
#define type_const 210
#define type_default 211
#define type_case 212
#define type_break 213

#define type_plus 300
#define type_minus 301
#define type_lt 302
#define type_gt 303
#define type_le 304
#define type_ge 305
#define type_eq 306
#define type_ne 307

#define type_mul 308
#define type_div 309
#define type_mod 310
#define type_assign 311
#define type_plus_plus 312
#define type_minus_minus 313
#define type_plus_assign 314
#define type_mul_assign 315
#define type_div_assign 316
#define type_minus_assign 317
#define type_mod_assign 318

#define type_end 400
#define type_error 401

#define KEYWORDS_NUM 14

class Scanner
{
private:
    std::string text; //исходный код программы
    int cPtr; //указатель на символ в исходном коде
    int line; //номер строки, на которой находится указатель

    std::string keywords[KEYWORDS_NUM];
    int keywordCode[KEYWORDS_NUM]{};

public:
    void scan(int& codeLex, std::string& stringLex);
    void readFile(std::string fileName);
    int GetPtr();
    int GetLine();
    void SetPtr(int newPtr);
    void SetLine(int newLine);
    Scanner();
};


