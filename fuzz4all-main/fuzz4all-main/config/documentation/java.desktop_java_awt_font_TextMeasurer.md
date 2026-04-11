# Class TextMeasurer

**Source:** `java.desktop\java\awt\font\TextMeasurer.html`

### Class Description

```java
public final class
TextMeasurer

extends
Object

implements
Cloneable
```

The

TextMeasurer

class provides the primitive operations
needed for line break: measuring up to a given advance, determining the
advance of a range of characters, and generating a

TextLayout

for a range of characters. It also provides
methods for incremental editing of paragraphs.

A

TextMeasurer

object is constructed with an

AttributedCharacterIterator

representing a single paragraph of text. The value returned by the

getBeginIndex

method of

AttributedCharacterIterator

defines the absolute index of the first character. The value
returned by the

getEndIndex

method of

AttributedCharacterIterator

defines the index
past the last character. These values define the range of indexes to
use in calls to the

TextMeasurer

. For example, calls to
get the advance of a range of text or the line break of a range of text
must use indexes between the beginning and end index values. Calls to

insertChar

and

deleteChar

reset the

TextMeasurer

to use the beginning index and end
index of the

AttributedCharacterIterator

passed in those calls.

Most clients will use the more convenient

LineBreakMeasurer

,
which implements the standard line break policy (placing as many words
as will fit on each line).

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TextMeasurer​(
AttributedCharacterIterator
text,

FontRenderContext
frc)

Constructs a

TextMeasurer

from the source text.
The source text should be a single entire paragraph.

**Parameters:**
- text

- the source paragraph. Cannot be null.
- frc

- the information about a graphics device which is needed
to measure the text correctly. Cannot be null.

---

### Method Details

#### public int getLineBreakIndex​(int start,
float maxAdvance)

Returns the index of the first character which will not fit on
on a line beginning at

start

and possible
measuring up to

maxAdvance

in graphical width.

**Parameters:**
- start

- the character index at which to start measuring.

start

is an absolute index, not relative to the
start of the paragraph
- maxAdvance

- the graphical width in which the line must fit

**Returns:**
- the index after the last character that will fit
on a line beginning at

start

, which is not longer
than

maxAdvance

in graphical width

**Throws:**
- IllegalArgumentException

- if

start

is
less than the beginning of the paragraph.

---

#### public float getAdvanceBetween​(int start,
int limit)

Returns the graphical width of a line beginning at

start

and including characters up to

limit

.

start

and

limit

are absolute indices,
not relative to the start of the paragraph.

**Parameters:**
- start

- the character index at which to start measuring
- limit

- the character index at which to stop measuring

**Returns:**
- the graphical width of a line beginning at

start

and including characters up to

limit

**Throws:**
- IndexOutOfBoundsException

- if

limit

is less
than

start
- IllegalArgumentException

- if

start

or

limit

is not between the beginning of
the paragraph and the end of the paragraph.

---

#### public
TextLayout
getLayout​(int start,
int limit)

Returns a

TextLayout

on the given character range.

**Parameters:**
- start

- the index of the first character
- limit

- the index after the last character. Must be greater
than

start

**Returns:**
- a

TextLayout

for the characters beginning at

start

up to (but not including)

limit

**Throws:**
- IndexOutOfBoundsException

- if

limit

is less
than

start
- IllegalArgumentException

- if

start

or

limit

is not between the beginning of
the paragraph and the end of the paragraph.

---

#### public void insertChar​(
AttributedCharacterIterator
newParagraph,
int insertPos)

Updates the

TextMeasurer

after a single character has
been inserted
into the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will
usually be more efficient to update an existing

TextMeasurer

than to create a new one from scratch.

**Parameters:**
- newParagraph

- the text of the paragraph after performing
the insertion. Cannot be null.
- insertPos

- the position in the text where the character was
inserted. Must not be less than the start of

newParagraph

, and must be less than the end of

newParagraph

.

