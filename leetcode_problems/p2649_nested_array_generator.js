// Given a multi-dimensional array of integers, return a generator object which yields integers in the same order as inorder traversal.
// A multi-dimensional array is a recursive data structure that contains both integers and other multi-dimensional arrays.
// inorder traversal iterates over each array from left to right, yielding any integers it encounters
//  or applying inorder traversal to any arrays it encounters.
// -------------------------
// 0 <= arr.flat().length <= 10 ** 5
// 0 <= arr.flat()[i] <= 10 ** 5
// maxNestingDepth <= 10 ** 5


/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    // working_sol (64.77%, 51.97%) -> (170ms, 79.13mb)  time: O(n) | space: O(1)
    for (let val of arr) {
        if (val instanceof Array) {
            yield* inorderTraversal(val);
        } else {
            yield val;
        };
    };
};


// Time complexity: O(n) <- n - number of elements in the entire structure.
// Always traversing all elements, array or integer is used once => O(n).
// -------------------------
// Auxiliary space: O(1).
// We're not creating anything extra and just returning values from original reference => O(1).
// Only stack of the recursion, can be considered. But it's ignored by default => O(g) <- g - maximum depths of nested arrays.
