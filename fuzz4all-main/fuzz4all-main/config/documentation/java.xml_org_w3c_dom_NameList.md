# Interface NameList

**Source:** `java.xml\org\w3c\dom\NameList.html`

### Class Description

```java
public interface
NameList
```

The

NameList

interface provides the abstraction of an ordered
collection of parallel pairs of name and namespace values (which could be
null values), without defining or constraining how this collection is
implemented. The items in the

NameList

are accessible via an
integral index, starting from 0.

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
getName​(int index)

Returns the

index

th name item in the collection.

**Parameters:**
- index

- Index into the collection.

**Returns:**
- The name at the

index

th position in the

NameList

, or

null

if there is no name for
the specified index or if the index is out of range.

---

#### String
getNamespaceURI​(int index)

Returns the

index

th namespaceURI item in the collection.

**Parameters:**
- index

- Index into the collection.

**Returns:**
- The namespace URI at the

index

th position in the

NameList

, or

null

if there is no name for
the specified index or if the index is out of range.

---

#### int getLength()

The number of pairs (name and namespaceURI) in the list. The range of
valid child node indices is 0 to

length-1

inclusive.

---

#### boolean contains​(
String
str)

Test if a name is part of this

NameList

.

**Parameters:**
- str

- The name to look for.

**Returns:**
- true

if the name has been found,

false

otherwise.

---

#### boolean containsNS​(
String
namespaceURI,

String
name)

Test if the pair namespaceURI/name is part of this

NameList

.

**Parameters:**
- namespaceURI

- The namespace URI to look for.
- name

- The name to look for.

**Returns:**
- true

if the pair namespaceURI/name has been
found,

false

otherwise.

---

### Additional Sections

#### Interface NameList

```java
public interface
NameList
```

The

NameList

interface provides the abstraction of an ordered
collection of parallel pairs of name and namespace values (which could be
null values), without defining or constraining how this collection is
implemented. The items in the

NameList

are accessible via an
integral index, starting from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

public interface

NameList

The

NameList

interface provides the abstraction of an ordered
collection of parallel pairs of name and namespace values (which could be
null values), without defining or constraining how this collection is
implemented. The items in the

NameList

are accessible via an
integral index, starting from 0.

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

Test if a name is part of this

NameList

.

boolean

containsNS

​(

String

namespaceURI,

String

name)

Test if the pair namespaceURI/name is part of this

NameList

.

int

getLength

()

The number of pairs (name and namespaceURI) in the list.

String

getName

​(int index)

Returns the

index

th name item in the collection.

String

getNamespaceURI

​(int index)

Returns the

index

th namespaceURI item in the collection.

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

Test if a name is part of this

NameList

.

boolean

containsNS

​(

String

namespaceURI,

String

name)

Test if the pair namespaceURI/name is part of this

NameList

.

int

getLength

()

The number of pairs (name and namespaceURI) in the list.

String

getName

​(int index)

Returns the

index

th name item in the collection.

String

getNamespaceURI

​(int index)

Returns the

index

th namespaceURI item in the collection.

---

#### Method Summary

Test if a name is part of this

NameList

.

Test if the pair namespaceURI/name is part of this

NameList

.

The number of pairs (name and namespaceURI) in the list.

Returns the

index

th name item in the collection.

Returns the

index

th namespaceURI item in the collection.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName​(int index)
```

Returns the

index

th name item in the collection.

**Parameters:** index

- Index into the collection.
**Returns:** The name at the

index

th position in the

NameList

, or

null

if there is no name for
the specified index or if the index is out of range.

- getNamespaceURI

```java
String
getNamespaceURI​(int index)
```

Returns the

index

th namespaceURI item in the collection.

**Parameters:** index

- Index into the collection.
**Returns:** The namespace URI at the

index

th position in the

NameList

, or

null

if there is no name for
the specified index or if the index is out of range.

- getLength

```java
int getLength()
```

The number of pairs (name and namespaceURI) in the list. The range of
valid child node indices is 0 to

length-1

inclusive.

- contains

```java
boolean contains​(
String
str)
```

Test if a name is part of this

NameList

.

**Parameters:** str

- The name to look for.
**Returns:** true

if the name has been found,

false

otherwise.

- containsNS

```java
boolean containsNS​(
String
namespaceURI,

String
name)
```

Test if the pair namespaceURI/name is part of this

NameList

.

**Parameters:** namespaceURI

- The namespace URI to look for.
**Parameters:** name

- The name to look for.
**Returns:** true

if the pair namespaceURI/name has been
found,

false

otherwise.

Method Detail

- getName

```java
String
getName​(int index)
```

Returns the

index

th name item in the collection.

**Parameters:** index

- Index into the collection.
**Returns:** The name at the

index

th position in the

NameList

, or

null

if there is no name for
the specified index or if the index is out of range.

- getNamespaceURI

```java
String
getNamespaceURI​(int index)
```

Returns the

index

th namespaceURI item in the collection.

**Parameters:** index

- Index into the collection.
**Returns:** The namespace URI at the

index

th position in the

NameList

, or

null

if there is no name for
the specified index or if the index is out of range.

- getLength

```java
int getLength()
```

The number of pairs (name and namespaceURI) in the list. The range of
valid child node indices is 0 to

length-1

inclusive.

- contains

```java
boolean contains​(
String
str)
```

Test if a name is part of this

NameList

.

**Parameters:** str

- The name to look for.
**Returns:** true

if the name has been found,

false

otherwise.

- containsNS

```java
boolean containsNS​(
String
namespaceURI,

String
name)
```

Test if the pair namespaceURI/name is part of this

NameList

.

**Parameters:** namespaceURI

- The namespace URI to look for.
**Parameters:** name

- The name to look for.
**Returns:** true

if the pair namespaceURI/name has been
found,

false

otherwise.

---

#### Method Detail

getName

```java
String
getName​(int index)
```

Returns the

index

th name item in the collection.

**Parameters:** index

- Index into the collection.
**Returns:** The name at the

index

th position in the

NameList

, or

null

if there is no name for
the specified index or if the index is out of range.

---

#### getName

String

getName​(int index)

Returns the

index

th name item in the collection.

getNamespaceURI

```java
String
getNamespaceURI​(int index)
```

Returns the

index

th namespaceURI item in the collection.

**Parameters:** index

- Index into the collection.
**Returns:** The namespace URI at the

index

th position in the

NameList

, or

null

if there is no name for
the specified index or if the index is out of range.

---

#### getNamespaceURI

String

getNamespaceURI​(int index)

Returns the

index

th namespaceURI item in the collection.

getLength

```java
int getLength()
```

The number of pairs (name and namespaceURI) in the list. The range of
valid child node indices is 0 to

length-1

inclusive.

---

#### getLength

int getLength()

The number of pairs (name and namespaceURI) in the list. The range of
valid child node indices is 0 to

length-1

inclusive.

contains

```java
boolean contains​(
String
str)
```

Test if a name is part of this

NameList

.

**Parameters:** str

- The name to look for.
**Returns:** true

if the name has been found,

false

otherwise.

---

#### contains

boolean contains​(

String

str)

Test if a name is part of this

NameList

.

containsNS

```java
boolean containsNS​(
String
namespaceURI,

String
name)
```

Test if the pair namespaceURI/name is part of this

NameList

.

**Parameters:** namespaceURI

- The namespace URI to look for.
**Parameters:** name

- The name to look for.
**Returns:** true

if the pair namespaceURI/name has been
found,

false

otherwise.

---

#### containsNS

boolean containsNS​(

String

namespaceURI,

String

name)

Test if the pair namespaceURI/name is part of this

NameList

.

---

