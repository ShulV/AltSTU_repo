jmp begin
.org 2
.db 080
.org 3
.db 090
.org 8
.db 0A5
.org 9
.db 0E0
begin: mvi a,5
mvi b,E
int 2
begin2: load a,E
mov b,a
mur a,b
dvi a,2
stor b,P1
load a,F
stor a,P2
call min
load a,RES
mov b,a
mur a,b
stor b,V
load a,C
stor a,P1
load a,D
stor a,P2
call min
load a,RES
mov b,a
mur a,b
load a,V
adr a,b
stor a,P1
load a,A
stor a,P2
call min
load a,RES
int 3
stop

E: .ds 1
F: .ds 1
C: .ds 1
D: .ds 1
A: .ds 1
V: .ds 1
P1: .ds 1
P2: .ds 1
RES: .ds 1

min: load a,P1
load b,P2
cmr a,b
jp next
mov b,a
next: stor b,RES
ret

.org 080
di
CYCLIN: push a
in 0
stor a,00(b)
adi b,1
pop a
loop a,CYCLIN
ei
rin

.org 090
di
out 1
ei
rin

.org 0A5
di
load a,C
out 3
load a,D
out 3
in 3
load a,C
in 3
load a,D
mvi b,00
stor b,V
stor b,P1
stor b,P2
stor b,RES
mvi sp,0fd
mvi a,begin2
RETURN: stor a,1(sp)
ei
rin

.org 0E0
di
pop a
push a
out 4
ei
rin