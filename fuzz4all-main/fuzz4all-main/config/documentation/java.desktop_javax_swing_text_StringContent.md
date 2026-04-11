# Class StringContent

**Source:** `java.desktop\javax\swing\text\StringContent.html`

### Class Description

```java
public final class
StringContent

extends
Object

implements
AbstractDocument.Content
,
Serializable
```

An implementation of the AbstractDocument.Content interface that is
a brute force implementation that is useful for relatively small
documents and/or debugging. It manages the character content
as a simple character array. It is also quite inefficient.

It is generally recommended that the gap buffer or piece table
implementations be used instead. This buffer does not scale up
to large sizes.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

AbstractDocument.Content

---

### Field Details

*No entries found.*

### Constructor Details

#### public StringContent()

Creates a new StringContent object. Initial size defaults to 10.

---

#### public StringContent​(int initialLength)

Creates a new StringContent object, with the initial
size specified. If the length is < 1, a size of 1 is used.

**Parameters:**
- initialLength

- the initial size

---

### Method Details

#### public int length()

Returns the length of the content.

**Specified by:**
- length

in interface

AbstractDocument.Content

**Returns:**
- the length >= 1

**See Also:**
- AbstractDocument.Content.length()

---

#### public
UndoableEdit
insertString​(int where,

String
str)
throws
BadLocationException

Inserts a string into the content.

**Specified by:**
- insertString

in interface

AbstractDocument.Content

**Parameters:**
- where

- the starting position >= 0 && < length()
- str

- the non-null string to insert

**Returns:**
- an UndoableEdit object for undoing

**Throws:**
- BadLocationException

- if the specified position is invalid

**See Also:**
- AbstractDocument.Content.insertString(int, java.lang.String)

---

#### public
UndoableEdit
remove​(int where,
int nitems)
throws
BadLocationException

Removes part of the content. where + nitems must be < length().

**Specified by:**
- remove

in interface

AbstractDocument.Content

**Parameters:**
- where

- the starting position >= 0
- nitems

- the number of characters to remove >= 0

**Returns:**
- an UndoableEdit object for undoing

**Throws:**
- BadLocationException

- if the specified position is invalid

**See Also:**
- AbstractDocument.Content.remove(int, int)

---

#### public
String
getString​(int where,
int len)
throws
BadLocationException

Retrieves a portion of the content. where + len must be <= length().

**Specified by:**
- getString

in interface

AbstractDocument.Content

**Parameters:**
- where

- the starting position >= 0
- len

- the length to retrieve >= 0

**Returns:**
- a string representing the content; may be empty

**Throws:**
- BadLocationException

- if the specified position is invalid

**See Also:**
- AbstractDocument.Content.getString(int, int)

---

#### public void getChars​(int where,
int len,

Segment
chars)
throws
BadLocationException

Retrieves a portion of the content. where + len must be <= length()

**Specified by:**
- getChars

in interface

AbstractDocument.Content

**Parameters:**
- where

- the starting position >= 0
- len

- the number of characters to retrieve >= 0
- chars

- the Segment object to return the characters in

**Throws:**
- BadLocationException

- if the specified position is invalid

**See Also:**
- AbstractDocument.Content.getChars(int, int, javax.swing.text.Segment)

---

#### public
Position
createPosition​(int offset)
throws
BadLocationException

Creates a position within the content that will
track change as the content is mutated.

**Specified by:**
- createPosition

in interface

AbstractDocument.Content

**Parameters:**
- offset

- the offset to create a position for >= 0

**Returns:**
- the position

**Throws:**
- BadLocationException

- if the specified position is invalid

---

#### protected
Vector
getPositionsInRange​(
Vector
v,
int offset,
int length)

Returns a Vector containing instances of UndoPosRef for the
Positions in the range

offset

to

offset

+

length

.
If

v

is not null the matching Positions are placed in
there. The vector with the resulting Positions are returned.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:**
- v

- the Vector to use, with a new one created on null
- offset

- the starting offset >= 0
- length

- the length >= 0

**Returns:**
- the set of instances

---

#### protected void updateUndoPositions​(
Vector
positions)

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:**
- positions

- the positions of the instances

---

### Additional Sections

#### Class StringContent

java.lang.Object

- javax.swing.text.StringContent

