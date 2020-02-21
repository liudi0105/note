# 集合

## List

Java 中的 List 接口有 `ArrayList`, `LinkedList`, `Vector`几种实现。

这三者都实现了 List 接口，使用方式也很相似,主要区别在于因为实现方式的不同,所以对不同的操作具有不同的效率。

ArrayList 是一个可改变大小的数组.当更多的元素加入到 ArrayList 中时,其大小将会动态地增长.内部的元素可以直接通过 get 与 set 方法进行访问,因为 ArrayList 本质上就是一个数组.

LinkedList 是一个双链表,在添加和删除元素时具有比 ArrayList 更好的性能.但在 get 与 set 方面弱于 ArrayList.

当然,这些对比都是指数据量很大或者操作很频繁的情况下的对比,如果数据和运算量很小,那么对比将失去意义.

Vector 和 ArrayList 类似,但属于强同步类。如果你的程序本身是线程安全的(thread-safe,没有在多个线程之间共享同一个集合/对象),那么使用 ArrayList 是更好的选择。

Vector 和 ArrayList 在更多元素添加进来时会请求更大的空间。Vector 每次请求其大小的双倍空间，而 ArrayList 每次对 size 增长 50%.

而 LinkedList 还实现了 Queue 接口,该接口比 List 提供了更多的方法,包括 offer(),peek(),poll()等.

注意: 默认情况下 ArrayList 的初始容量非常小,所以如果可以预估数据量的话,分配一个较大的初始值属于最佳实践,这样可以减少调整大小的开销。

## Set 是如何确保元素不重复的

在 Java 的 Set 体系中，根据实现方式不同主要分为两大类。HashSet 和 TreeSet。

1、TreeSet 是二叉树实现的,Treeset 中的数据是自动排好序的，不允许放入 null 值 2、HashSet 是哈希表实现的,HashSet 中的数据是无序的，可以放入 null，但只能放入一个 null，两者中的值都不能重复，就如数据库中唯一约束

在 HashSet 中，基本的操作都是有 HashMap 底层实现的，因为 HashSet 底层是用 HashMap 存储数据的。当向 HashSet 中添加元素的时候，首先计算元素的 hashcode 值，然后通过扰动计算和按位与的方式计算出这个元素的存储位置，如果这个位置位空，就将元素添加进去；如果不为空，则用 equals 方法比较元素是否相等，相等就不添加，否则找一个空位添加。

TreeSet 的底层是 TreeMap 的 keySet()，而 TreeMap 是基于红黑树实现的，红黑树是一种平衡二叉查找树，它能保证任何一个节点的左右子树的高度差不会超过较矮的那棵的一倍。

TreeMap 是按 key 排序的，元素在插入 TreeSet 时 compareTo()方法要被调用，所以 TreeSet 中的元素要实现 Comparable 接口。TreeSet 作为一种 Set，它不允许出现重复元素。TreeSet 是用 compareTo()来判断重复元素的。
