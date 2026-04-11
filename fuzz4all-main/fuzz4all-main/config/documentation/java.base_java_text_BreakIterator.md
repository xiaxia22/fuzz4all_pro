# Class BreakIterator

**Source:** `java.base\java\text\BreakIterator.html`

### Class Description

```java
public abstract class
BreakIterator

extends
Object

implements
Cloneable
```

The

BreakIterator

class implements methods for finding
the location of boundaries in text. Instances of

BreakIterator

maintain a current position and scan over text
returning the index of characters where boundaries occur.
Internally,

BreakIterator

scans text using a

CharacterIterator

, and is thus able to scan text held
by any object implementing that protocol. A

StringCharacterIterator

is used to scan

String

objects passed to

setText

.

You use the factory methods provided by this class to create
instances of various types of break iterators. In particular,
use

getWordInstance

,

getLineInstance

,

getSentenceInstance

, and

getCharacterInstance

to create

BreakIterator

s that perform
word, line, sentence, and character boundary analysis respectively.
A single

BreakIterator

can work only on one unit
(word, line, sentence, and so on). You must use a different iterator
for each unit boundary analysis you wish to perform.

Line boundary analysis determines where a text string can be
broken when line-wrapping. The mechanism correctly handles
punctuation and hyphenated words. Actual line breaking needs
to also consider the available line width and is handled by
higher-level software.

Sentence boundary analysis allows selection with correct interpretation
of periods within numbers and abbreviations, and trailing punctuation
marks such as quotation marks and parentheses.

Word boundary analysis is used by search and replace functions, as
well as within text editing applications that allow the user to
select words with a double click. Word selection provides correct
interpretation of punctuation marks within and following
words. Characters that are not part of a word, such as symbols
or punctuation marks, have word-breaks on both sides.

Character boundary analysis allows users to interact with characters
as they expect to, for example, when moving the cursor through a text
string. Character boundary analysis provides correct navigation
through character strings, regardless of how the character is stored.
The boundaries returned may be those of supplementary characters,
combining character sequences, or ligature clusters.
For example, an accented character might be stored as a base character
and a diacritical mark. What users consider to be a character can
differ between languages.

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

**All Implemented Interfaces:** Cloneable

---

### Field Details

#### public static final int DONE

DONE is returned by previous(), next(), next(int), preceding(int)
and following(int) when either the first or last text boundary has been
reached.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected BreakIterator()

Constructor. BreakIterator is stateless and has no default behavior.

---

### Method Details

#### public
Object
clone()

Create a copy of this iterator

**Overrides:**
- clone

in class

Object

**Returns:**
- A copy of this

**See Also:**
- Cloneable

---

#### public abstract int first()

Returns the first boundary. The iterator's current position is set
to the first text boundary.

**Returns:**
- The character index of the first text boundary.

---

#### public abstract int last()

Returns the last boundary. The iterator's current position is set
to the last text boundary.

**Returns:**
- The character index of the last text boundary.

---

#### public abstract int next​(int n)

Returns the nth boundary from the current boundary. If either
the first or last text boundary has been reached, it returns

BreakIterator.DONE

and the current position is set to either
the first or last text boundary depending on which one is reached. Otherwise,
the iterator's current position is set to the new boundary.
For example, if the iterator's current position is the mth text boundary
and three more boundaries exist from the current boundary to the last text
boundary, the next(2) call will return m + 2. The new text position is set
to the (m + 2)th text boundary. A next(4) call would return

BreakIterator.DONE

and the last text boundary would become the
new text position.

**Parameters:**
- n

- which boundary to return. A value of 0
does nothing. Negative values move to previous boundaries
and positive values move to later boundaries.

**Returns:**
- The character index of the nth boundary from the current position
or

BreakIterator.DONE

if either first or last text boundary
has been reached.

---

#### public abstract int next()

Returns the boundary following the current boundary. If the current boundary
is the last text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary following the current boundary.

**Returns:**
- The character index of the next text boundary or

BreakIterator.DONE

if the current boundary is the last text
boundary.
Equivalent to next(1).

**See Also:**
- next(int)

---

#### public abstract int previous()

Returns the boundary preceding the current boundary. If the current boundary
is the first text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary preceding the current boundary.

**Returns:**
- The character index of the previous text boundary or

BreakIterator.DONE

if the current boundary is the first text
boundary.

---

#### public abstract int following​(int offset)

Returns the first boundary following the specified character offset. If the
specified offset equals to the last text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always greater than the offset or the value

BreakIterator.DONE

.

**Parameters:**
- offset

- the character offset to begin scanning.

**Returns:**
- The first boundary after the specified offset or

BreakIterator.DONE

if the last text boundary is passed in
as the offset.

**Throws:**
- IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.

---

#### public int preceding​(int offset)

Returns the last boundary preceding the specified character offset. If the
specified offset equals to the first text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always less than the offset or the value

BreakIterator.DONE

.

**Parameters:**
- offset

- the character offset to begin scanning.

**Returns:**
- The last boundary before the specified offset or

BreakIterator.DONE

if the first text boundary is passed in
as the offset.

**Throws:**
- IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.

**Since:**
- 1.2

---

#### public boolean isBoundary​(int offset)

Returns true if the specified character offset is a text boundary.

**Parameters:**
- offset

- the character offset to check.

**Returns:**
- true

if "offset" is a boundary position,

false

otherwise.

**Throws:**
- IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.

**Since:**
- 1.2

---

#### public abstract int current()

Returns character index of the text boundary that was most
recently returned by next(), next(int), previous(), first(), last(),
following(int) or preceding(int). If any of these methods returns

BreakIterator.DONE

because either first or last text boundary
has been reached, it returns the first or last text boundary depending on
which one is reached.