**Throws:**
- IndexOutOfBoundsException

- if

insertPos

is less
than the start of

newParagraph

or greater than
or equal to the end of

newParagraph
- NullPointerException

- if

newParagraph

is

null

---

#### public void deleteChar​(
AttributedCharacterIterator
newParagraph,
int deletePos)

Updates the

TextMeasurer

after a single character has
been deleted
from the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will usually be more efficient
to update an existing

TextMeasurer

than to create a new one
from scratch.

**Parameters:**
- newParagraph

- the text of the paragraph after performing
the deletion. Cannot be null.
- deletePos

- the position in the text where the character was removed.
Must not be less than
the start of

newParagraph

, and must not be greater than the
end of

newParagraph

.

**Throws:**
- IndexOutOfBoundsException

- if

deletePos

is
less than the start of

newParagraph

or greater
than the end of

newParagraph
- NullPointerException

- if

newParagraph

is

null

---

### Additional Sections

#### Class TextMeasurer

java.lang.Object

- java.awt.font.TextMeasurer

java.awt.font.TextMeasurer

**All Implemented Interfaces:** Cloneable

```java
public final class
TextMeasurer

extends
Object

implements
Cloneable
```

The

TextMeasurer

class provides the primitive operations
needed for line break: measuring up to a given advance, determining the
advance of a range of characters, and generating a

TextLayout

for a range of characters. It also provides
methods for incremental editing of paragraphs.

A

TextMeasurer

object is constructed with an

AttributedCharacterIterator

representing a single paragraph of text. The value returned by the

getBeginIndex

method of

AttributedCharacterIterator

defines the absolute index of the first character. The value
returned by the

getEndIndex

method of

AttributedCharacterIterator

defines the index
past the last character. These values define the range of indexes to
use in calls to the

TextMeasurer

. For example, calls to
get the advance of a range of text or the line break of a range of text
must use indexes between the beginning and end index values. Calls to

insertChar

and

deleteChar

reset the

TextMeasurer

to use the beginning index and end
index of the

AttributedCharacterIterator

passed in those calls.

Most clients will use the more convenient

LineBreakMeasurer

,
which implements the standard line break policy (placing as many words
as will fit on each line).

**Since:** 1.3
**See Also:** LineBreakMeasurer

public final class

TextMeasurer

extends

Object

implements

Cloneable

The

TextMeasurer

class provides the primitive operations
needed for line break: measuring up to a given advance, determining the
advance of a range of characters, and generating a

TextLayout

for a range of characters. It also provides
methods for incremental editing of paragraphs.

A

TextMeasurer

object is constructed with an

AttributedCharacterIterator

representing a single paragraph of text. The value returned by the

getBeginIndex

method of

AttributedCharacterIterator

defines the absolute index of the first character. The value
returned by the

getEndIndex

method of

AttributedCharacterIterator

defines the index
past the last character. These values define the range of indexes to
use in calls to the

TextMeasurer

. For example, calls to
get the advance of a range of text or the line break of a range of text
must use indexes between the beginning and end index values. Calls to

insertChar

and

deleteChar

reset the

TextMeasurer

to use the beginning index and end
index of the

AttributedCharacterIterator

passed in those calls.

Most clients will use the more convenient

LineBreakMeasurer

,
which implements the standard line break policy (placing as many words
as will fit on each line).

A

TextMeasurer

object is constructed with an

AttributedCharacterIterator

representing a single paragraph of text. The value returned by the

getBeginIndex

method of

AttributedCharacterIterator

defines the absolute index of the first character. The value
returned by the

getEndIndex

method of

AttributedCharacterIterator

defines the index
past the last character. These values define the range of indexes to
use in calls to the

TextMeasurer

. For example, calls to
get the advance of a range of text or the line break of a range of text
must use indexes between the beginning and end index values. Calls to

insertChar

and

deleteChar

reset the

TextMeasurer

to use the beginning index and end
index of the

