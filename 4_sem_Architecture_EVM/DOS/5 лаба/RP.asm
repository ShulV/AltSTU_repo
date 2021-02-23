jmp begin 		; безусловный переход на начало программы
.org 2			; зарезервировать соотвествующие €чейки
.db 080			; программных прерываний
.org 3			;
.db 090			;
.org 8			;
.db 0A5			;
.org 9			;
.db 0E0			;

begin: mvi a,0 		;
stor a,FLAG 		; флаг использовани€ функции (с измененными знаками или нет)
mvi a,2			; кол-во параметров дл€ ввода
mvi b,X			;
int 2			; вызов программного прерывани€ ввода
begin2: load a,X	; начало программы, где X,Y уже введены
load b,Y		;
call FUNC 		;	
push a 			;
load a,Y 		;
load b,X 		;
call FUNC 		;
pop b 			;
adr a,b 		;
push a 			;
mvi a,2 		;
mvi b,3 		;
call FUNC 		;
pop b 			;
xchg 			;
sbr a,b 		;
int 3 			; вызов программного прерывани€ вывода
stop 			;

X: .ds 1 		;
Y: .ds 1 		;
FLAG: .ds 1		;

FUNC: push b		; ‘”Ќ ÷»я ѕќƒ—„≈“ F(A,B)
			; на вход - регистры rA, rB
			; на выход - rA
push a			;
load a,FLAG;		;
cmi a, 0 		; a-0 результат в рег. признаков
jz FUNC2		; переход по нулю на алгоритм с неизмененными знаками
FUNC1:pop a		; алгоритм с измененными знаками
sbr a,b 		; *
xchg			;
mur a,b 		;
pop a 			;
push b 			;
xchg 			;
mur a,b 		;
adi b,1 		; *
pop a 			;
sbr a,b 		; *
jmp endfunc 		; безусловный переход на выход из подпрограммы
FUNC2:pop a		; алгоритм с неизмененными знаками
adr a,b 		; *
xchg 			;
mur a,b 		;
pop a 			;
push b 			;
xchg 			;
mur a,b 		;
sbi b,1 		; *
pop a 			;
adr a,b 		; *
endfunc:ret 		; 

.org 080 		; 1 ѕ–ќ√–јћћЌќ≈ ѕ–≈–џ¬јЌ»≈ (¬¬ќƒ)
di 			;
CYCLIN: push a		;
in 0			;
stor a,00(b)		;
adi b,1			;
pop a			;
loop a,CYCLIN		;
ei 			;
rin 			;

.org 090 		; 2 ѕ–ќ√–јћћЌќ≈ ѕ–≈–џ¬јЌ»≈ (¬џ¬ќƒ)
di 			;
out 2 			;
ei 			;
rin 			;

.org 0A5		; 1 јѕѕј–ј“Ќќ≈ ѕ–≈–џ¬јЌ»≈
			; прерывание Ц изменение знаков У-Ф на У+Ф
			; и У+Ф на У-Ф в алгоритме подпрограммы 
			; и рестарт программы с очисткой стека и рабочих переменных
di			;
mvi a,1 		;
stor a,FLAG 		; флаг дл€ выбора алгоритма
exit1: mvi sp, 0fd 	; почистить стек
mvi a, begin2		; 
stor a, 01(sp) 		; в sp команду из начала программы
ei			;
rin			;

.org 0E0		; 2 јѕѕј–ј“Ќќ≈ ѕ–≈–џ¬јЌ»≈
di			;
load a,01(sp)		; загрузка SP (счЄтчика)
out 6			;
load a,00(sp)		; загрузка F (флагов/признаков)
out 7			;
ei			;
rin			;

