#### Thread 类中的 start() 和 run() 方法有什么区别？

start() 方法启动新创建的线程，使被创建的线程状态变为可运行状态。当你调用 run() 方法的时候，只会是在原来的线程中调用，没有新的线程启动。start() 方法才会启动新线程。如果我们调用了 Thread 的 run() 方法，它的行为和普通的方法一样，直接运行 run() 方法。为了在新的线程中执行我们的代码，必须使用 Thread.start() 方法。

#### Runnable 和 Callable 有什么区别？

Runnable 和 Callable 都代表那些要在不同的线程中执行的任务。Runnable 从 JDK1.0 开始就有了，Callable 是在 JDK1.5增加的。它们的主要区别是 Callable 的 call() 方法可以返回值和抛出异常，而 Runnable 的 run() 方法则没有这些功能。Callable 可以返回装载有计算结果的 Future 对象。

#### 如何在 Java 中新建一个线程？

1. 实现 Runnable 接口，然后将它传递给 Thread 的构造函数，创建一个 Thread 对象
2. 直接继承 Thread 类。

#### Thread 的 interrupted() 和 isInterrupted() 方法有什么区别？

- interrupted

  ```java
  public static boolean interrupted()
  ```

  检查当前正在运行的线程是否被标记为已中断，并将当前线程的中断标记重置。

- isInterrupted

  ```java
  public boolean isInterrupted()
  ```

  检查调用该方法的对象所代表的线程是否被标记为已中断。

#### suspend() 方法与 resume() 方法的缺点

suspend 和sleep 其实本质是一样的，但是 suspend 之后还要认为的恢复线程（resume），而 resume 操作有可能就会被阻塞而造成死锁；

而sleep却是等待时候后自动回复，也就是说在这中间不会涉及到其他操作。这样就避免了死锁的产生（恢复操作遭到阻塞）。

#### Java 中 wait() 和 sleep() 方法有什么区别？

| wait()                               | sleep()                |
| ------------------------------------ | ---------------------- |
| 在 Thread 类中                       | 在 Object 类中         |
| 调用后，线程会释放锁                 | 调用后，线程不会释放锁 |
| 其他线程调用 notify() 方法后恢复执行 | 一定时间后恢复执行     |

#### 有线程 T1、T2 和 T3。你如何确保 T2 线程在 T1 之后执行，并且 T3 线程在 T2 之后执行？

可以用 Thread 类的 `join` 方法实现这一效果。

#### Java 中新的 Lock 接口相对于同步代码块（synchronized block）有什么优势？

多线程和并发编程中使用 lock 接口的最大优势是它为读和写提供两个单独的锁，可以让你构建高性能数据结构，比如 `ConcurrentHashMap` 和条件阻塞。

#### 如果让你实现一个高性能缓存，支持并发读取和单一写入，你如何保证数据完整性。

#### 如何在 Java 中编写代码解决生产者消费者问题？

#### 写一段死锁代码。你在 Java 中如何解决死锁？

#### 什么是原子操作？Java 中有哪些原子操作？

#### Java 中你如何唤醒阻塞线程？

#### Java 中 `CyclicBarriar` 和 `CountdownLatch` 有什么区别？

#### 你在多线程环境中遇到的最多的问题是什么？你如何解决的？

#### 什么是不可变类？它对于编写并发应用有何帮助？



1. Java 中绿色线程和本地线程的区别？
2. 线程和进程的区别？
3. 多线程的上下文切换是什么？
4. 死锁和活锁的区别？死锁和饥饿的区别？
5. Java 中使用什么线程调度算法？
6. Java 中线程调度是什么？
7. 线程中如何处理某个未处理异常？
8. 什么是线程组？为什么 Java 中不建议使用线程组？
9. 为什么使用 `Executor` 框架比直接创建线程要好？
10. Java 中 `Executor` 和 `Executors` 的区别？[答案](http://javarevisited.blogspot.sg/2017/02/difference-between-executor-executorservice-and-executors-in-java.html)
11. 在 windows 和 linux 系统上分别如何找到占用 CPU 最多的线程？