AttributedCharacterIterator

passed in those calls.

Most clients will use the more convenient

LineBreakMeasurer

,
which implements the standard line break policy (placing as many words
as will fit on each line).

Most clients will use the more convenient

LineBreakMeasurer

,
which implements the standard line break policy (placing as many words
as will fit on each line).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TextMeasurer

​(

AttributedCharacterIterator

text,

FontRenderContext

frc)

Constructs a

TextMeasurer

from the source text.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

deleteChar

​(

AttributedCharacterIterator

newParagraph,
int deletePos)

Updates the

TextMeasurer

after a single character has
been deleted
from the paragraph currently represented by this

TextMeasurer

.

float

getAdvanceBetween

​(int start,
int limit)

Returns the graphical width of a line beginning at

start

and including characters up to

limit

.

TextLayout

getLayout

​(int start,
int limit)

Returns a

TextLayout

on the given character range.

int

getLineBreakIndex

​(int start,
float maxAdvance)

Returns the index of the first character which will not fit on
on a line beginning at

start

and possible
measuring up to

maxAdvance

in graphical width.

void

insertChar

​(

AttributedCharacterIterator

newParagraph,
int insertPos)

Updates the

TextMeasurer

after a single character has
been inserted
into the paragraph currently represented by this

TextMeasurer

.

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

Constructor Summary

Constructors

Constructor

Description

TextMeasurer

​(

AttributedCharacterIterator

text,

FontRenderContext

frc)

Constructs a

TextMeasurer

from the source text.

---

#### Constructor Summary

Constructs a

TextMeasurer

from the source text.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

deleteChar

​(

AttributedCharacterIterator

newParagraph,
int deletePos)

Updates the

TextMeasurer

after a single character has
been deleted
from the paragraph currently represented by this

TextMeasurer

.

float

getAdvanceBetween

​(int start,
int limit)

Returns the graphical width of a line beginning at

start

and including characters up to

limit

.

TextLayout

getLayout

​(int start,
int limit)

Returns a

TextLayout

on the given character range.

int

getLineBreakIndex

​(int start,
float maxAdvance)

Returns the index of the first character which will not fit on
on a line beginning at

start

and possible
measuring up to

maxAdvance

in graphical width.

void

insertChar

​(

AttributedCharacterIterator

newParagraph,
int insertPos)

Updates the

TextMeasurer

after a single character has
been inserted
into the paragraph currently represented by this

TextMeasurer

.

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

Updates the

TextMeasurer

after a single character has
been deleted
from the paragraph currently represented by this

TextMeasurer

.

Returns the graphical width of a line beginning at

start

and including characters up to

limit

.

Returns a

TextLayout

on the given character range.

Returns the index of the first character which will not fit on
on a line beginning at

start

and possible
measuring up to

maxAdvance

in graphical width.

Updates the

TextMeasurer

after a single character has
been inserted
into the paragraph currently represented by this

TextMeasurer

.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TextMeasurer

```java
public TextMeasurer​(
AttributedCharacterIterator
text,

FontRenderContext
frc)
```

Constructs a

TextMeasurer

from the source text.
The source text should be a single entire paragraph.

**Parameters:** text

- the source paragraph. Cannot be null.
**Parameters:** frc

- the information about a graphics device which is needed
to measure the text correctly. Cannot be null.

============ METHOD DETAIL ==========

- Method Detail

- getLineBreakIndex

```java
public int getLineBreakIndex​(int start,
float maxAdvance)
```

Returns the index of the first character which will not fit on
on a line beginning at

start

and possible
measuring up to

maxAdvance

in graphical width.

**Parameters:** start

- the character index at which to start measuring.

start

is an absolute index, not relative to the
start of the paragraph
**Parameters:** maxAdvance

- the graphical width in which the line must fit
**Returns:** the index after the last character that will fit
on a line beginning at

start

, which is not longer
than

maxAdvance

