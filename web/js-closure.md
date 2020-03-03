# 闭包的理解

## 什么是闭包

一个函数的许多变量和绑定了这些变量的环境的表达式（通常是一个函数），因而这些变量也是该表达式的一部分。

## 闭包的特点

1. 作为一个函数变量的一个引用，当函数返回时，其处于激活状态
2. 一个闭包就是当一个函数返回时，一个没有释放资源的栈区

## 闭包的常用方式

### 第一种写法

```js
function Circle(r) {
  this.r = r
}

Circle.PI = 3.14159
Circle.prototype.area = function() {
  return Circle.PI * this.r * this.r
}

const c = new Circle(1.0)
const area = c.area
console.log(area)
```

### 第二种写法

```js
const Circle = function() {
  const obj = new Object()
  obj.PI = 3.14159

  obj.area = function(r) {
    return this.PI * r * r
  }
  return obj
}

const c = new Circle()
const area = c.area(1.0)
console.log(area)
```

### 第三种写法

```js
const Circle = new Object()
Circle.PI = 3.14159
Circle.Area = function(r) {
  return this.PI * r * r
}
const area = Circle.Area(1.0)
console.log(area)
```

### 第四种写法

```js
const Circle = {
  PI: 3.14159,
  area: function(r) {
    return this.PI * r * r
  }
}
const area = Circle.area(1.0)
console.log(area)
```

### Prototype

```js
const dom = function() {}
dom.Show = function() {
  console.log('show function worked')
}
dom.prototype.Display = function() {
  console.log('prototype display worked')
}
dom.display() // error
dom.Show()
const domObj = new Dom()
domObj.Display()
domObj.Show() // error
```

1. 不使用 prototype 属性定义的对象方法，是静态方法，只能直接用类名进行调用！另外，此静态方法中无法使用 this 变量来调用对象其他的属性！

2. 使用 prototype 属性定义的对象方法，是非静态方法，只有在实例化后才能使用！其就去内部可以 this 来引用对象自身中的其他属性！

### 作用域

```js
const dom = function() {
  const Name = 'Default'
  this.Sex = 'Boy'
  this.success = function() {
    console.log('success worked')
  }
}
console.log(dom.Name) // Undefined
console.log(dom.Sex) // Undefined
```

Javascript 中每个 function 都会形成一个作用域，函数内的变量在函数外部无法访问

### JS 闭包的用途

#### 匿名执行函数

```js
const data = {
  table: [],
  tree: {}
}(function(dm) {
  for (let i = 0; i < dm.table.rows; i++) {
    const row = dm.table.rows[i]
    for (let j = 0; j < row.cells; i++) {
      drawCell(i, j)
    }
  }
})(data)
```

这里创建了一个匿名函数，并立即执行它，由于外部无法引用它内部的变量，因此在函数执行完后会立刻释放资源，关键是不污染全局对象

#### 结果缓存

#### 封装

#### 实现类和继承
