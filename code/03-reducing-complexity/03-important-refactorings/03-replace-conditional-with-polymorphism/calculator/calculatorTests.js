export default function calculatorTests(Calculator, name) {
  describe(`${name} Calculator`, () => {
    describe('add', () => {
      test('with two integers', () => {
        const calculator = new Calculator();
        calculator.execute('add 5 3');
        expect(calculator.result).toBe(8);
      });

      test('with two floats', () => {
        const calculator = new Calculator();
        calculator.execute('add 5.5 3.3');
        expect(calculator.result).toBe(8.8);
      });

      test('with two negative numbers', () => {
        const calculator = new Calculator();
        calculator.execute('add -5 -3');
        expect(calculator.result).toBe(-8);
      });

      test('with first number negative', () => {
        const calculator = new Calculator();
        calculator.execute('add -5 3');
        expect(calculator.result).toBe(-2);
      });

      test('with second number negative', () => {
        const calculator = new Calculator();
        calculator.execute('add 5 -3');
        expect(calculator.result).toBe(2);
      })

      test('with two negative floats', () => {
        const calculator = new Calculator();
        calculator.execute('add -5.5 -3.3');
        expect(calculator.result).toBe(-8.8);
      })
    });

    describe('subtract', () => {
      test('with two integers', () => {
        const calculator = new Calculator();
        calculator.execute('subtract 5 3');
        expect(calculator.result).toBe(2);
      });

      test('with two floats', () => {
        const calculator = new Calculator();
        calculator.execute('subtract 5.5 3.3');
        expect(calculator.result).toBe(2.2);
      });

      test('with two negative numbers', () => {
        const calculator = new Calculator();
        calculator.execute('subtract -5 -3');
        expect(calculator.result).toBe(-2);
      });

      test('with first number negative', () => {
        const calculator = new Calculator();
        calculator.execute('subtract -5 3');
        expect(calculator.result).toBe(-8);
      });

      test('with second number negative', () => {
        const calculator = new Calculator();
        calculator.execute('subtract 5 -3');
        expect(calculator.result).toBe(8);
      })

      test('with two negative floats', () => {
        const calculator = new Calculator();
        calculator.execute('subtract -5.5 -3.3');
        expect(calculator.result).toBe(-2.2);
      })
    });

    describe('multiply', () => {
      test('with two integers', () => {
        const calculator = new Calculator();
        calculator.execute('multiply 5 3');
        expect(calculator.result).toBe(15);
      });

      test('with two floats', () => {
        const calculator = new Calculator();
        calculator.execute('multiply 5.5 3.3');
        expect(calculator.result).toBe(18.15);
      });

      test('with two negative numbers', () => {
        const calculator = new Calculator();
        calculator.execute('multiply -5 -3');
        expect(calculator.result).toBe(15);
      });

      test('with first number negative', () => {
        const calculator = new Calculator();
        calculator.execute('multiply -5 3');
        expect(calculator.result).toBe(-15);
      });

      test('with second number negative', () => {
        const calculator = new Calculator();
        calculator.execute('multiply 5 -3');
        expect(calculator.result).toBe(-15);
      })

      test('with two negative floats', () => {
        const calculator = new Calculator();
        calculator.execute('multiply -5.5 -3.3');
        expect(calculator.result).toBe(18.15);
      })
    });

    describe('divide', () => {
      test('with two integers', () => {
        const calculator = new Calculator();
        calculator.execute('divide 5 3');
        expect(calculator.result).toBeCloseTo(1.6666666666666667);
      });

      test('with two floats', () => {
        const calculator = new Calculator();
        calculator.execute('divide 5.5 3.3');
        expect(calculator.result).toBeCloseTo(1.6666666666666667);
      });

      test('with two negative numbers', () => {
        const calculator = new Calculator();
        calculator.execute('divide -5 -3');
        expect(calculator.result).toBeCloseTo(1.6666666666666667);
      });

      test('with first number negative', () => {
        const calculator = new Calculator();
        calculator.execute('divide -5 3');
        expect(calculator.result).toBeCloseTo(-1.6666666666666667);
      });

      test('with second number negative', () => {
        const calculator = new Calculator();
        calculator.execute('divide 5 -3');
        expect(calculator.result).toBeCloseTo(-1.6666666666666667);
      })

      test('with two negative floats', () => {
        const calculator = new Calculator();
        calculator.execute('divide -5.5 -3.3');
        expect(calculator.result).toBeCloseTo(1.6666666666666667);
      })
    });

    describe('multiple operations', () => {
      test('adds using initial value', () => {
        const calculator = new Calculator(5);
        calculator.execute('add 5');
        calculator.execute('add 3');
        expect(calculator.result).toBe(13);
      });

      test('adds ignoring initial value', () => {
        const calculator = new Calculator(5);
        calculator.execute('add 5 3');
        calculator.execute('add 5');
        expect(calculator.result).toBe(13);
      });

      test('subtracts using initial value', () => {
        const calculator = new Calculator(7);
        calculator.execute('subtract 5');
        calculator.execute('subtract 3');
        expect(calculator.result).toBe(-1);
      });

      test('subtracts ignoring initial value', () => {
        const calculator = new Calculator(7);
        calculator.execute('subtract 5 3');
        calculator.execute('subtract 5');
        expect(calculator.result).toBe(-3);
      });

      test('multiplies using initial value', () => {
        const calculator = new Calculator(2);
        calculator.execute('multiply 5');
        calculator.execute('multiply 3');
        expect(calculator.result).toBe(30);
      });

      test('multiplies ignoring initial value', () => {
        const calculator = new Calculator(2);
        calculator.execute('multiply 5 3');
        calculator.execute('multiply 5');
        expect(calculator.result).toBe(75);
      });

      test('divides using initial value', () => {
        const calculator = new Calculator(100);
        calculator.execute('divide 5');
        calculator.execute('divide 3');
        expect(calculator.result).toBeCloseTo(6.666666666666667);
      });

      test('divides ignoring initial value', () => {
        const calculator = new Calculator(100);
        calculator.execute('divide 10 5');
        calculator.execute('divide 3');
        expect(calculator.result).toBeCloseTo(0.666666666666667);
      });
    });
  });
}
