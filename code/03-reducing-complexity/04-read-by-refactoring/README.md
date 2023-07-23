# Read by Refactoring Live Demo

The `commandline` directory is used for a live demo of the Read by Refactoring technique. Specifically, the contents of the `commandline/src/CommandLine/Core/TokenPartitioner.cs`.

## Demo Script

1. Open the project
2. Run the tests with coverage
3. Open `TokenPartitioner.cs`
4. Confirm that "Auto Test" is configured correctly and working
   1. Save needs to trigger a test run
   2. Save needs to trigger building relevant projects
5. Start refactoring `PartitionTokensByType`
   1. Extract method with entire contents, name it `Run`.
   2. Create an inner class named `TokenHandler`
   3. Move `Run` into `TokenHandler`
   4. Change `Run` from `static` to instance method
   5. Change call of `Run` to `new TokenHandler().Run`
   6. Promote local variables in `Run` to fields in `TokenHandler`
   7. Start extract methods from `Run`

## Project Background and Source

The code for this demo is a slightly modified version of the [.NET `commandline` library](https://github.com/commandlineparser/commandline), specifically the [`1e3607b97af6141743edb3c434c06d5b492f6fb3`](https://github.com/commandlineparser/commandline/tree/1e3607b97af6141743edb3c434c06d5b492f6fb3) Git SHA which was commited on March 7, 2023. The project's source code may look different since then. The project's original README file can be found at `commandline/README.md`. It includes additional information about the library.

The following modifications have been made to the project to facilitate the live demo:

* Switched to .NET 7.0 for all projects
* Clarifies an ambiguous reference in to `ReferenceEqualityComparer` in `CommandLine/Core/TokenPartitioner.cs`

The original `LICENSE` file has been preserved in the `commandline` directory, and it should be considered the license that this code is published under.
