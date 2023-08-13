# Sample for Replace Conditional with Polymorphism Refactoring

The `calculator/index.js` contains the original implementation that uses a conditional to determine the operation to perform. The file `calculator/index.refactored.js` contains that uses polymorphism to separate the different operations.

The same set of tests are used to evaluate the correctness of each file. These are defined in `calculator/calculatorTests.js`. The `index.test.js` and `index.refactored.test.js` files import the appropriate `Calculator` instance to test.

## Running the Tests

Assuming that you have `node` version 20.5.1 or higher, and at least version 9.8.0 of `npm`, then you should be able to run the tests with `npm run test` after installing the dependencies with `npm install`.