in graphical width
**Throws:** IllegalArgumentException

- if

start

is
less than the beginning of the paragraph.

- getAdvanceBetween

```java
public float getAdvanceBetween​(int start,
int limit)
```

Returns the graphical width of a line beginning at

start

and including characters up to

limit

.

start

and

limit

are absolute indices,
not relative to the start of the paragraph.

**Parameters:** start

- the character index at which to start measuring
**Parameters:** limit

- the character index at which to stop measuring
**Returns:** the graphical width of a line beginning at

start

and including characters up to

limit
**Throws:** IndexOutOfBoundsException

- if

limit

is less
than

start
**Throws:** IllegalArgumentException

- if

start

or

limit

is not between the beginning of
the paragraph and the end of the paragraph.

- getLayout

```java
public
TextLayout
getLayout​(int start,
int limit)
```

Returns a

TextLayout

on the given character range.

**Parameters:** start

- the index of the first character
**Parameters:** limit

- the index after the last character. Must be greater
than

start
**Returns:** a

TextLayout

for the characters beginning at

start

up to (but not including)

limit
**Throws:** IndexOutOfBoundsException

- if

limit

is less
than

start
**Throws:** IllegalArgumentException

- if

start

or

limit

is not between the beginning of
the paragraph and the end of the paragraph.

- insertChar

```java
public void insertChar​(
AttributedCharacterIterator
newParagraph,
int insertPos)
```

Updates the

TextMeasurer

after a single character has
been inserted
into the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will
usually be more efficient to update an existing

TextMeasurer

than to create a new one from scratch.

**Parameters:** newParagraph

- the text of the paragraph after performing
the insertion. Cannot be null.
**Parameters:** insertPos

- the position in the text where the character was
inserted. Must not be less than the start of

newParagraph

, and must be less than the end of

newParagraph

.
**Throws:** IndexOutOfBoundsException

- if

insertPos

is less
than the start of

newParagraph

or greater than
or equal to the end of

newParagraph
**Throws:** NullPointerException

- if

newParagraph

is

null

- deleteChar

```java
public void deleteChar​(
AttributedCharacterIterator
newParagraph,
int deletePos)
```

Updates the

TextMeasurer

after a single character has
been deleted
from the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will usually be more efficient
to update an existing

TextMeasurer

than to create a new one
from scratch.

**Parameters:** newParagraph

- the text of the paragraph after performing
the deletion. Cannot be null.
**Parameters:** deletePos

- the position in the text where the character was removed.
Must not be less than
the start of

newParagraph

, and must not be greater than the
end of

newParagraph

.
**Throws:** IndexOutOfBoundsException

- if

deletePos

is
less than the start of

newParagraph

or greater
than the end of

newParagraph
**Throws:** NullPointerException

- if

newParagraph

is

null

Constructor Detail

- TextMeasurer

```java
public TextMeasurer​(
AttributedCharacterIterator
text,

FontRenderContext
frc)
```

Constructs a

TextMeasurer

from the source text.
The source text should be a single entire paragraph.

**Parameters:** text

- the source paragraph. Cannot be null.
**Parameters:** frc

- the information about a graphics device which is needed
to measure the text correctly. Cannot be null.

---

#### Constructor Detail

TextMeasurer

```java
public TextMeasurer​(
AttributedCharacterIterator
text,

FontRenderContext
frc)
```

Constructs a

TextMeasurer

from the source text.
The source text should be a single entire paragraph.

**Parameters:** text

- the source paragraph. Cannot be null.
**Parameters:** frc

- the information about a graphics device which is needed
to measure the text correctly. Cannot be null.

---

#### TextMeasurer

public TextMeasurer​(

AttributedCharacterIterator

text,

FontRenderContext

frc)

Constructs a

TextMeasurer

from the source text.
The source text should be a single entire paragraph.

Method Detail

- getLineBreakIndex

```java
public int getLineBreakIndex​(int start,
float maxAdvance)
```