**Returns:**
- The text boundary returned from the above methods, first or last
text boundary.

**See Also:**
- next()

,

next(int)

,

previous()

,

first()

,

last()

,

following(int)

,

preceding(int)

---

#### public abstract
CharacterIterator
getText()

Get the text being scanned

**Returns:**
- the text being scanned

---

#### public void setText​(
String
newText)

Set a new text string to be scanned. The current scan
position is reset to first().

**Parameters:**
- newText

- new text to scan.

---

#### public abstract void setText​(
CharacterIterator
newText)

Set a new text for scanning. The current scan
position is reset to first().

**Parameters:**
- newText

- new text to scan.

---

#### public static
BreakIterator
getWordInstance()

Returns a new

BreakIterator

instance
for

word breaks

for the

default locale

.

**Returns:**
- A break iterator for word breaks

---

#### public static
BreakIterator
getWordInstance​(
Locale
locale)

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- A break iterator for word breaks

**Throws:**
- NullPointerException

- if

locale

is null

---

#### public static
BreakIterator
getLineInstance()

Returns a new

BreakIterator

instance
for

line breaks

for the

default locale

.

**Returns:**
- A break iterator for line breaks

---

#### public static
BreakIterator
getLineInstance​(
Locale
locale)

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- A break iterator for line breaks

**Throws:**
- NullPointerException

- if

locale

is null

---

#### public static
BreakIterator
getCharacterInstance()

Returns a new

BreakIterator

instance
for

character breaks

for the

default locale

.

**Returns:**
- A break iterator for character breaks

---

#### public static
BreakIterator
getCharacterInstance​(
Locale
locale)

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- A break iterator for character breaks

**Throws:**
- NullPointerException

- if

locale

is null

---

#### public static
BreakIterator
getSentenceInstance()

Returns a new

BreakIterator

instance
for

sentence breaks

for the

default locale

.

**Returns:**
- A break iterator for sentence breaks

---

#### public static
BreakIterator
getSentenceInstance​(
Locale
locale)

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- A break iterator for sentence breaks

**Throws:**
- NullPointerException

- if

locale

is null

---

#### public static
Locale
[] getAvailableLocales()

Returns an array of all locales for which the

get*Instance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

BreakIteratorProvider

implementations.
It must contain at least a

Locale

instance equal to

Locale.US

.

**Returns:**
- An array of locales for which localized

BreakIterator

instances are available.

---

### Additional Sections

#### Class BreakIterator

java.lang.Object

- java.text.BreakIterator

java.text.BreakIterator

**All Implemented Interfaces:** Cloneable

```java
public abstract class
BreakIterator

extends
Object

implements
Cloneable
```

The

BreakIterator

class implements methods for finding
the location of boundaries in text. Instances of

BreakIterator

maintain a current position and scan over text
returning the index of characters where boundaries occur.
Internally,

BreakIterator

scans text using a

CharacterIterator

, and is thus able to scan text held
by any object implementing that protocol. A

StringCharacterIterator

is used to scan

String

objects passed to

setText

.

You use the factory methods provided by this class to create
instances of various types of break iterators. In particular,
use

getWordInstance

,

getLineInstance

,

getSentenceInstance

, and

getCharacterInstance

to create

BreakIterator

s that perform
word, line, sentence, and character boundary analysis respectively.
A single

BreakIterator

can work only on one unit
(word, line, sentence, and so on). You must use a different iterator
for each unit boundary analysis you wish to perform.

Line boundary analysis determines where a text string can be
broken when line-wrapping. The mechanism correctly handles
punctuation and hyphenated words. Actual line breaking needs
to also consider the available line width and is handled by
higher-level software.

Sentence boundary analysis allows selection with correct interpretation
of periods within numbers and abbreviations, and trailing punctuation
marks such as quotation marks and parentheses.

Word boundary analysis is used by search and replace functions, as
well as within text editing applications that allow the user to
select words with a double click. Word selection provides correct
interpretation of punctuation marks within and following
words. Characters that are not part of a word, such as symbols
or punctuation marks, have word-breaks on both sides.

Character boundary analysis allows users to interact with characters
as they expect to, for example, when moving the cursor through a text
string. Character boundary analysis provides correct navigation
through character strings, regardless of how the character is stored.
The boundaries returned may be those of supplementary characters,
combining character sequences, or ligature clusters.
For example, an accented character might be stored as a base character
and a diacritical mark. What users consider to be a character can
differ between languages.

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

**Since:** 1.1
**See Also:** CharacterIterator

public abstract class

BreakIterator

extends

Object

implements

Cloneable

The

BreakIterator

class implements methods for finding
the location of boundaries in text. Instances of

BreakIterator

maintain a current position and scan over text
returning the index of characters where boundaries occur.
Internally,

BreakIterator

scans text using a

CharacterIterator

, and is thus able to scan text held
by any object implementing that protocol. A

StringCharacterIterator

is used to scan

String

objects passed to

setText

.

You use the factory methods provided by this class to create
instances of various types of break iterators. In particular,
use

getWordInstance

,

getLineInstance

,

getSentenceInstance

, and

getCharacterInstance

to create

BreakIterator

s that perform
word, line, sentence, and character boundary analysis respectively.
A single

BreakIterator

can work only on one unit
(word, line, sentence, and so on). You must use a different iterator
for each unit boundary analysis you wish to perform.

Line boundary analysis determines where a text string can be
broken when line-wrapping. The mechanism correctly handles
punctuation and hyphenated words. Actual line breaking needs
to also consider the available line width and is handled by
higher-level software.

Sentence boundary analysis allows selection with correct interpretation
of periods within numbers and abbreviations, and trailing punctuation
marks such as quotation marks and parentheses.

