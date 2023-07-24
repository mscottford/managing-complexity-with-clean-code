// This project can be run using `dotnet run`.

var tiger = new Tiger();
var chicken = new Chicken();

// Outputs "It's fast!"
PrintSpeedStatus(tiger);
// Outputs "It's slow!"
PrintSpeedStatus(chicken);

void PrintSpeedStatus(Animal animal)
{
    if (animal is Tiger)
    {
        System.Console.WriteLine("It's fast!");
    }
    else if (animal is Chicken)
    {
        System.Console.WriteLine("It's slow!");
    }
    else
    {
        System.Console.WriteLine("It's doesn't move!");
    }
}

abstract class Animal
{
    public virtual int Speed { get { return 0; } }
}

class Tiger : Animal
{
    public new int Speed { get { return 20; } }
}

class Chicken : Animal
{
    public override int Speed { get { return 5; } }
}
