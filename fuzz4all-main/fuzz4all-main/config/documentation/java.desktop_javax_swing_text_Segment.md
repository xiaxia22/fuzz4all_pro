# Class Segment

**Source:** `java.desktop\javax\swing\text\Segment.html`

### Class Description

```java
public class
Segment

extends
Object

implements
Cloneable
,
CharacterIterator
,
CharSequence
```

A segment of a character array representing a fragment
of text. It should be treated as immutable even though
the array is directly accessible. This gives fast access
to fragments of text without the overhead of copying
around characters. This is effectively an unprotected
String.

The Segment implements the java.text.CharacterIterator
interface to support use with the i18n support without
copying text into a string.

**All Implemented Interfaces:** CharSequence

,

Cloneable

,

CharacterIterator

---

### Field Details

#### public char[] array

This is the array containing the text of
interest. This array should never be modified;
it is available only for efficiency.

---

#### public int offset

This is the offset into the array that
the desired text begins.

---

#### public int count

This is the number of array elements that
make up the text of interest.

---

### Constructor Details

#### public Segment()

Creates a new segment.

---

#### public Segment​(char[] array,
int offset,
int count)

Creates a new segment referring to an existing array.

**Parameters:**
- array

- the array to refer to
- offset

- the offset into the array
- count

- the number of characters

---

### Method Details

#### public void setPartialReturn​(boolean p)

Flag to indicate that partial returns are valid. If the flag is true,
an implementation of the interface method Document.getText(position,length,Segment)
should return as much text as possible without making a copy. The default
state of the flag is false which will cause Document.getText(position,length,Segment)
to provide the same return behavior it always had, which may or may not
make a copy of the text depending upon the request.

**Parameters:**
- p

- whether or not partial returns are valid.

**Since:**
- 1.4

---

#### public boolean isPartialReturn()

Flag to indicate that partial returns are valid.

**Returns:**
- whether or not partial returns are valid.

**Since:**
- 1.4

---

#### public
String
toString()

Converts a segment into a String.

**Specified by:**
- toString

in interface

CharSequence

**Overrides:**
- toString

in class

Object

**Returns:**
- the string

---

#### public char first()

Sets the position to getBeginIndex() and returns the character at that
position.

**Specified by:**
- first

in interface

CharacterIterator

**Returns:**
- the first character in the text, or DONE if the text is empty

**See Also:**
- getBeginIndex()

**Since:**
- 1.3

---

#### public char last()

Sets the position to getEndIndex()-1 (getEndIndex() if the text is empty)
and returns the character at that position.

**Specified by:**
- last

in interface

CharacterIterator

**Returns:**
- the last character in the text, or DONE if the text is empty

**See Also:**
- getEndIndex()

**Since:**
- 1.3

---

#### public char current()

Gets the character at the current position (as returned by getIndex()).

**Specified by:**
- current

in interface

CharacterIterator

**Returns:**
- the character at the current position or DONE if the current
position is off the end of the text.

**See Also:**
- getIndex()

**Since:**
- 1.3

---

#### public char next()

Increments the iterator's index by one and returns the character
at the new index. If the resulting index is greater or equal
to getEndIndex(), the current index is reset to getEndIndex() and
a value of DONE is returned.

**Specified by:**
- next

in interface

CharacterIterator

**Returns:**
- the character at the new position or DONE if the new
position is off the end of the text range.

**Since:**
- 1.3

---

#### public char previous()

Decrements the iterator's index by one and returns the character
at the new index. If the current index is getBeginIndex(), the index
remains at getBeginIndex() and a value of DONE is returned.

**Specified by:**
- previous

in interface

CharacterIterator

**Returns:**
- the character at the new position or DONE if the current
position is equal to getBeginIndex().

**Since:**
- 1.3

---

#### public char setIndex​(int position)

Sets the position to the specified position in the text and returns that
character.

**Specified by:**
- setIndex

in interface

CharacterIterator

**Parameters:**
- position