Word boundary analysis is used by search and replace functions, as
well as within text editing applications that allow the user to
select words with a double click. Word selection provides correct
interpretation of punctuation marks within and following
words. Characters that are not part of a word, such as symbols
or punctuation marks, have word-breaks on both sides.

Character boundary analysis allows users to interact with characters
as they expect to, for example, when moving the cursor through a text
string. Character boundary analysis provides correct navigation
through character strings, regardless of how the character is stored.
The boundaries returned may be those of supplementary characters,
combining character sequences, or ligature clusters.
For example, an accented character might be stored as a base character
and a diacritical mark. What users consider to be a character can
differ between languages.

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

You use the factory methods provided by this class to create
instances of various types of break iterators. In particular,
use

getWordInstance

,

getLineInstance

,

getSentenceInstance

, and

getCharacterInstance

to create

BreakIterator

s that perform
word, line, sentence, and character boundary analysis respectively.
A single

BreakIterator

can work only on one unit
(word, line, sentence, and so on). You must use a different iterator
for each unit boundary analysis you wish to perform.

Line boundary analysis determines where a text string can be
broken when line-wrapping. The mechanism correctly handles
punctuation and hyphenated words. Actual line breaking needs
to also consider the available line width and is handled by
higher-level software.

Sentence boundary analysis allows selection with correct interpretation
of periods within numbers and abbreviations, and trailing punctuation
marks such as quotation marks and parentheses.

Word boundary analysis is used by search and replace functions, as
well as within text editing applications that allow the user to
select words with a double click. Word selection provides correct
interpretation of punctuation marks within and following
words. Characters that are not part of a word, such as symbols
or punctuation marks, have word-breaks on both sides.

Character boundary analysis allows users to interact with characters
as they expect to, for example, when moving the cursor through a text
string. Character boundary analysis provides correct navigation
through character strings, regardless of how the character is stored.
The boundaries returned may be those of supplementary characters,
combining character sequences, or ligature clusters.
For example, an accented character might be stored as a base character
and a diacritical mark. What users consider to be a character can
differ between languages.

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

Line boundary analysis determines where a text string can be
broken when line-wrapping. The mechanism correctly handles
punctuation and hyphenated words. Actual line breaking needs
to also consider the available line width and is handled by
higher-level software.

Sentence boundary analysis allows selection with correct interpretation
of periods within numbers and abbreviations, and trailing punctuation
marks such as quotation marks and parentheses.

Word boundary analysis is used by search and replace functions, as
well as within text editing applications that allow the user to
select words with a double click. Word selection provides correct
interpretation of punctuation marks within and following
words. Characters that are not part of a word, such as symbols
or punctuation marks, have word-breaks on both sides.

Character boundary analysis allows users to interact with characters
as they expect to, for example, when moving the cursor through a text
string. Character boundary analysis provides correct navigation
through character strings, regardless of how the character is stored.
The boundaries returned may be those of supplementary characters,
combining character sequences, or ligature clusters.
For example, an accented character might be stored as a base character
and a diacritical mark. What users consider to be a character can
differ between languages.

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

Sentence boundary analysis allows selection with correct interpretation
of periods within numbers and abbreviations, and trailing punctuation
marks such as quotation marks and parentheses.

Word boundary analysis is used by search and replace functions, as
well as within text editing applications that allow the user to
select words with a double click. Word selection provides correct
interpretation of punctuation marks within and following
words. Characters that are not part of a word, such as symbols
or punctuation marks, have word-breaks on both sides.

Character boundary analysis allows users to interact with characters
as they expect to, for example, when moving the cursor through a text
string. Character boundary analysis provides correct navigation
through character strings, regardless of how the character is stored.
The boundaries returned may be those of supplementary characters,
combining character sequences, or ligature clusters.
For example, an accented character might be stored as a base character
and a diacritical mark. What users consider to be a character can
differ between languages.

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

Word boundary analysis is used by search and replace functions, as
well as within text editing applications that allow the user to
select words with a double click. Word selection provides correct
interpretation of punctuation marks within and following
words. Characters that are not part of a word, such as symbols
or punctuation marks, have word-breaks on both sides.

Character boundary analysis allows users to interact with characters
as they expect to, for example, when moving the cursor through a text
string. Character boundary analysis provides correct navigation
through character strings, regardless of how the character is stored.
The boundaries returned may be those of supplementary characters,
combining character sequences, or ligature clusters.
For example, an accented character might be stored as a base character
and a diacritical mark. What users consider to be a character can
differ between languages.

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

Character boundary analysis allows users to interact with characters
as they expect to, for example, when moving the cursor through a text
string. Character boundary analysis provides correct navigation
through character strings, regardless of how the character is stored.
The boundaries returned may be those of supplementary characters,
combining character sequences, or ligature clusters.
For example, an accented character might be stored as a base character
and a diacritical mark. What users consider to be a character can
differ between languages.

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

The

BreakIterator

instances returned by the factory methods
of this class are intended for use with natural languages only, not for
programming language text. It is however possible to define subclasses
that tokenize a programming language.

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

Examples

:

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

Creating and using text boundaries:

```java
public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}
```

Print each element in order:

```java
public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}
```

Print each element in reverse order:

```java
public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}
```

Print first element:

```java
public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}
```

Print last element:

