# Class AbstractWriter

**Source:** `java.desktop\javax\swing\text\AbstractWriter.html`

### Class Description

```java
public abstract class
AbstractWriter

extends
Object
```

AbstractWriter is an abstract class that actually
does the work of writing out the element tree
including the attributes. In terms of how much is
written out per line, the writer defaults to 100.
But this value can be set by subclasses.

**Direct Known Subclasses:** HTMLWriter

,

MinimalHTMLWriter

---

### Field Details

#### protected static final char NEWLINE

How the text packages models newlines.

**See Also:**
- getLineSeparator()

,

Constant Field Values

---

### Constructor Details

#### protected AbstractWriter​(
Writer
w,

Document
doc)

Creates a new AbstractWriter.
Initializes the ElementIterator with the default
root of the document.

**Parameters:**
- w

- a Writer.
- doc

- a Document

---

#### protected AbstractWriter​(
Writer
w,

Document
doc,
int pos,
int len)

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:**
- w

- a Writer
- doc

- an Element
- pos

- The location in the document to fetch the
content.
- len

- The amount to write out.

---

#### protected AbstractWriter​(
Writer
w,

Element
root)

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:**
- w

- a Writer
- root

- an Element

---

#### protected AbstractWriter​(
Writer
w,

Element
root,
int pos,
int len)

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:**
- w

- a Writer
- root

- an Element
- pos

- The location in the document to fetch the
content.
- len

- The amount to write out.

---

### Method Details

#### public int getStartOffset()

Returns the first offset to be output.

**Returns:**
- the first offset to be output

**Since:**
- 1.3

---

#### public int getEndOffset()

Returns the last offset to be output.

**Returns:**
- the last offset to be output

**Since:**
- 1.3

---

#### protected
ElementIterator
getElementIterator()

Fetches the ElementIterator.

**Returns:**
- the ElementIterator.

---

#### protected
Writer
getWriter()

Returns the Writer that is used to output the content.

**Returns:**
- the Writer that is used to output the content

**Since:**
- 1.3

---

#### protected
Document
getDocument()

Fetches the document.

**Returns:**
- the Document.

---

#### protected boolean inRange​(
Element
next)

This method determines whether the current element
is in the range specified. When no range is specified,
the range is initialized to be the entire document.
inRange() returns true if the range specified intersects
with the element's range.

**Parameters:**
- next

- an Element.

**Returns:**
- boolean that indicates whether the element
is in the range.

---

#### protected abstract void write()
throws
IOException
,

BadLocationException

This abstract method needs to be implemented
by subclasses. Its responsibility is to
iterate over the elements and use the write()
methods to generate output in the desired format.

**Throws:**
- IOException

- if an I/O problem has occurred
- BadLocationException

- for an invalid location within
the document

---

#### protected
String
getText​(
Element
elem)
throws
BadLocationException

Returns the text associated with the element.
The assumption here is that the element is a
leaf element. Throws a BadLocationException
when encountered.

**Parameters:**
- elem

- an

Element

**Returns:**
- the text as a

String

**Throws:**
- BadLocationException

- if pos represents an invalid
location within the document

---

#### protected void text​(
Element
elem)
throws
BadLocationException
,

IOException

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

**Parameters:**
- elem

- an Element.

**Throws:**
- IOException

- on any I/O error
- BadLocationException

- if pos represents an invalid
location within the document.

---

#### protected void setLineLength​(int l)

Enables subclasses to set the number of characters they
want written per line. The default is 100.

**Parameters:**
- l

- the maximum line length.

---

#### protected int getLineLength()

Returns the maximum line length.

**Returns:**
- the maximum line length

**Since:**
- 1.3

---

#### protected void setCurrentLineLength​(int length)

Sets the current line length.

**Parameters:**
- length

- the new line length

**Since:**
- 1.3

---

#### protected int getCurrentLineLength()

Returns the current line length.

**Returns:**
- the current line length

**Since:**
- 1.3

---

#### protected boolean isLineEmpty()

Returns true if the current line should be considered empty. This
is true when

getCurrentLineLength

== 0 ||

indent

has been invoked on an empty line.

**Returns:**
- true if the current line should be considered empty

**Since:**
- 1.3

---

#### protected void setCanWrapLines​(boolean newValue)

Sets whether or not lines can be wrapped. This can be toggled
during the writing of lines. For example, outputting HTML might
set this to false when outputting a quoted string.

**Parameters:**
- newValue

- new value for line wrapping

**Since:**
- 1.3

---

#### protected boolean getCanWrapLines()

Returns whether or not the lines can be wrapped. If this is false
no lineSeparator's will be output.

**Returns:**
- whether or not the lines can be wrapped

**Since:**
- 1.3

---

#### protected void setIndentSpace​(int space)

Enables subclasses to specify how many spaces an indent
maps to. When indentation takes place, the indent level
is multiplied by this mapping. The default is 2.

**Parameters:**
- space

- an int representing the space to indent mapping.

---

#### protected int getIndentSpace()

Returns the amount of space to indent.

**Returns:**
- the amount of space to indent

**Since:**
- 1.3

---

#### public void setLineSeparator​(
String
value)

Sets the String used to represent newlines. This is initialized
in the constructor from either the Document, or the System property
line.separator.

**Parameters:**
- value

- the new line separator

**Since:**
- 1.3

---

#### public
String
getLineSeparator()

Returns the string used to represent newlines.

**Returns:**
- the string used to represent newlines

**Since:**
- 1.3

---

#### protected void incrIndent()

Increments the indent level. If indenting would cause