- the position within the text. Valid values range from
getBeginIndex() to getEndIndex(). An IllegalArgumentException is thrown
if an invalid value is supplied.

**Returns:**
- the character at the specified position or DONE if the specified position is equal to getEndIndex()

**Since:**
- 1.3

---

#### public int getBeginIndex()

Returns the start index of the text.

**Specified by:**
- getBeginIndex

in interface

CharacterIterator

**Returns:**
- the index at which the text begins.

**Since:**
- 1.3

---

#### public int getEndIndex()

Returns the end index of the text. This index is the index of the first
character following the end of the text.

**Specified by:**
- getEndIndex

in interface

CharacterIterator

**Returns:**
- the index after the last character in the text

**Since:**
- 1.3

---

#### public int getIndex()

Returns the current index.

**Specified by:**
- getIndex

in interface

CharacterIterator

**Returns:**
- the current index.

**Since:**
- 1.3

---

#### public char charAt​(int index)

Returns the

char

value at the specified index. An index ranges from zero
to

length() - 1

. The first

char

value of the sequence is at
index zero, the next at index one, and so on, as for array
indexing.

If the

char

value specified by the index is a

surrogate

, the surrogate
value is returned.

**Specified by:**
- charAt

in interface

CharSequence

**Parameters:**
- index

- the index of the

char

value to be returned

**Returns:**
- the specified

char

value

**Since:**
- 1.6

---

#### public int length()

Returns the length of this character sequence. The length is the number
of 16-bit

char

s in the sequence.

**Specified by:**
- length

in interface

CharSequence

**Returns:**
- the number of

char

s in this sequence

**Since:**
- 1.6

---

#### public
CharSequence
subSequence​(int start,
int end)

Returns a

CharSequence

that is a subsequence of this sequence.
The subsequence starts with the

char

value at the specified index and
ends with the

char

value at index

end - 1

. The length
(in

char

s) of the
returned sequence is

end - start

, so if

start == end

then an empty sequence is returned.

**Specified by:**
- subSequence

in interface

CharSequence

**Parameters:**
- start

- the start index, inclusive
- end

- the end index, exclusive

**Returns:**
- the specified subsequence

**Since:**
- 1.6

---

#### public
Object
clone()

Creates a shallow copy.

**Specified by:**
- clone

in interface

CharacterIterator

**Overrides:**
- clone

in class

Object

**Returns:**
- the copy

**See Also:**
- Cloneable

---

### Additional Sections

#### Class Segment

java.lang.Object

- javax.swing.text.Segment

javax.swing.text.Segment

**All Implemented Interfaces:** CharSequence

,

Cloneable

,

CharacterIterator

```java
public class
Segment

extends
Object

implements
Cloneable
,
CharacterIterator
,
CharSequence
```

A segment of a character array representing a fragment
of text. It should be treated as immutable even though
the array is directly accessible. This gives fast access
to fragments of text without the overhead of copying
around characters. This is effectively an unprotected
String.

The Segment implements the java.text.CharacterIterator
interface to support use with the i18n support without
copying text into a string.

public class

Segment

extends

Object

implements

Cloneable

,

CharacterIterator

,

CharSequence

A segment of a character array representing a fragment
of text. It should be treated as immutable even though
the array is directly accessible. This gives fast access
to fragments of text without the overhead of copying
around characters. This is effectively an unprotected
String.

The Segment implements the java.text.CharacterIterator
interface to support use with the i18n support without
copying text into a string.

The Segment implements the java.text.CharacterIterator
interface to support use with the i18n support without
copying text into a string.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

char[]

array

This is the array containing the text of
interest.

int

count

This is the number of array elements that
make up the text of interest.

int

offset

This is the offset into the array that
the desired text begins.

- Fields declared in interface java.text.

CharacterIterator

DONE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Segment

()

Creates a new segment.

Segment

​(char[] array,
int offset,
int count)

Creates a new segment referring to an existing array.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

char

