# Class GapContent

**Source:** `java.desktop\javax\swing\text\GapContent.html`

### Class Description

```java
public class
GapContent

extends
Object

implements
AbstractDocument.Content
,
Serializable
```

An implementation of the AbstractDocument.Content interface
implemented using a gapped buffer similar to that used by emacs.
The underlying storage is a array of unicode characters with
a gap somewhere. The gap is moved to the location of changes
to take advantage of common behavior where most changes are
in the same location. Changes that occur at a gap boundary are
generally cheap and moving the gap is generally cheaper than
moving the array contents directly to accommodate the change.

The positions tracking change are also generally cheap to
maintain. The Position implementations (marks) store the array
index and can easily calculate the sequential position from
the current gap location. Changes only require update to the
the marks between the old and new gap boundaries when the gap
is moved, so generally updating the marks is pretty cheap.
The marks are stored sorted so they can be located quickly
with a binary search. This increases the cost of adding a
mark, and decreases the cost of keeping the mark updated.

**All Implemented Interfaces:** Serializable

,

AbstractDocument.Content

---

### Field Details

*No entries found.*

### Constructor Details

#### public GapContent()

Creates a new GapContent object. Initial size defaults to 10.

---

#### public GapContent​(int initialLength)

Creates a new GapContent object, with the initial
size specified. The initial size will not be allowed
to go below 2, to give room for the implied break and
the gap.

**Parameters:**
- initialLength

- the initial size

---

### Method Details

#### protected
Object
allocateArray​(int len)

Allocate an array to store items of the type
appropriate (which is determined by the subclass).

---

#### protected int getArrayLength()

Get the length of the allocated array.

---

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

- the starting position >= 0, < length()
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

Removes part of the content.

**Specified by:**
- remove

in interface

AbstractDocument.Content

**Parameters:**
- where

- the starting position >= 0, where + nitems < length()
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

Retrieves a portion of the content.

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
- a string representing the content

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

Retrieves a portion of the content. If the desired content spans
the gap, we copy the content. If the desired content does not
span the gap, the actual store is returned to avoid the copy since
it is contiguous.

**Specified by:**
- getChars

in interface

AbstractDocument.Content

**Parameters:**
- where

- the starting position >= 0, where + len <= length()
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

- the offset to track >= 0

**Returns:**
- the position

**Throws:**
- BadLocationException

- if the specified position is invalid

---

#### protected void shiftEnd​(int newSize)

Make the gap bigger, moving any necessary data and updating
the appropriate marks

---

#### protected void shiftGap​(int newGapStart)

Move the start of the gap to a new location,
without changing the size of the gap. This
moves the data in the array and updates the
marks accordingly.

---

#### protected void resetMarksAtZero()

Resets all the marks that have an offset of 0 to have an index of
zero as well.

---

#### protected void shiftGapStartDown​(int newGapStart)

Adjust the gap end downward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap start down to the new gap start are squeezed
to the end of the gap (their location has been
removed).

---

#### protected void shiftGapEndUp​(int newGapEnd)

Adjust the gap end upward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap end up to the new gap end are squeezed
to the end of the gap (their location has been
removed).

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
positions,
int offset,
int length)

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:**
- positions

- the UndoPosRef instances to reset
- offset

- where the string was inserted
- length

- length of inserted string

---

#### protected final
Object
getArray()

Access to the array. The actual type
of the array is known only by the subclass.

---

#### protected final int getGapStart()

Access to the start of the gap.

---

#### protected final int getGapEnd()

Access to the end of the gap.

---

#### protected void replace​(int position,
int rmSize,

Object
addItems,
int addSize)

Replace the given logical position in the storage with
the given new items. This will move the gap to the area
being changed if the gap is not currently located at the
change location.

**Parameters:**
- position

- the location to make the replacement. This
is not the location in the underlying storage array, but
the location in the contiguous space being modeled.
- rmSize

- the number of items to remove
- addItems

- the new items to place in storage.

---

### Additional Sections

#### Class GapContent

java.lang.Object

- javax.swing.text.GapContent

javax.swing.text.GapContent

**All Implemented Interfaces:** Serializable

,

AbstractDocument.Content

```java
public class
GapContent

extends
Object

implements
AbstractDocument.Content
,
Serializable
```

