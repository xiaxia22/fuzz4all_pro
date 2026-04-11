# Interface AbstractDocument.Content

**Source:** `java.desktop\javax\swing\text\AbstractDocument.Content.html`

### Class Description

```java
public static interface
AbstractDocument.Content
```

Interface to describe a sequence of character content that
can be edited. Implementations may or may not support a
history mechanism which will be reflected by whether or not
mutations return an UndoableEdit implementation.

**All Known Implementing Classes:** GapContent

,

StringContent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Position
createPosition​(int offset)
throws
BadLocationException

Creates a position within the content that will
track change as the content is mutated.

**Parameters:**
- offset

- the offset in the content >= 0

**Returns:**
- a Position

**Throws:**
- BadLocationException

- for an invalid offset

---

#### int length()

Current length of the sequence of character content.

**Returns:**
- the length >= 0

---

#### UndoableEdit
insertString​(int where,

String
str)
throws
BadLocationException

Inserts a string of characters into the sequence.

**Parameters:**
- where

- offset into the sequence to make the insertion >= 0
- str

- string to insert

**Returns:**
- if the implementation supports a history mechanism,
a reference to an

Edit

implementation will be returned,
otherwise returns

null

**Throws:**
- BadLocationException

- thrown if the area covered by
the arguments is not contained in the character sequence

---

#### UndoableEdit
remove​(int where,
int nitems)
throws
BadLocationException

Removes some portion of the sequence.

**Parameters:**
- where

- The offset into the sequence to make the
insertion >= 0.
- nitems

- The number of items in the sequence to remove >= 0.

**Returns:**
- If the implementation supports a history mechanism,
a reference to an Edit implementation will be returned,
otherwise null.

**Throws:**
- BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

---

#### String
getString​(int where,
int len)
throws
BadLocationException

Fetches a string of characters contained in the sequence.

**Parameters:**
- where

- Offset into the sequence to fetch >= 0.
- len

- number of characters to copy >= 0.

**Returns:**
- the string

**Throws:**
- BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

---

#### void getChars​(int where,
int len,

Segment
txt)
throws
BadLocationException

Gets a sequence of characters and copies them into a Segment.

**Parameters:**
- where

- the starting offset >= 0
- len

- the number of characters >= 0
- txt

- the target location to copy into

**Throws:**
- BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

---

### Additional Sections

#### Interface AbstractDocument.Content

**All Known Implementing Classes:** GapContent

,

StringContent

**Enclosing class:** AbstractDocument

```java
public static interface
AbstractDocument.Content
```

Interface to describe a sequence of character content that
can be edited. Implementations may or may not support a
history mechanism which will be reflected by whether or not
mutations return an UndoableEdit implementation.

**See Also:** AbstractDocument

public static interface

AbstractDocument.Content

Interface to describe a sequence of character content that
can be edited. Implementations may or may not support a
history mechanism which will be reflected by whether or not
mutations return an UndoableEdit implementation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Position

createPosition

​(int offset)

Creates a position within the content that will
track change as the content is mutated.

void

getChars

​(int where,
int len,

Segment

txt)

Gets a sequence of characters and copies them into a Segment.

String

getString

​(int where,
int len)

Fetches a string of characters contained in the sequence.

UndoableEdit

insertString

​(int where,

String

str)

Inserts a string of characters into the sequence.

int

length

()

Current length of the sequence of character content.

UndoableEdit

remove

​(int where,
int nitems)

Removes some portion of the sequence.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Position

createPosition

​(int offset)

Creates a position within the content that will
track change as the content is mutated.

void

getChars

​(int where,
int len,

Segment

txt)

Gets a sequence of characters and copies them into a Segment.

String

getString

​(int where,
int len)

Fetches a string of characters contained in the sequence.

UndoableEdit

insertString

​(int where,

String

str)

Inserts a string of characters into the sequence.

int

length

()

Current length of the sequence of character content.

UndoableEdit

remove

​(int where,
int nitems)

Removes some portion of the sequence.

---

#### Method Summary

Creates a position within the content that will
track change as the content is mutated.

Gets a sequence of characters and copies them into a Segment.

Fetches a string of characters contained in the sequence.

Inserts a string of characters into the sequence.

Current length of the sequence of character content.

Removes some portion of the sequence.

============ METHOD DETAIL ==========

- Method Detail

- createPosition

```java
Position
createPosition​(int offset)
throws
BadLocationException
```

Creates a position within the content that will
track change as the content is mutated.

**Parameters:** offset

- the offset in the content >= 0
**Returns:** a Position
**Throws:** BadLocationException

- for an invalid offset

- length

```java
int length()
```

Current length of the sequence of character content.

**Returns:** the length >= 0

- insertString

```java
UndoableEdit
insertString​(int where,

String
str)
throws
BadLocationException
```

Inserts a string of characters into the sequence.

**Parameters:** where

- offset into the sequence to make the insertion >= 0
**Parameters:** str

- string to insert
**Returns:** if the implementation supports a history mechanism,
a reference to an

Edit

implementation will be returned,
otherwise returns

null
**Throws:** BadLocationException

- thrown if the area covered by
the arguments is not contained in the character sequence

- remove

```java
UndoableEdit
remove​(int where,
int nitems)
throws
BadLocationException
```

Removes some portion of the sequence.

**Parameters:** where

- The offset into the sequence to make the
insertion >= 0.
**Parameters:** nitems

