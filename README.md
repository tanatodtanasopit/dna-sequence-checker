# DNA Sequence Checker

A simple Python tool that validates a DNA sequence and reports its length, base composition, and GC content.

## What it does

Given a DNA sequence, the program:

- Checks that the sequence is valid (contains only the bases A, T, C, and G)
- Reports the total length of the sequence
- Counts each base (A, G, C, T)
- Calculates the GC content as a percentage

If the sequence contains any invalid character, it rejects the input and asks again.

## How to run it

```bash
python dna_checker.py
```

Then type or paste a DNA sequence when prompted. Input is case-insensitive (`atgc` and `ATGC` are treated the same).

## Example

```
DNA sequence: AAGGCCTT
Valid sequence
Length: 8
A: 2 G: 2 C: 2 T: 2
GC Content: 50.0
```

Entering an invalid sequence:

```
DNA sequence: ATGCN
Invalid sequence
```

## How it works

The program loops over each character in the sequence to confirm every base is valid, then uses Python's built-in string methods to count bases and compute GC content. GC content is calculated as `(G + C) / length * 100`, which makes it comparable across sequences of any length.

## Built with

- Python 3 (standard library only, no external packages required)

## About

This is the first project in a self-directed bioinformatics learning path, built while working through Python fundamentals. A future version will read the sequence from a file rather than requiring manual input.