```java
public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Print the element at a specified position:

```java
public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}
```

Find the next word:

```java
public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}
```

(The iterator returned by BreakIterator.getWordInstance() is unique in that
the break positions it returns don't represent both the start and end of the
thing being iterated over. That is, a sentence-break iterator returns breaks
that each represent the end of one sentence and the beginning of the next.
With the word-break iterator, the characters between two boundaries might be a
word, or they might be the punctuation or whitespace between two words. The
above code uses a simple heuristic to determine which boundary is the beginning
of a word: If the characters between this boundary and the next boundary
include at least one letter (this can be an alphabetical letter, a CJK ideograph,
a Hangul syllable, a Kana character, etc.), then the text between this boundary
and the next is a word; otherwise, it's the material between words.)

public static void main(String args[]) {
if (args.length == 1) {
String stringToExamine = args[0];
//print each word in order
BreakIterator boundary = BreakIterator.getWordInstance();
boundary.setText(stringToExamine);
printEachForward(boundary, stringToExamine);
//print each sentence in reverse order
boundary = BreakIterator.getSentenceInstance(Locale.US);
boundary.setText(stringToExamine);
printEachBackward(boundary, stringToExamine);
printFirst(boundary, stringToExamine);
printLast(boundary, stringToExamine);
}
}

public static void printEachForward(BreakIterator boundary, String source) {
int start = boundary.first();
for (int end = boundary.next();
end != BreakIterator.DONE;
start = end, end = boundary.next()) {
System.out.println(source.substring(start,end));
}
}

public static void printEachBackward(BreakIterator boundary, String source) {
int end = boundary.last();
for (int start = boundary.previous();
start != BreakIterator.DONE;
end = start, start = boundary.previous()) {
System.out.println(source.substring(start,end));
}
}

public static void printFirst(BreakIterator boundary, String source) {
int start = boundary.first();
int end = boundary.next();
System.out.println(source.substring(start,end));
}

public static void printLast(BreakIterator boundary, String source) {
int end = boundary.last();
int start = boundary.previous();
System.out.println(source.substring(start,end));
}

public static void printAt(BreakIterator boundary, int pos, String source) {
int end = boundary.following(pos);
int start = boundary.previous();
System.out.println(source.substring(start,end));
}

public static int nextWordStartAfter(int pos, String text) {
BreakIterator wb = BreakIterator.getWordInstance();
wb.setText(text);
int last = wb.following(pos);
int current = wb.next();
while (current != BreakIterator.DONE) {
for (int p = last; p < current; p++) {
if (Character.isLetter(text.codePointAt(p)))
return last;
}
last = current;
current = wb.next();
}
return BreakIterator.DONE;
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DONE

DONE is returned by previous(), next(), next(int), preceding(int)
and following(int) when either the first or last text boundary has been
reached.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

BreakIterator

()

Constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Create a copy of this iterator

abstract int

current

()

Returns character index of the text boundary that was most
recently returned by next(), next(int), previous(), first(), last(),
following(int) or preceding(int).

abstract int

first

()

Returns the first boundary.

abstract int

following

​(int offset)

Returns the first boundary following the specified character offset.

static

Locale

[]

getAvailableLocales

()

Returns an array of all locales for which the

get*Instance

methods of this class can return
localized instances.

static

BreakIterator

getCharacterInstance

()

Returns a new

BreakIterator

instance
for

character breaks

for the

default locale

.

static

BreakIterator

getCharacterInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

static

BreakIterator

getLineInstance

()

Returns a new

BreakIterator

instance
for

line breaks

for the

default locale

.

static

BreakIterator

getLineInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

static

BreakIterator

getSentenceInstance

()

Returns a new

BreakIterator

instance
for

sentence breaks

for the

default locale

.

static

BreakIterator

getSentenceInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

abstract

CharacterIterator

getText

()

Get the text being scanned

static

BreakIterator

getWordInstance

()

Returns a new

BreakIterator

instance
for

word breaks

for the

default locale

.

static

BreakIterator

getWordInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

boolean

isBoundary

​(int offset)

Returns true if the specified character offset is a text boundary.

abstract int

last

()

Returns the last boundary.

abstract int

next

()

Returns the boundary following the current boundary.

abstract int

next

​(int n)

Returns the nth boundary from the current boundary.

int

preceding

​(int offset)

Returns the last boundary preceding the specified character offset.

abstract int

previous

()

Returns the boundary preceding the current boundary.

void

setText

​(

String

newText)

Set a new text string to be scanned.

abstract void

setText

​(

CharacterIterator

newText)

Set a new text for scanning.

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static int

DONE

DONE is returned by previous(), next(), next(int), preceding(int)
and following(int) when either the first or last text boundary has been
reached.

---

#### Field Summary

DONE is returned by previous(), next(), next(int), preceding(int)
and following(int) when either the first or last text boundary has been
reached.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

BreakIterator

()

Constructor.

---

#### Constructor Summary

Constructor.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Create a copy of this iterator

abstract int

current

()

Returns character index of the text boundary that was most
recently returned by next(), next(int), previous(), first(), last(),
following(int) or preceding(int).

abstract int

first

()

Returns the first boundary.

abstract int

following

​(int offset)

Returns the first boundary following the specified character offset.

static

Locale

[]

getAvailableLocales

()

Returns an array of all locales for which the

get*Instance

methods of this class can return
localized instances.

static

BreakIterator

getCharacterInstance

()

Returns a new

BreakIterator

instance
for

character breaks

for the

default locale

.

static

BreakIterator

getCharacterInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

static

BreakIterator

getLineInstance

()

Returns a new

BreakIterator

instance
for

line breaks

for the

default locale

.

static

BreakIterator

getLineInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

static

BreakIterator

getSentenceInstance

()

Returns a new

BreakIterator

instance
for

sentence breaks

for the

default locale

.

static

BreakIterator

getSentenceInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

abstract

CharacterIterator

getText

()

Get the text being scanned

static

BreakIterator

getWordInstance

()

Returns a new

BreakIterator

instance
for

word breaks

for the

default locale

.

static

BreakIterator

getWordInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

boolean

isBoundary

​(int offset)

Returns true if the specified character offset is a text boundary.

abstract int

last

()

Returns the last boundary.

abstract int

next

()

Returns the boundary following the current boundary.

abstract int

next

​(int n)

Returns the nth boundary from the current boundary.

int

preceding

​(int offset)

Returns the last boundary preceding the specified character offset.

abstract int

previous

()

Returns the boundary preceding the current boundary.

void

setText

​(

String

newText)

Set a new text string to be scanned.

abstract void

setText

​(

CharacterIterator

newText)

Set a new text for scanning.

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Create a copy of this iterator

Returns character index of the text boundary that was most
recently returned by next(), next(int), previous(), first(), last(),
following(int) or preceding(int).

Returns the first boundary.

Returns the first boundary following the specified character offset.

Returns an array of all locales for which the

get*Instance

methods of this class can return
localized instances.

Returns a new

BreakIterator

instance
for

character breaks

for the

default locale

.

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

Returns a new

BreakIterator

instance
for

line breaks

for the

default locale

.

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

Returns a new

BreakIterator

instance
for

sentence breaks

for the

default locale

.

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

Get the text being scanned

Returns a new

BreakIterator

instance
for

word breaks

for the

default locale

.

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

Returns true if the specified character offset is a text boundary.

Returns the last boundary.

Returns the boundary following the current boundary.

Returns the nth boundary from the current boundary.

Returns the last boundary preceding the specified character offset.

Returns the boundary preceding the current boundary.

Set a new text string to be scanned.

Set a new text for scanning.

Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- DONE

```java
public static final int DONE
```

DONE is returned by previous(), next(), next(int), preceding(int)
and following(int) when either the first or last text boundary has been
reached.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BreakIterator

```java
protected BreakIterator()
```

Constructor. BreakIterator is stateless and has no default behavior.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Create a copy of this iterator

**Overrides:** clone

in class

Object
**Returns:** A copy of this
**See Also:** Cloneable

- first

```java
public abstract int first()
```

Returns the first boundary. The iterator's current position is set
to the first text boundary.

**Returns:** The character index of the first text boundary.

- last

```java
public abstract int last()
```

Returns the last boundary. The iterator's current position is set
to the last text boundary.

**Returns:** The character index of the last text boundary.

- next

```java
public abstract int next​(int n)
```

Returns the nth boundary from the current boundary. If either
the first or last text boundary has been reached, it returns

BreakIterator.DONE

and the current position is set to either
the first or last text boundary depending on which one is reached. Otherwise,
the iterator's current position is set to the new boundary.
For example, if the iterator's current position is the mth text boundary
and three more boundaries exist from the current boundary to the last text
boundary, the next(2) call will return m + 2. The new text position is set
to the (m + 2)th text boundary. A next(4) call would return

BreakIterator.DONE

and the last text boundary would become the
new text position.

**Parameters:** n

- which boundary to return. A value of 0
does nothing. Negative values move to previous boundaries
and positive values move to later boundaries.
**Returns:** The character index of the nth boundary from the current position
or

BreakIterator.DONE

if either first or last text boundary
has been reached.

- next

```java
public abstract int next()
```

Returns the boundary following the current boundary. If the current boundary
is the last text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary following the current boundary.

**Returns:** The character index of the next text boundary or

BreakIterator.DONE

if the current boundary is the last text
boundary.
Equivalent to next(1).
**See Also:** next(int)

- previous

```java
public abstract int previous()
```

Returns the boundary preceding the current boundary. If the current boundary
is the first text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary preceding the current boundary.

**Returns:** The character index of the previous text boundary or

BreakIterator.DONE

if the current boundary is the first text
boundary.

- following

```java
public abstract int following​(int offset)
```

Returns the first boundary following the specified character offset. If the
specified offset equals to the last text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always greater than the offset or the value

BreakIterator.DONE

.

**Parameters:** offset

- the character offset to begin scanning.
**Returns:** The first boundary after the specified offset or

BreakIterator.DONE

if the last text boundary is passed in
as the offset.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.

- preceding

```java
public int preceding​(int offset)
```

Returns the last boundary preceding the specified character offset. If the
specified offset equals to the first text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always less than the offset or the value

BreakIterator.DONE

.

**Parameters:** offset

- the character offset to begin scanning.
**Returns:** The last boundary before the specified offset or

BreakIterator.DONE

if the first text boundary is passed in
as the offset.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.
**Since:** 1.2

- isBoundary

```java
public boolean isBoundary​(int offset)
```

Returns true if the specified character offset is a text boundary.

**Parameters:** offset

- the character offset to check.
**Returns:** true

if "offset" is a boundary position,

false

otherwise.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.
**Since:** 1.2

- current

```java
public abstract int current()
```

Returns character index of the text boundary that was most
recently returned by next(), next(int), previous(), first(), last(),
following(int) or preceding(int). If any of these methods returns

BreakIterator.DONE

because either first or last text boundary
has been reached, it returns the first or last text boundary depending on
which one is reached.

**Returns:** The text boundary returned from the above methods, first or last
text boundary.
**See Also:** next()

,

next(int)

,

previous()

,

first()

,

last()

,

following(int)

,

preceding(int)

- getText

```java
public abstract
CharacterIterator
getText()
```

Get the text being scanned

**Returns:** the text being scanned

- setText

```java
public void setText​(
String
newText)
```

Set a new text string to be scanned. The current scan
position is reset to first().

**Parameters:** newText

- new text to scan.

- setText

```java
public abstract void setText​(
CharacterIterator
newText)
```

Set a new text for scanning. The current scan
position is reset to first().

**Parameters:** newText

- new text to scan.

- getWordInstance

```java
public static
BreakIterator
getWordInstance()
```

Returns a new

BreakIterator

instance
for

word breaks

for the

default locale

.

**Returns:** A break iterator for word breaks

- getWordInstance

```java
public static
BreakIterator
getWordInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for word breaks
**Throws:** NullPointerException