javax.swing.text.StringContent

**All Implemented Interfaces:** Serializable

,

AbstractDocument.Content

```java
public final class
StringContent

extends
Object

implements
AbstractDocument.Content
,
Serializable
```

An implementation of the AbstractDocument.Content interface that is
a brute force implementation that is useful for relatively small
documents and/or debugging. It manages the character content
as a simple character array. It is also quite inefficient.

It is generally recommended that the gap buffer or piece table
implementations be used instead. This buffer does not scale up
to large sizes.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public final class

StringContent

extends

Object

implements

AbstractDocument.Content

,

Serializable

An implementation of the AbstractDocument.Content interface that is
a brute force implementation that is useful for relatively small
documents and/or debugging. It manages the character content
as a simple character array. It is also quite inefficient.

It is generally recommended that the gap buffer or piece table
implementations be used instead. This buffer does not scale up
to large sizes.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

It is generally recommended that the gap buffer or piece table
implementations be used instead. This buffer does not scale up
to large sizes.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringContent

()

Creates a new StringContent object.

StringContent

​(int initialLength)

Creates a new StringContent object, with the initial
size specified.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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

chars)

Retrieves a portion of the content.

protected

Vector

getPositionsInRange

​(

Vector

v,
int offset,
int length)

Returns a Vector containing instances of UndoPosRef for the
Positions in the range

offset

to

offset

+

length

.

String

getString

​(int where,
int len)

Retrieves a portion of the content.

UndoableEdit

insertString

​(int where,

String

str)

Inserts a string into the content.

int

length

()

Returns the length of the content.

UndoableEdit

remove

​(int where,
int nitems)

Removes part of the content.

protected void

updateUndoPositions

​(

Vector

positions)

Resets the location for all the UndoPosRef instances
in

positions

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

StringContent

()

Creates a new StringContent object.

StringContent

​(int initialLength)

Creates a new StringContent object, with the initial
size specified.

---

#### Constructor Summary

Creates a new StringContent object.

Creates a new StringContent object, with the initial
size specified.

Method Summary

All Methods

Instance Methods

Concrete Methods

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

chars)

Retrieves a portion of the content.

protected

Vector

getPositionsInRange

​(

Vector

v,
int offset,
int length)

Returns a Vector containing instances of UndoPosRef for the
Positions in the range

offset

to

offset

+

length

.

String

getString

​(int where,
int len)

Retrieves a portion of the content.

UndoableEdit

insertString

​(int where,

String

str)

Inserts a string into the content.

int

length

()

Returns the length of the content.

UndoableEdit

remove

​(int where,
int nitems)

Removes part of the content.

protected void

updateUndoPositions

​(

Vector

positions)

Resets the location for all the UndoPosRef instances
in

positions

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

Creates a position within the content that will
track change as the content is mutated.

Retrieves a portion of the content.

Returns a Vector containing instances of UndoPosRef for the
Positions in the range

offset

to

offset

+

length

.

Inserts a string into the content.

Returns the length of the content.

Removes part of the content.

Resets the location for all the UndoPosRef instances
in

positions

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

- StringContent

```java
public StringContent()
```

Creates a new StringContent object. Initial size defaults to 10.

- StringContent

```java
public StringContent​(int initialLength)
```

Creates a new StringContent object, with the initial
size specified. If the length is < 1, a size of 1 is used.

**Parameters:** initialLength

- the initial size

============ METHOD DETAIL ==========

- Method Detail

- length

```java
public int length()
```

Returns the length of the content.

**Specified by:** length

in interface

AbstractDocument.Content
**Returns:** the length >= 1
**See Also:** AbstractDocument.Content.length()

- insertString

```java
public
UndoableEdit
insertString​(int where,

String
str)
throws
BadLocationException
```

Inserts a string into the content.

**Specified by:** insertString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0 && < length()
**Parameters:** str

- the non-null string to insert
**Returns:** an UndoableEdit object for undoing
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.insertString(int, java.lang.String)

- remove

```java
public
UndoableEdit
remove​(int where,
int nitems)
throws
BadLocationException
```

Removes part of the content. where + nitems must be < length().

**Specified by:** remove

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** nitems

- the number of characters to remove >= 0
**Returns:** an UndoableEdit object for undoing
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.remove(int, int)

