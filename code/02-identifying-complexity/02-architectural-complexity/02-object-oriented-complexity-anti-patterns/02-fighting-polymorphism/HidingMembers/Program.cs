// This project can be run using `dotnet run`.

var tiger = new Tiger();
// Outputs "Speed as `Tiger`: 20"
System.Console.WriteLine($"Speed as `Tiger`: {tiger.Speed}");

var animal = tiger as Animal;
// Outputs "Speed as `Animal`: 0"
System.Console.WriteLine($"Speed as `Animal`: {animal.Speed}");

abstract class Animal
{
    public virtual int Speed { get { return 0; } }
}

class Tiger : Animal
{
    public new int Speed { get { return 20; } }
}
