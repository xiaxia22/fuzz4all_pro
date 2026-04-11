# Class SizeSequence

**Source:** `java.desktop\javax\swing\SizeSequence.html`

### Class Description

```java
public class
SizeSequence

extends
Object
```

A

SizeSequence

object
efficiently maintains an ordered list
of sizes and corresponding positions.
One situation for which

SizeSequence

might be appropriate is in a component
that displays multiple rows of unequal size.
In this case, a single

SizeSequence

object could be used to track the heights
and Y positions of all rows.

Another example would be a multi-column component,
such as a

JTable

,
in which the column sizes are not all equal.
The

JTable

might use a single

SizeSequence

object
to store the widths and X positions of all the columns.
The

JTable

could then use the

SizeSequence

object
to find the column corresponding to a certain position.
The

JTable

could update the

SizeSequence

object
whenever one or more column sizes changed.

The following figure shows the relationship between size and position data
for a multi-column component.

In the figure, the first index (0) corresponds to the first column,
the second index (1) to the second column, and so on.
The first column's position starts at 0,
and the column occupies

size

0

pixels,
where

size

0

is the value returned by

getSize(0)

.
Thus, the first column ends at

size

0

- 1.
The second column then begins at
the position

size

0

and occupies

size

1

(

getSize(1)

) pixels.

Note that a

SizeSequence

object simply represents intervals
along an axis.
In our examples, the intervals represent height or width in pixels.
However, any other unit of measure (for example, time in days)
could be just as valid.

Implementation Notes

Normally when storing the size and position of entries,
one would choose between
storing the sizes or storing their positions
instead. The two common operations that are needed during
rendering are:

getIndex(position)

and

setSize(index, size)

.
Whichever choice of internal format is made one of these
operations is costly when the number of entries becomes large.
If sizes are stored, finding the index of the entry
that encloses a particular position is linear in the
number of entries. If positions are stored instead, setting
the size of an entry at a particular index requires updating
the positions of the affected entries, which is also a linear
calculation.

Like the above techniques this class holds an array of N integers
internally but uses a hybrid encoding, which is halfway
between the size-based and positional-based approaches.
The result is a data structure that takes the same space to store
the information but can perform most operations in Log(N) time
instead of O(N), where N is the number of entries in the list.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public SizeSequence()

Creates a new

SizeSequence

object
that contains no entries. To add entries, you
can use

insertEntries

or

setSizes

.

**See Also:**
- insertEntries(int, int, int)

,

setSizes(int[])

---

#### public SizeSequence​(int numEntries)

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size 0.

**Parameters:**
- numEntries

- the number of sizes to track

**Throws:**
- NegativeArraySizeException

- if

numEntries < 0

---

#### public SizeSequence​(int numEntries,
int value)

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size

value

.

**Parameters:**
- numEntries

- the number of sizes to track
- value

- the initial value of each size

---

#### public SizeSequence​(int[] sizes)

Creates a new

SizeSequence

object
that contains the specified sizes.

**Parameters:**
- sizes

- the array of sizes to be contained in
the

SizeSequence

---

### Method Details

#### public void setSizes​(int[] sizes)

Resets this

SizeSequence

object,
using the data in the

sizes

argument.
This method reinitializes this object so that it
contains as many entries as the

sizes

array.
Each entry's size is initialized to the value of the
corresponding item in

sizes

.

**Parameters:**
- sizes

- the array of sizes to be contained in
this

SizeSequence

---

#### public int[] getSizes()

Returns the size of all entries.

**Returns:**
- a new array containing the sizes in this object

---

#### public int getPosition​(int index)

Returns the start position for the specified entry.
For example,

getPosition(0)

returns 0,

getPosition(1)

is equal to

getSize(0)

,

getPosition(2)

is equal to

getSize(0)

+

getSize(1)

,
and so on.

Note that if

index

is greater than

length

the value returned may
be meaningless.

**Parameters:**
- index

- the index of the entry whose position is desired

**Returns:**
- the starting position of the specified entry

---

#### public int getIndex​(int position)

Returns the index of the entry
that corresponds to the specified position.
For example,

getIndex(0)

is 0,
since the first entry always starts at position 0.

**Parameters:**
- position

- the position of the entry

**Returns:**
- the index of the entry that occupies the specified position

---

#### public int getSize​(int index)

Returns the size of the specified entry.
If

index

is out of the range

(0 <= index < getSizes().length)

