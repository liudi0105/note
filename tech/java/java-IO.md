---
author: liudi
createTime: 2020-01-13
updateTime: 2020-01-13
---

# Java IO

## Java IO Class Overview Table

Having discussed sources, destinations, input, output and the various IO purposes targeted by the Java IO classes, here is a table listing most (if not all) Java IO classes divided by input, output, being byte based or character based, and any more specific purpose they may be addressing, like buffering, parsing etc.

|                  | Byte Based                          |                                   | Character Based                 |                           |
| ---------------- | ----------------------------------- | --------------------------------- | ------------------------------- | ------------------------- |
|                  | Input                               | Output                            | Input                           | Output                    |
| Basic            | InputStream                         | OutputStream                      | Reader InputStreamReader        | Writer OutputStreamWriter |
| Arrays           | ByteArrayInputStream                | ByteArrayOutputStream             | CharArrayReader                 | CharArrayWriter           |
| Files            | FileInputStream RandomAccessFile    | FileOutputStream RandomAccessFile | FileReader                      | FileWriter                |
| Pipes            | PipedInputStream                    | PipedOutputStream                 | PipedReader                     | PipedWriter               |
| Buffering        | BufferedInputStream                 | BufferedOutputStream              | BufferedReader                  | BufferedWriter            |
| Filtering        | FilterInputStream                   | FilterOutputStream                | FilterReader                    | FilterWriter              |
| Parsing          | PushbackInputStream StreamTokenizer |                                   | PushbackReader LineNumberReader |                           |
| Strings          |                                     |                                   | StringReader                    | StringWriter              |
| Data             | DataInputStream                     | DataOutputStream                  |                                 |                           |
| Data - Formatted |                                     | PrintStream                       |                                 | PrintWriter               |
| Objects          | ObjectInputStream                   | ObjectOutputStream                |                                 |                           |
| Utilities        | SequenceInputStream                 |                                   |                                 |                           |

## 字节流和字符流的区别

## 什么是缓冲区

## 什么是序列化，如何实现 Java 序列化

序列化就是一种用来处理对象流的机制，将对象的内容进行流化。可以对流化后的对象进行读写操作，可以将流化后的对象传输于网络之间。序列化是为了解决在对象流读写操作时所引发的问题

序列化的实现：将需要被序列化的类实现 Serialize 接口，没有需要实现的方法，此接口只是为了标注对象可被序列化的，然后使用一个输出流（如：FileOutputStream）来构造一个 ObjectOutputStream(对象流)对象，再使用 ObjectOutputStream 对象的 write(Object obj)方法就可以将参数 obj 的对象写出

## PrintStream、BufferedWriter、PrintWriter

PrintStream 类的输出功能非常强大，通常如果需要输出文本内容，都应该将输出流包装成 PrintStream 后进行输出。它还提供其他两项功能。与其他输出流不同，PrintStream 永远不会抛出 IOException；而是，异常情况仅设置可通过 checkError 方法测试的内部标志。另外，为了自动刷新，可以创建一个 PrintStream

BufferedWriter:将文本写入字符输出流，缓冲各个字符从而提供单个字符，数组和字符串的高效写入。通过 write()方法可以将获取到的字符输出，然后通过 newLine()进行换行操作。BufferedWriter 中的字符流必须通过调用 flush 方法才能将其刷出去。并且 BufferedWriter 只能对字符流进行操作。如果要对字节流操作，则使用 BufferedInputStream

PrintWriter 的 println 方法自动添加换行，不会抛异常，若关心异常，需要调用 checkError 方法看是否有异常发生，PrintWriter 构造方法可指定参数，实现自动刷新缓存（autoflush）

## 什么是节点流，什么是处理流，它们各有什么用处，处理流的创建有什么特征

节点流：直与数据源相连，用于输入或者输出
处理流：在节点流的基础上对之进行加工，进行一些功能的扩展
处理流的构造器必须要传入节点流的对象