charAt

​(int index)

Returns the

char

value at the specified index.

Object

clone

()

Creates a shallow copy.

char

current

()

Gets the character at the current position (as returned by getIndex()).

char

first

()

Sets the position to getBeginIndex() and returns the character at that
position.

int

getBeginIndex

()

Returns the start index of the text.

int

getEndIndex

()

Returns the end index of the text.

int

getIndex

()

Returns the current index.

boolean

isPartialReturn

()

Flag to indicate that partial returns are valid.

char

last

()

Sets the position to getEndIndex()-1 (getEndIndex() if the text is empty)
and returns the character at that position.

int

length

()

Returns the length of this character sequence.

char

next

()

Increments the iterator's index by one and returns the character
at the new index.

char

previous

()

Decrements the iterator's index by one and returns the character
at the new index.

char

setIndex

​(int position)

Sets the position to the specified position in the text and returns that
character.

void

setPartialReturn

​(boolean p)

Flag to indicate that partial returns are valid.

CharSequence

subSequence

​(int start,
int end)

Returns a

CharSequence

that is a subsequence of this sequence.

String

toString

()

Converts a segment into a String.

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

wait

,

wait

,

wait

- Methods declared in interface java.lang.

CharSequence

chars

,

codePoints

Field Summary

Fields

Modifier and Type

Field

Description

char[]

array

This is the array containing the text of
interest.

int

count

This is the number of array elements that
make up the text of interest.

int

offset

This is the offset into the array that
the desired text begins.

- Fields declared in interface java.text.

CharacterIterator

DONE

---

#### Field Summary

This is the array containing the text of
interest.

This is the number of array elements that
make up the text of interest.

This is the offset into the array that
the desired text begins.

Fields declared in interface java.text.

CharacterIterator

DONE

---

#### Fields declared in interface java.text. CharacterIterator

Constructor Summary

Constructors

Constructor

Description

Segment

()

Creates a new segment.

Segment

​(char[] array,
int offset,
int count)

Creates a new segment referring to an existing array.

---

#### Constructor Summary

Creates a new segment.

Creates a new segment referring to an existing array.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

char

charAt

​(int index)

Returns the

char

value at the specified index.

Object

clone

()

Creates a shallow copy.

char

current

()

Gets the character at the current position (as returned by getIndex()).

char

first

()

Sets the position to getBeginIndex() and returns the character at that
position.

int

getBeginIndex

()

Returns the start index of the text.

int

getEndIndex

()

Returns the end index of the text.

int

getIndex

()

Returns the current index.

boolean

isPartialReturn

()

Flag to indicate that partial returns are valid.

char

last

()

Sets the position to getEndIndex()-1 (getEndIndex() if the text is empty)
and returns the character at that position.

int

length

()

Returns the length of this character sequence.

char

next

()

Increments the iterator's index by one and returns the character
at the new index.

char

previous

()

Decrements the iterator's index by one and returns the character
at the new index.

char

setIndex

​(int position)

Sets the position to the specified position in the text and returns that
character.

void

setPartialReturn

​(boolean p)

Flag to indicate that partial returns are valid.

CharSequence

subSequence

​(int start,
int end)

Returns a

CharSequence

that is a subsequence of this sequence.

String

toString

()

Converts a segment into a String.

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

wait

,

wait

,

wait

- Methods declared in interface java.lang.

CharSequence

chars

,

codePoints

---

#### Method Summary

Returns the

char

value at the specified index.

Creates a shallow copy.

Gets the character at the current position (as returned by getIndex()).

Sets the position to getBeginIndex() and returns the character at that
position.

Returns the start index of the text.

Returns the end index of the text.

Returns the current index.

Flag to indicate that partial returns are valid.

Sets the position to getEndIndex()-1 (getEndIndex() if the text is empty)
and returns the character at that position.

Returns the length of this character sequence.

Increments the iterator's index by one and returns the character
at the new index.

Decrements the iterator's index by one and returns the character
at the new index.