the behavior is unspecified.

**Parameters:**
- index

- the index corresponding to the entry

**Returns:**
- the size of the entry

---

#### public void setSize​(int index,
int size)

Sets the size of the specified entry.
Note that if the value of

index

does not fall in the range:

(0 <= index < getSizes().length)

the behavior is unspecified.

**Parameters:**
- index

- the index corresponding to the entry
- size

- the size of the entry

---

#### public void insertEntries​(int start,
int length,
int value)

Adds a contiguous group of entries to this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

**Parameters:**
- start

- the index to be assigned to the first entry
in the group
- length

- the number of entries in the group
- value

- the size to be assigned to each new entry

**Throws:**
- ArrayIndexOutOfBoundsException

- if the parameters
are outside of the range:
(

0 <= start < (getSizes().length)) AND (length >= 0)

---

#### public void removeEntries​(int start,
int length)

Removes a contiguous group of entries
from this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

**Parameters:**
- start

- the index of the first entry to be removed
- length

- the number of entries to be removed

---

### Additional Sections

#### Class SizeSequence

java.lang.Object

- javax.swing.SizeSequence

javax.swing.SizeSequence

```java
public class
SizeSequence

extends
Object
```

A

SizeSequence

object
efficiently maintains an ordered list
of sizes and corresponding positions.
One situation for which

SizeSequence

might be appropriate is in a component
that displays multiple rows of unequal size.
In this case, a single

SizeSequence

object could be used to track the heights
and Y positions of all rows.

Another example would be a multi-column component,
such as a

JTable

,
in which the column sizes are not all equal.
The

JTable

might use a single

SizeSequence

object
to store the widths and X positions of all the columns.
The

JTable

could then use the

SizeSequence

object
to find the column corresponding to a certain position.
The

JTable

could update the

SizeSequence

object
whenever one or more column sizes changed.

The following figure shows the relationship between size and position data
for a multi-column component.

In the figure, the first index (0) corresponds to the first column,
the second index (1) to the second column, and so on.
The first column's position starts at 0,
and the column occupies

size

0

pixels,
where

size

0

is the value returned by

getSize(0)

.
Thus, the first column ends at

size

0

- 1.
The second column then begins at
the position

size

0

and occupies

size

1

(

getSize(1)

) pixels.

Note that a

SizeSequence

object simply represents intervals
along an axis.
In our examples, the intervals represent height or width in pixels.
However, any other unit of measure (for example, time in days)
could be just as valid.

Implementation Notes

Normally when storing the size and position of entries,
one would choose between
storing the sizes or storing their positions
instead. The two common operations that are needed during
rendering are:

getIndex(position)

and

setSize(index, size)

.
Whichever choice of internal format is made one of these
operations is costly when the number of entries becomes large.
If sizes are stored, finding the index of the entry
that encloses a particular position is linear in the
number of entries. If positions are stored instead, setting
the size of an entry at a particular index requires updating
the positions of the affected entries, which is also a linear
calculation.

Like the above techniques this class holds an array of N integers
internally but uses a hybrid encoding, which is halfway
between the size-based and positional-based approaches.
The result is a data structure that takes the same space to store
the information but can perform most operations in Log(N) time
instead of O(N), where N is the number of entries in the list.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

**Since:** 1.3

public class

SizeSequence

extends

Object

A

SizeSequence

object
efficiently maintains an ordered list
of sizes and corresponding positions.
One situation for which

SizeSequence

might be appropriate is in a component
that displays multiple rows of unequal size.
In this case, a single

SizeSequence

object could be used to track the heights
and Y positions of all rows.

Another example would be a multi-column component,
such as a

JTable

,
in which the column sizes are not all equal.
The

JTable

might use a single

SizeSequence

object
to store the widths and X positions of all the columns.
The

JTable

could then use the

SizeSequence

object
to find the column corresponding to a certain position.
The

JTable

could update the

SizeSequence

object
whenever one or more column sizes changed.

The following figure shows the relationship between size and position data
for a multi-column component.

In the figure, the first index (0) corresponds to the first column,
the second index (1) to the second column, and so on.
The first column's position starts at 0,
and the column occupies

size

0

pixels,
where

size

0

is the value returned by

getSize(0)

.
Thus, the first column ends at

size

0

- 1.
The second column then begins at
the position

size

0

and occupies

size

1

(

getSize(1)

) pixels.

Note that a

SizeSequence