Returns the index of the first character which will not fit on
on a line beginning at

start

and possible
measuring up to

maxAdvance

in graphical width.

**Parameters:** start

- the character index at which to start measuring.

start

is an absolute index, not relative to the
start of the paragraph
**Parameters:** maxAdvance

- the graphical width in which the line must fit
**Returns:** the index after the last character that will fit
on a line beginning at

start

, which is not longer
than

maxAdvance

in graphical width
**Throws:** IllegalArgumentException

- if

start

is
less than the beginning of the paragraph.

- getAdvanceBetween

```java
public float getAdvanceBetween​(int start,
int limit)
```

Returns the graphical width of a line beginning at

start

and including characters up to

limit

.

start

and

limit

are absolute indices,
not relative to the start of the paragraph.

**Parameters:** start

- the character index at which to start measuring
**Parameters:** limit

- the character index at which to stop measuring
**Returns:** the graphical width of a line beginning at

start

and including characters up to

limit
**Throws:** IndexOutOfBoundsException

- if

limit

is less
than

start
**Throws:** IllegalArgumentException

- if

start

or

limit

is not between the beginning of
the paragraph and the end of the paragraph.

- getLayout

```java
public
TextLayout
getLayout​(int start,
int limit)
```

Returns a

TextLayout

on the given character range.

**Parameters:** start

- the index of the first character
**Parameters:** limit

- the index after the last character. Must be greater
than

start
**Returns:** a

TextLayout

for the characters beginning at

start

up to (but not including)

limit
**Throws:** IndexOutOfBoundsException

- if

limit

is less
than

start
**Throws:** IllegalArgumentException

- if

start

or

limit

is not between the beginning of
the paragraph and the end of the paragraph.

- insertChar

```java
public void insertChar​(
AttributedCharacterIterator
newParagraph,
int insertPos)
```

Updates the

TextMeasurer

after a single character has
been inserted
into the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will
usually be more efficient to update an existing

TextMeasurer

than to create a new one from scratch.

**Parameters:** newParagraph

- the text of the paragraph after performing
the insertion. Cannot be null.
**Parameters:** insertPos

- the position in the text where the character was
inserted. Must not be less than the start of

newParagraph

, and must be less than the end of

newParagraph

.
**Throws:** IndexOutOfBoundsException

- if

insertPos

is less
than the start of

newParagraph

or greater than
or equal to the end of

newParagraph
**Throws:** NullPointerException

- if

newParagraph

is

null

- deleteChar

```java
public void deleteChar​(
AttributedCharacterIterator
newParagraph,
int deletePos)
```

Updates the

TextMeasurer

after a single character has
been deleted
from the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will usually be more efficient
to update an existing

TextMeasurer

than to create a new one
from scratch.

**Parameters:** newParagraph

- the text of the paragraph after performing
the deletion. Cannot be null.
**Parameters:** deletePos

- the position in the text where the character was removed.
Must not be less than
the start of

newParagraph

, and must not be greater than the
end of

newParagraph

.
**Throws:** IndexOutOfBoundsException

- if

deletePos

is
less than the start of

newParagraph

or greater
than the end of

newParagraph
**Throws:** NullPointerException

- if

newParagraph

is

null

---

#### Method Detail

getLineBreakIndex

```java
public int getLineBreakIndex​(int start,
float maxAdvance)
```

Returns the index of the first character which will not fit on
on a line beginning at

start

and possible
measuring up to

maxAdvance

in graphical width.

**Parameters:** start

- the character index at which to start measuring.

start

is an absolute index, not relative to the
start of the paragraph
**Parameters:** maxAdvance

- the graphical width in which the line must fit
**Returns:** the index after the last character that will fit
on a line beginning at

start

, which is not longer
than

maxAdvance

in graphical width
**Throws:** IllegalArgumentException

- if

start

is
less than the beginning of the paragraph.

---

#### getLineBreakIndex