getIndentSpace()

*

getIndentLevel()

to be >
than

getLineLength()

this will not cause an indent.

---

#### protected void decrIndent()

Decrements the indent level.

---

#### protected int getIndentLevel()

Returns the current indentation level. That is, the number of times

incrIndent

has been invoked minus the number of times

decrIndent

has been invoked.

**Returns:**
- the current indentation level

**Since:**
- 1.3

---

#### protected void indent()
throws
IOException

Does indentation. The number of spaces written
out is indent level times the space to map mapping. If the current
line is empty, this will not make it so that the current line is
still considered empty.

**Throws:**
- IOException

- on any I/O error

---

#### protected void write​(char ch)
throws
IOException

Writes out a character. This is implemented to invoke
the

write

method that takes a char[].

**Parameters:**
- ch

- a char.

**Throws:**
- IOException

- on any I/O error

---

#### protected void write​(
String
content)
throws
IOException

Writes out a string. This is implemented to invoke the

write

method that takes a char[].

**Parameters:**
- content

- a String.

**Throws:**
- IOException

- on any I/O error

---

#### protected void writeLineSeparator()
throws
IOException

Writes the line separator. This invokes

output

directly
as well as setting the

lineLength

to 0.

**Throws:**
- IOException

- on any I/O error

**Since:**
- 1.3

---

#### protected void write​(char[] chars,
int startIndex,
int length)
throws
IOException

All write methods call into this one. If

getCanWrapLines()

returns false, this will call

output

with each sequence
of

chars

that doesn't contain a NEWLINE, followed
by a call to

writeLineSeparator

. On the other hand,
if

getCanWrapLines()

returns true, this will split the
string, as necessary, so

getLineLength

is honored.
The only exception is if the current string contains no whitespace,
and won't fit in which case the line length will exceed

getLineLength

.

**Parameters:**
- chars

- characters to output
- startIndex

- starting index
- length

- length of output

**Throws:**
- IOException

- on any I/O error

**Since:**
- 1.3

---

#### protected void writeAttributes​(
AttributeSet
attr)
throws
IOException

Writes out the set of attributes as " <name>=<value>"
pairs. It throws an IOException when encountered.

**Parameters:**
- attr

- an AttributeSet.

**Throws:**
- IOException

- on any I/O error

---

#### protected void output​(char[] content,
int start,
int length)
throws
IOException

The last stop in writing out content. All the write methods eventually
make it to this method, which invokes

write

on the
Writer.

This method also updates the line length based on

length

. If this is invoked to output a newline, the
current line length will need to be reset as will no longer be
valid. If it is up to the caller to do this. Use

writeLineSeparator

to write out a newline, which will
property update the current line length.

**Parameters:**
- content

- characters to output
- start

- starting index
- length

- length of output

**Throws:**
- IOException

- on any I/O error

**Since:**
- 1.3

---

### Additional Sections

#### Class AbstractWriter

java.lang.Object

- javax.swing.text.AbstractWriter

javax.swing.text.AbstractWriter

**Direct Known Subclasses:** HTMLWriter

,

MinimalHTMLWriter

```java
public abstract class
AbstractWriter

extends
Object
```

AbstractWriter is an abstract class that actually
does the work of writing out the element tree
including the attributes. In terms of how much is
written out per line, the writer defaults to 100.
But this value can be set by subclasses.

public abstract class

AbstractWriter

extends

Object

AbstractWriter is an abstract class that actually
does the work of writing out the element tree
including the attributes. In terms of how much is
written out per line, the writer defaults to 100.
But this value can be set by subclasses.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static char

NEWLINE

How the text packages models newlines.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractWriter

​(

Writer

w,

Document

doc)

Creates a new AbstractWriter.

protected

AbstractWriter

​(

Writer

w,

Document

doc,
int pos,
int len)

Creates a new AbstractWriter.

protected

AbstractWriter

​(

Writer

w,

Element

root)

Creates a new AbstractWriter.

protected

AbstractWriter

​(

Writer

w,

Element

root,
int pos,
int len)

Creates a new AbstractWriter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

decrIndent

()

Decrements the indent level.

protected boolean

getCanWrapLines

()

Returns whether or not the lines can be wrapped.

protected int

getCurrentLineLength

()

Returns the current line length.

protected

Document

getDocument

()

Fetches the document.

protected

ElementIterator

getElementIterator

()

Fetches the ElementIterator.

int

getEndOffset

()

Returns the last offset to be output.

protected int

getIndentLevel

()

Returns the current indentation level.

protected int

getIndentSpace

()

Returns the amount of space to indent.

protected int

getLineLength

()

Returns the maximum line length.

String

getLineSeparator

()

Returns the string used to represent newlines.

int

getStartOffset

()

Returns the first offset to be output.

protected

String

getText

​(

Element

elem)

Returns the text associated with the element.

protected

Writer

getWriter

()

Returns the Writer that is used to output the content.

protected void

incrIndent

()

Increments the indent level.

protected void

indent

()

Does indentation.

protected boolean

inRange

​(

Element

next)

This method determines whether the current element
is in the range specified.

protected boolean

isLineEmpty

()

Returns true if the current line should be considered empty.

protected void

output

​(char[] content,
int start,
int length)

The last stop in writing out content.

protected void

setCanWrapLines

​(boolean newValue)

Sets whether or not lines can be wrapped.

protected void

setCurrentLineLength

​(int length)

Sets the current line length.

protected void

setIndentSpace

​(int space)

Enables subclasses to specify how many spaces an indent
maps to.

protected void