Sets the position to the specified position in the text and returns that
character.

Returns a

CharSequence

that is a subsequence of this sequence.

Converts a segment into a String.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.lang.

CharSequence

chars

,

codePoints

---

#### Methods declared in interface java.lang. CharSequence

============ FIELD DETAIL ===========

- Field Detail

- array

```java
public char[] array
```

This is the array containing the text of
interest. This array should never be modified;
it is available only for efficiency.

- offset

```java
public int offset
```

This is the offset into the array that
the desired text begins.

- count

```java
public int count
```

This is the number of array elements that
make up the text of interest.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Segment

```java
public Segment()
```

Creates a new segment.

- Segment

```java
public Segment​(char[] array,
int offset,
int count)
```

Creates a new segment referring to an existing array.

**Parameters:** array

- the array to refer to
**Parameters:** offset

- the offset into the array
**Parameters:** count

- the number of characters

============ METHOD DETAIL ==========

- Method Detail

- setPartialReturn

```java
public void setPartialReturn​(boolean p)
```

Flag to indicate that partial returns are valid. If the flag is true,
an implementation of the interface method Document.getText(position,length,Segment)
should return as much text as possible without making a copy. The default
state of the flag is false which will cause Document.getText(position,length,Segment)
to provide the same return behavior it always had, which may or may not
make a copy of the text depending upon the request.

**Parameters:** p

- whether or not partial returns are valid.
**Since:** 1.4

- isPartialReturn

```java
public boolean isPartialReturn()
```

Flag to indicate that partial returns are valid.

**Returns:** whether or not partial returns are valid.
**Since:** 1.4

- toString

```java
public
String
toString()
```

Converts a segment into a String.

**Specified by:** toString

in interface

CharSequence
**Overrides:** toString

in class

Object
**Returns:** the string

- first

```java
public char first()
```

Sets the position to getBeginIndex() and returns the character at that
position.

**Specified by:** first

in interface

CharacterIterator
**Returns:** the first character in the text, or DONE if the text is empty
**Since:** 1.3
**See Also:** getBeginIndex()

- last

```java
public char last()
```

Sets the position to getEndIndex()-1 (getEndIndex() if the text is empty)
and returns the character at that position.

**Specified by:** last

in interface

CharacterIterator
**Returns:** the last character in the text, or DONE if the text is empty
**Since:** 1.3
**See Also:** getEndIndex()

- current

```java
public char current()
```

Gets the character at the current position (as returned by getIndex()).

**Specified by:** current

in interface

CharacterIterator
**Returns:** the character at the current position or DONE if the current
position is off the end of the text.
**Since:** 1.3
**See Also:** getIndex()

- next

```java
public char next()
```

Increments the iterator's index by one and returns the character
at the new index. If the resulting index is greater or equal
to getEndIndex(), the current index is reset to getEndIndex() and
a value of DONE is returned.

**Specified by:** next

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the new
position is off the end of the text range.
**Since:** 1.3

- previous

```java
public char previous()
```

Decrements the iterator's index by one and returns the character
at the new index. If the current index is getBeginIndex(), the index
remains at getBeginIndex() and a value of DONE is returned.

**Specified by:** previous

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the current
position is equal to getBeginIndex().
**Since:** 1.3

- setIndex

```java
public char setIndex​(int position)
```

Sets the position to the specified position in the text and returns that
character.

**Specified by:** setIndex

in interface

CharacterIterator
**Parameters:** position

- the position within the text. Valid values range from
getBeginIndex() to getEndIndex(). An IllegalArgumentException is thrown
if an invalid value is supplied.
**Returns:** the character at the specified position or DONE if the specified position is equal to getEndIndex()
**Since:** 1.3

- getBeginIndex

```java
public int getBeginIndex()
```

Returns the start index of the text.

**Specified by:** getBeginIndex

in interface

CharacterIterator
**Returns:** the index at which the text begins.
**Since:** 1.3

