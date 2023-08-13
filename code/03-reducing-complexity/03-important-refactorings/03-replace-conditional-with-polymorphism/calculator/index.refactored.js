export default class RefactoredCalculator {
  constructor(value = 0) {
    this.value = value;
    this.operations = {
      'add': new AddOperation(this),
      'subtract': new SubtractOperation(this),
      'multiply': new MultiplyOperation(this),
      'divide': new DivideOperation(this),
    }
  }

  execute(command) {
    const [operation, firstOperand, secondOperand] = command.split(' ');

    if (!this.operations[operation]) {    
      throw new Error('Invalid operation');
    }

    this.operations[operation].execute(firstOperand, secondOperand);
  }

  get result() {
    return this.value;
  }
};

class Operation {
  constructor(calculator) {
    this.calculator = calculator;
  }

  execute(firstOperand, secondOperand) {
    throw new Error('Not implemented');
  }
}

class AddOperation extends Operation {
  execute(firstOperand, secondOperand) {
    if (secondOperand) {
      this.calculator.value = Number(firstOperand) + Number(secondOperand);
    } else {
      this.calculator.value += Number(firstOperand);
    }
  }
}

class SubtractOperation extends Operation {
  execute(firstOperand, secondOperand) {
    if (secondOperand) {
      this.calculator.value = Number(firstOperand) - Number(secondOperand);
    } else {
      this.calculator.value -= Number(firstOperand);
    }
  }
}

class MultiplyOperation extends Operation {
  execute(firstOperand, secondOperand) {
    if (secondOperand) {
      this.calculator.value = Number(firstOperand) * Number(secondOperand);
    } else {
      this.calculator.value *= Number(firstOperand);
    }
  }
}

class DivideOperation extends Operation {
  execute(firstOperand, secondOperand) {
    if (secondOperand) {
      this.calculator.value = Number(firstOperand) / Number(secondOperand);
    } else {
      this.calculator.value /= Number(firstOperand);
    }
  }
}