- if

locale

is null

- getLineInstance

```java
public static
BreakIterator
getLineInstance()
```

Returns a new

BreakIterator

instance
for

line breaks

for the

default locale

.

**Returns:** A break iterator for line breaks

- getLineInstance

```java
public static
BreakIterator
getLineInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for line breaks
**Throws:** NullPointerException

- if

locale

is null

- getCharacterInstance

```java
public static
BreakIterator
getCharacterInstance()
```

Returns a new

BreakIterator

instance
for

character breaks

for the

default locale

.

**Returns:** A break iterator for character breaks

- getCharacterInstance

```java
public static
BreakIterator
getCharacterInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for character breaks
**Throws:** NullPointerException

- if

locale

is null

- getSentenceInstance

```java
public static
BreakIterator
getSentenceInstance()
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the

default locale

.

**Returns:** A break iterator for sentence breaks

- getSentenceInstance

```java
public static
BreakIterator
getSentenceInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for sentence breaks
**Throws:** NullPointerException

- if

locale

is null

- getAvailableLocales

```java
public static
Locale
[] getAvailableLocales()
```

Returns an array of all locales for which the

get*Instance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

BreakIteratorProvider

implementations.
It must contain at least a

Locale

instance equal to

Locale.US

.

**Returns:** An array of locales for which localized

