export default class Calculator {
  constructor(value = 0) {
    this.value = value;
  }

  execute(command) {
    const [operation, firstOperand, secondOperand] = command.split(' ');

    switch (operation) {
      case 'add':
        if (secondOperand) {
          this.value = Number(firstOperand) + Number(secondOperand);
        } else {
          this.value += Number(firstOperand);
        }
        break;
      case 'subtract':
        if (secondOperand) {
          this.value = Number(firstOperand) - Number(secondOperand);
        } else {
          this.value -= Number(firstOperand);
        }
        break;
      case 'multiply':
        if (secondOperand) {
          this.value = Number(firstOperand) * Number(secondOperand);
        } else {
          this.value *= Number(firstOperand);
        }
        break;
      case 'divide':
        if (secondOperand) {
          this.value = Number(firstOperand) / Number(secondOperand);
        } else {
          this.value /= Number(firstOperand);
        }
        break;
      default:
        throw new Error('Invalid operation');
    }
  }

  get result() {
    return this.value;
  }
};
