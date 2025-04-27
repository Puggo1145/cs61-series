function f(array=[]) {
    array.push(5)
    return array.length
}


// In js, default argument is not a part of a function's value
// It is like a normal formal parameter created when a function is called
console.log(f())
console.log(f())
console.log(f())