object simply represents intervals
along an axis.
In our examples, the intervals represent height or width in pixels.
However, any other unit of measure (for example, time in days)
could be just as valid.

Implementation Notes

Normally when storing the size and position of entries,
one would choose between
storing the sizes or storing their positions
instead. The two common operations that are needed during
rendering are:

getIndex(position)

and

setSize(index, size)

.
Whichever choice of internal format is made one of these
operations is costly when the number of entries becomes large.
If sizes are stored, finding the index of the entry
that encloses a particular position is linear in the
number of entries. If positions are stored instead, setting
the size of an entry at a particular index requires updating
the positions of the affected entries, which is also a linear
calculation.

Like the above techniques this class holds an array of N integers
internally but uses a hybrid encoding, which is halfway
between the size-based and positional-based approaches.
The result is a data structure that takes the same space to store
the information but can perform most operations in Log(N) time
instead of O(N), where N is the number of entries in the list.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

Another example would be a multi-column component,
such as a

JTable

,
in which the column sizes are not all equal.
The

JTable

might use a single

SizeSequence

object
to store the widths and X positions of all the columns.
The

JTable

could then use the

SizeSequence

object
to find the column corresponding to a certain position.
The

JTable

could update the

SizeSequence

object
whenever one or more column sizes changed.

The following figure shows the relationship between size and position data
for a multi-column component.

In the figure, the first index (0) corresponds to the first column,
the second index (1) to the second column, and so on.
The first column's position starts at 0,
and the column occupies

size

0

pixels,
where

size

0

is the value returned by

getSize(0)

.
Thus, the first column ends at

size

0

- 1.
The second column then begins at
the position

size

0

and occupies

size

1

(

getSize(1)

) pixels.

Note that a

SizeSequence

object simply represents intervals
along an axis.
In our examples, the intervals represent height or width in pixels.
However, any other unit of measure (for example, time in days)
could be just as valid.

Implementation Notes

Normally when storing the size and position of entries,
one would choose between
storing the sizes or storing their positions
instead. The two common operations that are needed during
rendering are:

getIndex(position)

and

setSize(index, size)

.
Whichever choice of internal format is made one of these
operations is costly when the number of entries becomes large.
If sizes are stored, finding the index of the entry
that encloses a particular position is linear in the
number of entries. If positions are stored instead, setting
the size of an entry at a particular index requires updating
the positions of the affected entries, which is also a linear
calculation.

Like the above techniques this class holds an array of N integers
internally but uses a hybrid encoding, which is halfway
between the size-based and positional-based approaches.
The result is a data structure that takes the same space to store
the information but can perform most operations in Log(N) time
instead of O(N), where N is the number of entries in the list.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

The following figure shows the relationship between size and position data
for a multi-column component.

In the figure, the first index (0) corresponds to the first column,
the second index (1) to the second column, and so on.
The first column's position starts at 0,
and the column occupies

size

0

pixels,
where

size

0

is the value returned by

getSize(0)

.
Thus, the first column ends at

size

0

- 1.
The second column then begins at
the position

size

0

and occupies

size

1

(

getSize(1)

) pixels.

Note that a

SizeSequence

object simply represents intervals
along an axis.
In our examples, the intervals represent height or width in pixels.
However, any other unit of measure (for example, time in days)
could be just as valid.

Implementation Notes

Normally when storing the size and position of entries,
one would choose between
storing the sizes or storing their positions
instead. The two common operations that are needed during
rendering are:

getIndex(position)

and

setSize(index, size)

.
Whichever choice of internal format is made one of these
operations is costly when the number of entries becomes large.
If sizes are stored, finding the index of the entry
that encloses a particular position is linear in the
number of entries. If positions are stored instead, setting
the size of an entry at a particular index requires updating
the positions of the affected entries, which is also a linear
calculation.

Like the above techniques this class holds an array of N integers
internally but uses a hybrid encoding, which is halfway
between the size-based and positional-based approaches.
The result is a data structure that takes the same space to store
the information but can perform most operations in Log(N) time
instead of O(N), where N is the number of entries in the list.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

In the figure, the first index (0) corresponds to the first column,
the second index (1) to the second column, and so on.
The first column's position starts at 0,
and the column occupies

size

0

pixels,
where

size

0

is the value returned by

getSize(0)

.
Thus, the first column ends at

size

0

- 1.
The second column then begins at
the position

size

0

and occupies

size

1