setLineLength

​(int l)

Enables subclasses to set the number of characters they
want written per line.

void

setLineSeparator

​(

String

value)

Sets the String used to represent newlines.

protected void

text

​(

Element

elem)

Writes out text.

protected abstract void

write

()

This abstract method needs to be implemented
by subclasses.

protected void

write

​(char ch)

Writes out a character.

protected void

write

​(char[] chars,
int startIndex,
int length)

All write methods call into this one.

protected void

write

​(

String

content)

Writes out a string.

protected void

writeAttributes

​(

AttributeSet

attr)

Writes out the set of attributes as " <name>=<value>"
pairs.

protected void

writeLineSeparator

()

Writes the line separator.

- Methods declared in class java.lang.

Object

clone

,

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

protected static char

NEWLINE

How the text packages models newlines.

---

#### Field Summary

How the text packages models newlines.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractWriter

​(

Writer

w,

Document

doc)

Creates a new AbstractWriter.

protected

AbstractWriter

​(

Writer

w,

Document

doc,
int pos,
int len)

Creates a new AbstractWriter.

protected

AbstractWriter

​(

Writer

w,

Element

root)

Creates a new AbstractWriter.

protected

AbstractWriter

​(

Writer

w,

Element

root,
int pos,
int len)

Creates a new AbstractWriter.

---

#### Constructor Summary

Creates a new AbstractWriter.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

decrIndent

()

Decrements the indent level.

protected boolean

getCanWrapLines

()

Returns whether or not the lines can be wrapped.

protected int

getCurrentLineLength

()

Returns the current line length.

protected

Document

getDocument

()

Fetches the document.

protected

ElementIterator

getElementIterator

()

Fetches the ElementIterator.

int

getEndOffset

()

Returns the last offset to be output.

protected int

getIndentLevel

()

Returns the current indentation level.

protected int

getIndentSpace

()

Returns the amount of space to indent.

protected int

getLineLength

()

Returns the maximum line length.

String

getLineSeparator

()

Returns the string used to represent newlines.

int

getStartOffset

()

Returns the first offset to be output.

protected

String

getText

​(

Element

elem)

Returns the text associated with the element.

protected

Writer

getWriter

()

Returns the Writer that is used to output the content.

protected void

incrIndent

()

Increments the indent level.

protected void

indent

()

Does indentation.

protected boolean

inRange

​(

Element

next)

This method determines whether the current element
is in the range specified.

protected boolean

isLineEmpty

()

Returns true if the current line should be considered empty.

protected void

output

​(char[] content,
int start,
int length)

The last stop in writing out content.

protected void

setCanWrapLines

​(boolean newValue)

Sets whether or not lines can be wrapped.

protected void

setCurrentLineLength

​(int length)

Sets the current line length.

protected void

setIndentSpace

​(int space)

Enables subclasses to specify how many spaces an indent
maps to.

protected void

setLineLength

​(int l)

Enables subclasses to set the number of characters they
want written per line.

void

setLineSeparator

​(

String

value)

Sets the String used to represent newlines.

protected void

text

​(

Element

elem)

Writes out text.

protected abstract void

write

()

This abstract method needs to be implemented
by subclasses.

protected void

write

​(char ch)

Writes out a character.

protected void

write

​(char[] chars,
int startIndex,
int length)

All write methods call into this one.

protected void

write

​(

String

content)

Writes out a string.

protected void

writeAttributes

​(

AttributeSet

attr)

Writes out the set of attributes as " <name>=<value>"
pairs.

protected void

writeLineSeparator

()

Writes the line separator.

- Methods declared in class java.lang.

Object

clone

,

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

Decrements the indent level.

Returns whether or not the lines can be wrapped.

Returns the current line length.

Fetches the document.

Fetches the ElementIterator.

Returns the last offset to be output.

Returns the current indentation level.

Returns the amount of space to indent.

Returns the maximum line length.

Returns the string used to represent newlines.

Returns the first offset to be output.

Returns the text associated with the element.

Returns the Writer that is used to output the content.

Increments the indent level.

Does indentation.

This method determines whether the current element
is in the range specified.

Returns true if the current line should be considered empty.

The last stop in writing out content.

Sets whether or not lines can be wrapped.

Sets the current line length.

Enables subclasses to specify how many spaces an indent
maps to.

Enables subclasses to set the number of characters they
want written per line.

Sets the String used to represent newlines.

Writes out text.

This abstract method needs to be implemented
by subclasses.

Writes out a character.

All write methods call into this one.

Writes out a string.

Writes out the set of attributes as " <name>=<value>"
pairs.

Writes the line separator.

Methods declared in class java.lang.

Object

clone

,

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

- NEWLINE

```java
protected static final char NEWLINE
```

How the text packages models newlines.

**See Also:** getLineSeparator()

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Document
doc)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the default
root of the document.

**Parameters:** w

- a Writer.
**Parameters:** doc

- a Document

- AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Document
doc,
int pos,
int len)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** doc

- an Element
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

- AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Element
root)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** root

- an Element

- AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Element
root,
int pos,
int len)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** root

- an Element
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

============ METHOD DETAIL ==========

- Method Detail

- getStartOffset

```java
public int getStartOffset()
```

Returns the first offset to be output.

**Returns:** the first offset to be output
**Since:** 1.3

- getEndOffset

```java
public int getEndOffset()
```

Returns the last offset to be output.

**Returns:** the last offset to be output
**Since:** 1.3

- getElementIterator

```java
protected
ElementIterator
getElementIterator()
```

Fetches the ElementIterator.

