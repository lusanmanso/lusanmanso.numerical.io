# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Numerical methods coursework in Python — implementations and problem solutions for a numerical analysis course (Spanish-language comments throughout). Topics include finite precision arithmetic, root-finding, and numerical differentiation.

## Commands

```bash
uv sync               # install dependencies
python <script>.py    # run any individual script
```

No test suite or linter is configured.

## Architecture

Each topic lives in its own directory (`tema1/`, `tema2/`, `tema4/`, `labs/`). Every file is a standalone script with all execution logic under `if __name__ == "__main__":`. There is no shared library or module imports between files — each script is self-contained.

**Dependencies:** `numpy` for numerical computation, `sympy` for symbolic math. Python 3.13+, managed with `uv`.

**Code style:**
- Lambda functions are preferred for mathematical expressions passed to solvers
- Output is verbose by design — intermediate steps and error values are printed to demonstrate convergence and numerical instability
- Comments and variable names are in Spanish