An implementation of the AbstractDocument.Content interface
implemented using a gapped buffer similar to that used by emacs.
The underlying storage is a array of unicode characters with
a gap somewhere. The gap is moved to the location of changes
to take advantage of common behavior where most changes are
in the same location. Changes that occur at a gap boundary are
generally cheap and moving the gap is generally cheaper than
moving the array contents directly to accommodate the change.

The positions tracking change are also generally cheap to
maintain. The Position implementations (marks) store the array
index and can easily calculate the sequential position from
the current gap location. Changes only require update to the
the marks between the old and new gap boundaries when the gap
is moved, so generally updating the marks is pretty cheap.
The marks are stored sorted so they can be located quickly
with a binary search. This increases the cost of adding a
mark, and decreases the cost of keeping the mark updated.

**See Also:** Serialized Form

public class

GapContent

extends

Object

implements

AbstractDocument.Content

,

Serializable

An implementation of the AbstractDocument.Content interface
implemented using a gapped buffer similar to that used by emacs.
The underlying storage is a array of unicode characters with
a gap somewhere. The gap is moved to the location of changes
to take advantage of common behavior where most changes are
in the same location. Changes that occur at a gap boundary are
generally cheap and moving the gap is generally cheaper than
moving the array contents directly to accommodate the change.

The positions tracking change are also generally cheap to
maintain. The Position implementations (marks) store the array
index and can easily calculate the sequential position from
the current gap location. Changes only require update to the
the marks between the old and new gap boundaries when the gap
is moved, so generally updating the marks is pretty cheap.
The marks are stored sorted so they can be located quickly
with a binary search. This increases the cost of adding a
mark, and decreases the cost of keeping the mark updated.

The positions tracking change are also generally cheap to
maintain. The Position implementations (marks) store the array
index and can easily calculate the sequential position from
the current gap location. Changes only require update to the
the marks between the old and new gap boundaries when the gap
is moved, so generally updating the marks is pretty cheap.
The marks are stored sorted so they can be located quickly
with a binary search. This increases the cost of adding a
mark, and decreases the cost of keeping the mark updated.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GapContent

()

Creates a new GapContent object.

GapContent

​(int initialLength)

Creates a new GapContent object, with the initial
size specified.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

allocateArray

​(int len)

Allocate an array to store items of the type
appropriate (which is determined by the subclass).

Position

createPosition

​(int offset)

Creates a position within the content that will
track change as the content is mutated.

protected

Object

getArray

()

Access to the array.

protected int

getArrayLength

()

Get the length of the allocated array.

void

getChars

​(int where,
int len,

Segment

chars)

Retrieves a portion of the content.

protected int

getGapEnd

()

Access to the end of the gap.

protected int

getGapStart

()

Access to the start of the gap.

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

replace

​(int position,
int rmSize,

Object

addItems,
int addSize)

Replace the given logical position in the storage with
the given new items.

protected void

resetMarksAtZero

()

Resets all the marks that have an offset of 0 to have an index of
zero as well.

protected void

shiftEnd

​(int newSize)

Make the gap bigger, moving any necessary data and updating
the appropriate marks

protected void

shiftGap

​(int newGapStart)

Move the start of the gap to a new location,
without changing the size of the gap.

protected void

shiftGapEndUp

​(int newGapEnd)

Adjust the gap end upward.

protected void

shiftGapStartDown

​(int newGapStart)

Adjust the gap end downward.

protected void

updateUndoPositions

​(

Vector

positions,
int offset,
int length)

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

GapContent

()

Creates a new GapContent object.

GapContent

​(int initialLength)

Creates a new GapContent object, with the initial
size specified.

---

#### Constructor Summary

Creates a new GapContent object.

Creates a new GapContent object, with the initial
size specified.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

allocateArray

​(int len)

Allocate an array to store items of the type
appropriate (which is determined by the subclass).

Position

createPosition

​(int offset)

Creates a position within the content that will
track change as the content is mutated.

protected

Object

getArray

()

Access to the array.

protected int

getArrayLength

()

Get the length of the allocated array.

void

getChars

​(int where,
int len,

Segment

chars)

Retrieves a portion of the content.

protected int

getGapEnd

()

Access to the end of the gap.

protected int

getGapStart

()

Access to the start of the gap.

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

replace

​(int position,
int rmSize,

Object

addItems,
int addSize)

Replace the given logical position in the storage with
the given new items.

protected void

resetMarksAtZero

()

