# Word Counter

A simple Python script that counts word frequencies in a text file.

## Description

This project reads a text file and counts how many times each word appears. Words are converted to lowercase for consistent counting, and the results are displayed in the console.

## Usage

```bash
python counter.py <filename>
```

### Example

```bash
python counter.py sample.txt
```

This will output the word frequencies like:
```
word: 5
example: 3
python: 2
...
```

## Requirements

- Python 3.x

No external dependencies are required.

## How it Works

1. Takes a filename as a command-line argument
2. Reads the file line by line
3. Converts each line to lowercase and splits it into words
4. Counts occurrences of each word
5. Prints the word count for each unique word

## Error Handling

If no filename is provided, the script will display an error message:
```
Too few arguments!
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