**Returns:** the ElementIterator.

- getWriter

```java
protected
Writer
getWriter()
```

Returns the Writer that is used to output the content.

**Returns:** the Writer that is used to output the content
**Since:** 1.3

- getDocument

```java
protected
Document
getDocument()
```

Fetches the document.

**Returns:** the Document.

- inRange

```java
protected boolean inRange​(
Element
next)
```

This method determines whether the current element
is in the range specified. When no range is specified,
the range is initialized to be the entire document.
inRange() returns true if the range specified intersects
with the element's range.

**Parameters:** next

- an Element.
**Returns:** boolean that indicates whether the element
is in the range.

- write

```java
protected abstract void write()
throws
IOException
,

BadLocationException
```

This abstract method needs to be implemented
by subclasses. Its responsibility is to
iterate over the elements and use the write()
methods to generate output in the desired format.

**Throws:** IOException

- if an I/O problem has occurred
**Throws:** BadLocationException

- for an invalid location within
the document

- getText

```java
protected
String
getText​(
Element
elem)
throws
BadLocationException
```

Returns the text associated with the element.
The assumption here is that the element is a
leaf element. Throws a BadLocationException
when encountered.

**Parameters:** elem

- an

Element
**Returns:** the text as a

String
**Throws:** BadLocationException

- if pos represents an invalid
location within the document

- text

```java
protected void text​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

**Parameters:** elem

- an Element.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- setLineLength

```java
protected void setLineLength​(int l)
```

Enables subclasses to set the number of characters they
want written per line. The default is 100.

**Parameters:** l

- the maximum line length.

- getLineLength

```java
protected int getLineLength()
```

Returns the maximum line length.

**Returns:** the maximum line length
**Since:** 1.3

- setCurrentLineLength

```java
protected void setCurrentLineLength​(int length)
```

Sets the current line length.

**Parameters:** length

- the new line length
**Since:** 1.3

- getCurrentLineLength

```java
protected int getCurrentLineLength()
```

Returns the current line length.

**Returns:** the current line length
**Since:** 1.3

- isLineEmpty

```java
protected boolean isLineEmpty()
```

Returns true if the current line should be considered empty. This
is true when

getCurrentLineLength

== 0 ||

indent

has been invoked on an empty line.

**Returns:** true if the current line should be considered empty
**Since:** 1.3

- setCanWrapLines

```java
protected void setCanWrapLines​(boolean newValue)
```

Sets whether or not lines can be wrapped. This can be toggled
during the writing of lines. For example, outputting HTML might
set this to false when outputting a quoted string.

**Parameters:** newValue

- new value for line wrapping
**Since:** 1.3

- getCanWrapLines

```java
protected boolean getCanWrapLines()
```

Returns whether or not the lines can be wrapped. If this is false
no lineSeparator's will be output.

**Returns:** whether or not the lines can be wrapped
**Since:** 1.3

- setIndentSpace

```java
protected void setIndentSpace​(int space)
```

Enables subclasses to specify how many spaces an indent
maps to. When indentation takes place, the indent level
is multiplied by this mapping. The default is 2.

**Parameters:** space

- an int representing the space to indent mapping.

- getIndentSpace

```java
protected int getIndentSpace()
```

Returns the amount of space to indent.

**Returns:** the amount of space to indent
**Since:** 1.3

- setLineSeparator

```java
public void setLineSeparator​(
String
value)
```

Sets the String used to represent newlines. This is initialized
in the constructor from either the Document, or the System property
line.separator.

**Parameters:** value

- the new line separator
**Since:** 1.3

- getLineSeparator

```java
public
String
getLineSeparator()
```

Returns the string used to represent newlines.

**Returns:** the string used to represent newlines
**Since:** 1.3

- incrIndent

```java
protected void incrIndent()
```

Increments the indent level. If indenting would cause

getIndentSpace()

*

getIndentLevel()

to be >
than

getLineLength()

this will not cause an indent.

- decrIndent

```java
protected void decrIndent()
```

Decrements the indent level.

- getIndentLevel

```java
protected int getIndentLevel()
```

Returns the current indentation level. That is, the number of times

incrIndent

has been invoked minus the number of times

decrIndent

has been invoked.

**Returns:** the current indentation level
**Since:** 1.3

- indent

```java
protected void indent()
throws
IOException
```

Does indentation. The number of spaces written
out is indent level times the space to map mapping. If the current
line is empty, this will not make it so that the current line is
still considered empty.

**Throws:** IOException

- on any I/O error

- write

```java
protected void write​(char ch)
throws
IOException
```

Writes out a character. This is implemented to invoke
the

write

method that takes a char[].

**Parameters:** ch

- a char.
**Throws:** IOException

- on any I/O error

- write

```java
protected void write​(
String
content)
throws
IOException
```

Writes out a string. This is implemented to invoke the

write

method that takes a char[].

**Parameters:** content

- a String.
**Throws:** IOException

- on any I/O error

- writeLineSeparator

```java
protected void writeLineSeparator()
throws
IOException
```

Writes the line separator. This invokes

output

directly
as well as setting the

lineLength

to 0.

**Throws:** IOException

- on any I/O error
**Since:** 1.3

- write

```java
protected void write​(char[] chars,
int startIndex,
int length)
throws
IOException
```

All write methods call into this one. If

getCanWrapLines()

returns false, this will call

output

with each sequence
of

chars

that doesn't contain a NEWLINE, followed
by a call to

writeLineSeparator

. On the other hand,
if

getCanWrapLines()

returns true, this will split the
string, as necessary, so

getLineLength

is honored.
The only exception is if the current string contains no whitespace,
and won't fit in which case the line length will exceed

getLineLength

.

**Parameters:** chars

- characters to output
**Parameters:** startIndex

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

- writeAttributes

```java
protected void writeAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the set of attributes as " <name>=<value>"
pairs. It throws an IOException when encountered.