BreakIterator

instances are available.

Field Detail

- DONE

```java
public static final int DONE
```

DONE is returned by previous(), next(), next(int), preceding(int)
and following(int) when either the first or last text boundary has been
reached.

**See Also:** Constant Field Values

---

#### Field Detail

DONE

```java
public static final int DONE
```

DONE is returned by previous(), next(), next(int), preceding(int)
and following(int) when either the first or last text boundary has been
reached.

**See Also:** Constant Field Values

---

#### DONE

public static final int DONE

DONE is returned by previous(), next(), next(int), preceding(int)
and following(int) when either the first or last text boundary has been
reached.

Constructor Detail

- BreakIterator

```java
protected BreakIterator()
```

Constructor. BreakIterator is stateless and has no default behavior.

---

#### Constructor Detail

BreakIterator

```java
protected BreakIterator()
```

Constructor. BreakIterator is stateless and has no default behavior.

---

#### BreakIterator

protected BreakIterator()

Constructor. BreakIterator is stateless and has no default behavior.

Method Detail

- clone

```java
public
Object
clone()
```

Create a copy of this iterator

**Overrides:** clone

in class

Object
**Returns:** A copy of this
**See Also:** Cloneable

- first

```java
public abstract int first()
```

Returns the first boundary. The iterator's current position is set
to the first text boundary.

**Returns:** The character index of the first text boundary.

- last

```java
public abstract int last()
```

Returns the last boundary. The iterator's current position is set
to the last text boundary.

**Returns:** The character index of the last text boundary.

- next

```java
public abstract int next​(int n)
```

Returns the nth boundary from the current boundary. If either
the first or last text boundary has been reached, it returns

BreakIterator.DONE

and the current position is set to either
the first or last text boundary depending on which one is reached. Otherwise,
the iterator's current position is set to the new boundary.
For example, if the iterator's current position is the mth text boundary
and three more boundaries exist from the current boundary to the last text
boundary, the next(2) call will return m + 2. The new text position is set
to the (m + 2)th text boundary. A next(4) call would return

BreakIterator.DONE

and the last text boundary would become the
new text position.

**Parameters:** n

- which boundary to return. A value of 0
does nothing. Negative values move to previous boundaries
and positive values move to later boundaries.
**Returns:** The character index of the nth boundary from the current position
or

BreakIterator.DONE

if either first or last text boundary
has been reached.

- next

```java
public abstract int next()
```

Returns the boundary following the current boundary. If the current boundary
is the last text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary following the current boundary.

**Returns:** The character index of the next text boundary or

BreakIterator.DONE

if the current boundary is the last text
boundary.
Equivalent to next(1).
**See Also:** next(int)

- previous

```java
public abstract int previous()
```

Returns the boundary preceding the current boundary. If the current boundary
is the first text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary preceding the current boundary.

**Returns:** The character index of the previous text boundary or

BreakIterator.DONE

if the current boundary is the first text
boundary.

- following

```java
public abstract int following​(int offset)
```

Returns the first boundary following the specified character offset. If the
specified offset equals to the last text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always greater than the offset or the value

BreakIterator.DONE

.

**Parameters:** offset

- the character offset to begin scanning.
**Returns:** The first boundary after the specified offset or

BreakIterator.DONE

if the last text boundary is passed in
as the offset.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.

- preceding

```java
public int preceding​(int offset)
```

Returns the last boundary preceding the specified character offset. If the
specified offset equals to the first text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always less than the offset or the value

BreakIterator.DONE

.

**Parameters:** offset

- the character offset to begin scanning.
**Returns:** The last boundary before the specified offset or

BreakIterator.DONE

if the first text boundary is passed in
as the offset.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.
**Since:** 1.2

- isBoundary

```java
public boolean isBoundary​(int offset)
```

Returns true if the specified character offset is a text boundary.

**Parameters:** offset

- the character offset to check.
**Returns:** true

if "offset" is a boundary position,

false

otherwise.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.
**Since:** 1.2

- current

```java
public abstract int current()
```

Returns character index of the text boundary that was most
recently returned by next(), next(int), previous(), first(), last(),
following(int) or preceding(int). If any of these methods returns

BreakIterator.DONE

because either first or last text boundary
has been reached, it returns the first or last text boundary depending on
which one is reached.

**Returns:** The text boundary returned from the above methods, first or last
text boundary.
**See Also:** next()

,

next(int)

,

previous()

,

first()

,

last()

,

following(int)

,

preceding(int)

- getText

