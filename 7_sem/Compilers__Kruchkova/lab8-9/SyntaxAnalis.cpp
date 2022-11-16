#include "SyntaxAnalis.h"

void SyntaxAnalis::ShowError(std::string err) {
    std::cout << err + "\nAt line" + std::to_string(scaner.GetLine()) << std::endl;
    std::exit(0);
}

void SyntaxAnalis::Prog() {
    savePoint = scaner.GetPtr();
    saveLine = scaner.GetLine();
    scaner.scan(currentType, currentLex);
    while (currentType != type_end) {
        if (currentType == type_int || currentType == type_short || currentType == type_long || currentType == type_bool || currentType == type_const) {
            scaner.SetPtr(savePoint);
            scaner.SetLine(saveLine);
            AnaliseData();
        }
        else if (currentType == type_void) {
            scaner.SetPtr(savePoint);
            scaner.SetLine(saveLine);
            AnaliseFunc();
        }
        else ShowError("Not type");
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
    }
    std::cout << "No errors" << std::endl;
}

void SyntaxAnalis::AnaliseData() {
    savePoint = scaner.GetPtr();
    saveLine = scaner.GetLine();
    scaner.scan(currentType, currentLex);
    if (currentType != type_const) {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
        savedType = TVar;
    }
    else savedType = TConst;
    scaner.scan(currentType, currentLex);
    if (currentType != type_int && currentType != type_short && currentType != type_long && currentType != type_bool) ShowError("Not type");
    savedVarType = currentType;
    AnaliseList();
    scaner.scan(currentType, currentLex);
    if (currentType != type_semicolon) ShowError("Not ;");
}

void SyntaxAnalis::AnaliseList() {
    do {
        AnaliseVariable();
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
    } while (currentType == type_comma);
    scaner.SetPtr(savePoint);
    scaner.SetLine(saveLine);
}

void SyntaxAnalis::AnaliseVariable() {
    scaner.scan(currentType, currentLex);
    if (currentType != type_ident) ShowError("Not id");
    root->Check(root->Cur, currentLex, false, TVar);
    root->Check(root->Cur, currentLex, false, TMass);
    root->Check(root->Cur, currentLex, false, TConst);
    std::string saveId = currentLex;
    savePoint = scaner.GetPtr();
    saveLine = scaner.GetLine();
    scaner.scan(currentType, currentLex);
    if (currentType == type_assign) {
        root->Add(&saveId, TVar)->SetTypeVar(savedVarType);
        AnaliseExpression();
    }
    else if (currentType == type_square_lparenthesis) {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
        root->Add(&saveId, TMass)->SetTypeVar(savedVarType);
        AnaliseSquare(true);
        scaner.scan(currentType, currentLex);
        if (currentType != type_assign) ShowError("Not =");
        scaner.scan(currentType, currentLex);
        if (currentType != type_lparenthesis) ShowError("Not {");
        do {
            scaner.scan(currentType, currentLex);
            if (currentType != type_int_const) ShowError("Not const");
            scaner.scan(currentType, currentLex);
        } while (currentType == type_comma);
        if (currentType != type_rparenthesis) ShowError("Not }");
    }
    else {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
        root->Add(&saveId, savedType)->SetTypeVar(savedVarType);
    }
}

void SyntaxAnalis::AnaliseSquare(bool type) {
    scaner.scan(currentType, currentLex);
    if (currentType != type_square_lparenthesis) ShowError("Not [");
    do {
        scaner.scan(currentType, currentLex);
        if (type) {
            if (currentType != type_int_const) ShowError("Not const int");
            root->Cur->AddToMass(std::stoi(currentLex));
        }
        else{
            if (currentType != type_int_const && currentType != type_ident) ShowError("Not const int or id");
            if (currentType != type_int_const) root->Check(root->Cur, currentLex, true, TVar);
        }
        scaner.scan(currentType, currentLex);
        if (currentType != type_square_rparenthesis) ShowError("Not ]");
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
    } while (currentType == type_square_lparenthesis);
    scaner.SetPtr(savePoint);
    scaner.SetLine(saveLine);
}