**Parameters:** attr

- an AttributeSet.
**Throws:** IOException

- on any I/O error

- output

```java
protected void output​(char[] content,
int start,
int length)
throws
IOException
```

The last stop in writing out content. All the write methods eventually
make it to this method, which invokes

write

on the
Writer.

This method also updates the line length based on

length

. If this is invoked to output a newline, the
current line length will need to be reset as will no longer be
valid. If it is up to the caller to do this. Use

writeLineSeparator

to write out a newline, which will
property update the current line length.

**Parameters:** content

- characters to output
**Parameters:** start

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

Field Detail

- NEWLINE

```java
protected static final char NEWLINE
```

How the text packages models newlines.

**See Also:** getLineSeparator()

,

Constant Field Values

---

#### Field Detail

NEWLINE

```java
protected static final char NEWLINE
```

How the text packages models newlines.

**See Also:** getLineSeparator()

,

Constant Field Values

---

#### NEWLINE

protected static final char NEWLINE

How the text packages models newlines.

Constructor Detail

- AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Document
doc)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the default
root of the document.

**Parameters:** w

- a Writer.
**Parameters:** doc

- a Document

- AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Document
doc,
int pos,
int len)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** doc

- an Element
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

- AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Element
root)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** root

- an Element

- AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Element
root,
int pos,
int len)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** root

- an Element
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

---

#### Constructor Detail

AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Document
doc)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the default
root of the document.

**Parameters:** w

- a Writer.
**Parameters:** doc

- a Document

---

#### AbstractWriter

protected AbstractWriter​(

Writer

w,

Document

doc)

Creates a new AbstractWriter.
Initializes the ElementIterator with the default
root of the document.

AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Document
doc,
int pos,
int len)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** doc

- an Element
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

---

#### AbstractWriter

protected AbstractWriter​(

Writer

w,

Document

doc,
int pos,
int len)

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Element
root)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** root

- an Element

---

#### AbstractWriter

protected AbstractWriter​(

Writer

w,

Element

root)

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

AbstractWriter

```java
protected AbstractWriter​(
Writer
w,

Element
root,
int pos,
int len)
```

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

**Parameters:** w

- a Writer
**Parameters:** root

- an Element
**Parameters:** pos

- The location in the document to fetch the
content.
**Parameters:** len

- The amount to write out.

---

#### AbstractWriter

protected AbstractWriter​(

Writer

w,

Element

root,
int pos,
int len)

Creates a new AbstractWriter.
Initializes the ElementIterator with the
element passed in.

Method Detail

- getStartOffset

```java
public int getStartOffset()
```

Returns the first offset to be output.

**Returns:** the first offset to be output
**Since:** 1.3

- getEndOffset

```java
public int getEndOffset()
```

Returns the last offset to be output.

**Returns:** the last offset to be output
**Since:** 1.3

- getElementIterator

```java
protected
ElementIterator
getElementIterator()
```

Fetches the ElementIterator.

**Returns:** the ElementIterator.

- getWriter

```java
protected
Writer
getWriter()
```

Returns the Writer that is used to output the content.

**Returns:** the Writer that is used to output the content
**Since:** 1.3

- getDocument

```java
protected
Document
getDocument()
```

Fetches the document.

**Returns:** the Document.

- inRange

```java
protected boolean inRange​(
Element
next)
```

This method determines whether the current element
is in the range specified. When no range is specified,
the range is initialized to be the entire document.
inRange() returns true if the range specified intersects
with the element's range.

**Parameters:** next

- an Element.
**Returns:** boolean that indicates whether the element
is in the range.

- write

```java
protected abstract void write()
throws
IOException
,

BadLocationException
```

This abstract method needs to be implemented
by subclasses. Its responsibility is to
iterate over the elements and use the write()
methods to generate output in the desired format.

**Throws:** IOException

- if an I/O problem has occurred
**Throws:** BadLocationException

- for an invalid location within
the document

- getText

```java
protected
String
getText​(
Element
elem)
throws
BadLocationException
```

Returns the text associated with the element.
The assumption here is that the element is a
leaf element. Throws a BadLocationException
when encountered.

**Parameters:** elem

- an

Element
**Returns:** the text as a

String
**Throws:** BadLocationException

- if pos represents an invalid
location within the document

- text