```java
public abstract
CharacterIterator
getText()
```

Get the text being scanned

**Returns:** the text being scanned

- setText

```java
public void setText​(
String
newText)
```

Set a new text string to be scanned. The current scan
position is reset to first().

**Parameters:** newText

- new text to scan.

- setText

```java
public abstract void setText​(
CharacterIterator
newText)
```

Set a new text for scanning. The current scan
position is reset to first().

**Parameters:** newText

- new text to scan.

- getWordInstance

```java
public static
BreakIterator
getWordInstance()
```

Returns a new

BreakIterator

instance
for

word breaks

for the

default locale

.

**Returns:** A break iterator for word breaks

- getWordInstance

```java
public static
BreakIterator
getWordInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for word breaks
**Throws:** NullPointerException

- if

locale

is null

- getLineInstance

```java
public static
BreakIterator
getLineInstance()
```

Returns a new

BreakIterator

instance
for

line breaks

for the

default locale

.

**Returns:** A break iterator for line breaks

- getLineInstance

```java
public static
BreakIterator
getLineInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for line breaks
**Throws:** NullPointerException

- if

locale

is null

- getCharacterInstance

```java
public static
BreakIterator
getCharacterInstance()
```

Returns a new

BreakIterator

instance
for

character breaks

for the

default locale

.

**Returns:** A break iterator for character breaks

- getCharacterInstance

```java
public static
BreakIterator
getCharacterInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for character breaks
**Throws:** NullPointerException

- if

locale

is null

- getSentenceInstance

```java
public static
BreakIterator
getSentenceInstance()
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the

default locale

.

**Returns:** A break iterator for sentence breaks

- getSentenceInstance

```java
public static
BreakIterator
getSentenceInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for sentence breaks
**Throws:** NullPointerException

- if

locale

is null

- getAvailableLocales

```java
public static
Locale
[] getAvailableLocales()
```

Returns an array of all locales for which the

get*Instance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

BreakIteratorProvider

implementations.
It must contain at least a

Locale

instance equal to

Locale.US

.

**Returns:** An array of locales for which localized

BreakIterator

instances are available.

---

#### Method Detail

clone

```java
public
Object
clone()
```

Create a copy of this iterator

**Overrides:** clone

in class

Object
**Returns:** A copy of this
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Create a copy of this iterator

first

```java
public abstract int first()
```

Returns the first boundary. The iterator's current position is set
to the first text boundary.

**Returns:** The character index of the first text boundary.

---

#### first

public abstract int first()

Returns the first boundary. The iterator's current position is set
to the first text boundary.

last

```java
public abstract int last()
```

Returns the last boundary. The iterator's current position is set
to the last text boundary.

**Returns:** The character index of the last text boundary.

---

#### last

public abstract int last()

Returns the last boundary. The iterator's current position is set
to the last text boundary.

next

```java
public abstract int next​(int n)
```

Returns the nth boundary from the current boundary. If either
the first or last text boundary has been reached, it returns

BreakIterator.DONE

and the current position is set to either
the first or last text boundary depending on which one is reached. Otherwise,
the iterator's current position is set to the new boundary.
For example, if the iterator's current position is the mth text boundary
and three more boundaries exist from the current boundary to the last text
boundary, the next(2) call will return m + 2. The new text position is set
to the (m + 2)th text boundary. A next(4) call would return

BreakIterator.DONE

and the last text boundary would become the
new text position.

**Parameters:** n

- which boundary to return. A value of 0
does nothing. Negative values move to previous boundaries
and positive values move to later boundaries.
**Returns:** The character index of the nth boundary from the current position
or

BreakIterator.DONE

if either first or last text boundary
has been reached.

---

#### next

public abstract int next​(int n)

Returns the nth boundary from the current boundary. If either
the first or last text boundary has been reached, it returns

BreakIterator.DONE

and the current position is set to either
the first or last text boundary depending on which one is reached. Otherwise,
the iterator's current position is set to the new boundary.
For example, if the iterator's current position is the mth text boundary
and three more boundaries exist from the current boundary to the last text
boundary, the next(2) call will return m + 2. The new text position is set
to the (m + 2)th text boundary. A next(4) call would return

BreakIterator.DONE

and the last text boundary would become the
new text position.

next

```java
public abstract int next()
```

Returns the boundary following the current boundary. If the current boundary
is the last text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary following the current boundary.

**Returns:** The character index of the next text boundary or

BreakIterator.DONE

if the current boundary is the last text
boundary.
Equivalent to next(1).
**See Also:** next(int)

---

#### next

public abstract int next()

Returns the boundary following the current boundary. If the current boundary
is the last text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary following the current boundary.

previous

```java
public abstract int previous()
```

Returns the boundary preceding the current boundary. If the current boundary
is the first text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary preceding the current boundary.

**Returns:** The character index of the previous text boundary or

BreakIterator.DONE

if the current boundary is the first text
boundary.

---

#### previous

public abstract int previous()

Returns the boundary preceding the current boundary. If the current boundary
is the first text boundary, it returns

BreakIterator.DONE

and
the iterator's current position is unchanged. Otherwise, the iterator's
current position is set to the boundary preceding the current boundary.

following

```java
public abstract int following​(int offset)
```

Returns the first boundary following the specified character offset. If the
specified offset equals to the last text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always greater than the offset or the value

BreakIterator.DONE

.

**Parameters:** offset

- the character offset to begin scanning.
**Returns:** The first boundary after the specified offset or

BreakIterator.DONE

if the last text boundary is passed in
as the offset.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.

---

#### following

public abstract int following​(int offset)

Returns the first boundary following the specified character offset. If the
specified offset equals to the last text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always greater than the offset or the value

BreakIterator.DONE

.

preceding

```java
public int preceding​(int offset)
```

Returns the last boundary preceding the specified character offset. If the
specified offset equals to the first text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always less than the offset or the value

BreakIterator.DONE

.

**Parameters:** offset

- the character offset to begin scanning.
**Returns:** The last boundary before the specified offset or

BreakIterator.DONE

if the first text boundary is passed in
as the offset.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.
**Since:** 1.2

---

#### preceding

public int preceding​(int offset)

Returns the last boundary preceding the specified character offset. If the
specified offset equals to the first text boundary, it returns

BreakIterator.DONE

and the iterator's current position is unchanged.
Otherwise, the iterator's current position is set to the returned boundary.
The value returned is always less than the offset or the value

BreakIterator.DONE

.

isBoundary

```java
public boolean isBoundary​(int offset)
```

Returns true if the specified character offset is a text boundary.

**Parameters:** offset

- the character offset to check.
**Returns:** true

if "offset" is a boundary position,

false

otherwise.
**Throws:** IllegalArgumentException

- if the specified offset is less than
the first text boundary or greater than the last text boundary.
**Since:** 1.2

---

#### isBoundary

public boolean isBoundary​(int offset)

Returns true if the specified character offset is a text boundary.

current

```java
public abstract int current()
```

Returns character index of the text boundary that was most
recently returned by next(), next(int), previous(), first(), last(),
following(int) or preceding(int). If any of these methods returns

BreakIterator.DONE

because either first or last text boundary
has been reached, it returns the first or last text boundary depending on
which one is reached.

**Returns:** The text boundary returned from the above methods, first or last
text boundary.
**See Also:** next()

,

next(int)

,

previous()

,

first()

,

last()

,

following(int)

,

preceding(int)

---

#### current

public abstract int current()

Returns character index of the text boundary that was most
recently returned by next(), next(int), previous(), first(), last(),
following(int) or preceding(int). If any of these methods returns

BreakIterator.DONE

because either first or last text boundary
has been reached, it returns the first or last text boundary depending on
which one is reached.

getText

```java
public abstract
CharacterIterator
getText()
```

Get the text being scanned

**Returns:** the text being scanned

---

#### getText

public abstract

CharacterIterator

getText()

Get the text being scanned

setText

```java
public void setText​(
String
newText)
```

Set a new text string to be scanned. The current scan
position is reset to first().

**Parameters:** newText

- new text to scan.

---

#### setText

public void setText​(

String

newText)

Set a new text string to be scanned. The current scan
position is reset to first().

setText

```java
public abstract void setText​(
CharacterIterator
newText)
```

Set a new text for scanning. The current scan
position is reset to first().

**Parameters:** newText

- new text to scan.

---

#### setText

public abstract void setText​(

CharacterIterator

newText)

Set a new text for scanning. The current scan
position is reset to first().

getWordInstance

```java
public static
BreakIterator
getWordInstance()
```

Returns a new

BreakIterator

instance
for

word breaks

for the

default locale

.

**Returns:** A break iterator for word breaks

---

#### getWordInstance

public static

BreakIterator

getWordInstance()

Returns a new

BreakIterator

instance
for

word breaks

for the

default locale

.

getWordInstance

```java
public static
BreakIterator
getWordInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for word breaks
**Throws:** NullPointerException

