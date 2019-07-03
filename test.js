function A() {}
const a = new A();

console.log(a.__proto__ === A.prototype);

console.log('a.constructor: ', a.constructor);
console.log('A.constructor: ', A.constructor);

console.log('a.prototype: ', a.prototype);
console.log('A.prototype: ', A.prototype);

a.prop = 'prop_of_a';
const b = Object.create(a);

console.log('a.__proto__: === A.prototype', a.__proto__ === A.prototype);
console.log('b.__proto__ === a: ', b.__proto__ === a);
console.log('A.__proto__: ', A.__proto__);
console.log(Function.prototype.bind.prototype);