- getEndIndex

```java
public int getEndIndex()
```

Returns the end index of the text. This index is the index of the first
character following the end of the text.

**Specified by:** getEndIndex

in interface

CharacterIterator
**Returns:** the index after the last character in the text
**Since:** 1.3

- getIndex

```java
public int getIndex()
```

Returns the current index.

**Specified by:** getIndex

in interface

CharacterIterator
**Returns:** the current index.
**Since:** 1.3

- charAt

```java
public char charAt​(int index)
```

Returns the

char

value at the specified index. An index ranges from zero
to

length() - 1

. The first

char

value of the sequence is at
index zero, the next at index one, and so on, as for array
indexing.

If the

char

value specified by the index is a

surrogate

, the surrogate
value is returned.

**Specified by:** charAt

in interface

CharSequence
**Parameters:** index

- the index of the

char

value to be returned
**Returns:** the specified

char

value
**Since:** 1.6

- length

```java
public int length()
```

Returns the length of this character sequence. The length is the number
of 16-bit

char

s in the sequence.

**Specified by:** length

in interface

CharSequence
**Returns:** the number of

char

s in this sequence
**Since:** 1.6

- subSequence

```java
public
CharSequence
subSequence​(int start,
int end)
```

Returns a

CharSequence

that is a subsequence of this sequence.
The subsequence starts with the

char

value at the specified index and
ends with the

char

value at index

end - 1

. The length
(in

char

s) of the
returned sequence is

end - start

, so if

start == end

then an empty sequence is returned.

**Specified by:** subSequence

in interface

CharSequence
**Parameters:** start

- the start index, inclusive
**Parameters:** end

- the end index, exclusive
**Returns:** the specified subsequence
**Since:** 1.6

- clone

```java
public
Object
clone()
```

Creates a shallow copy.

**Specified by:** clone

in interface

CharacterIterator
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

Field Detail

- array

```java
public char[] array
```

This is the array containing the text of
interest. This array should never be modified;
it is available only for efficiency.

- offset

```java
public int offset
```

This is the offset into the array that
the desired text begins.

- count

```java
public int count
```

This is the number of array elements that
make up the text of interest.

---

#### Field Detail

array

```java
public char[] array
```

This is the array containing the text of
interest. This array should never be modified;
it is available only for efficiency.

---

#### array

public char[] array

This is the array containing the text of
interest. This array should never be modified;
it is available only for efficiency.

offset

```java
public int offset
```

This is the offset into the array that
the desired text begins.

---

#### offset

public int offset

This is the offset into the array that
the desired text begins.

count

```java
public int count
```

This is the number of array elements that
make up the text of interest.

---

#### count

public int count

This is the number of array elements that
make up the text of interest.

Constructor Detail

- Segment

```java
public Segment()
```

Creates a new segment.

- Segment

```java
public Segment​(char[] array,
int offset,
int count)
```

Creates a new segment referring to an existing array.

**Parameters:** array

- the array to refer to
**Parameters:** offset

- the offset into the array
**Parameters:** count

- the number of characters

---

#### Constructor Detail

Segment

```java
public Segment()
```

Creates a new segment.

---

#### Segment

public Segment()

Creates a new segment.

Segment

```java
public Segment​(char[] array,
int offset,
int count)
```

Creates a new segment referring to an existing array.

**Parameters:** array

- the array to refer to
**Parameters:** offset

- the offset into the array
**Parameters:** count

- the number of characters

---

#### Segment

public Segment​(char[] array,
int offset,
int count)

Creates a new segment referring to an existing array.

Method Detail

- setPartialReturn

```java
public void setPartialReturn​(boolean p)
```

Flag to indicate that partial returns are valid. If the flag is true,
an implementation of the interface method Document.getText(position,length,Segment)
should return as much text as possible without making a copy. The default
state of the flag is false which will cause Document.getText(position,length,Segment)
to provide the same return behavior it always had, which may or may not
make a copy of the text depending upon the request.

