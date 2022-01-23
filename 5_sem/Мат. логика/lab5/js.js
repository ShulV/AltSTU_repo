window.onload = function () {


    let output_block = document.getElementById("output-block__result");
    let btn = document.getElementById("input-block__btn");
    btn.addEventListener("click", () => {
        let input = document.getElementById("input-block__input");
        let input_text = input.value;
        let paragraph = document.createElement("p");
        paragraph.className = "output-block__p";
        if (input_text) paragraph.innerHTML = input_text;
        else paragraph.innerHTML = "пустая строка";
        
        if (input_text) {
            paragraph.innerHTML = input_text;
            let stack = [];
            let obj1 = {iter: 0, result: ""};
            let obj2 = {iter: 0, result: ""}; //для второго итерации сразу 1, т.к. в цикле одна пропадает
            let obj3 = {iter: 0, result: ""};
            isValid(input_text, stack, obj1)
            if(isValid2(input_text, obj2)) paragraph.classList.add('success');
            else paragraph.classList.add('error');
            console.log("Строка: " + input_text + ", длина: " + input_text.length);
            console.log("Алгоритм 1:");
            console.table(obj1);
            console.log("Алгоритм 2:");
            console.table(obj2);
        }
        else {
            paragraph.innerHTML = "пустая строка";
            paragraph.classList.add('warning');
        }
        output_block.appendChild(paragraph);
        input.value = '';
    })
};

//рекурсивный алгоритм со стеком
function isValid(string, stack, obj) {
    obj.iter++;
    if (string[0]==')') {
        if ('(' != stack.pop()) return obj.result=false;
    } 
    else stack.push(string[0]);

    if (string.length>1) {
            if (!isValid(string.slice(1), stack, obj)) return obj.result=false;
    } 
    else {
        if (string[0] != ')') return obj.result=false;
    }

    return obj.result = (stack.length == 0);
}

//рекурсивный алгоритм без стека
function isValid2(string, obj) {
    let wasExit = false;
    for(let i=0; i<string.length-1; i++) {
        obj.iter++;
        if(string[i] == '(' && string[i+1] == ')') {
            string = string.slice(0,i) + string.slice(i+2);
            // console.log("Вырезали из строки (): " + string);
            wasExit = true;
            break;
        }
    }
    if (wasExit) return obj.result=isValid2(string, obj); //если вышли по break

    if(string==='') return obj.result=true;
    else return obj.result=false;
}
