; процедура преобразования строки символов в двоичное число.
; вход - ds:bx   - адрес строки
; выход - ax - число со знаком
;
str2bin  proc
	push bx
	push cx
	sub ax,ax        ; обнулить ax
	sub ch,ch        ; очистить ch
        mov cl,byte ptr [bx]  ; счетчик символов - в CX
blanks: cmp byte ptr[bx+1],' '   ;цикл пропуска пробелов
        jne chk_neg
	inc bx
        loop blanks
        jmp  good        ; не обнаружено чисел. результат - 0
;
; Следующие команды выполняются в случае знака  "-"
;
chk_neg: cmp byte ptr [bx+1],'-'
	jne chk_pos
	inc bx               ; продвинуть указатель
	dec cx               ; уменьшить счетчик
	call conv_ab         ; вызвать программу преобразования
        jc thru              ;
	cmp ax,32768         ; число < -32768
	ja  no_good          ; да, ошибка
        neg ax               ; изменить знак числа
        js  good             ; o'key , выходим
;
; Следующие команды выполняются в случае, если знак не минус
;
chk_pos: cmp byte ptr [bx+1],'+'   ; sign '+' ?
        jne go_conv           ; нет , идти на преобразование
        inc bx                ; сместить указатель в строке
        dec cx                ; уменьшить счетчик символов
go_conv: call conv_ab         ; преобразовать строку в число
        jc thru               ; в случае ошибки - на выход
        cmp ax,32767          ; число не слишком велико ?
        ja no_good            ; слишком велико, ошибка
good:   clc                   ; очистить флаг CY
        jnc thru              
no_good: stc                  ; set carry flag
thru:   pop cx                ; восстановить значения регистров
	pop bx
	jmp skipit
;
; Процедура собственно преобразования числа
;
conv_ab proc
	push bp
	push bx
	push si
	mov  bp,bx      ; поместить указатель на строку в bp
        sub  bx,bx      ; очистить bx
range:  cmp byte ptr ds:[bp+1],'0'  ; символ - цифра ?
        jb  non_dig                 ; нет не цифра
        cmp byte ptr ds:[bp+1],'9'  ; символ > '9'
        jbe digit                   ; символ - цифра
non_dig: stc                        ; установить флаг ошибки
        jc end_conv                 ; и выйти из процедуры
digit:  mov si,10
	push dx                     ; сохранить dx
        mul si                      ; (ax)*(si)->(dx;ax)
        pop dx                      ; восстановить dx
        mov bl,ds:[bp+1]            ; взять очередной символ из строки
        and bx,0fh                  ; преобразовать символ в двоичное
        add ax,bx                   ; добавить цифруу к старому результату
        jc  end_conv                ; если результат слишком велик,то выйти
        inc bp                      ; адрес след цифры в строке
        loop range                  ; замкнуть цикл по количеству символов
        clc                         ; сбросить флаг переноса(нет ошибки)
end_conv:   pop si                    ; восстановить регистры и выйти
         pop bx
         pop bp
         ret
conv_ab  endp
skipit   ret
str2bin  endp
