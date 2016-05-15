# lambda-calc-spec
Not that lambda calculus really needs a spec...

I can remember Dave Thomas saying that whenever he picks up a new programming
language, the first thing he does is implement a markdown parser. I think
that's really neat... I want to make lambda calculus my "markdown parser."

This is meant to be a simple, consistently easy to implement, full-featured
lambda calculus.

## MVP
### Architecture
#### Pipeline
Tokenizer -> Parser -> Evaluator -> PrettyPrinter

#### Components
 - Mechanism for program to read some code via STDIN

### Names
Single character, `a`-`z`

### Lambda
Single argument, arg and body are dot separated, use `\` for actual lambda
character, e.g. `\x.x`

### Application
Parens indicate application, in the spirit of Lisp. E.g. `(\x.x \y.y)` returns
the second identity function

### General
 - I believe full closures are needed.
 - Whitespace is ignored by the tokenizer

### Examples
 - `\x.x` evaluates to `\x.x`
 - `x` fails to evaluate
 - `(\x.x \y.y)` evaluates to `\y.y` although preserving the `y`s is not
   necessary
 - `((\x.\y.x \b.b) \c.c)` evaluates to `\b.b`
