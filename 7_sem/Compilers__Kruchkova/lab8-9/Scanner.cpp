#include "Scanner.h"

Scanner::Scanner() {
    cPtr = 0;
    line = 1;

    keywords[0] = "int";
    keywords[1] = "bool";
    keywords[2] = "short";
    keywords[3] = "long";
    keywords[4] = "void";
    keywords[5] = "return";
    keywords[6] = "main";
    keywords[7] = "true";
    keywords[8] = "false";
    keywords[9] = "switch";
    keywords[10] = "const";
    keywords[11] = "default";
    keywords[12] = "case";
    keywords[13] = "break";

    keywordCode[0] = type_int;
    keywordCode[1] = type_bool;
    keywordCode[2] = type_short;
    keywordCode[3] = type_long;
    keywordCode[4] = type_void;
    keywordCode[5] = type_return;
    keywordCode[6] = type_main;
    keywordCode[7] = type_true;
    keywordCode[8] = type_false;
    keywordCode[9] = type_switch;
    keywordCode[10] = type_const;
    keywordCode[11] = type_default;
    keywordCode[12] = type_case;
    keywordCode[13] = type_break;
}

//������ ���� � �������� �����
void Scanner::readFile(std::string fileName) {
    std::string codeModuleInfo;
    FILE* file;
    //"input.txt"
    fopen_s(&file, fileName.c_str(), "r");

    if (file == nullptr) {
        std::cout << "File is not open" << std::endl;
        std::exit(0);
    }
    //������������ ������ �����
    while (!feof(file)) {
        char c;
        fscanf_s(file, "%c", &c);
        codeModuleInfo.append(std::string(1, c));
    }

    codeModuleInfo.append("\0"); //��������� ������ ��������� ��������� ����
    codeModuleInfo.erase(codeModuleInfo.length() - 1);
    fclose(file); //��������� ���� ����� ���������� ������

    this->text = codeModuleInfo;
}

int Scanner::GetPtr() {
    return cPtr;
}

int Scanner::GetLine() {
    return line;
}

void Scanner::SetPtr(int newPtr) {
    cPtr = newPtr;
}

void Scanner::SetLine(int newLine) {
    line = newLine;
}