- getString

```java
public
String
getString​(int where,
int len)
throws
BadLocationException
```

Retrieves a portion of the content. where + len must be <= length().

**Specified by:** getString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the length to retrieve >= 0
**Returns:** a string representing the content; may be empty
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.getString(int, int)

- getChars

```java
public void getChars​(int where,
int len,

Segment
chars)
throws
BadLocationException
```

Retrieves a portion of the content. where + len must be <= length()

**Specified by:** getChars

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the number of characters to retrieve >= 0
**Parameters:** chars

- the Segment object to return the characters in
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.getChars(int, int, javax.swing.text.Segment)

- createPosition

```java
public
Position
createPosition​(int offset)
throws
BadLocationException
```

Creates a position within the content that will
track change as the content is mutated.

**Specified by:** createPosition

in interface

AbstractDocument.Content
**Parameters:** offset

- the offset to create a position for >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the specified position is invalid

- getPositionsInRange

```java
protected
Vector
getPositionsInRange​(
Vector
v,
int offset,
int length)
```

Returns a Vector containing instances of UndoPosRef for the
Positions in the range

offset

to

offset

+

length

.
If

v

is not null the matching Positions are placed in
there. The vector with the resulting Positions are returned.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** v

- the Vector to use, with a new one created on null
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the length >= 0
**Returns:** the set of instances

- updateUndoPositions

```java
protected void updateUndoPositions​(
Vector
positions)
```

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** positions

- the positions of the instances

Constructor Detail

- StringContent

```java
public StringContent()
```

Creates a new StringContent object. Initial size defaults to 10.

- StringContent

```java
public StringContent​(int initialLength)
```

Creates a new StringContent object, with the initial
size specified. If the length is < 1, a size of 1 is used.

**Parameters:** initialLength

- the initial size

---

#### Constructor Detail

StringContent

```java
public StringContent()
```

Creates a new StringContent object. Initial size defaults to 10.

---

#### StringContent

public StringContent()

Creates a new StringContent object. Initial size defaults to 10.

StringContent

```java
public StringContent​(int initialLength)
```

Creates a new StringContent object, with the initial
size specified. If the length is < 1, a size of 1 is used.

**Parameters:** initialLength

- the initial size

---

#### StringContent

public StringContent​(int initialLength)

Creates a new StringContent object, with the initial
size specified. If the length is < 1, a size of 1 is used.

Method Detail

- length

```java
public int length()
```

Returns the length of the content.

**Specified by:** length

in interface

AbstractDocument.Content
**Returns:** the length >= 1
**See Also:** AbstractDocument.Content.length()

- insertString

```java
public
UndoableEdit
insertString​(int where,

String
str)
throws
BadLocationException
```

Inserts a string into the content.

**Specified by:** insertString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0 && < length()
**Parameters:** str

- the non-null string to insert
**Returns:** an UndoableEdit object for undoing
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.insertString(int, java.lang.String)

- remove

```java
public
UndoableEdit
remove​(int where,
int nitems)
throws
BadLocationException
```

Removes part of the content. where + nitems must be < length().

**Specified by:** remove

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** nitems

- the number of characters to remove >= 0
**Returns:** an UndoableEdit object for undoing
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.remove(int, int)

- getString

```java
public
String
getString​(int where,
int len)
throws
BadLocationException
```

Retrieves a portion of the content. where + len must be <= length().

**Specified by:** getString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the length to retrieve >= 0
**Returns:** a string representing the content; may be empty
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.getString(int, int)

- getChars

```java
public void getChars​(int where,
int len,

Segment
chars)
throws
BadLocationException
```

Retrieves a portion of the content. where + len must be <= length()

**Specified by:** getChars

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the number of characters to retrieve >= 0
**Parameters:** chars

- the Segment object to return the characters in
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.getChars(int, int, javax.swing.text.Segment)

- createPosition

```java
public
Position
createPosition​(int offset)
throws
BadLocationException
```

Creates a position within the content that will
track change as the content is mutated.

**Specified by:** createPosition

in interface

AbstractDocument.Content
**Parameters:** offset

- the offset to create a position for >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the specified position is invalid

- getPositionsInRange

```java
protected
Vector
getPositionsInRange​(
Vector
v,
int offset,
int length)
```