Resets all the marks that have an offset of 0 to have an index of
zero as well.

protected void

shiftEnd

​(int newSize)

Make the gap bigger, moving any necessary data and updating
the appropriate marks

protected void

shiftGap

​(int newGapStart)

Move the start of the gap to a new location,
without changing the size of the gap.

protected void

shiftGapEndUp

​(int newGapEnd)

Adjust the gap end upward.

protected void

shiftGapStartDown

​(int newGapStart)

Adjust the gap end downward.

protected void

updateUndoPositions

​(

Vector

positions,
int offset,
int length)

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

Allocate an array to store items of the type
appropriate (which is determined by the subclass).

Creates a position within the content that will
track change as the content is mutated.

Access to the array.

Get the length of the allocated array.

Retrieves a portion of the content.

Access to the end of the gap.

Access to the start of the gap.

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

Replace the given logical position in the storage with
the given new items.

Resets all the marks that have an offset of 0 to have an index of
zero as well.

Make the gap bigger, moving any necessary data and updating
the appropriate marks

Move the start of the gap to a new location,
without changing the size of the gap.

Adjust the gap end upward.

Adjust the gap end downward.

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

- GapContent

```java
public GapContent()
```

Creates a new GapContent object. Initial size defaults to 10.

- GapContent

```java
public GapContent​(int initialLength)
```

Creates a new GapContent object, with the initial
size specified. The initial size will not be allowed
to go below 2, to give room for the implied break and
the gap.

**Parameters:** initialLength

- the initial size

============ METHOD DETAIL ==========

- Method Detail

- allocateArray

```java
protected
Object
allocateArray​(int len)
```

Allocate an array to store items of the type
appropriate (which is determined by the subclass).

- getArrayLength

```java
protected int getArrayLength()
```

Get the length of the allocated array.

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

- the starting position >= 0, < length()
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

Removes part of the content.

**Specified by:** remove

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0, where + nitems < length()
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

Retrieves a portion of the content.

**Specified by:** getString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the length to retrieve >= 0
**Returns:** a string representing the content
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

Retrieves a portion of the content. If the desired content spans
the gap, we copy the content. If the desired content does not
span the gap, the actual store is returned to avoid the copy since
it is contiguous.

**Specified by:** getChars

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0, where + len <= length()
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

- the offset to track >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the specified position is invalid

- shiftEnd

```java
protected void shiftEnd​(int newSize)
```

Make the gap bigger, moving any necessary data and updating
the appropriate marks

- shiftGap

```java
protected void shiftGap​(int newGapStart)
```

Move the start of the gap to a new location,
without changing the size of the gap. This
moves the data in the array and updates the
marks accordingly.

- resetMarksAtZero

```java
protected void resetMarksAtZero()
```

Resets all the marks that have an offset of 0 to have an index of
zero as well.

- shiftGapStartDown

```java
protected void shiftGapStartDown​(int newGapStart)
```

Adjust the gap end downward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap start down to the new gap start are squeezed
to the end of the gap (their location has been
removed).

- shiftGapEndUp

```java
protected void shiftGapEndUp​(int newGapEnd)
```

