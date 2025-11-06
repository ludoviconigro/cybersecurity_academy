# Specifica che stiamo compilando un modulo (non built-in) chiamato "hello".
obj-m += hello.o

# La regola 'all' utilizza il comando make per compilare il modulo,
# cercando i file sorgente del kernel in /lib/modules/$(shell uname -r)/build.
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

# La regola 'clean' rimuove i file oggetto e altri file temporanei creati durante la compilazione.
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
