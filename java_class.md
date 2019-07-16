# Java面试题汇总

## Java基础

### 1、Java中的方法覆盖（Overriding）和方法重载（Overloading）是什么意思

Java中的方法重载发生在同一个类里面两个或者是多个方法的方法名相同但是参数不同的情况。与此相对，方法覆盖是说子类重新定义了父类的方法。方法覆盖必须有相同的方法名，参数列表和返回类型。覆盖者可能不会限制它所覆盖的方法的访问。

### 2、Java中的访问修饰符

|当前类|同一包内|子类|其他包|
|-|-|-|-|
|public|Y|Y|Y|
|protect|Y|Y|N|
|default|Y|N|N|
|private|N|N|N|

### 3、Java 中 switch 支持什么类型的变量

byte, short, int, char, enum, String(JDK7)