void SyntaxAnalis::AnaliseExpression() {
    savePoint = scaner.GetPtr();
    saveLine = scaner.GetLine();
    scaner.scan(currentType, currentLex);
    if (currentType != type_plus && currentType != type_minus) {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
    }
    do {
        AnaliseAdd();
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
    } while (currentType == type_lt || currentType == type_gt || currentType == type_le || currentType == type_ge ||
        currentType == type_eq || currentType == type_ne);
    scaner.SetPtr(savePoint);
    scaner.SetLine(saveLine);
}

void SyntaxAnalis::AnaliseAdd() {
    do {
        AnaliseMultiply();
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
    } while (currentType == type_plus || currentType == type_minus);
    scaner.SetPtr(savePoint);
    scaner.SetLine(saveLine);
}

void SyntaxAnalis::AnaliseMultiply() {
    do {
        AnaliseBasicExpress();
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
    } while (currentType == type_mul || currentType == type_div || currentType == type_mod);
    scaner.SetPtr(savePoint);
    scaner.SetLine(saveLine);
}

void SyntaxAnalis::AnaliseBasicExpress() {
    std::string saveId;
    savePoint = scaner.GetPtr();
    saveLine = scaner.GetLine();
    scaner.scan(currentType, currentLex);
    if (currentType == type_lbracket) {
        AnaliseExpression();
        scaner.scan(currentType, currentLex);
        if (currentType != type_rbracket) ShowError("Not )");
    }
    else if (currentType == type_ident) {
        saveId = currentLex;
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
        if (currentType == type_square_lparenthesis) {
            root->Check(root->Cur, saveId, true, TMass);
            scaner.SetPtr(savePoint);
            scaner.SetLine(saveLine);
            AnaliseSquare(false);
        }
        else {
            root->Check(root->Cur, saveId, true, TVar);
            scaner.SetPtr(savePoint);
            scaner.SetLine(saveLine);
        }
    }
    else if (currentType != type_int_const && currentType != type_char_const)
        ShowError("Not basic expression");
}

void SyntaxAnalis::AnaliseFunc() {
    scaner.scan(currentType, currentLex);
    if (currentType != type_void) ShowError("Not void");
    scaner.scan(currentType, currentLex);
    if (currentType != type_ident && currentType != type_main) ShowError("Not id");
    root->Check(root->Cur, currentLex, false, TFunc);
    root->Add(&currentLex, TFunc);
    SemTree* savedPos = root->NewBlock();
    scaner.scan(currentType, currentLex);
    if (currentType != type_lbracket) ShowError("Not (");
    scaner.scan(currentType, currentLex);
    if (currentType != type_rbracket) ShowError("Not )");
    AnaliseSosOp();
    root->SetCurrent(savedPos);
}

void SyntaxAnalis::AnaliseSosOp() {
    scaner.scan(currentType, currentLex);
    if (currentType != type_lparenthesis) ShowError("Not {");
    savePoint = scaner.GetPtr();
    saveLine = scaner.GetLine();
    scaner.scan(currentType, currentLex);
    while (currentType != type_rparenthesis) {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
        AnaliseOpAndData();
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
    }
}

void SyntaxAnalis::AnaliseOpAndData() {
    savePoint = scaner.GetPtr();
    saveLine = scaner.GetLine();
    scaner.scan(currentType, currentLex);
    if (currentType == type_int || currentType == type_short || currentType == type_long || currentType == type_bool || currentType == type_const) {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
        AnaliseData();
    }
    else if (currentType == type_ident) {
        root->Check(root->Cur, currentLex, true, TVar);
        scaner.scan(currentType, currentLex);
        if (currentType == type_assign) {
            AnaliseExpression();
            scaner.scan(currentType, currentLex);
            if (currentType != type_semicolon) ShowError("Not ;");
        }
        else if (currentType == type_plus_assign || currentType == type_mul_assign || currentType == type_div_assign || 
            currentType == type_minus_assign || currentType == type_mod_assign) {
            scaner.SetPtr(savePoint);
            scaner.SetLine(saveLine);
            AnaliseBitSave();
        }
        else if (currentType == type_plus_plus || currentType == type_minus_minus) {
            scaner.SetPtr(savePoint);
            scaner.SetLine(saveLine);
            AnaliseInc();
        }
        else {
            ShowError("Not = or function");
        }
    }
    else if (currentType == type_plus_plus || currentType == type_minus_minus) {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
        AnaliseInc();
    }
    else if (currentType == type_lparenthesis) {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
        SemTree* savedPos = root->NewBlock();
        AnaliseSosOp();
        root->SetCurrent(savedPos);
    }
    else if (currentType == type_switch) {
        scaner.SetPtr(savePoint);
        scaner.SetLine(saveLine);
        AnaliseSwitch();
    }
    else if(currentType != type_semicolon) ShowError("Not operator or data");
}

