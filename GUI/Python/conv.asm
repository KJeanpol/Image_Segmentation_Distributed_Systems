%include "linux64.inc"

section .data
    newline db 10,0
    picDir db "mybin.txt", 0
    kerDir db "kernel.txt", 0
    outfile db "res.txt", 0
    contents db '-updated-', 0h

section .bss
    argc resb 8
    argPos resb 8
    text resb 3
    Num resb 9

section .text
    global _start

_start:
; ----- test zone------

    ; exit
; ---------------------
    pop rcx
    pop rax

_printArgsLoop:
    mov rcx, [argPos]
    inc rcx
    mov [argPos], rcx

    add r15,1
    cmp r15, 1
    je _setROw
    cmp r15, 2
    je _setCol

_setCol:
    
    pop rax
    mov rcx, [argPos]
    call atoi
    sub rax, 1
    mov rbp, rax ; rbp = col
    jmp conv

_setROw:  
    pop rax
    mov rcx, [argPos]
    call atoi
    sub rax, 1
    mov r11, rax ; rbx = row
    jmp _printArgsLoop

; ------------------------------------------------------------------------
conv:
; init del for i
    mov r12, 1 ; i fila
    jmp testi

bodyi:
; init del for j
    mov r13, 1 ; j columna
    jmp testj

bodyj:
; init del for m
    mov r10, 0 ; aka sum
    mov r14, 0 ; m
    jmp testm

bodym:
; init del for n
    mov r15, 0 ; n
    jmp testn

bodyn:
;------------------------------------------------------------------------------------------------------------------------------------------------------------
    push r10
    push r11
    call readpic
    mov r8, rax
    push r8
    call readker
    sub rax, 2
    pop r8
    imul r8, rax
    pop r11
    pop r10
    add r10, r8
;------------------------------------------------------------------------------------------------------------------------------------------------------------
    inc r15 ; incremento n
testn:
    cmp r15, 3
    jl bodyn

    inc r14 ; incremento m

testm:
    cmp r14, 3
    jl bodym

    push r11
    cmp r10, 0
    jl nega
    cmp r10, 255
    jg pos
    jmp proc

pos:
    mov r10, 255
    jmp proc

nega:
    mov r10, 0

proc:
    mov rsi, r10
    call writer
    pop r11

    inc r13 ; incremento j

testj:
    cmp r13, rbp
    jl bodyj

    inc r12 ; incremento i

testi:
    cmp r12, r11 ;rbx
    jl bodyi
    exit

; ---------------------------------------------------------------

atoi:
    push    rbx             ; preserve ebx on the stack to be restored after function runs
    push    rcx             ; preserve ecx on the stack to be restored after function runs
    push    rdx             ; preserve edx on the stack to be restored after function runs
    push    rsi             ; preserve esi on the stack to be restored after function runs
    mov     rsi, rax        ; move pointer in eax into esi (our number to convert)
    mov     rax, 0          ; initialise eax with decimal value 0
    mov     rcx, 0          ; initialise ecx with decimal value 0
 
.multiplyLoop:
    xor     rbx, rbx        ; resets both lower and uppper bytes of ebx to be 0
    mov     bl, [rsi+rcx]   ; move a single byte into ebx register's lower half
    cmp     bl, 48          ; compare ebx register's lower half value against ascii value 48 (char value 0)
    jl      .finished       ; jump if less than to label finished
    cmp     bl, 57          ; compare ebx register's lower half value against ascii value 57 (char value 9)
    jg      .finished       ; jump if greater than to label finished
 
    sub     bl, 48          ; convert ebx register's lower half to decimal representation of ascii value
    add     rax, rbx        ; add ebx to our interger value in eax
    mov     rbx, 10         ; move decimal value 10 into ebx
    mul     rbx             ; multiply eax by ebx to get place value
    inc     rcx             ; increment ecx (our counter register)
    jmp     .multiplyLoop   ; continue multiply loop
 