Returns a Vector containing instances of UndoPosRef for the
Positions in the range

offset

to

offset

+

length

.
If

v

is not null the matching Positions are placed in
there. The vector with the resulting Positions are returned.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** v

- the Vector to use, with a new one created on null
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the length >= 0
**Returns:** the set of instances

- updateUndoPositions

```java
protected void updateUndoPositions​(
Vector
positions)
```

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** positions

- the positions of the instances

---

#### Method Detail

length

```java
public int length()
```

Returns the length of the content.

**Specified by:** length

in interface

AbstractDocument.Content
**Returns:** the length >= 1
**See Also:** AbstractDocument.Content.length()

---

#### length

public int length()

Returns the length of the content.

insertString

```java
public
UndoableEdit
insertString​(int where,

String
str)
throws
BadLocationException
```

Inserts a string into the content.

**Specified by:** insertString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0 && < length()
**Parameters:** str

- the non-null string to insert
**Returns:** an UndoableEdit object for undoing
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.insertString(int, java.lang.String)

---

#### insertString

public

UndoableEdit

insertString​(int where,

String

str)
throws

BadLocationException

Inserts a string into the content.

remove

```java
public
UndoableEdit
remove​(int where,
int nitems)
throws
BadLocationException
```

Removes part of the content. where + nitems must be < length().

**Specified by:** remove

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** nitems

- the number of characters to remove >= 0
**Returns:** an UndoableEdit object for undoing
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.remove(int, int)

---

#### remove

public

UndoableEdit

remove​(int where,
int nitems)
throws

BadLocationException

Removes part of the content. where + nitems must be < length().

getString

```java
public
String
getString​(int where,
int len)
throws
BadLocationException
```

Retrieves a portion of the content. where + len must be <= length().

**Specified by:** getString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the length to retrieve >= 0
**Returns:** a string representing the content; may be empty
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.getString(int, int)

---

#### getString

public

String

getString​(int where,
int len)
throws

BadLocationException

Retrieves a portion of the content. where + len must be <= length().

getChars

```java
public void getChars​(int where,
int len,

Segment
chars)
throws
BadLocationException
```

Retrieves a portion of the content. where + len must be <= length()

**Specified by:** getChars

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the number of characters to retrieve >= 0
**Parameters:** chars

- the Segment object to return the characters in
**Throws:** BadLocationException

- if the specified position is invalid
**See Also:** AbstractDocument.Content.getChars(int, int, javax.swing.text.Segment)

---

#### getChars

public void getChars​(int where,
int len,

Segment

chars)
throws

BadLocationException

Retrieves a portion of the content. where + len must be <= length()

createPosition

```java
public
Position
createPosition​(int offset)
throws
BadLocationException
```

Creates a position within the content that will
track change as the content is mutated.

**Specified by:** createPosition

in interface

AbstractDocument.Content
**Parameters:** offset

- the offset to create a position for >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the specified position is invalid

---

#### createPosition

public

Position

createPosition​(int offset)
throws

BadLocationException

Creates a position within the content that will
track change as the content is mutated.

getPositionsInRange

```java
protected
Vector
getPositionsInRange​(
Vector
v,
int offset,
int length)
```

Returns a Vector containing instances of UndoPosRef for the
Positions in the range

offset

to

offset

+

length

.
If

v

is not null the matching Positions are placed in
there. The vector with the resulting Positions are returned.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** v

- the Vector to use, with a new one created on null
**Parameters:** offset

- the starting offset >= 0
**Parameters:** length

- the length >= 0
**Returns:** the set of instances

---

#### getPositionsInRange

protected

Vector

getPositionsInRange​(

Vector

v,
int offset,
int length)

Returns a Vector containing instances of UndoPosRef for the
Positions in the range

offset

to

offset

+

length

.
If

v

is not null the matching Positions are placed in
there. The vector with the resulting Positions are returned.

This is meant for internal usage, and is generally not of interest
to subclasses.

This is meant for internal usage, and is generally not of interest
to subclasses.

updateUndoPositions

```java
protected void updateUndoPositions​(
Vector
positions)
```

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** positions

- the positions of the instances

---

#### updateUndoPositions

protected void updateUndoPositions​(

Vector

positions)

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

This is meant for internal usage, and is generally not of interest
to subclasses.

---

