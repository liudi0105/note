# Java 多线程编程

## 一些概念

### 进程和线程

1. 线程: 计算机能够分配的最小 CPU 运算单位。
2. 进程：进程是一个具有一定独立功能的程序关于某个数据集合的一次运行活动。
   线程和进程的区别和联系：

- 不同进程的内存空间不共享，同一进程内的线程内存空间共享。
- 线程存在于进程内，一个进程内存在一个或多个线程。

### 并发和并行

1. 并发：如果一个系统支持同时存在多个任务，那么这是一个并发系统。
2. 并行：系统中有多个任务同时执行，那么这是一个并行系统，并行系统一定是并发系统。

## 多线程的实现方式

### 继承 Thread 类

线程有两种实现方式，一种是继承 Thread 类，示例代码如下：

```java
public class ThreadDemo extends Thread {

    public static void main(String[] args) {
        System.out.println("main thread name: " + Thread.currentThread().getName());
        new ThreadDemo().start();
    }

    @Override
    public void run() {
        System.out.println("run thread name: " + Thread.currentThread().getName());
    }
}
```

### 实现 Runnable 接口

另一种方式是实现 Runnable 接口，示例代码如下：

```java
public class RunnableDemo implements Runnable {

    public static void main(String[] args) {
        System.out.println("main thread name: " + Thread.currentThread().getName());
        new Thread(new RunnableDemo()).start();
    }

    @Override
    public void run() {
        System.out.println("run thread name: " + Thread.currentThread().getName());
    }
}
```

## 线程的常用方法

在 Thread 类中 Java 提供了一些方法，使我们能够对线程的运行状态进行干预。

### sleep()

sleep() 方法使当前正在执行的线程进入指定时长的休眠状态，但不释放当前的线程锁。

### yield()

yield() 方法使当前正在执行的线程进入可执行状态，yield 并未使线程从运行状态进入等待、睡眠或阻塞状态。线程进入可运行状态后有可能被线程调度程序再次选中，此时 yield 的效果并不明显。

## 线程的同步

在讨论线程的同步之前我们来看看两个名词，竞态条件和临界区。

- 竞态条件：由于线程的 CPU 资源在线程调度程序的调配下是随机的，由于临界区的存在，多个线程在不同的执行时序下出现会不同的结果，这种现象叫作竞态条件。

- 临界区：访问或操作共享数据的代码块，或者说会发生竞态条件的代码区域。

由于在并发的情况下存在竞态条件，对多线程不加干预的情况下运行程序，很有可能得出不正确的结果。消除竞态条件的一个方法就是使临界区的代码在多个线程之间串行执行，也就是我们常说的同步。

### synchorized

Java 语言为我们提供了一个内置的 synchronized 关键字，被它修饰的方法叫同步方法，被它修饰的代码块被称为同步代码块，在这里将统一称为同步代码。
同步代码具有以下的特性：

1. 原子性：线程在执行这段代码时，时间上是连续的，不会因线程的调度而失去执行时间。
2. 可见性：TODO。
3. 有序性：有效解决重排序问题。即对于同一个锁，前一个 unlock 操作总是先于后一个 lock 操作。

synchronized 保持原子性的实现方式是锁机制，synchronized 有三种用法：

1. 作用在实例方法上，这时监视器（monitor）的锁是当前对象（`this`），用法如下：

   ```java
   public class SynchronizedDemo {
       private int i = 0;

       public synchronized void compute() {
           System.out.println(i++);
       }
   }
   ```

2. 作用在静态方法上，这时的监视器（monitor）的锁是当前代码所在类的 Class 对象。因为 Class 对象存在于永久态，全局只有一个，因此这个锁是一个全局锁。用法如下：

   ```java
   public class SynchronizedDemo {
       private i = 0;

       public static synchronized void compute() {
           System.out.println(i++);
       }
   }
   ```

3. synchronized 作用在代码块中时，实例方法使用的是当前对象，静态方法中使用的是当前代码所在类的 Class 对象，当然也可以自定义锁，用法如下：

   ```java
   public class SynchronizedDemo {
      private Object lock = new Object();
      private i = 0;

      public void compute() {
          synchronized(lock) {
              System.out.println(i++);
          }

      }
   }
   ```

### 对象锁

另一种同步的方式是使用 `java.concurrent.locks.Lock` 接口，该接口声明了三个主要的方法：

1. lock()：获取锁
2. unlock()：释放锁
3. newCondition()：新建一个 `Condition` 并绑定到当前对象

lock 和 unlock 的用法如下：

```java
public class LockDemo implements Runnable {

    private static Lock lock = new ReentrantLock();

    public static void main(String[] args) {
        new Thread(new LockDemo()).start();
        new Thread(new LockDemo()).start();
        new Thread(new LockDemo()).start();
        new Thread(new LockDemo()).start();
        new Thread(new LockDemo()).start();
    }

    @Override
    public void run() {
        lock.lock();
        try {
            for (int i = 0; i < 4; i++) {
                System.out.println(Thread.currentThread().getName() + ": " + i);
            }
        } finally {
            lock.unlock();
        }
    }
}
```

结果：

```
Thread-0: 0
Thread-0: 1
Thread-0: 2
Thread-0: 3
Thread-1: 0
Thread-1: 1
Thread-1: 2
Thread-1: 3
Thread-2: 0
Thread-2: 1
Thread-2: 2
Thread-2: 3
Thread-4: 0
Thread-4: 1
Thread-4: 2
Thread-4: 3
Thread-3: 0
Thread-3: 1
Thread-3: 2
Thread-3: 3
```

### Lock 和 Condition

Lock 接口用于控制多个线程执行一个任务时的竞态条件带来的问题。
Condition 接口用于控制多线程之间的、基于状态的条件等待。

Condition 的用例：

```java
TODO
```

## 线程间的通信

由上面的 synchronized 同步代码块可以看出，Java 中的同步锁是任意对象。

因为 Java 中的的所有类都是 Object 类的子类（Object 类除外），Object 为我们提供的线程间通信的方法适用于所有对象。

### wait()

wait() 方法使持有当前锁的线程进入等待状态，并将当该线程放入当前锁的等待队列中，直到被唤醒（notify, notifyAll）或被中断

### notify()

当对象以锁的角色被一个线程所持有时，执行 notify() 方法后，当前同步代码执行完毕并释放锁后，会随机唤醒一个当前被该锁 wait() 的线程。

### notifyAll()

notifyAll() 和 notify() 方法类似，不过它唤醒所有当前被该锁 wait() 的线程。

注意：因为 wait，notify 和 notifyAll 都须要在获取锁的条件下被执行，因此只能存在于同步代码中

### 为什么线程间的通信方法在 Ojbect 中，而不是在 Thread 类中

### 线程的优先级

#### 继承性

#### 规则性

#### 随机性

## 对象及变量的并发访问

### volatle

### 管道通信

### join 方法

### ThreadLocal

### InhreitableThreadLocal

### ReentrantLock

### ReentrantReadWriteLock

## 定时器 Timer

### Timer 类

### TimerTask 类

### schedule 方法

### cancel 方法

## 单例模式

## 其他

### 线程状态

### 线程组

### simpleDateFormat 非线程安全