```java
protected void text​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

**Parameters:** elem

- an Element.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

- setLineLength

```java
protected void setLineLength​(int l)
```

Enables subclasses to set the number of characters they
want written per line. The default is 100.

**Parameters:** l

- the maximum line length.

- getLineLength

```java
protected int getLineLength()
```

Returns the maximum line length.

**Returns:** the maximum line length
**Since:** 1.3

- setCurrentLineLength

```java
protected void setCurrentLineLength​(int length)
```

Sets the current line length.

**Parameters:** length

- the new line length
**Since:** 1.3

- getCurrentLineLength

```java
protected int getCurrentLineLength()
```

Returns the current line length.

**Returns:** the current line length
**Since:** 1.3

- isLineEmpty

```java
protected boolean isLineEmpty()
```

Returns true if the current line should be considered empty. This
is true when

getCurrentLineLength

== 0 ||

indent

has been invoked on an empty line.

**Returns:** true if the current line should be considered empty
**Since:** 1.3

- setCanWrapLines

```java
protected void setCanWrapLines​(boolean newValue)
```

Sets whether or not lines can be wrapped. This can be toggled
during the writing of lines. For example, outputting HTML might
set this to false when outputting a quoted string.

**Parameters:** newValue

- new value for line wrapping
**Since:** 1.3

- getCanWrapLines

```java
protected boolean getCanWrapLines()
```

Returns whether or not the lines can be wrapped. If this is false
no lineSeparator's will be output.

**Returns:** whether or not the lines can be wrapped
**Since:** 1.3

- setIndentSpace

```java
protected void setIndentSpace​(int space)
```

Enables subclasses to specify how many spaces an indent
maps to. When indentation takes place, the indent level
is multiplied by this mapping. The default is 2.

**Parameters:** space

- an int representing the space to indent mapping.

- getIndentSpace

```java
protected int getIndentSpace()
```

Returns the amount of space to indent.

**Returns:** the amount of space to indent
**Since:** 1.3

- setLineSeparator

```java
public void setLineSeparator​(
String
value)
```

Sets the String used to represent newlines. This is initialized
in the constructor from either the Document, or the System property
line.separator.

**Parameters:** value

- the new line separator
**Since:** 1.3

- getLineSeparator

```java
public
String
getLineSeparator()
```

Returns the string used to represent newlines.

**Returns:** the string used to represent newlines
**Since:** 1.3

- incrIndent

```java
protected void incrIndent()
```

Increments the indent level. If indenting would cause

getIndentSpace()

*

getIndentLevel()

to be >
than

getLineLength()

this will not cause an indent.

- decrIndent

```java
protected void decrIndent()
```

Decrements the indent level.

- getIndentLevel

```java
protected int getIndentLevel()
```

Returns the current indentation level. That is, the number of times

incrIndent

has been invoked minus the number of times

decrIndent

has been invoked.

**Returns:** the current indentation level
**Since:** 1.3

- indent

```java
protected void indent()
throws
IOException
```

Does indentation. The number of spaces written
out is indent level times the space to map mapping. If the current
line is empty, this will not make it so that the current line is
still considered empty.

**Throws:** IOException

- on any I/O error

- write

```java
protected void write​(char ch)
throws
IOException
```

Writes out a character. This is implemented to invoke
the

write

method that takes a char[].

**Parameters:** ch

- a char.
**Throws:** IOException

- on any I/O error

- write

```java
protected void write​(
String
content)
throws
IOException
```

Writes out a string. This is implemented to invoke the

write

method that takes a char[].

**Parameters:** content

- a String.
**Throws:** IOException

- on any I/O error

- writeLineSeparator

```java
protected void writeLineSeparator()
throws
IOException
```

Writes the line separator. This invokes

output

directly
as well as setting the

lineLength

to 0.

**Throws:** IOException

- on any I/O error
**Since:** 1.3

- write

```java
protected void write​(char[] chars,
int startIndex,
int length)
throws
IOException
```

All write methods call into this one. If

getCanWrapLines()

returns false, this will call

output

with each sequence
of

chars

that doesn't contain a NEWLINE, followed
by a call to

writeLineSeparator

. On the other hand,
if

getCanWrapLines()

returns true, this will split the
string, as necessary, so

getLineLength

is honored.
The only exception is if the current string contains no whitespace,
and won't fit in which case the line length will exceed

getLineLength

.

**Parameters:** chars

- characters to output
**Parameters:** startIndex

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

- writeAttributes

```java
protected void writeAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the set of attributes as " <name>=<value>"
pairs. It throws an IOException when encountered.

**Parameters:** attr

- an AttributeSet.
**Throws:** IOException

- on any I/O error

- output

```java
protected void output​(char[] content,
int start,
int length)
throws
IOException
```

The last stop in writing out content. All the write methods eventually
make it to this method, which invokes

write

on the
Writer.

This method also updates the line length based on

length

. If this is invoked to output a newline, the
current line length will need to be reset as will no longer be
valid. If it is up to the caller to do this. Use

writeLineSeparator

to write out a newline, which will
property update the current line length.

**Parameters:** content

- characters to output
**Parameters:** start

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

---

#### Method Detail

getStartOffset

```java
public int getStartOffset()
```

Returns the first offset to be output.

**Returns:** the first offset to be output
**Since:** 1.3

---

#### getStartOffset

public int getStartOffset()

Returns the first offset to be output.

getEndOffset

```java
public int getEndOffset()
```

Returns the last offset to be output.

**Returns:** the last offset to be output
**Since:** 1.3

---

#### getEndOffset

public int getEndOffset()

Returns the last offset to be output.

getElementIterator

```java
protected
ElementIterator
getElementIterator()
```

Fetches the ElementIterator.

**Returns:** the ElementIterator.

---

#### getElementIterator

protected

ElementIterator

getElementIterator()

Fetches the ElementIterator.

getWriter

```java
protected
Writer
getWriter()
```

Returns the Writer that is used to output the content.

**Returns:** the Writer that is used to output the content
**Since:** 1.3

---

#### getWriter

protected

Writer

getWriter()

Returns the Writer that is used to output the content.

getDocument

```java
protected
Document
getDocument()
```

Fetches the document.

**Returns:** the Document.

---

#### getDocument

protected

Document

getDocument()

Fetches the document.

inRange

```java
protected boolean inRange​(
Element
next)
```

This method determines whether the current element
is in the range specified. When no range is specified,
the range is initialized to be the entire document.
inRange() returns true if the range specified intersects
with the element's range.

