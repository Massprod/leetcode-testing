// Given two arrays arr1 and arr2, return a new array joinedArray.
// All the objects in each of the two inputs arrays will contain an id field that has an integer value. 
//  joinedArray is an array formed by merging arr1 and arr2 based on their id key.
// The length of joinedArray should be the length of unique values of id.
// The returned array should be sorted in ascending order based on the id key.
// If a given id exists in one array but not the other, the single object with that id should be included in the result array without modification.
// If two objects share an id, their properties should be merged into a single object:
//  - If a key only exists in one object, that single key-value pair should be included in the object.
//  - If a key is included in both objects, the value in the object from arr2 should override the value from arr1.
// -----------------------------
// arr1 and arr2 are valid JSON arrays
// Each object in arr1 and arr2 has a unique integer id key
// 2 <= JSON.stringify(arr1).length <= 10 ** 6
// 2 <= JSON.stringify(arr2).length <= 10 ** 6


/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    // working_sol (81.66%, 78.39%) -> (308ms, 91.17mb)  time: O(n * log n) | space: O(n + m)
    const uniqueIds = {};
    
    for (let record of arr1) {
        uniqueIds[record['id']] = record;
    };

    for (let record of arr2) {
        const curId = record['id'];
        if (curId in uniqueIds) {
            // Every new record in
            uniqueIds[curId] = {...uniqueIds[curId], ...record};
        } else {
            uniqueIds[curId] = record;
        };
    };
    return Object.values(uniqueIds).sort((record1, record2) => {
        return record1['id'] - record2['id'];
    });
};


// Time complexity: O(n * log n) <- m - length of the input array `arr1`, n - length of the input array `arr2`,
//                                  g - number of unique keys in `arr1` records, h - number of unique keys in `arr2` records.
// In the worst case: every record `id` in `arr1`, `arr2` is the same, and every key inside of them, except `id` is unique. 
// Always traversing whole input array `arr1`, once => O(m).
// Extra traversing whole input array `arr2`, with covering all unique keys inside of every record => O(m + n * (g + h)).
// Sorting combined array with all `id`s stored in it => O(n * log n).
// -----------------------------
// Auxiliary space: O(n + m).
// In the worst case: all records have unique `id`s.
// All records from `arr1` and `arr2` will be stored in `uniqueIds` and sorted later => O(n + m).
