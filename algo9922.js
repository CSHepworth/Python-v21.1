/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

var str1 = "   hello world     ";
var expected1 = "hello world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
    newstr = "";
    for (var i = 0; i < str.length; i++) {
        if (str[i] != " " && str[i - 1] != " ") {
            newstr += str[i];
        }
    }
    return newstr;
}

console.log(trim(str1));



var strA1 = "yes";
var strB1 = "eys";
var expected1 = true;

var strA2 = "yes";
var strB2 = "eYs";
var expected2 = true;

var strA3 = "no";
var strB3 = "noo";
var expected3 = false;

var strA4 = "silent";
var strB4 = "listen";
var expected4 = true;


/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {
    var splits1 = s1.split("");
    var splits2 = s2.split("");
    console.log(splits2);
    revarr = splits1.reverse();
    console.log(revarr);
    if (revarr = splits2 ) {
        return true;
    }
    else {
        return false;
    }
}

console.log(isAnagram(strA3, strB3));