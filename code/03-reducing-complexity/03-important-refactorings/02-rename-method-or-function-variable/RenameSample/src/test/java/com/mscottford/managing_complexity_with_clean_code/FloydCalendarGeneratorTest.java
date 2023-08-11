package com.mscottford.managing_complexity_with_clean_code;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static java.util.Arrays.asList;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertIterableEquals;

public class FloydCalendarGeneratorTest {

    FloydTriangleGenerator generator;

    @BeforeEach
    void setUp() {
        generator = new FloydTriangleGenerator();
    }

    @Test
    void firstRow() {
        var triangle = generator.g(1);

        assertIterableEquals(asList(asList(1)), triangle);
    }

    @Test
    void twoRows() {
        var actualTriangle = generator.g(2);
        var expectedTriangle = asList(
                asList(1),
                asList(2, 3)
        );

        assertIterableEquals(expectedTriangle, actualTriangle);
    }

    @Test
    void threeRows() {
        var actualTriangle = generator.g(3);
        var expectedTriangle = asList(
                asList(1),
                asList(2, 3),
                asList(4, 5, 6)
        );

        assertIterableEquals(expectedTriangle, actualTriangle);
    }

    @Test
    void threeFormattedRows() {
        var actual = generator.f(3);
        var expected = """
                1
                2 3
                4 5 6
                """;
        assertEquals(expected, actual);
    }

    @Test
    void fourRows() {
        var actualTriangle = generator.g(4);
        var expectedTriangle = asList(
                asList(1),
                asList(2, 3),
                asList(4, 5, 6),
                asList(7, 8, 9, 10)
        );

        assertIterableEquals(expectedTriangle, actualTriangle);
    }

    @Test
    void fiveRows() {
        var actualTriangle = generator.g(5);
        var expectedTriangle = asList(
                asList(1),
                asList(2, 3),
                asList(4, 5, 6),
                asList(7, 8, 9, 10),
                asList(11, 12, 13, 14, 15)
        );

        assertIterableEquals(expectedTriangle, actualTriangle);
    }

    @Test
    void fiveFormattedRows() {
        var actual = generator.f(5);
        var expected = """
                01
                02  03
                04  05  06
                07  08  09  10
                11  12  13  14  15
                """;
        assertEquals(expected, actual);
    }

    @Test
    void sixRows() {
        var actualTriangle = generator.g(6);
        var expectedTriangle = asList(
                asList(1),
                asList(2, 3),
                asList(4, 5, 6),
                asList(7, 8, 9, 10),
                asList(11, 12, 13, 14, 15),
                asList(16, 17, 18, 19, 20, 21)
        );

        assertIterableEquals(expectedTriangle, actualTriangle);
    }

    @Test
    void fourteenRows() {
        var actualTriangle = generator.g(14);
        var expectedTriangle = asList(
                asList(1),
                asList(2, 3),
                asList(4, 5, 6),
                asList(7, 8, 9, 10),
                asList(11, 12, 13, 14, 15),
                asList(16, 17, 18, 19, 20, 21),
                asList(22, 23, 24, 25, 26, 27, 28),
                asList(29, 30, 31, 32, 33, 34, 35, 36),
                asList(37, 38, 39, 40, 41, 42, 43, 44, 45),
                asList(46, 47, 48, 49, 50, 51, 52, 53, 54, 55),
                asList(56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66),
                asList(67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78),
                asList(79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91),
                asList(92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105)
        );

        assertIterableEquals(expectedTriangle, actualTriangle);
    }

    @Test
    void fourteenFormattedRows() {
        var actual = generator.f(14);
        var expected = """
                001
                002   003
                004   005   006
                007   008   009   010
                011   012   013   014   015
                016   017   018   019   020   021
                022   023   024   025   026   027   028
                029   030   031   032   033   034   035   036
                037   038   039   040   041   042   043   044   045
                046   047   048   049   050   051   052   053   054   055
                056   057   058   059   060   061   062   063   064   065   066
                067   068   069   070   071   072   073   074   075   076   077   078
                079   080   081   082   083   084   085   086   087   088   089   090   091
                092   093   094   095   096   097   098   099   100   101   102   103   104   105
                """;
        assertEquals(expected, actual);
    }


}
