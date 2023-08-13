# Sample for Replace Conditional with Function Lookup

The `calculator/lib/calculator/default.rb` contains the original implementation that uses a conditional to determine the operation to perform. The file `calculator/lib/calculator/refactored.rb` contains the version that uses functions to separate the different operations.

The same set of tests are used to evaluate the correctness of each file. These are defined in `calculator/spec/calculator/calculator_examples.rb`. The `calculator/spec/calculator/default_spec.rb` and `calculator/spec/calculator/refactored_spec.rb` files pass in the appropriate `Calculator` instance to test.

## Running the Tests

Assuming that you have `ruby` version 3.0.5 or higher, and at least version 2.4.18 of `bundle`, then you should be able to run the tests with `bundle exec rake spec` after installing the dependencies with `bundle install`.
