// Given an object or array obj, return a compact object.
// A compact object is the same as the original object, except with keys containing falsy values removed.
// This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys.
// A value is considered falsy when Boolean(value) returns false.
// You may assume the obj is the output of JSON.parse. In other words, it is valid JSON.
// ------------------------
// obj is a valid JSON object
// 2 <= JSON.stringify(obj).length <= 10 ** 6


/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
  // working_sol (81.77%, 76.96%) -> (78ms, 59.46mb)  time: O(n) | space: O(n)
  let out = {};
  if (Array.isArray(obj)) {
    out = [];
    obj.map((value) => {
      if (value instanceof Object || Array.isArray(value)) {
        out.push(
          compactObject(value)
        );
        return;
      };
      // `bool` + True
      const res = Boolean(value);
      if (res && value) {
        out.push(value);
      };
    });
  } else if (obj instanceof Object) {
    Object.entries(obj).map(([key, value]) => {
      if (value instanceof Object || Array.isArray(value)) {
        out[key] = compactObject(value);
        return;
      };
      const res = Boolean(value);
      // `bool` + True
      if (res && value) {
        out[key] = value;
      };
    })
  };
  return out;
};


// Time complexity: O(n) <- n - unique elements in input and nested objects.
// Always traversing all unique elements => O(n).
// ------------------------
// Auxiliary space: O(n)
// `out` <- allocates space for all the elements, creating a copy => O(n).


let test = [null, 0, false, 1];
let testOut = JSON.stringify([1]);
let testRes = JSON.stringify(compactObject(test));
console.assert(
   testOut === testRes, `Test: ${testOut} | TestResult: ${testRes} <- Failed`
);

test = {"a": null, "b": [false, 1]};
testOut = JSON.stringify({"b": [1]});
testRes = JSON.stringify(compactObject(test));
console.assert(
   testOut === testRes, `Test: ${testOut} | TestResult: ${testRes} <- Failed`
);

test = [null, 0, 5, [0], [false, 16]]
testOut = JSON.stringify([5, [], [16]]);
testRes = JSON.stringify(compactObject(test));
console.assert(
   testOut === testRes, `Test: ${testOut} | TestResult: ${testRes} <- Failed`
);
