# LegalDoc_genAI
Mike Legal Task

Drive Link -> https://drive.google.com/drive/folders/1hL-1zGZ05mh7N8J9_px_43lr6VVoozoq?usp=sharing
(The above drive contains all the files and documents used in this project


My cluase extraction regex explanation is as follows

1. Positive Lookbehind (?<=\n):
   - Asserts that what follows should be preceded by a newline character.

2. Capturing Group (\d+(\.\d+)*[.)]):
   - Captures numbered or bulleted clauses.
   - \d matches a digit (equivalent to [0-9]).
   - (\.\d+)* captures sub-clause numbers after a dot.
   - [.)] matches either a dot or a closing parenthesis.

3. \s*:
   - Matches optional whitespace characters.

4. Capturing Group ((?:(?!\n\d+(\.\d+)*[.)]|\n\d+\s*;)[\s\S])*):
   - Captures the content of each clause.
   - Uses negative lookahead to ensure content doesn't start with a new clause number or line with digit and semicolon.
   - [\s\S] matches any whitespace or non-whitespace character.
   - * allows for multiple occurrences of the content.