**Parameters:** next

- an Element.
**Returns:** boolean that indicates whether the element
is in the range.

---

#### inRange

protected boolean inRange​(

Element

next)

This method determines whether the current element
is in the range specified. When no range is specified,
the range is initialized to be the entire document.
inRange() returns true if the range specified intersects
with the element's range.

write

```java
protected abstract void write()
throws
IOException
,

BadLocationException
```

This abstract method needs to be implemented
by subclasses. Its responsibility is to
iterate over the elements and use the write()
methods to generate output in the desired format.

**Throws:** IOException

- if an I/O problem has occurred
**Throws:** BadLocationException

- for an invalid location within
the document

---

#### write

protected abstract void write()
throws

IOException

,

BadLocationException

This abstract method needs to be implemented
by subclasses. Its responsibility is to
iterate over the elements and use the write()
methods to generate output in the desired format.

getText

```java
protected
String
getText​(
Element
elem)
throws
BadLocationException
```

Returns the text associated with the element.
The assumption here is that the element is a
leaf element. Throws a BadLocationException
when encountered.

**Parameters:** elem

- an

Element
**Returns:** the text as a

String
**Throws:** BadLocationException

- if pos represents an invalid
location within the document

---

#### getText

protected

String

getText​(

Element

elem)
throws

BadLocationException

Returns the text associated with the element.
The assumption here is that the element is a
leaf element. Throws a BadLocationException
when encountered.

text

```java
protected void text​(
Element
elem)
throws
BadLocationException
,

IOException
```

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

**Parameters:** elem

- an Element.
**Throws:** IOException

- on any I/O error
**Throws:** BadLocationException

- if pos represents an invalid
location within the document.

---

#### text

protected void text​(

Element

elem)
throws

BadLocationException

,

IOException

Writes out text. If a range is specified when the constructor
is invoked, then only the appropriate range of text is written
out.

setLineLength

```java
protected void setLineLength​(int l)
```

Enables subclasses to set the number of characters they
want written per line. The default is 100.

**Parameters:** l

- the maximum line length.

---

#### setLineLength

protected void setLineLength​(int l)

Enables subclasses to set the number of characters they
want written per line. The default is 100.

getLineLength

```java
protected int getLineLength()
```

Returns the maximum line length.

**Returns:** the maximum line length
**Since:** 1.3

---

#### getLineLength

protected int getLineLength()

Returns the maximum line length.

setCurrentLineLength

```java
protected void setCurrentLineLength​(int length)
```

Sets the current line length.

**Parameters:** length

- the new line length
**Since:** 1.3

---

#### setCurrentLineLength

protected void setCurrentLineLength​(int length)

Sets the current line length.

getCurrentLineLength

```java
protected int getCurrentLineLength()
```

Returns the current line length.

**Returns:** the current line length
**Since:** 1.3

---

#### getCurrentLineLength

protected int getCurrentLineLength()

Returns the current line length.

isLineEmpty

```java
protected boolean isLineEmpty()
```

Returns true if the current line should be considered empty. This
is true when

getCurrentLineLength

== 0 ||

indent

has been invoked on an empty line.

**Returns:** true if the current line should be considered empty
**Since:** 1.3

---

#### isLineEmpty

protected boolean isLineEmpty()

Returns true if the current line should be considered empty. This
is true when

getCurrentLineLength

== 0 ||

indent

has been invoked on an empty line.

setCanWrapLines

```java
protected void setCanWrapLines​(boolean newValue)
```

Sets whether or not lines can be wrapped. This can be toggled
during the writing of lines. For example, outputting HTML might
set this to false when outputting a quoted string.

**Parameters:** newValue

- new value for line wrapping
**Since:** 1.3

---

#### setCanWrapLines

protected void setCanWrapLines​(boolean newValue)

Sets whether or not lines can be wrapped. This can be toggled
during the writing of lines. For example, outputting HTML might
set this to false when outputting a quoted string.

getCanWrapLines

```java
protected boolean getCanWrapLines()
```

Returns whether or not the lines can be wrapped. If this is false
no lineSeparator's will be output.

**Returns:** whether or not the lines can be wrapped
**Since:** 1.3

---

#### getCanWrapLines

protected boolean getCanWrapLines()

Returns whether or not the lines can be wrapped. If this is false
no lineSeparator's will be output.

setIndentSpace

```java
protected void setIndentSpace​(int space)
```

Enables subclasses to specify how many spaces an indent
maps to. When indentation takes place, the indent level
is multiplied by this mapping. The default is 2.

**Parameters:** space

- an int representing the space to indent mapping.

---

#### setIndentSpace

protected void setIndentSpace​(int space)

Enables subclasses to specify how many spaces an indent
maps to. When indentation takes place, the indent level
is multiplied by this mapping. The default is 2.

getIndentSpace

```java
protected int getIndentSpace()
```

Returns the amount of space to indent.

**Returns:** the amount of space to indent
**Since:** 1.3

---

#### getIndentSpace

protected int getIndentSpace()

Returns the amount of space to indent.

setLineSeparator

```java
public void setLineSeparator​(
String
value)
```

Sets the String used to represent newlines. This is initialized
in the constructor from either the Document, or the System property
line.separator.

**Parameters:** value

- the new line separator
**Since:** 1.3

---

#### setLineSeparator

public void setLineSeparator​(

String

value)

Sets the String used to represent newlines. This is initialized
in the constructor from either the Document, or the System property
line.separator.

getLineSeparator

```java
public
String
getLineSeparator()
```

