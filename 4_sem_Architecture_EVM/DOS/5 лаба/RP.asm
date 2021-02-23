jmp begin 		; ����������� ������� �� ������ ���������
.org 2			; ��������������� �������������� ������
.db 080			; ����������� ����������
.org 3			;
.db 090			;
.org 8			;
.db 0A5			;
.org 9			;
.db 0E0			;

begin: mvi a,0 		;
stor a,FLAG 		; ���� ������������� ������� (� ����������� ������� ��� ���)
mvi a,2			; ���-�� ���������� ��� �����
mvi b,X			;
int 2			; ����� ������������ ���������� �����
begin2: load a,X	; ������ ���������, ��� X,Y ��� �������
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
int 3 			; ����� ������������ ���������� ������
stop 			;

X: .ds 1 		;
Y: .ds 1 		;
FLAG: .ds 1		;

FUNC: push b		; ������� ������� F(A,B)
			; �� ���� - �������� rA, rB
			; �� ����� - rA
push a			;
load a,FLAG;		;
cmi a, 0 		; a-0 ��������� � ���. ���������
jz FUNC2		; ������� �� ���� �� �������� � ������������� �������
FUNC1:pop a		; �������� � ����������� �������
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
jmp endfunc 		; ����������� ������� �� ����� �� ������������
FUNC2:pop a		; �������� � ������������� �������
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

.org 080 		; 1 ����������� ���������� (����)
di 			;
CYCLIN: push a		;
in 0			;
stor a,00(b)		;
adi b,1			;
pop a			;
loop a,CYCLIN		;
ei 			;
rin 			;

.org 090 		; 2 ����������� ���������� (�����)
di 			;
out 2 			;
ei 			;
rin 			;

.org 0A5		; 1 ���������� ����������
			; ���������� � ��������� ������ �-� �� �+�
			; � �+� �� �-� � ��������� ������������ 
			; � ������� ��������� � �������� ����� � ������� ����������
di			;
mvi a,1 		;
stor a,FLAG 		; ���� ��� ������ ���������
exit1: mvi sp, 0fd 	; ��������� ����
mvi a, begin2		; 
stor a, 01(sp) 		; � sp ������� �� ������ ���������
ei			;
rin			;

.org 0E0		; 2 ���������� ����������
di			;
load a,01(sp)		; �������� SP (��������)
out 6			;
load a,00(sp)		; �������� F (������/���������)
out 7			;
ei			;
rin			;

