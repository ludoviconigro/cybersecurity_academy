
#include <linux/module.h>
#include <linux/kernel.h>
static int startup(void) (1)
{
printk(KERN_NOTICE "Hello, Kernel Reporting for Duty!\n"); (2) (3)
return 0;
}
static void shutdown(void) (4)
{
printk(KERN_NOTICE "Bye bye!\n");
}
module_init(startup); (5)
module_exit(shutdown); (6)
MODULE_LICENSE("GPL");
