// The `toFlatObject` function below was copied from the `axios` project,
// specifically from the `lib/utils.js` file. It was retrieved from
// https://github.com/axios/axios/blob/21a5ad34c4a5956d81d338059ac0dd34a19ed094/lib/utils.js#L394-L418 on
// July 23, 2023.
//
// All original comments have been removed.
//
// Comments have been added to illustrate the calculatation of the
// maximum and average indentation level complexity metrics.
//
// The license that applies to this code appears at the bottom of this file.

const toFlatObject = (sourceObj, destObj, filter, propFilter) => {
  // Indentation level 1
  let props;
  // Indentation level 1
  let i;
  // Indentation level 1
  let prop;
  // Indentation level 1
  const merged = {};

  // Indentation level 1
  destObj = destObj || {};
  
  // Indentation level 1
  if (sourceObj == null) return destObj;

  // Indentation level 1
  do {
    // Indentation level 2
    props = Object.getOwnPropertyNames(sourceObj);
    // Indentation level 2
    i = props.length;
    // Indentation level 2
    while (i-- > 0) {
      // Indentation level 3
      prop = props[i];
      // Indentation level 3
      if ((!propFilter || propFilter(prop, sourceObj, destObj)) && !merged[prop]) {
        // Indentation level 4
        destObj[prop] = sourceObj[prop];
        // Indentation level 4
        merged[prop] = true;
      // Indentation level 3
      }
    // Indentation level 2
    }
    // Indentation level 2
    sourceObj = filter !== false && getPrototypeOf(sourceObj);
  // Indentation level 1
  } while (sourceObj && (!filter || filter(sourceObj, destObj)) && sourceObj !== Object.prototype);
  // Indentation level 1
  return destObj;

  // Max indentation level: 4
  // Average indentation level: 2.15
}

// The license below was copied from https://github.com/axios/axios/blob/21a5ad34c4a5956d81d338059ac0dd34a19ed094/LICENSE.

// # Copyright (c) 2014-present Matt Zabriskie & Collaborators
//
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.