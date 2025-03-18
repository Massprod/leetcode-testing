// Write code that enhances all arrays such that you can call the array.groupBy(fn)
//  method on any array and it will return a grouped version of the array.
// A grouped array is an object where each key is the output of fn(arr[i])
//  and each value is an array containing all items in the original array
//  which generate that key.
// The provided callback fn will accept an item in the array and return a string key.
// The order of each value list should be the order the items appear in the array.
// Any order of keys is acceptable.
// Please solve it without lodash's _.groupBy function.
// ---------------------------
// 0 <= array.length <= 10 ** 5
// fn returns a string


// working_sol (90.81%, 23.22%) -> (96ms, 78.51mb)  time: O(n) | space: O(n)
/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((out, value) => {
        const fnKey = fn(value);
        out[fnKey] = out[fnKey] || []
        out[fnKey].push(value)
        return out
    }, {})
};


// Time complexity: O(n) <- n - length of the input array.
// Always calling function on every index of the input array, once => O(n).
// ---------------------------
// Auxiliary space: O(n)
// In the worst case, every return value is unique.
// Output array will allocate space for each unique key.
