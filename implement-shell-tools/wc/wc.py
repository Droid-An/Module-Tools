import os
import argparse

parser = argparse.ArgumentParser(
    prog="wc",
    description="Counts words in a file that contain a particular character",
)

parser.add_argument(
    "-l",
    action="store_true",
    help="The number of lines in each input file is written to the standard output.",
)
parser.add_argument(
    "-w",
    action="store_true",
    help="The number of words in each input file is written to the standard output.",
)
parser.add_argument(
    "-c",
    action="store_true",
    help="The number of bytes in each input file is written to the standard output.",
)
parser.add_argument("path", nargs="+", help="The path to search")

args = parser.parse_args()

if not args.w and not args.c and not args.l:
    args.w = args.c = args.l = True
per_file_totals = []
output = []
column_widths = []
for path in args.path:
    output_for_one_file = []
    if args.l or args.w:
        with open(path) as file:
            lines = file.readlines()
            # lines count
            if args.l:
                num_lines = len(lines)
                output_for_one_file.append(num_lines)
            # word count
            if args.w:
                word_count = 0
                for line in lines:
                    lin = line.rstrip()
                    wds = lin.split()
                    word_count += len(wds)

                output_for_one_file.append(word_count)

    if args.c:
        file_size = os.path.getsize(path)
        output_for_one_file.append(file_size)

    if len(args.path) > 1:
        per_file_totals.append(output_for_one_file.copy())
    output_for_one_file.append(path)
    output.append(output_for_one_file)
if len(args.path) > 1:
    total_results = [sum(i) for i in zip(*per_file_totals)]
    total_results.append("total")
    output.append(total_results)

    num_cols = len(total_results) - 1
    column_widths = [len(str(total_results[i])) for i in range(num_cols)]
elif len(args.path) == 1:
    num_cols = len(output[0]) - 1
    column_widths = [len(str([output[0][i]])) for i in range(num_cols)]
for row in output:
    line_parts = []
    for i in range(num_cols):
        # Right-align with 1 space padding (like wc)
        line_parts.append(str(row[i]).rjust(column_widths[i] + 6))
    print("".join(line_parts), row[-1])
