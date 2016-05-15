# lambda-calc-spec
Not that lambda calculus really needs a spec...

I can remember Dave Thomas saying that whenever he picks up a new programming
language, the first thing he does it implement a markdown parser. I think
that's really neat... I want to make lambda calculus my "markdown parser."

## MVP
### Architecture
#### Pipeline
Tokenizer -> Parser -> Desugarer (just identity for MVP) -> Evaluator

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