public int getLineBreakIndex​(int start,
float maxAdvance)

Returns the index of the first character which will not fit on
on a line beginning at

start

and possible
measuring up to

maxAdvance

in graphical width.

getAdvanceBetween

```java
public float getAdvanceBetween​(int start,
int limit)
```

Returns the graphical width of a line beginning at

start

and including characters up to

limit

.

start

and

limit

are absolute indices,
not relative to the start of the paragraph.

**Parameters:** start

- the character index at which to start measuring
**Parameters:** limit

- the character index at which to stop measuring
**Returns:** the graphical width of a line beginning at

start

and including characters up to

limit
**Throws:** IndexOutOfBoundsException

- if

limit

is less
than

start
**Throws:** IllegalArgumentException

- if

start

or

limit

is not between the beginning of
the paragraph and the end of the paragraph.

---

#### getAdvanceBetween

public float getAdvanceBetween​(int start,
int limit)

Returns the graphical width of a line beginning at

start

and including characters up to

limit

.

start

and

limit

are absolute indices,
not relative to the start of the paragraph.

getLayout

```java
public
TextLayout
getLayout​(int start,
int limit)
```

Returns a

TextLayout

on the given character range.

**Parameters:** start

- the index of the first character
**Parameters:** limit

- the index after the last character. Must be greater
than

start
**Returns:** a

TextLayout

for the characters beginning at

start

up to (but not including)

limit
**Throws:** IndexOutOfBoundsException

- if

limit

is less
than

start
**Throws:** IllegalArgumentException

- if

start

or

limit

is not between the beginning of
the paragraph and the end of the paragraph.

---

#### getLayout

public

TextLayout

getLayout​(int start,
int limit)

Returns a

TextLayout

on the given character range.

insertChar

```java
public void insertChar​(
AttributedCharacterIterator
newParagraph,
int insertPos)
```

Updates the

TextMeasurer

after a single character has
been inserted
into the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will
usually be more efficient to update an existing

TextMeasurer

than to create a new one from scratch.

**Parameters:** newParagraph

- the text of the paragraph after performing
the insertion. Cannot be null.
**Parameters:** insertPos

- the position in the text where the character was
inserted. Must not be less than the start of

newParagraph

, and must be less than the end of

newParagraph

.
**Throws:** IndexOutOfBoundsException

- if

insertPos

is less
than the start of

newParagraph

or greater than
or equal to the end of

newParagraph
**Throws:** NullPointerException

- if

newParagraph

is

null

---

#### insertChar

public void insertChar​(

AttributedCharacterIterator

newParagraph,
int insertPos)

Updates the

TextMeasurer

after a single character has
been inserted
into the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will
usually be more efficient to update an existing

TextMeasurer

than to create a new one from scratch.

deleteChar

```java
public void deleteChar​(
AttributedCharacterIterator
newParagraph,
int deletePos)
```

Updates the

TextMeasurer

after a single character has
been deleted
from the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will usually be more efficient
to update an existing

TextMeasurer

than to create a new one
from scratch.

**Parameters:** newParagraph

- the text of the paragraph after performing
the deletion. Cannot be null.
**Parameters:** deletePos

- the position in the text where the character was removed.
Must not be less than
the start of

newParagraph

, and must not be greater than the
end of

newParagraph

.
**Throws:** IndexOutOfBoundsException

- if

deletePos

is
less than the start of

newParagraph

or greater
than the end of

newParagraph
**Throws:** NullPointerException

- if

newParagraph

is

null

---

#### deleteChar

public void deleteChar​(

AttributedCharacterIterator

newParagraph,
int deletePos)

Updates the

TextMeasurer

after a single character has
been deleted
from the paragraph currently represented by this

TextMeasurer

. After this call, this

TextMeasurer

is equivalent to a new

TextMeasurer

created from the text; however, it will usually be more efficient
to update an existing

TextMeasurer

than to create a new one
from scratch.

---