(

getSize(1)

) pixels.

Note that a

SizeSequence

object simply represents intervals
along an axis.
In our examples, the intervals represent height or width in pixels.
However, any other unit of measure (for example, time in days)
could be just as valid.

Implementation Notes

Normally when storing the size and position of entries,
one would choose between
storing the sizes or storing their positions
instead. The two common operations that are needed during
rendering are:

getIndex(position)

and

setSize(index, size)

.
Whichever choice of internal format is made one of these
operations is costly when the number of entries becomes large.
If sizes are stored, finding the index of the entry
that encloses a particular position is linear in the
number of entries. If positions are stored instead, setting
the size of an entry at a particular index requires updating
the positions of the affected entries, which is also a linear
calculation.

Like the above techniques this class holds an array of N integers
internally but uses a hybrid encoding, which is halfway
between the size-based and positional-based approaches.
The result is a data structure that takes the same space to store
the information but can perform most operations in Log(N) time
instead of O(N), where N is the number of entries in the list.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

Note that a

SizeSequence

object simply represents intervals
along an axis.
In our examples, the intervals represent height or width in pixels.
However, any other unit of measure (for example, time in days)
could be just as valid.

Implementation Notes

Normally when storing the size and position of entries,
one would choose between
storing the sizes or storing their positions
instead. The two common operations that are needed during
rendering are:

getIndex(position)

and

setSize(index, size)

.
Whichever choice of internal format is made one of these
operations is costly when the number of entries becomes large.
If sizes are stored, finding the index of the entry
that encloses a particular position is linear in the
number of entries. If positions are stored instead, setting
the size of an entry at a particular index requires updating
the positions of the affected entries, which is also a linear
calculation.

Like the above techniques this class holds an array of N integers
internally but uses a hybrid encoding, which is halfway
between the size-based and positional-based approaches.
The result is a data structure that takes the same space to store
the information but can perform most operations in Log(N) time
instead of O(N), where N is the number of entries in the list.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

---

#### Implementation Notes

Like the above techniques this class holds an array of N integers
internally but uses a hybrid encoding, which is halfway
between the size-based and positional-based approaches.
The result is a data structure that takes the same space to store
the information but can perform most operations in Log(N) time
instead of O(N), where N is the number of entries in the list.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

Two operations that remain O(N) in the number of entries are
the

insertEntries

and

removeEntries

methods, both
of which are implemented by converting the internal array to
a set of integer sizes, copying it into the new array, and then
reforming the hybrid representation in place.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SizeSequence

()

Creates a new

SizeSequence

object
that contains no entries.

SizeSequence

​(int numEntries)

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size 0.

SizeSequence

​(int[] sizes)

Creates a new

SizeSequence

object
that contains the specified sizes.

SizeSequence

​(int numEntries,
int value)

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size

value

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIndex

​(int position)

Returns the index of the entry
that corresponds to the specified position.

int

getPosition

​(int index)

Returns the start position for the specified entry.

int

getSize

​(int index)

Returns the size of the specified entry.

int[]

getSizes

()

Returns the size of all entries.

void

insertEntries

​(int start,
int length,
int value)

Adds a contiguous group of entries to this

SizeSequence

.

void

removeEntries

​(int start,
int length)

Removes a contiguous group of entries
from this

SizeSequence

.

void

setSize

​(int index,
int size)

Sets the size of the specified entry.

void

setSizes

​(int[] sizes)

Resets this

SizeSequence

object,
using the data in the

sizes

argument.

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

SizeSequence

()

Creates a new

SizeSequence

object
that contains no entries.

SizeSequence

​(int numEntries)

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size 0.

SizeSequence

​(int[] sizes)

Creates a new

SizeSequence

object
that contains the specified sizes.

SizeSequence

​(int numEntries,
int value)

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size

value

.

---

#### Constructor Summary

Creates a new

SizeSequence

object
that contains no entries.

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size 0.

Creates a new

SizeSequence

object
that contains the specified sizes.

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size

value

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIndex

​(int position)

Returns the index of the entry
that corresponds to the specified position.

int

getPosition

​(int index)

Returns the start position for the specified entry.

int

getSize

​(int index)

Returns the size of the specified entry.

int[]

getSizes

()

Returns the size of all entries.

void

insertEntries

​(int start,
int length,
int value)

Adds a contiguous group of entries to this

SizeSequence

.

void

removeEntries

​(int start,
int length)

Removes a contiguous group of entries
from this

