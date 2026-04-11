# Interface DOMStringList

**Source:** `java.xml\org\w3c\dom\DOMStringList.html`

### Class Description

```java
public interface
DOMStringList
```

The

DOMStringList

interface provides the abstraction of an
ordered collection of

DOMString

values, without defining or
constraining how this collection is implemented. The items in the

DOMStringList

are accessible via an integral index, starting
from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
item​(int index)

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMString

s in the list, this returns

null

.

**Parameters:**
- index

- Index into the collection.

**Returns:**
- The

DOMString

at the

index

th
position in the

DOMStringList

, or

null

if
that is not a valid index.

---

#### int getLength()

The number of

DOMString

s in the list. The range of valid
child node indices is 0 to

length-1

inclusive.

---

#### boolean contains​(
String
str)

Test if a string is part of this

DOMStringList

.

**Parameters:**
- str

- The string to look for.

**Returns:**
- true

if the string has been found,

false

otherwise.

---

### Additional Sections

#### Interface DOMStringList

```java
public interface
DOMStringList
```

The

DOMStringList

interface provides the abstraction of an
ordered collection of

DOMString

values, without defining or
constraining how this collection is implemented. The items in the

DOMStringList

are accessible via an integral index, starting
from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

public interface

DOMStringList

The

DOMStringList

interface provides the abstraction of an
ordered collection of

DOMString

values, without defining or
constraining how this collection is implemented. The items in the

DOMStringList

are accessible via an integral index, starting
from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

contains

​(

String

str)

Test if a string is part of this

DOMStringList

.

int

getLength

()

The number of

DOMString

s in the list.

String

item

​(int index)

Returns the

index

th item in the collection.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

contains

​(

String

str)

Test if a string is part of this

DOMStringList

.

int

getLength

()

The number of

DOMString

s in the list.

String

item

​(int index)

Returns the

index

th item in the collection.

---

#### Method Summary

Test if a string is part of this

DOMStringList

.

The number of

DOMString

s in the list.

Returns the

index

th item in the collection.

============ METHOD DETAIL ==========

- Method Detail

- item

```java
String
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMString

s in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

DOMString

at the

index

th
position in the

DOMStringList

, or

null

if
that is not a valid index.

- getLength

```java
int getLength()
```

The number of

DOMString

s in the list. The range of valid
child node indices is 0 to

length-1

inclusive.

- contains

```java
boolean contains​(
String
str)
```

Test if a string is part of this

DOMStringList

.

**Parameters:** str

- The string to look for.
**Returns:** true

if the string has been found,

false

otherwise.

Method Detail

- item

```java
String
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMString

s in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

DOMString

at the

index

th
position in the

DOMStringList

, or

null

if
that is not a valid index.

- getLength

```java
int getLength()
```

The number of

DOMString

s in the list. The range of valid
child node indices is 0 to

length-1

inclusive.

- contains

```java
boolean contains​(
String
str)
```

Test if a string is part of this

DOMStringList

.

**Parameters:** str

- The string to look for.
**Returns:** true

if the string has been found,

false

otherwise.

---

#### Method Detail

item

```java
String
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMString

s in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

DOMString

at the

index

th
position in the

DOMStringList

, or

null

if
that is not a valid index.

---

#### item

String

item​(int index)

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMString

s in the list, this returns

null

.

getLength

```java
int getLength()
```

The number of

DOMString

s in the list. The range of valid
child node indices is 0 to

length-1

inclusive.

---

#### getLength

int getLength()

The number of

DOMString

s in the list. The range of valid
child node indices is 0 to

length-1

inclusive.

contains

```java
boolean contains​(
String
str)
```

Test if a string is part of this

DOMStringList

.

**Parameters:** str

- The string to look for.
**Returns:** true

if the string has been found,

false

otherwise.

---

#### contains

boolean contains​(

String

str)

Test if a string is part of this

DOMStringList

.

---

