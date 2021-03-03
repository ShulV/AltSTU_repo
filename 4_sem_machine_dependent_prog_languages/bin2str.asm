; процедура преобразования двоичного числа в строку символов
; вход - ax - число;
; выход - строка по адресу ds:bx
bin2str proc
        push dx
	push cx
	push bx
	push si
	push ax
	mov cx,6
fill_buff:
        mov byte ptr [bx+1],' '    ; заполнить строку пробелами
	inc bx
	loop fill_buff
	mov  si,10                 ; подготовиться к делению на 10
        or  ax,ax                  ; если в (ax) отрицательное число
        jns clr_div
        neg ax                     ; то изменить его знак
clr_div:
        sub dx,dx                  ; очистить старшую половину делимого
        div si                     ;(dx;ax)/10 -> (рез -> ax, ост->dx)
        add dx,'0'                 ; преобразовать остаток в симв. вид
        dec bx
        mov [bx+1],dl              ; запомнить очередн. цифру в строке
        or  ax,ax                  ; в регистре ax - 0?
        jnz clr_div                ; нет, повторить процедуру
        pop ax
	or ax,ax                   ; исх.число отрицательно ?
        jns no_more                ; нет, тогда все
        dec bx
        mov byte ptr [bx+1],'-'    ; поместить в строку знак '-'
no_more:   
        pop si
        pop bx
        mov byte ptr [bx],6                  ; поместить счетчик символов
        pop cx
        pop dx
        ret
bin2str endp