**Parameters:** p

- whether or not partial returns are valid.
**Since:** 1.4

- isPartialReturn

```java
public boolean isPartialReturn()
```

Flag to indicate that partial returns are valid.

**Returns:** whether or not partial returns are valid.
**Since:** 1.4

- toString

```java
public
String
toString()
```

Converts a segment into a String.

**Specified by:** toString

in interface

CharSequence
**Overrides:** toString

in class

Object
**Returns:** the string

- first

```java
public char first()
```

Sets the position to getBeginIndex() and returns the character at that
position.

**Specified by:** first

in interface

CharacterIterator
**Returns:** the first character in the text, or DONE if the text is empty
**Since:** 1.3
**See Also:** getBeginIndex()

- last

```java
public char last()
```

Sets the position to getEndIndex()-1 (getEndIndex() if the text is empty)
and returns the character at that position.

**Specified by:** last

in interface

CharacterIterator
**Returns:** the last character in the text, or DONE if the text is empty
**Since:** 1.3
**See Also:** getEndIndex()

- current

```java
public char current()
```

Gets the character at the current position (as returned by getIndex()).

**Specified by:** current

in interface

CharacterIterator
**Returns:** the character at the current position or DONE if the current
position is off the end of the text.
**Since:** 1.3
**See Also:** getIndex()

- next

```java
public char next()
```

Increments the iterator's index by one and returns the character
at the new index. If the resulting index is greater or equal
to getEndIndex(), the current index is reset to getEndIndex() and
a value of DONE is returned.

**Specified by:** next

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the new
position is off the end of the text range.
**Since:** 1.3

- previous

```java
public char previous()
```

Decrements the iterator's index by one and returns the character
at the new index. If the current index is getBeginIndex(), the index
remains at getBeginIndex() and a value of DONE is returned.

**Specified by:** previous

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the current
position is equal to getBeginIndex().
**Since:** 1.3

- setIndex

```java
public char setIndex​(int position)
```

Sets the position to the specified position in the text and returns that
character.

**Specified by:** setIndex

in interface

CharacterIterator
**Parameters:** position

- the position within the text. Valid values range from
getBeginIndex() to getEndIndex(). An IllegalArgumentException is thrown
if an invalid value is supplied.
**Returns:** the character at the specified position or DONE if the specified position is equal to getEndIndex()
**Since:** 1.3

- getBeginIndex

```java
public int getBeginIndex()
```

Returns the start index of the text.

**Specified by:** getBeginIndex

in interface

CharacterIterator
**Returns:** the index at which the text begins.
**Since:** 1.3

- getEndIndex

```java
public int getEndIndex()
```

Returns the end index of the text. This index is the index of the first
character following the end of the text.

**Specified by:** getEndIndex

in interface

CharacterIterator
**Returns:** the index after the last character in the text
**Since:** 1.3

- getIndex

```java
public int getIndex()
```

Returns the current index.

**Specified by:** getIndex

in interface

CharacterIterator
**Returns:** the current index.
**Since:** 1.3

- charAt

```java
public char charAt​(int index)
```

Returns the

char

value at the specified index. An index ranges from zero
to

length() - 1

. The first

char

value of the sequence is at
index zero, the next at index one, and so on, as for array
indexing.

If the

char

value specified by the index is a

surrogate

, the surrogate
value is returned.

**Specified by:** charAt

in interface

CharSequence
**Parameters:** index

- the index of the

char

value to be returned
**Returns:** the specified

char

value
**Since:** 1.6

- length

```java
public int length()
```

Returns the length of this character sequence. The length is the number
of 16-bit

char

s in the sequence.

**Specified by:** length

in interface

CharSequence
**Returns:** the number of

char

s in this sequence
**Since:** 1.6

- subSequence

```java
public
CharSequence
subSequence​(int start,
int end)
```

Returns a

CharSequence

that is a subsequence of this sequence.
The subsequence starts with the

char

value at the specified index and
ends with the