- if

locale

is null

---

#### getWordInstance

public static

BreakIterator

getWordInstance​(

Locale

locale)

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

getLineInstance

```java
public static
BreakIterator
getLineInstance()
```

Returns a new

BreakIterator

instance
for

line breaks

for the

default locale

.

**Returns:** A break iterator for line breaks

---

#### getLineInstance

public static

BreakIterator

getLineInstance()

Returns a new

BreakIterator

instance
for

line breaks

for the

default locale

.

getLineInstance

```java
public static
BreakIterator
getLineInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for line breaks
**Throws:** NullPointerException

- if

locale

is null

---

#### getLineInstance

public static

BreakIterator

getLineInstance​(

Locale

locale)

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

getCharacterInstance

```java
public static
BreakIterator
getCharacterInstance()
```

Returns a new

BreakIterator

instance
for

character breaks

for the

default locale

.

**Returns:** A break iterator for character breaks

---

#### getCharacterInstance

public static

BreakIterator

getCharacterInstance()

Returns a new

BreakIterator

instance
for

character breaks

for the

default locale

.

getCharacterInstance

```java
public static
BreakIterator
getCharacterInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for character breaks
**Throws:** NullPointerException

- if

locale

is null

---

#### getCharacterInstance

public static

BreakIterator

getCharacterInstance​(

Locale

locale)

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

getSentenceInstance

```java
public static
BreakIterator
getSentenceInstance()
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the

default locale

.

**Returns:** A break iterator for sentence breaks

---

#### getSentenceInstance

public static

BreakIterator

getSentenceInstance()

Returns a new

BreakIterator

instance
for

sentence breaks

for the

default locale

.

getSentenceInstance

```java
public static
BreakIterator
getSentenceInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for sentence breaks
**Throws:** NullPointerException

- if

locale

is null

---

#### getSentenceInstance

public static

BreakIterator

getSentenceInstance​(

Locale

locale)

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

getAvailableLocales

```java
public static
Locale
[] getAvailableLocales()
```

Returns an array of all locales for which the

get*Instance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

BreakIteratorProvider

implementations.
It must contain at least a

Locale

instance equal to

Locale.US

.

**Returns:** An array of locales for which localized

BreakIterator

instances are available.

---

#### getAvailableLocales

public static

Locale

[] getAvailableLocales()

Returns an array of all locales for which the

get*Instance

methods of this class can return
localized instances.
The returned array represents the union of locales supported by the Java
runtime and by installed

BreakIteratorProvider

implementations.
It must contain at least a

Locale

instance equal to

Locale.US

.

---

