// Write code that enhances all arrays such that you can call the snail(rowsCount, colsCount)
//  method that transforms the 1D array into a 2D array organised in the pattern known as snail traversal order.
// Invalid input values should output an empty array.
// If rowsCount * colsCount !== nums.length, the input is considered invalid.
// Snail traversal order starts at the top left cell with the first value of the current array.
// It then moves through the entire first column from top to bottom,
//  followed by moving to the next column on the right and traversing it from bottom to top.
// This pattern continues, alternating the direction of traversal with each column, until the entire current array is covered.
// For example, when given the input array [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15]
//  with rowsCount = 5 and colsCount = 4, the desired output matrix is shown below.
// Note that iterating the matrix following the arrows corresponds to the order of numbers in the original array.
// -------------------------------
// 0 <= nums.length <= 250
// 1 <= nums[i] <= 1000
// 1 <= rowsCount <= 250
// 1 <= colsCount <= 250


/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    // working_sol (53.88%, 40.25%) -> (180ms, 64.94mb)  time: O(m * n) | space: O(m * n)
    let out = [];
    if (rowsCount * colsCount !== this.length) {
        return out;
    };
    // Create matrix.
    out = Array.from({ length: rowsCount }, () => Array(colsCount).fill(0));
    // SnailPopulate
    let curRow = 0;
    let curCol = 0;
    let rowDir = 1;

    for (let value of this) {
        out[curRow][curCol] = value;
        curRow += rowDir;
        if (rowsCount === curRow || curRow < 0) {
            curCol += 1;
            rowDir *= -1
            curRow += rowDir;
        };
    };
    return out;
};


// Time complexity: O(m * n) <- m - length of the input value `rowsCount`, n - length of the input value `colsCount`.
// Always creating matrix of size `m * n` => O(m * n).
// Extra traversing every cell of the matrix to populate with correct values => O((m * n) * 2).
// -------------------------------
// Auxiliary space: O(m * n)
// `out` <- allocates space for `m * n` cells of the matrix => O(m * n).