- The number of items in the sequence to remove >= 0.
**Returns:** If the implementation supports a history mechanism,
a reference to an Edit implementation will be returned,
otherwise null.
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

- getString

```java
String
getString​(int where,
int len)
throws
BadLocationException
```

Fetches a string of characters contained in the sequence.

**Parameters:** where

- Offset into the sequence to fetch >= 0.
**Parameters:** len

- number of characters to copy >= 0.
**Returns:** the string
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

- getChars

```java
void getChars​(int where,
int len,

Segment
txt)
throws
BadLocationException
```

Gets a sequence of characters and copies them into a Segment.

**Parameters:** where

- the starting offset >= 0
**Parameters:** len

- the number of characters >= 0
**Parameters:** txt

- the target location to copy into
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

Method Detail

- createPosition

```java
Position
createPosition​(int offset)
throws
BadLocationException
```

Creates a position within the content that will
track change as the content is mutated.

**Parameters:** offset

- the offset in the content >= 0
**Returns:** a Position
**Throws:** BadLocationException

- for an invalid offset

- length

```java
int length()
```

Current length of the sequence of character content.

**Returns:** the length >= 0

- insertString

```java
UndoableEdit
insertString​(int where,

String
str)
throws
BadLocationException
```

Inserts a string of characters into the sequence.

**Parameters:** where

- offset into the sequence to make the insertion >= 0
**Parameters:** str

- string to insert
**Returns:** if the implementation supports a history mechanism,
a reference to an

Edit

implementation will be returned,
otherwise returns

null
**Throws:** BadLocationException

- thrown if the area covered by
the arguments is not contained in the character sequence

- remove

```java
UndoableEdit
remove​(int where,
int nitems)
throws
BadLocationException
```

Removes some portion of the sequence.

**Parameters:** where

- The offset into the sequence to make the
insertion >= 0.
**Parameters:** nitems

- The number of items in the sequence to remove >= 0.
**Returns:** If the implementation supports a history mechanism,
a reference to an Edit implementation will be returned,
otherwise null.
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

- getString

```java
String
getString​(int where,
int len)
throws
BadLocationException
```

Fetches a string of characters contained in the sequence.

**Parameters:** where

- Offset into the sequence to fetch >= 0.
**Parameters:** len

- number of characters to copy >= 0.
**Returns:** the string
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

- getChars

```java
void getChars​(int where,
int len,

Segment
txt)
throws
BadLocationException
```

Gets a sequence of characters and copies them into a Segment.

**Parameters:** where

- the starting offset >= 0
**Parameters:** len

- the number of characters >= 0
**Parameters:** txt

- the target location to copy into
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

---

#### Method Detail

createPosition

```java
Position
createPosition​(int offset)
throws
BadLocationException
```

Creates a position within the content that will
track change as the content is mutated.

**Parameters:** offset

- the offset in the content >= 0
**Returns:** a Position
**Throws:** BadLocationException

- for an invalid offset

---

#### createPosition

Position

createPosition​(int offset)
throws

BadLocationException

Creates a position within the content that will
track change as the content is mutated.

length

```java
int length()
```

Current length of the sequence of character content.

**Returns:** the length >= 0

---

#### length

int length()

Current length of the sequence of character content.

insertString

```java
UndoableEdit
insertString​(int where,

String
str)
throws
BadLocationException
```

Inserts a string of characters into the sequence.

**Parameters:** where

- offset into the sequence to make the insertion >= 0
**Parameters:** str

- string to insert
**Returns:** if the implementation supports a history mechanism,
a reference to an

Edit

implementation will be returned,
otherwise returns

null
**Throws:** BadLocationException

- thrown if the area covered by
the arguments is not contained in the character sequence

---

#### insertString

UndoableEdit

insertString​(int where,

String

str)
throws

BadLocationException

Inserts a string of characters into the sequence.

remove

```java
UndoableEdit
remove​(int where,
int nitems)
throws
BadLocationException
```

Removes some portion of the sequence.

**Parameters:** where

- The offset into the sequence to make the
insertion >= 0.
**Parameters:** nitems

- The number of items in the sequence to remove >= 0.
**Returns:** If the implementation supports a history mechanism,
a reference to an Edit implementation will be returned,
otherwise null.
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

---

#### remove

UndoableEdit

remove​(int where,
int nitems)
throws

BadLocationException

Removes some portion of the sequence.

getString

```java
String
getString​(int where,
int len)
throws
BadLocationException
```

Fetches a string of characters contained in the sequence.

**Parameters:** where

- Offset into the sequence to fetch >= 0.
**Parameters:** len

- number of characters to copy >= 0.
**Returns:** the string
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

---

#### getString

String

getString​(int where,
int len)
throws

BadLocationException

Fetches a string of characters contained in the sequence.

getChars

```java
void getChars​(int where,
int len,

Segment
txt)
throws
BadLocationException
```

Gets a sequence of characters and copies them into a Segment.

**Parameters:** where

- the starting offset >= 0
**Parameters:** len

- the number of characters >= 0
**Parameters:** txt

- the target location to copy into
**Throws:** BadLocationException

- Thrown if the area covered by
the arguments is not contained in the character sequence.

---

#### getChars

void getChars​(int where,
int len,

Segment

txt)
throws

BadLocationException

Gets a sequence of characters and copies them into a Segment.

---