Adjust the gap end upward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap end up to the new gap end are squeezed
to the end of the gap (their location has been
removed).

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
positions,
int offset,
int length)
```

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** positions

- the UndoPosRef instances to reset
**Parameters:** offset

- where the string was inserted
**Parameters:** length

- length of inserted string

- getArray

```java
protected final
Object
getArray()
```

Access to the array. The actual type
of the array is known only by the subclass.

- getGapStart

```java
protected final int getGapStart()
```

Access to the start of the gap.

- getGapEnd

```java
protected final int getGapEnd()
```

Access to the end of the gap.

- replace

```java
protected void replace​(int position,
int rmSize,

Object
addItems,
int addSize)
```

Replace the given logical position in the storage with
the given new items. This will move the gap to the area
being changed if the gap is not currently located at the
change location.

**Parameters:** position

- the location to make the replacement. This
is not the location in the underlying storage array, but
the location in the contiguous space being modeled.
**Parameters:** rmSize

- the number of items to remove
**Parameters:** addItems

- the new items to place in storage.

Constructor Detail

- GapContent

```java
public GapContent()
```

Creates a new GapContent object. Initial size defaults to 10.

- GapContent

```java
public GapContent​(int initialLength)
```

Creates a new GapContent object, with the initial
size specified. The initial size will not be allowed
to go below 2, to give room for the implied break and
the gap.

**Parameters:** initialLength

- the initial size

---

#### Constructor Detail

GapContent

```java
public GapContent()
```

Creates a new GapContent object. Initial size defaults to 10.

---

#### GapContent

public GapContent()

Creates a new GapContent object. Initial size defaults to 10.

GapContent

```java
public GapContent​(int initialLength)
```

Creates a new GapContent object, with the initial
size specified. The initial size will not be allowed
to go below 2, to give room for the implied break and
the gap.

**Parameters:** initialLength

- the initial size

---

#### GapContent

public GapContent​(int initialLength)

Creates a new GapContent object, with the initial
size specified. The initial size will not be allowed
to go below 2, to give room for the implied break and
the gap.

Method Detail

- allocateArray

```java
protected
Object
allocateArray​(int len)
```

Allocate an array to store items of the type
appropriate (which is determined by the subclass).

- getArrayLength

```java
protected int getArrayLength()
```

Get the length of the allocated array.

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

- the starting position >= 0, < length()
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

Removes part of the content.

**Specified by:** remove

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0, where + nitems < length()
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

Retrieves a portion of the content.

**Specified by:** getString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the length to retrieve >= 0
**Returns:** a string representing the content
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

Retrieves a portion of the content. If the desired content spans
the gap, we copy the content. If the desired content does not
span the gap, the actual store is returned to avoid the copy since
it is contiguous.

**Specified by:** getChars

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0, where + len <= length()
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

- the offset to track >= 0
**Returns:** the position
**Throws:** BadLocationException

- if the specified position is invalid

- shiftEnd

```java
protected void shiftEnd​(int newSize)
```

Make the gap bigger, moving any necessary data and updating
the appropriate marks

- shiftGap

```java
protected void shiftGap​(int newGapStart)
```

Move the start of the gap to a new location,
without changing the size of the gap. This
moves the data in the array and updates the
marks accordingly.

- resetMarksAtZero

```java
protected void resetMarksAtZero()
```

Resets all the marks that have an offset of 0 to have an index of
zero as well.

- shiftGapStartDown

```java
protected void shiftGapStartDown​(int newGapStart)
```

Adjust the gap end downward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap start down to the new gap start are squeezed
to the end of the gap (their location has been
removed).

- shiftGapEndUp

```java
protected void shiftGapEndUp​(int newGapEnd)
```

Adjust the gap end upward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap end up to the new gap end are squeezed
to the end of the gap (their location has been
removed).

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
positions,
int offset,
int length)
```

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** positions

- the UndoPosRef instances to reset
**Parameters:** offset

- where the string was inserted
**Parameters:** length

- length of inserted string

- getArray

```java
protected final
Object
getArray()
```

Access to the array. The actual type
of the array is known only by the subclass.

- getGapStart

```java
protected final int getGapStart()
```

Access to the start of the gap.

- getGapEnd

```java
protected final int getGapEnd()
```

Access to the end of the gap.

- replace

```java
protected void replace​(int position,
int rmSize,

Object
addItems,
int addSize)
```

Replace the given logical position in the storage with
the given new items. This will move the gap to the area
being changed if the gap is not currently located at the
change location.

**Parameters:** position

- the location to make the replacement. This
is not the location in the underlying storage array, but
the location in the contiguous space being modeled.
**Parameters:** rmSize

- the number of items to remove
**Parameters:** addItems

- the new items to place in storage.

---

#### Method Detail

allocateArray

```java
protected
Object
allocateArray​(int len)
```

Allocate an array to store items of the type
appropriate (which is determined by the subclass).

---

#### allocateArray

protected

Object

allocateArray​(int len)

Allocate an array to store items of the type
appropriate (which is determined by the subclass).

getArrayLength

```java
protected int getArrayLength()
```

Get the length of the allocated array.

---

#### getArrayLength

protected int getArrayLength()

Get the length of the allocated array.

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

- the starting position >= 0, < length()
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

Removes part of the content.

**Specified by:** remove

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0, where + nitems < length()
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

Removes part of the content.

getString

```java
public
String
getString​(int where,
int len)
throws
BadLocationException
```

Retrieves a portion of the content.

**Specified by:** getString

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0
**Parameters:** len

- the length to retrieve >= 0
**Returns:** a string representing the content
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

