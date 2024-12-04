// Given a multi-dimensional array arr and a depth n, return a flattened version of that array.
// A multi-dimensional array is a recursive data structure that contains integers or other multi-dimensional arrays.
// A flattened array is a version of that array with some or all of the sub-arrays removed
//  and replaced with the actual elements in that sub-array.
// This flattening operation should only be done if the current depth of nesting is less than n.
// The depth of the elements in the first array are considered to be 0.
// Please solve it without the built-in Array.flat method.
// -----------------------------
// 0 <= count of numbers in arr <= 10 ** 5
// 0 <= count of subarrays in arr <= 10 ** 5
// maxDepth <= 1000
// -1000 <= each number <= 1000
// 0 <= n <= 1000


/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    // working_sol (37.59%, 65.53%) -> (164ms, 78.09mb)  time: O(m) | space: O(m)
    const flattenArray = (element, curDepth, maxDepth) => {
        if (maxDepth === curDepth || !Array.isArray(element)) {
            return element;
        };
        let flatArray = [];
        for (let arrElement of element) {
            let result = flattenArray(arrElement, curDepth + 1, maxDepth);
            if (Array.isArray(result)) {
                flatArray.push(...result);
            } else {
                flatArray.push(result);
            };
        };
        return flatArray;
    };

    return flattenArray(arr, 0, n)
};


// Time complexity: O(m) <- m - number of elements in the input array `arr`.
// Always using every element `integer` or `array` once => O(m).
// -----------------------------
// Auxiliary space: O(m)
// In the worst case every element in `arr` can be flattened or used.
// `returnValue` <- will allocate space for each element from `arr` => O(m)
