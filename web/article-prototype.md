# JavaScript 中的 this, constructor, prototype

## constructor

对象的 constructor 属性，指向该对象的构造函数。实例对象自身没有 constructor 属性，该属性继承自其原型对象。原型对象的 constructor 指向其对应的构造函数。  
先来看一段代码：

```js
function A() {}
const a = new A()

console.log(a.constructor) // [Function: A]
console.log(A.constructor) // [Function: Function]
```

所有函数的 `constructor` 属性指向 `Function` ，包括 `Function` 自身。

_prototype_：函数的 prototype 属性，指向该函数作为构造函数时所创建的对象的原型对象，除了 `Function.prototype.bind()`，其他函数都有 prototype 属性。

```js
console.log(a.prototype) // undefined
console.log(A.prototype) // A {}
console.log(A.prototype.constructor === A) // true
```

函数 A 在被创建时会添加一个 prototype 属性对象（我们叫作 P），P 的 constructor 属性指向 A。也就是说，一个构造函数对应一个原型对象，反过来也成立，他们内部维护着对方的一个引用。

---

## **proto**

对象的 **proto** 属性，指向对象的原型对象

```js
const b = Object.create(a)

console.log(b.__proto__ === a) // true
console.log(a.__proto__ === A.prototype) // true
```

**构造函数所创建的对象，继承构造函数对应原型对象的属性（变量和方法）**，这是 JS 中属性继承的方式，构造函数在创建一个实例对象时，会为该对象创建一个 **proto** 属性对象，该属性指向构造函数的 prototype 属性对象。**proto** 并非 ECMAScript 标准，主流的浏览器为了完善原型链模式增加此属性，因此不建议在代码中使用此属性，可使用 Object.getProtoTypeOf() 和 Object.setPrototypeOf() 替代。

---

## 原型链

由 **proto** 属性组成的链式结构被叫作原型链。

```js
function Obj() {
  this.a = 'propA'
}
const a = new Obj()
const b = Object.create(a)

console.log(b.a) // propA
```

---

## 静态属性与实例属性

每个构造函数都有一个属性，叫做 prototype(原型)。它可以为特定的一类对象定义通用的方法和公有变量  
通常，私有变量可以用如下方法：

```js
function func() {
  var a = 0;
  var innerFunc() {}
}

console.log(func.a)  // undefined
console.log(func.innerFunc)  // undefined
```

通过函数名定义的方法和变量为静态属性，只能通过函数名加点操作符的形式获取

```js
function Obj() {}
Obj.method = function() {}
Obj.a = 10

console.log(Obj.a) // [10]
console.log(Obj.method) // [Function]

const obj = new Obj()
console.log(obj.a) // undefined
console.log(obj.method) // undefined
```

实例属性

```js
function Obj() {
  this.a = []
  this.method = function() {}
}

console.log(typeof Obj.a) // undefined
console.log(typeof Obj.method) // undefined

const o = new Obj()
console.log(typeof o.a) // object
console.log(typeof o.fn) // function
```

实例属性的这种实现方法有个问题，就是每当创建一个对象时，就会创建一个属性的一个实例。然而当一个属性是方法时，我们更倾向于只创建一个方法实例。这时，就有了 prototype。

prototype，定义一组规则 a，并使对像 b 的 prototype 属性指向 a（为了行文方便，这里把 a 看作原型链的上层，b 为下层），我们说 b 的原型是 a，b 可以使用 a 的任意属性，并且所有 a 的下层对象共用 a 的属性。这是 JS 实现继承的方式。