char

value at index

end - 1

. The length
(in

char

s) of the
returned sequence is

end - start

, so if

start == end

then an empty sequence is returned.

**Specified by:** subSequence

in interface

CharSequence
**Parameters:** start

- the start index, inclusive
**Parameters:** end

- the end index, exclusive
**Returns:** the specified subsequence
**Since:** 1.6

- clone

```java
public
Object
clone()
```

Creates a shallow copy.

**Specified by:** clone

in interface

CharacterIterator
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

---

#### Method Detail

setPartialReturn

```java
public void setPartialReturn​(boolean p)
```

Flag to indicate that partial returns are valid. If the flag is true,
an implementation of the interface method Document.getText(position,length,Segment)
should return as much text as possible without making a copy. The default
state of the flag is false which will cause Document.getText(position,length,Segment)
to provide the same return behavior it always had, which may or may not
make a copy of the text depending upon the request.

**Parameters:** p

- whether or not partial returns are valid.
**Since:** 1.4

---

#### setPartialReturn

public void setPartialReturn​(boolean p)

Flag to indicate that partial returns are valid. If the flag is true,
an implementation of the interface method Document.getText(position,length,Segment)
should return as much text as possible without making a copy. The default
state of the flag is false which will cause Document.getText(position,length,Segment)
to provide the same return behavior it always had, which may or may not
make a copy of the text depending upon the request.

isPartialReturn

```java
public boolean isPartialReturn()
```

Flag to indicate that partial returns are valid.

**Returns:** whether or not partial returns are valid.
**Since:** 1.4

---

#### isPartialReturn

public boolean isPartialReturn()

Flag to indicate that partial returns are valid.

toString

```java
public
String
toString()
```

Converts a segment into a String.

**Specified by:** toString

in interface

CharSequence
**Overrides:** toString

in class

Object
**Returns:** the string

---

#### toString

public

String

toString()

Converts a segment into a String.

first

```java
public char first()
```

Sets the position to getBeginIndex() and returns the character at that
position.

**Specified by:** first

in interface

CharacterIterator
**Returns:** the first character in the text, or DONE if the text is empty
**Since:** 1.3
**See Also:** getBeginIndex()

---

#### first

public char first()

Sets the position to getBeginIndex() and returns the character at that
position.

last

```java
public char last()
```

Sets the position to getEndIndex()-1 (getEndIndex() if the text is empty)
and returns the character at that position.

**Specified by:** last

in interface

CharacterIterator
**Returns:** the last character in the text, or DONE if the text is empty
**Since:** 1.3
**See Also:** getEndIndex()

---

#### last

public char last()

Sets the position to getEndIndex()-1 (getEndIndex() if the text is empty)
and returns the character at that position.

current

```java
public char current()
```

Gets the character at the current position (as returned by getIndex()).

**Specified by:** current

in interface

CharacterIterator
**Returns:** the character at the current position or DONE if the current
position is off the end of the text.
**Since:** 1.3
**See Also:** getIndex()

---

#### current

public char current()

Gets the character at the current position (as returned by getIndex()).

next

```java
public char next()
```

Increments the iterator's index by one and returns the character
at the new index. If the resulting index is greater or equal
to getEndIndex(), the current index is reset to getEndIndex() and
a value of DONE is returned.

**Specified by:** next

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the new
position is off the end of the text range.
**Since:** 1.3

---

#### next

public char next()

Increments the iterator's index by one and returns the character
at the new index. If the resulting index is greater or equal
to getEndIndex(), the current index is reset to getEndIndex() and
a value of DONE is returned.

previous

```java
public char previous()
```

Decrements the iterator's index by one and returns the character
at the new index. If the current index is getBeginIndex(), the index
remains at getBeginIndex() and a value of DONE is returned.

**Specified by:** previous

in interface

CharacterIterator
**Returns:** the character at the new position or DONE if the current
position is equal to getBeginIndex().
**Since:** 1.3

---