SizeSequence

.

void

setSize

​(int index,
int size)

Sets the size of the specified entry.

void

setSizes

​(int[] sizes)

Resets this

SizeSequence

object,
using the data in the

sizes

argument.

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

Returns the index of the entry
that corresponds to the specified position.

Returns the start position for the specified entry.

Returns the size of the specified entry.

Returns the size of all entries.

Adds a contiguous group of entries to this

SizeSequence

.

Removes a contiguous group of entries
from this

SizeSequence

.

Sets the size of the specified entry.

Resets this

SizeSequence

object,
using the data in the

sizes

argument.

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

- SizeSequence

```java
public SizeSequence()
```

Creates a new

SizeSequence

object
that contains no entries. To add entries, you
can use

insertEntries

or

setSizes

.

**See Also:** insertEntries(int, int, int)

,

setSizes(int[])

- SizeSequence

```java
public SizeSequence​(int numEntries)
```

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size 0.

**Parameters:** numEntries

- the number of sizes to track
**Throws:** NegativeArraySizeException

- if

numEntries < 0

- SizeSequence

```java
public SizeSequence​(int numEntries,
int value)
```

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size

value

.

**Parameters:** numEntries

- the number of sizes to track
**Parameters:** value

- the initial value of each size

- SizeSequence

```java
public SizeSequence​(int[] sizes)
```

Creates a new

SizeSequence

object
that contains the specified sizes.

**Parameters:** sizes

- the array of sizes to be contained in
the

SizeSequence

============ METHOD DETAIL ==========

- Method Detail

- setSizes

```java
public void setSizes​(int[] sizes)
```

Resets this

SizeSequence

object,
using the data in the

sizes

argument.
This method reinitializes this object so that it
contains as many entries as the

sizes

array.
Each entry's size is initialized to the value of the
corresponding item in

sizes

.

**Parameters:** sizes

- the array of sizes to be contained in
this

SizeSequence

- getSizes

```java
public int[] getSizes()
```

Returns the size of all entries.

**Returns:** a new array containing the sizes in this object

- getPosition

```java
public int getPosition​(int index)
```

Returns the start position for the specified entry.
For example,

getPosition(0)

returns 0,

getPosition(1)

is equal to

getSize(0)

,

getPosition(2)

is equal to

getSize(0)

+

getSize(1)

,
and so on.

Note that if

index

is greater than

length

the value returned may
be meaningless.

**Parameters:** index

- the index of the entry whose position is desired
**Returns:** the starting position of the specified entry

- getIndex

```java
public int getIndex​(int position)
```

Returns the index of the entry
that corresponds to the specified position.
For example,

getIndex(0)

is 0,
since the first entry always starts at position 0.

**Parameters:** position

- the position of the entry
**Returns:** the index of the entry that occupies the specified position

- getSize

```java
public int getSize​(int index)
```

Returns the size of the specified entry.
If

index

is out of the range

(0 <= index < getSizes().length)

the behavior is unspecified.

**Parameters:** index

- the index corresponding to the entry
**Returns:** the size of the entry

- setSize

```java
public void setSize​(int index,
int size)
```

Sets the size of the specified entry.
Note that if the value of

index

does not fall in the range:

(0 <= index < getSizes().length)

the behavior is unspecified.

**Parameters:** index

- the index corresponding to the entry
**Parameters:** size

- the size of the entry

- insertEntries

```java
public void insertEntries​(int start,
int length,
int value)
```

Adds a contiguous group of entries to this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

**Parameters:** start

- the index to be assigned to the first entry
in the group
**Parameters:** length

- the number of entries in the group
**Parameters:** value

- the size to be assigned to each new entry
**Throws:** ArrayIndexOutOfBoundsException

- if the parameters
are outside of the range:
(

0 <= start < (getSizes().length)) AND (length >= 0)

- removeEntries

```java
public void removeEntries​(int start,
int length)
```

Removes a contiguous group of entries
from this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

**Parameters:** start

- the index of the first entry to be removed
**Parameters:** length

- the number of entries to be removed

Constructor Detail

- SizeSequence

```java
public SizeSequence()
```

Creates a new

SizeSequence

object
that contains no entries. To add entries, you
can use

insertEntries

or

setSizes

.

**See Also:** insertEntries(int, int, int)

,

setSizes(int[])

- SizeSequence

```java
public SizeSequence​(int numEntries)
```

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size 0.

