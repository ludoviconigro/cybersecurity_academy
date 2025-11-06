>CONSIGLIATO
>> - CREA UNA COPIA DELLA MACCHINA VIRTUALE PER POTER RIPRISTINARE IL TUTTO SE LA MACCHINA VIENE BUTTATA GIU'
>>> - O USA UNA MACCHINA NUOVA SENZA NIENTE

Manda questi comandi 
```bash
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09$ mkdir rootkit
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09$ cd rootkit/
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit$ mkdir kernel
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit$ cd kernel/
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo apt install linux-headers-$(uname -r)
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo apt install gcc-13
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo apt install make -y
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ make
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo insmod hello.ko
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ ls
hello.c   hello.mod    hello.mod.o  Makefile       Module.symvers
hello.ko  hello.mod.c  hello.o      modules.order
```
Per vedere i messaggi del Kernel
```bash
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo dmesg
```
Fra i quali vedremo 
```bash
[ 2525.292703] Hello, Kernel Reporting for Duty!
```
Per fare una query filtrata si può lanciare 
```bash
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo dmesg | grep 'Hello'
[ 2525.292703] Hello, Kernel Reporting for Duty!
```
Per vedere gli ultimi messaggi del kernel
```bash
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo dmesg | tail
[  926.703274] perf: interrupt took too long (39199 > 38577), lowering kernel.perf_event_max_sample_rate to 5000
[ 1594.610125] perf: interrupt took too long (49400 > 48998), lowering kernel.perf_event_max_sample_rate to 4000
[ 1800.286272] workqueue: blk_mq_run_work_fn hogged CPU for >13333us 35 times, consider switching to WQ_UNBOUND
[ 1961.990338] hrtimer: interrupt took 3543068 ns
[ 2069.740216] workqueue: psi_avgs_work hogged CPU for >13333us 4 times, consider switching to WQ_UNBOUND
[ 2226.506858] perf: interrupt took too long (62682 > 61750), lowering kernel.perf_event_max_sample_rate to 3000
[ 2525.217215] hello: loading out-of-tree module taints kernel.
[ 2525.218245] hello: module verification failed: signature and/or required key missing - tainting kernel
[ 2525.292703] Hello, Kernel Reporting for Duty!
[ 2545.739585] workqueue: psi_avgs_work hogged CPU for >13333us 5 times, consider switching to WQ_UNBOUND
```
per elencare tutti i moduli del kernel attualmente caricati nel sistema Linux.
```bash
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo lsmod
```
Per chiudere il modulo 
```bash
ubuntu@ubuntu2404:~/cybersecurity_academy/LAB_09/rootkit/kernel$ sudo rmmod hello
```
Dando poi il comando uscirà l'output
```bash
sudo dmesg

[ 3178.690726] Bye bye!
```