#### previous

public char previous()

Decrements the iterator's index by one and returns the character
at the new index. If the current index is getBeginIndex(), the index
remains at getBeginIndex() and a value of DONE is returned.

setIndex

```java
public char setIndex​(int position)
```

Sets the position to the specified position in the text and returns that
character.

**Specified by:** setIndex

in interface

CharacterIterator
**Parameters:** position

- the position within the text. Valid values range from
getBeginIndex() to getEndIndex(). An IllegalArgumentException is thrown
if an invalid value is supplied.
**Returns:** the character at the specified position or DONE if the specified position is equal to getEndIndex()
**Since:** 1.3

---

#### setIndex

public char setIndex​(int position)

Sets the position to the specified position in the text and returns that
character.

getBeginIndex

```java
public int getBeginIndex()
```

Returns the start index of the text.

**Specified by:** getBeginIndex

in interface

CharacterIterator
**Returns:** the index at which the text begins.
**Since:** 1.3

---

#### getBeginIndex

public int getBeginIndex()

Returns the start index of the text.

getEndIndex

```java
public int getEndIndex()
```

Returns the end index of the text. This index is the index of the first
character following the end of the text.

**Specified by:** getEndIndex

in interface

CharacterIterator
**Returns:** the index after the last character in the text
**Since:** 1.3

---

#### getEndIndex

public int getEndIndex()

Returns the end index of the text. This index is the index of the first
character following the end of the text.

getIndex

```java
public int getIndex()
```

Returns the current index.

**Specified by:** getIndex

in interface

CharacterIterator
**Returns:** the current index.
**Since:** 1.3

---

#### getIndex

public int getIndex()

Returns the current index.

charAt

```java
public char charAt​(int index)
```

Returns the

char

value at the specified index. An index ranges from zero
to

length() - 1

. The first

char

value of the sequence is at
index zero, the next at index one, and so on, as for array
indexing.

If the

char

value specified by the index is a

surrogate

, the surrogate
value is returned.

**Specified by:** charAt

in interface

CharSequence
**Parameters:** index

- the index of the

char

value to be returned
**Returns:** the specified

char

value
**Since:** 1.6

---

#### charAt

public char charAt​(int index)

Returns the

char

value at the specified index. An index ranges from zero
to

length() - 1

. The first

char

value of the sequence is at
index zero, the next at index one, and so on, as for array
indexing.

If the

char

value specified by the index is a

surrogate

, the surrogate
value is returned.

If the

char

value specified by the index is a

surrogate

, the surrogate
value is returned.

length

```java
public int length()
```

Returns the length of this character sequence. The length is the number
of 16-bit

char

s in the sequence.

**Specified by:** length

in interface

CharSequence
**Returns:** the number of

char

s in this sequence
**Since:** 1.6

---

#### length

public int length()

Returns the length of this character sequence. The length is the number
of 16-bit

char

s in the sequence.

subSequence

```java
public
CharSequence
subSequence​(int start,
int end)
```

Returns a

CharSequence

that is a subsequence of this sequence.
The subsequence starts with the

char

value at the specified index and
ends with the

char

value at index

end - 1

. The length
(in

char

s) of the
returned sequence is

end - start

, so if

start == end

then an empty sequence is returned.

**Specified by:** subSequence

in interface

CharSequence
**Parameters:** start

- the start index, inclusive
**Parameters:** end

- the end index, exclusive
**Returns:** the specified subsequence
**Since:** 1.6

---

#### subSequence

public

CharSequence

subSequence​(int start,
int end)

Returns a

CharSequence

that is a subsequence of this sequence.
The subsequence starts with the

char

value at the specified index and
ends with the

char

value at index

end - 1

. The length
(in

char

s) of the
returned sequence is

end - start

, so if

start == end

then an empty sequence is returned.

clone

```java
public
Object
clone()
```

Creates a shallow copy.

**Specified by:** clone

in interface

CharacterIterator
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a shallow copy.

---