**Parameters:** numEntries

- the number of sizes to track
**Throws:** NegativeArraySizeException

- if

numEntries < 0

- SizeSequence

```java
public SizeSequence​(int numEntries,
int value)
```

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size

value

.

**Parameters:** numEntries

- the number of sizes to track
**Parameters:** value

- the initial value of each size

- SizeSequence

```java
public SizeSequence​(int[] sizes)
```

Creates a new

SizeSequence

object
that contains the specified sizes.

**Parameters:** sizes

- the array of sizes to be contained in
the

SizeSequence

---

#### Constructor Detail

SizeSequence

```java
public SizeSequence()
```

Creates a new

SizeSequence

object
that contains no entries. To add entries, you
can use

insertEntries

or

setSizes

.

**See Also:** insertEntries(int, int, int)

,

setSizes(int[])

---

#### SizeSequence

public SizeSequence()

Creates a new

SizeSequence

object
that contains no entries. To add entries, you
can use

insertEntries

or

setSizes

.

SizeSequence

```java
public SizeSequence​(int numEntries)
```

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size 0.

**Parameters:** numEntries

- the number of sizes to track
**Throws:** NegativeArraySizeException

- if

numEntries < 0

---

#### SizeSequence

public SizeSequence​(int numEntries)

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size 0.

SizeSequence

```java
public SizeSequence​(int numEntries,
int value)
```

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size

value

.

**Parameters:** numEntries

- the number of sizes to track
**Parameters:** value

- the initial value of each size

---

#### SizeSequence

public SizeSequence​(int numEntries,
int value)

Creates a new

SizeSequence

object
that contains the specified number of entries,
all initialized to have size

value

.

SizeSequence

```java
public SizeSequence​(int[] sizes)
```

Creates a new

SizeSequence

object
that contains the specified sizes.

**Parameters:** sizes

- the array of sizes to be contained in
the

SizeSequence

---

#### SizeSequence

public SizeSequence​(int[] sizes)

Creates a new

SizeSequence

object
that contains the specified sizes.

Method Detail

- setSizes

```java
public void setSizes​(int[] sizes)
```

Resets this

SizeSequence

object,
using the data in the

sizes

argument.
This method reinitializes this object so that it
contains as many entries as the

sizes

array.
Each entry's size is initialized to the value of the
corresponding item in

sizes

.

**Parameters:** sizes

- the array of sizes to be contained in
this

SizeSequence

- getSizes

```java
public int[] getSizes()
```

Returns the size of all entries.

**Returns:** a new array containing the sizes in this object

- getPosition

```java
public int getPosition​(int index)
```

Returns the start position for the specified entry.
For example,

getPosition(0)

returns 0,

getPosition(1)

is equal to

getSize(0)

,

getPosition(2)

is equal to

getSize(0)

+

getSize(1)

,
and so on.

Note that if

index

is greater than

length

the value returned may
be meaningless.

**Parameters:** index

- the index of the entry whose position is desired
**Returns:** the starting position of the specified entry

- getIndex

```java
public int getIndex​(int position)
```

Returns the index of the entry
that corresponds to the specified position.
For example,

getIndex(0)

is 0,
since the first entry always starts at position 0.

**Parameters:** position

- the position of the entry
**Returns:** the index of the entry that occupies the specified position

- getSize

```java
public int getSize​(int index)
```

Returns the size of the specified entry.
If

index

is out of the range

(0 <= index < getSizes().length)

the behavior is unspecified.

**Parameters:** index

- the index corresponding to the entry
**Returns:** the size of the entry

- setSize

```java
public void setSize​(int index,
int size)
```

Sets the size of the specified entry.
Note that if the value of

index

does not fall in the range:

(0 <= index < getSizes().length)

the behavior is unspecified.

**Parameters:** index

- the index corresponding to the entry
**Parameters:** size

- the size of the entry

- insertEntries

```java
public void insertEntries​(int start,
int length,
int value)
```

Adds a contiguous group of entries to this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

**Parameters:** start

- the index to be assigned to the first entry
in the group
**Parameters:** length

- the number of entries in the group
**Parameters:** value

- the size to be assigned to each new entry
**Throws:** ArrayIndexOutOfBoundsException

- if the parameters
are outside of the range:
(

0 <= start < (getSizes().length)) AND (length >= 0)

- removeEntries

```java
public void removeEntries​(int start,
int length)
```

Removes a contiguous group of entries
from this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