.finished:
    mov     rbx, 10         ; move decimal value 10 into ebx
    div     rbx             ; divide eax by value in ebx (in this case 10)
    pop     rsi             ; restore esi from the value we pushed onto the stack at the start
    pop     rdx             ; restore edx from the value we pushed onto the stack at the start
    pop     rcx             ; restore ecx from the value we pushed onto the stack at the start
    pop     rbx             ; restore ebx from the value we pushed onto the stack at the start
    ret


readpic:
    mov qword [text], 0
    mov qword [text+1], 0
    mov qword [text+2], 0
    ; r12 i
    ; r13 j
    ; r14 m
    ; r15 n

    ; r8 = i - 1 + m
    mov r8, r12
    dec r8
    add r8, r14

    ; r9 = j - 1 + n
    mov r9, r13
    dec r9
    add r9, r15

    ; r8 = 3*col*r8
    push rbp
    inc rbp
    imul r8, 3
    imul r8, rbp
    pop rbp

    ; r9 = 3*r9
    imul r9, 3

    add r8, r9

    mov rax, SYS_OPEN
    mov rdi, picDir
    mov rsi, O_RDONLY
    mov rdx, 0
    syscall

    push rax
    mov	rdi, rax
    mov	rax, SYS_LSEEK
    mov	rsi, r8 ; inicio
    mov	rdx, 0
    syscall

    mov rax, SYS_READ
    mov rsi, text
    mov rdx, 3
    syscall

    mov rax, SYS_CLOSE
    pop rdi
    syscall

    mov rax, text
    call atoi
    ret

readker:
    mov qword [text], 0
    mov qword [text+1], 0
    mov qword [text+2], 0
    ; r14 m
    ; r15 n
    ; r8 = m
    ; r9 = n
    mov r8, r14
    imul r8, 9
    mov r9, r15
    imul r9, 3

    add r8, r9

    mov rax, SYS_OPEN
    mov rdi, kerDir
    mov rsi, O_RDONLY
    mov rdx, 0
    syscall

    push rax
    mov	rdi, rax
    mov	rax, SYS_LSEEK
    mov	rsi, r8 ; inicio
    mov	rdx, 0
    syscall

    mov rax, SYS_READ
    mov rsi, text
    mov rdx, 3
    syscall

    mov rax, SYS_CLOSE
    pop rdi
    syscall

    mov rax, text
    call atoi
    ret

writer:
    mov qword [Num], 0
    mov qword [Num+1], 0
    mov qword [Num+2], 0
    mov qword [Num+3], 0
    mov qword [Num+4], 0
    mov qword [Num+5], 0
    mov qword [Num+6], 0
    mov qword [Num+6], 0
    mov     rdi, Num
    call    IntToBin8
    mov     rdx, rax
    
    call _write
    ret

IntToBin8:
    mov     rcx, 7
    mov     rdx, rdi
    
.NextNibble:
    shl     sil, 1
    setc    byte [rdi]
    add     byte [rdi], "0"
    add     rdi, 1
    sub     rcx, 1
    jns     .NextNibble    

    mov     byte [rdi], 10
    
    mov     rax, rdi
    sub     rax, rdx
    inc     rax
    ret
    
_write:
; r8 = i - 1 + m
    mov r8, r12
    dec r8
    add r8, r14

    ; r9 = j - 1 + n
    mov r9, r13
    dec r9
    add r9, r15

    ; r8 = 3*col*r8
    push rbp
    inc rbp
    imul r8, 8
    imul r8, rbp
    pop rbp

    ; r9 = 3*r9
    imul r9, 8

    add r8, r9

    mov rax, SYS_OPEN
    mov rdi, outfile
    mov rsi, O_CREAT+O_WRONLY
    mov rdx, 0644o
    syscall
   
    push rax
    mov	rdi, rax
    mov	rax, SYS_LSEEK
    mov	rsi, r8 ; inicio
    mov	rdx, 0
    syscall

    mov rax, SYS_WRITE
    mov rsi, Num
    mov rdx, 8
    syscall
 
    mov rax, SYS_CLOSE
    pop rdi
    syscall
    ret

 