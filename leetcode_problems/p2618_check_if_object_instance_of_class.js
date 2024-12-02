// Write a function that checks if a given value is an instance of a given class or superclass.
// For this problem, an object is considered an instance of a given class if that object has access to that class's methods.
// There are no constraints on the data types that can be passed to the function. For example, the value or the class could be undefined.


/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    // working_sol (86.32%, 61.09%) -> (77ms, 59.35mb)  time: O(1) | space: O(1)
    if ((classFunction === null || classFunction === undefined)
        || (obj === null || obj === undefined)) {
        return false;
    }
    let proto = Object.getPrototypeOf(obj);
    while (proto) {
        if (proto.constructor === classFunction) {
            return true; // Found parent prototype
        }
        proto = Object.getPrototypeOf(proto);
    }
    return false;
};


// Time complexity: O(1)
// --------------------
// Auxiliary space: O(1)