**Parameters:** start

- the index of the first entry to be removed
**Parameters:** length

- the number of entries to be removed

---

#### Method Detail

setSizes

```java
public void setSizes​(int[] sizes)
```

Resets this

SizeSequence

object,
using the data in the

sizes

argument.
This method reinitializes this object so that it
contains as many entries as the

sizes

array.
Each entry's size is initialized to the value of the
corresponding item in

sizes

.

**Parameters:** sizes

- the array of sizes to be contained in
this

SizeSequence

---

#### setSizes

public void setSizes​(int[] sizes)

Resets this

SizeSequence

object,
using the data in the

sizes

argument.
This method reinitializes this object so that it
contains as many entries as the

sizes

array.
Each entry's size is initialized to the value of the
corresponding item in

sizes

.

getSizes

```java
public int[] getSizes()
```

Returns the size of all entries.

**Returns:** a new array containing the sizes in this object

---

#### getSizes

public int[] getSizes()

Returns the size of all entries.

getPosition

```java
public int getPosition​(int index)
```

Returns the start position for the specified entry.
For example,

getPosition(0)

returns 0,

getPosition(1)

is equal to

getSize(0)

,

getPosition(2)

is equal to

getSize(0)

+

getSize(1)

,
and so on.

Note that if

index

is greater than

length

the value returned may
be meaningless.

**Parameters:** index

- the index of the entry whose position is desired
**Returns:** the starting position of the specified entry

---

#### getPosition

public int getPosition​(int index)

Returns the start position for the specified entry.
For example,

getPosition(0)

returns 0,

getPosition(1)

is equal to

getSize(0)

,

getPosition(2)

is equal to

getSize(0)

+

getSize(1)

,
and so on.

Note that if

index

is greater than

length

the value returned may
be meaningless.

Note that if

index

is greater than

length

the value returned may
be meaningless.

getIndex

```java
public int getIndex​(int position)
```

Returns the index of the entry
that corresponds to the specified position.
For example,

getIndex(0)

is 0,
since the first entry always starts at position 0.

**Parameters:** position

- the position of the entry
**Returns:** the index of the entry that occupies the specified position

---

#### getIndex

public int getIndex​(int position)

Returns the index of the entry
that corresponds to the specified position.
For example,

getIndex(0)

is 0,
since the first entry always starts at position 0.

getSize

```java
public int getSize​(int index)
```

Returns the size of the specified entry.
If

index

is out of the range

(0 <= index < getSizes().length)

the behavior is unspecified.

**Parameters:** index

- the index corresponding to the entry
**Returns:** the size of the entry

---

#### getSize

public int getSize​(int index)

Returns the size of the specified entry.
If

index

is out of the range

(0 <= index < getSizes().length)

the behavior is unspecified.

setSize

```java
public void setSize​(int index,
int size)
```

Sets the size of the specified entry.
Note that if the value of

index

does not fall in the range:

(0 <= index < getSizes().length)

the behavior is unspecified.

**Parameters:** index

- the index corresponding to the entry
**Parameters:** size

- the size of the entry

---

#### setSize

public void setSize​(int index,
int size)

Sets the size of the specified entry.
Note that if the value of

index

does not fall in the range:

(0 <= index < getSizes().length)

the behavior is unspecified.

insertEntries

```java
public void insertEntries​(int start,
int length,
int value)
```

Adds a contiguous group of entries to this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

**Parameters:** start

- the index to be assigned to the first entry
in the group
**Parameters:** length

- the number of entries in the group
**Parameters:** value

- the size to be assigned to each new entry
**Throws:** ArrayIndexOutOfBoundsException

- if the parameters
are outside of the range:
(

0 <= start < (getSizes().length)) AND (length >= 0)

---

#### insertEntries

public void insertEntries​(int start,
int length,
int value)

Adds a contiguous group of entries to this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

removeEntries

```java
public void removeEntries​(int start,
int length)
```

Removes a contiguous group of entries
from this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

**Parameters:** start

- the index of the first entry to be removed
**Parameters:** length

- the number of entries to be removed

---

#### removeEntries

public void removeEntries​(int start,
int length)

Removes a contiguous group of entries
from this

SizeSequence

.
Note that the values of

start

and

length

must satisfy the following
conditions:

(0 <= start < getSizes().length)
AND (length >= 0)

. If these conditions are
not met, the behavior is unspecified and an exception
may be thrown.

---

