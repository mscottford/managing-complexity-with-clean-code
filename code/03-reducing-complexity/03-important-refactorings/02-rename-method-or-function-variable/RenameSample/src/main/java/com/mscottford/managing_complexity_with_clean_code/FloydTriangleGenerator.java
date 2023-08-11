package com.mscottford.managing_complexity_with_clean_code;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.ArrayList;
import java.util.List;

public class FloydTriangleGenerator {
    public List<List<Integer>> g(int rc) {
        var r = new ArrayList<List<Integer>>();

        int v = 1;
        int cc = 1;
        for (int ri = 0; ri < rc; ri++) {
            var ro = new ArrayList<Integer>();
            for (int ci = 0; ci < cc; ci++) {
                ro.add(v);
                v++;
            }

            r.add(ro);
            cc++;
        }

        return r;
    }

    public String f(int rowCount) {
        var rows = g(rowCount);

        var buffer = new StringWriter();
        var writer = new PrintWriter(buffer, true);

        var lastRow = rows.get(rows.size() - 1);
        var maxValue = lastRow.get(lastRow.size() - 1);
        var valueWidth = maxValue.toString().length();
        var valueFormat = "%0" + valueWidth + "d";
        var valueSeparator = " ".repeat(valueWidth);

        for (var row: rows) {
            var separator = "";
            for (var value: row) {
                writer.print(separator);
                writer.format(valueFormat, value);
                separator = valueSeparator;
            }
            writer.println();
        }

        return buffer.toString();
    }
}
