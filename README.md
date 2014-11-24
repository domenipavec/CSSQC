CSS-Quality-Control
===================

## Installation

Prerequisites:
- Python 3.0
- python setuptools

Clone the repository:
```
git clone https://github.com/matematik7/CSSQC.git
```

Install:
```
sudo ./setup.py install
```

## Usage

To run the program type:
```
cssqc -i input_file(s)
```

### Optional arguments

```
cssqc -h
```
Display full argument options help.

```
cssqc -c config_file
```
Specify config file.
All options in config file override the options specified in cssqc/defaults.cfg.
The format is the same as cssqc/defaults.cfg.

```
cssqc -v
```
More verbose warning description and some file statistics.

```
cssqc --bangFormat off
```
All rules can also be overriden on command line using two dashes and rule name.

## Rules

All rules can be deactivated using *off* option.
Rules can be activated using *on*, unless otherwise specified.

### bangFormat

Format of spaces around bang(!) before important.
Options are 'before', 'after', 'both' and 'none'.

Default is 'before'.

### closingBraces

Closing braces on its own line, for oneliners preceeded by space.
Options are 'exact' and 'atleast'. 'atleast' allows any number of spaces.

Default is 'atleast'.

### colonFormat

Format of spaces around colon(:) in properties.
Options are 'before', 'after', 'both', 'none' and 'align'.
You can specify multiple options separated by comma.

Default is 'after,align'.

### duplicatedProperties

Warn on duplicated properties in ruleset.

Default is 'on'.

### finalNewline

File must have newline at the end.

Default is 'on'.

### forceQuote

Force use of single(') or double(") quotes.
Options are 'single' and 'double'.

Default is 'off'.

### groupProperties

Group properties.
Grouping rules are defined in cssqc/group/*.dat.
OPT must be valid grouping name.

Default is 'off'.

### hexFormat
Format hex colors.
Options are:
- 'long' (must be 6 characters long)
- 'short' (must be 3 characters when possible)
- 'lowercase', 'uppercase' and
- 'validate' (must be 3 or 6 characters long).

Multiple options can be specified, separated by comma.

Default is 'validate,lowercase'

### indentation

Ensure proper indentation.
OPT can be integer number of spaces or 'tab'.
Allows right align for properties with same suffix.

Default is '4'.

### lowercase

Force everything lowercase except hex colors, strings and comments.

Default is 'on'.

### nestingDepth

Allow only nested rules up to 'OPT'-th level.
OPT must be integer.

Default is 4.

### noColrKeyword

Do not allow specifing colors with keywords.

Default is 'on'.

### noDescendantSelector

Do not allow descendant selectors.

Default is 'off'.

### noEmptyRules

Do not allow rulesets with empty blocks.

Default is 'on'.

### noIDs

Do not allow IDs in selectors.

Default is 'off'.

### noJSPrefix

Do not allow "js-" prefixes in selectors.

Default is 'on'.

### noLeadingZeros

Do not allow leading zeros with decimals (e.g. 0.3px).

Default is 'off'.

### noMultipleClass

Do not allow multiple class selectors (e.g. .class1.class2).

Default is 'off'.

### noOverqualifying

Do not allow overqualifying.
Options are 'class', 'id' and 'both'.
Class means no tag with class, but only if there are not 2 different rules for different tags with same class.
ID means nothing additional when using ID qualifier.

Default is 'id'.

### noRedundantBodySelectors

Do not allow redundant body selectors (e.g. body {} is ok, but body div {} is not).

Default is 'off'.

### noRedundantChildSelectors

Do not allow redundant child selectors (e.g. ul.class li is ok, but ul li {} is not).

Default is 'off'.

### noTagWithClass

Do not allow tag with class in selectors (e.g. div.class).

Default is 'off'.

### noTrailingZeros

Do not allow trailing zeros with decimals (e.g. .30px).

Default is 'on'.

### noUnderscores

Do not allow underscores in class, id and mixin names.

Default is 'on'.

### noUnversalSelectors

Do not allow universal selectors on their own (e.g. div * {} is not allowed, but *.class {} is ok).

Default is 'on'.

### noZeroPercentage

Do not allow percentage after 0 value.

Default is 'off'.

### noZeroUnits

Do not allow units after 0 value.

Default is 'on'.

### onePropertySingleLine

Force single line for rulesets with only one property.

Default is 'on'.

### openingBraces

Opening braces on the same line as last selector preceeded by one space,
followed by newline (or space for oneliners).
Options are 'exact' and 'atleast'. 'atleast' allows any number of spaces.

Default is 'atleast'.

### propertyOrder

Force ordered properties.
Orders are defined in 'cssqc/order/*.dat'.
OPT must be valid order name.

Default is 'off'.

### propertyValidate

Validate property names.

Default is 'on'.

### selectorDepth

Allow selector depth up to 'OPT'.
OPT must be integer.

Default is '4'.

### singleLinePerProperty

Do not allow property over multiple lines.

Default is 'on'.

### singleLinePerSelector

Do not allow selector over multiple lines.

Default is 'on'.

### singlePropertyPerLine

Only allow one property on each line.

Default is 'on'.

### singleSelectorPerLine

Only allow one selector on each line.

Default is 'off'.

### spaceAfterComma

Commas in lists should be followed by space.

Default is 'on'.

### trailingSemicolon

Last property in ruleset must be semicolon terminated.

Default is 'on'.