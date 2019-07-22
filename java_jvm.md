# Java面试题汇总

## Java虚拟机

### 1、Java虚拟机运行时的数据区

在JDK1.8之前，JVM运行时数据区分为堆、虚拟机栈、本地方法栈、方法区、长距离计数器。如下图所示：

![内存模型](./java_se_jvm.jpg)

*虚拟机栈*：线程私有。每个栈帧对应一次方法调用。栈帧中存放了局部变量表（基本数据类型变量和对象引用）、操作数栈、方法出口等信息。当栈的深度超过JVM所允许的范围，就会抛出StackOverflowError的错误。

*本地方法栈*：线程私有，主要与虚拟机用到的Native方法相关。

*程序计数器*：也叫PC寄存器，JVM支持多个线程同时运行，每个线程都有自己的程序计数器。若当前执行的是JVM的方法，则该寄存器中保存当前执行指令的地址。倘若执行的是native方法，则寄存器中为空。

*方法区*：方法区存放类的信息（包括类的字节码，类的结构）、常量、静态变量等。字符串常量池就是在方法区中。虽然Java虚拟机规范把方法区描述为堆的一个逻辑部分，也叫 Non-Heap （非堆）或 Permanent Generation （永久代）。从JDK7开始“去永久代”，JDK7的HotSpot中，已经把原本在方法区中的静态变量、字符串常量池等移到堆内存中。“永久区”是“方法区在HotSpot”上的实现。
*堆*：堆中存放的是对象（包括数组）。当申请不到空间时会抛出OutOfMemoryError。

## 2、PermGen（永久代）

“方法区”是JVM的规范，而“永久代”是方法区的一种实现，并且只有HotSpot才有“PermGen space”，而对于其他类型的虚拟机并没有“PermGen space”。

## 3、Metaspace（元空间）

在JDK8中，永久代已经不存在，类信息、编译后的代码数据等已经移动到MetaSpace（元空间）中，元空间不在堆内存中，直接中用本地内存（NativeMemory）。元空间和永久代的本质类似，都是对JVM规范中方法区的实现。  
不过元空间与永久代之间最大的区别在于：元空间并不在虚拟机中，而是使用本地内存。

## 4、堆内存划分

在JDK7及之前的JDK版本中，堆内存通常被分为三块区域：Young Generation（年轻代）、Old Generation（年老代）、Permanent Generation for VM Matedata（永久代）。  