Retrieves a portion of the content.

getChars

```java
public void getChars​(int where,
int len,

Segment
chars)
throws
BadLocationException
```

Retrieves a portion of the content. If the desired content spans
the gap, we copy the content. If the desired content does not
span the gap, the actual store is returned to avoid the copy since
it is contiguous.

**Specified by:** getChars

in interface

AbstractDocument.Content
**Parameters:** where

- the starting position >= 0, where + len <= length()
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

Retrieves a portion of the content. If the desired content spans
the gap, we copy the content. If the desired content does not
span the gap, the actual store is returned to avoid the copy since
it is contiguous.

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

- the offset to track >= 0
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

shiftEnd

```java
protected void shiftEnd​(int newSize)
```

Make the gap bigger, moving any necessary data and updating
the appropriate marks

---

#### shiftEnd

protected void shiftEnd​(int newSize)

Make the gap bigger, moving any necessary data and updating
the appropriate marks

shiftGap

```java
protected void shiftGap​(int newGapStart)
```

Move the start of the gap to a new location,
without changing the size of the gap. This
moves the data in the array and updates the
marks accordingly.

---

#### shiftGap

protected void shiftGap​(int newGapStart)

Move the start of the gap to a new location,
without changing the size of the gap. This
moves the data in the array and updates the
marks accordingly.

resetMarksAtZero

```java
protected void resetMarksAtZero()
```

Resets all the marks that have an offset of 0 to have an index of
zero as well.

---

#### resetMarksAtZero

protected void resetMarksAtZero()

Resets all the marks that have an offset of 0 to have an index of
zero as well.

shiftGapStartDown

```java
protected void shiftGapStartDown​(int newGapStart)
```

Adjust the gap end downward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap start down to the new gap start are squeezed
to the end of the gap (their location has been
removed).

---

#### shiftGapStartDown

protected void shiftGapStartDown​(int newGapStart)

Adjust the gap end downward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap start down to the new gap start are squeezed
to the end of the gap (their location has been
removed).

shiftGapEndUp

```java
protected void shiftGapEndUp​(int newGapEnd)
```

Adjust the gap end upward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap end up to the new gap end are squeezed
to the end of the gap (their location has been
removed).

---

#### shiftGapEndUp

protected void shiftGapEndUp​(int newGapEnd)

Adjust the gap end upward. This doesn't move
any data, but it does update any marks affected
by the boundary change. All marks from the old
gap end up to the new gap end are squeezed
to the end of the gap (their location has been
removed).

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

updateUndoPositions

```java
protected void updateUndoPositions​(
Vector
positions,
int offset,
int length)
```

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

**Parameters:** positions

- the UndoPosRef instances to reset
**Parameters:** offset

- where the string was inserted
**Parameters:** length

- length of inserted string

---

#### updateUndoPositions

protected void updateUndoPositions​(

Vector

positions,
int offset,
int length)

Resets the location for all the UndoPosRef instances
in

positions

.

This is meant for internal usage, and is generally not of interest
to subclasses.

This is meant for internal usage, and is generally not of interest
to subclasses.

getArray

```java
protected final
Object
getArray()
```

Access to the array. The actual type
of the array is known only by the subclass.

---

#### getArray

protected final

Object

getArray()

Access to the array. The actual type
of the array is known only by the subclass.

getGapStart

```java
protected final int getGapStart()
```

Access to the start of the gap.

---

#### getGapStart

protected final int getGapStart()

Access to the start of the gap.

getGapEnd

```java
protected final int getGapEnd()
```

Access to the end of the gap.

---

#### getGapEnd

protected final int getGapEnd()

Access to the end of the gap.

replace

```java
protected void replace​(int position,
int rmSize,

Object
addItems,
int addSize)
```

Replace the given logical position in the storage with
the given new items. This will move the gap to the area
being changed if the gap is not currently located at the
change location.

**Parameters:** position

- the location to make the replacement. This
is not the location in the underlying storage array, but
the location in the contiguous space being modeled.
**Parameters:** rmSize

- the number of items to remove
**Parameters:** addItems

- the new items to place in storage.

---

#### replace

protected void replace​(int position,
int rmSize,

Object

addItems,
int addSize)

Replace the given logical position in the storage with
the given new items. This will move the gap to the area
being changed if the gap is not currently located at the
change location.

---