void SyntaxAnalis::AnaliseSwitch() {
    scaner.scan(currentType, currentLex);
    if (currentType != type_switch) ShowError("Not switch");
    scaner.scan(currentType, currentLex);
    if (currentType != type_lbracket) ShowError("Not (");
    AnaliseExpression();
    scaner.scan(currentType, currentLex);
    if (currentType != type_rbracket) ShowError("Not )");
    scaner.scan(currentType, currentLex);
    if (currentType != type_lparenthesis) ShowError("Not {");
    scaner.scan(currentType, currentLex);
    while (currentType == type_case) {
        scaner.scan(currentType, currentLex);
        if (currentType != type_int_const) ShowError("Not const");
        scaner.scan(currentType, currentLex);
        if (currentType != type_colon) ShowError("Not :");
        AnaliseOps();
        scaner.scan(currentType, currentLex);
    }
    if (currentType == type_default) {
        scaner.scan(currentType, currentLex);
        if (currentType != type_colon) ShowError("Not :");
        AnaliseOps();
        scaner.scan(currentType, currentLex);
    }
    if (currentType != type_rparenthesis) ShowError("Not }");
}

void SyntaxAnalis::AnaliseOps() {
    savePoint = scaner.GetPtr();
    saveLine = scaner.GetLine();
    scaner.scan(currentType, currentLex);
    while (currentType != type_case && currentType != type_default && currentType != type_rparenthesis) {
        if (currentType == type_break) {
            scaner.scan(currentType, currentLex);
            if (currentType != type_semicolon) ShowError("Not ;");
        }
        else {
            scaner.SetPtr(savePoint);
            scaner.SetLine(saveLine);
            AnaliseOpAndData();
        }
        savePoint = scaner.GetPtr();
        saveLine = scaner.GetLine();
        scaner.scan(currentType, currentLex);
    }
    scaner.SetPtr(savePoint);
    scaner.SetLine(saveLine);
}

void SyntaxAnalis::AnaliseInc() {
    scaner.scan(currentType, currentLex);
    if (currentType == type_plus_plus || currentType == type_minus_minus) {
        scaner.scan(currentType, currentLex);
        if (currentType != type_ident) ShowError("Not id");
        root->Check(root->Cur, currentLex, true, TVar);
    }
    else if (currentType == type_ident) {
        root->Check(root->Cur, currentLex, true, TVar);
        scaner.scan(currentType, currentLex);
        if (currentType != type_plus_plus && currentType != type_minus_minus) ShowError("Not ++ or --");
    }
    else ShowError("Not ++ or --");
}

void SyntaxAnalis::AnaliseBitSave() {
    scaner.scan(currentType, currentLex);
    if (currentType != type_ident) ShowError("Not id");
    root->Check(root->Cur, currentLex, true, TVar);
    scaner.scan(currentType, currentLex);
    if (currentType != type_plus_assign && currentType != type_mul_assign && currentType != type_div_assign &&
        currentType != type_minus_assign && currentType != type_mod_assign) ShowError("Not BitSave");
    AnaliseExpression();
}


SyntaxAnalis::SyntaxAnalis(std::string fileName) {
    scaner.readFile(fileName);
    currentType = -1;
    savePoint = -1;
    saveLine = -1;
    SemTree::SetCurrent(root);
}