Returns the string used to represent newlines.

**Returns:** the string used to represent newlines
**Since:** 1.3

---

#### getLineSeparator

public

String

getLineSeparator()

Returns the string used to represent newlines.

incrIndent

```java
protected void incrIndent()
```

Increments the indent level. If indenting would cause

getIndentSpace()

*

getIndentLevel()

to be >
than

getLineLength()

this will not cause an indent.

---

#### incrIndent

protected void incrIndent()

Increments the indent level. If indenting would cause

getIndentSpace()

*

getIndentLevel()

to be >
than

getLineLength()

this will not cause an indent.

decrIndent

```java
protected void decrIndent()
```

Decrements the indent level.

---

#### decrIndent

protected void decrIndent()

Decrements the indent level.

getIndentLevel

```java
protected int getIndentLevel()
```

Returns the current indentation level. That is, the number of times

incrIndent

has been invoked minus the number of times

decrIndent

has been invoked.

**Returns:** the current indentation level
**Since:** 1.3

---

#### getIndentLevel

protected int getIndentLevel()

Returns the current indentation level. That is, the number of times

incrIndent

has been invoked minus the number of times

decrIndent

has been invoked.

indent

```java
protected void indent()
throws
IOException
```

Does indentation. The number of spaces written
out is indent level times the space to map mapping. If the current
line is empty, this will not make it so that the current line is
still considered empty.

**Throws:** IOException

- on any I/O error

---

#### indent

protected void indent()
throws

IOException

Does indentation. The number of spaces written
out is indent level times the space to map mapping. If the current
line is empty, this will not make it so that the current line is
still considered empty.

write

```java
protected void write​(char ch)
throws
IOException
```

Writes out a character. This is implemented to invoke
the

write

method that takes a char[].

**Parameters:** ch

- a char.
**Throws:** IOException

- on any I/O error

---

#### write

protected void write​(char ch)
throws

IOException

Writes out a character. This is implemented to invoke
the

write

method that takes a char[].

write

```java
protected void write​(
String
content)
throws
IOException
```

Writes out a string. This is implemented to invoke the

write

method that takes a char[].

**Parameters:** content

- a String.
**Throws:** IOException

- on any I/O error

---

#### write

protected void write​(

String

content)
throws

IOException

Writes out a string. This is implemented to invoke the

write

method that takes a char[].

writeLineSeparator

```java
protected void writeLineSeparator()
throws
IOException
```

Writes the line separator. This invokes

output

directly
as well as setting the

lineLength

to 0.

**Throws:** IOException

- on any I/O error
**Since:** 1.3

---

#### writeLineSeparator

protected void writeLineSeparator()
throws

IOException

Writes the line separator. This invokes

output

directly
as well as setting the

lineLength

to 0.

write

```java
protected void write​(char[] chars,
int startIndex,
int length)
throws
IOException
```

All write methods call into this one. If

getCanWrapLines()

returns false, this will call

output

with each sequence
of

chars

that doesn't contain a NEWLINE, followed
by a call to

writeLineSeparator

. On the other hand,
if

getCanWrapLines()

returns true, this will split the
string, as necessary, so

getLineLength

is honored.
The only exception is if the current string contains no whitespace,
and won't fit in which case the line length will exceed

getLineLength

.

**Parameters:** chars

- characters to output
**Parameters:** startIndex

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

---

#### write

protected void write​(char[] chars,
int startIndex,
int length)
throws

IOException

All write methods call into this one. If

getCanWrapLines()

returns false, this will call

output

with each sequence
of

chars

that doesn't contain a NEWLINE, followed
by a call to

writeLineSeparator

. On the other hand,
if

getCanWrapLines()

returns true, this will split the
string, as necessary, so

getLineLength

is honored.
The only exception is if the current string contains no whitespace,
and won't fit in which case the line length will exceed

getLineLength

.

writeAttributes

```java
protected void writeAttributes​(
AttributeSet
attr)
throws
IOException
```

Writes out the set of attributes as " <name>=<value>"
pairs. It throws an IOException when encountered.

**Parameters:** attr

- an AttributeSet.
**Throws:** IOException

- on any I/O error

---

#### writeAttributes

protected void writeAttributes​(

AttributeSet

attr)
throws

IOException

Writes out the set of attributes as " <name>=<value>"
pairs. It throws an IOException when encountered.

output

```java
protected void output​(char[] content,
int start,
int length)
throws
IOException
```

The last stop in writing out content. All the write methods eventually
make it to this method, which invokes

write

on the
Writer.

This method also updates the line length based on

length

. If this is invoked to output a newline, the
current line length will need to be reset as will no longer be
valid. If it is up to the caller to do this. Use

writeLineSeparator

to write out a newline, which will
property update the current line length.

**Parameters:** content

- characters to output
**Parameters:** start

- starting index
**Parameters:** length

- length of output
**Throws:** IOException

- on any I/O error
**Since:** 1.3

---

#### output

protected void output​(char[] content,
int start,
int length)
throws

IOException

The last stop in writing out content. All the write methods eventually
make it to this method, which invokes

write

on the
Writer.

This method also updates the line length based on

length

. If this is invoked to output a newline, the
current line length will need to be reset as will no longer be
valid. If it is up to the caller to do this. Use

writeLineSeparator

to write out a newline, which will
property update the current line length.

This method also updates the line length based on

length

. If this is invoked to output a newline, the
current line length will need to be reset as will no longer be
valid. If it is up to the caller to do this. Use

writeLineSeparator

to write out a newline, which will
property update the current line length.

---