void Scanner::scan(int& codeLexeme, std::string& stringLexeme)
{
    while (true) {
        stringLexeme = "";
        //������� ��������/��������� �� ������ ������/�����
        while ((text[cPtr] == ' ') || (text[cPtr] == '\n') || (text[cPtr] == '\t')) {
            if (text[cPtr] == '\n') line++;
            cPtr++;
        }
        //������� ������������� �����������
        if ((text[cPtr] == '/') && (text[cPtr + 1] == '/')) {
            cPtr += 2;
            while (text[cPtr] != '\n' && text[cPtr] != '\0')
                cPtr++;
        }
        //������������� �����������
        else if ((text[cPtr] == '/') && (text[cPtr + 1] == '*')) {
            cPtr += 2;
            while ((text[cPtr + 1] != '/') || (text[cPtr] != '*')) {
                if (text[cPtr] == '\n') line++;
                cPtr++;
                if (text[cPtr + 1] == '\0') {
                    codeLexeme = type_end;
                    stringLexeme = "end";
                    return;
                }
            }
            cPtr += 2;
        }
        //����� ��������� ����
        else if (text[cPtr] == '\0') {
            codeLexeme = type_end;
            stringLexeme = "end";
            return;
        }
        else
        {
            //�������� ���������
            if ((text[cPtr] <= '9') && (text[cPtr] >= '1')) {
                stringLexeme.append(std::string(1, text[cPtr++]));
                while ((text[cPtr] <= '9') && (text[cPtr] >= '0'))
                    stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_int_const;
                return;
            }
            //�������� ��������� 0
            else if (text[cPtr] == '0' && (text[cPtr + 1] <= '9' && text[cPtr + 1] >= '0')) {
                while ((text[cPtr + 1] <= '9') && (text[cPtr + 1] >= '0'))
                    stringLexeme.append(std::string(1, text[cPtr++]));
            }
            else if (text[cPtr] == '0' && (text[cPtr + 1] > '9' || text[cPtr + 1] < '0')) {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_int_const;
                return;
            }
            //�������� �� �������� ����� ��� ������������
            else if (((text[cPtr] >= 'a') && (text[cPtr] <= 'z')) ||
                text[cPtr] == '_' ||
                ((text[cPtr] >= 'A') && (text[cPtr] <= 'Z'))) {
                stringLexeme.append(std::string(1, text[cPtr++]));
                while ((text[cPtr] <= '9') && (text[cPtr] >= '0') ||
                    ((text[cPtr] >= 'a') && (text[cPtr] <= 'z')) ||
                    text[cPtr] == '_' || ((text[cPtr] >= 'A') && (text[cPtr] <= 'Z')))
                    stringLexeme.append(std::string(1, text[cPtr++]));

                for (size_t i = 0; i < KEYWORDS_NUM; i++) {
                    if (keywords[i] == stringLexeme)
                    {
                        codeLexeme = keywordCode[i];
                        return;
                    }
                }
                codeLexeme = type_ident;
                return;

            }
            //�����
            else if (text[cPtr] == '.') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_dot;
                return;
            }
            //�������
            else if (text[cPtr] == ',') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_comma;
                return;
            }
            //���������
            else if (text[cPtr] == ':') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_colon;
                return;
            }
            //����� � �������
            else if (text[cPtr] == ';') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_semicolon;
                return;
            }
            //������� ������������� ������
            else if (text[cPtr] == '(') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_lbracket;
                return;
            }
            //������� ������������� ������
            else if (text[cPtr] == ')') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_rbracket;
                return;
            }
            //�������� ������������� ������
            else if (text[cPtr] == '{') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_lparenthesis;
                return;
            }
            //�������� ������������� ������
            else if (text[cPtr] == '}') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_rparenthesis;
                return;
            }
            //���������� ������������� ������
            else if (text[cPtr] == '[') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_square_lparenthesis;
                return;
            }
            //���������� ������������� ������
            else if (text[cPtr] == ']') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                codeLexeme = type_square_rparenthesis;
                return;
            }
            //��������
            else if (text[cPtr] == '\'') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] != '\'') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    if (text[cPtr] == '\'') {
                        stringLexeme.append(std::string(1, text[cPtr++]));
                        codeLexeme = type_char_const;
                        return;
                    }
                    std::cout << "Error char constant" << std::endl;
                    codeLexeme = type_error;
                    return;
                }
                codeLexeme = type_quote;
                return;
            }
            //���� ����
            else if (text[cPtr] == '+') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_plus_assign;
                    return;
                }
                if (text[cPtr] == '+') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_plus_plus;
                    return;
                }
                codeLexeme = type_plus;
                return;
            }
            //���� �����, -=, --
            else if (text[cPtr] == '-') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_minus_assign;
                    return;
                }
                if (text[cPtr] == '-') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_minus_minus;
                    return;
                }
                codeLexeme = type_minus;
                return;
            }
            //���� ��������
            else if (text[cPtr] == '*') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_mul_assign;
                    return;
                }
                codeLexeme = type_mul;
                return;
            }
            //���� �������
            else if (text[cPtr] == '/') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_div_assign;
                    return;
                }
                codeLexeme = type_div;
                return;
            }
            //���� �������� ��������� ������� �� �������
            else if (text[cPtr] == '%') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_mod_assign;
                    return;
                }
                codeLexeme = type_mod;
                return;
            }
            else if (text[cPtr] == '!') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_ne;
                    return;
                }
                std::cout << "Error no '!' operation" << std::endl;
                codeLexeme = type_error;
                return;
            }
            //���� ������ ��� (������ ��� �����)
            else if (text[cPtr] == '<') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_le;
                    return;
                }
                codeLexeme = type_lt;
                return;
            }
            //���� ������ ��� (������ ��� �����)
            else if (text[cPtr] == '>') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_ge;
                    return;
                }
                codeLexeme = type_gt;
                return;
            }
            //���� ������������ ��� ���������
            else if (text[cPtr] == '=') {
                stringLexeme.append(std::string(1, text[cPtr++]));
                if (text[cPtr] == '=') {
                    stringLexeme.append(std::string(1, text[cPtr++]));
                    codeLexeme = type_eq;
                    return;
                }
                codeLexeme = type_assign;
                return;
            }

            stringLexeme.append(std::string(1, text[cPtr++]));
            std::string message = "Wrong at line ";
            message.append(std::to_string(line));
            message.append("  Error symbol: ");
            message.append(stringLexeme);
            std::cout << message;
            codeLexeme = type_error;
        }
    }
}