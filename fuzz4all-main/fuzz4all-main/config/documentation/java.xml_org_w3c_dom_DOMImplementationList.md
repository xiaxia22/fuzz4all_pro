# Interface DOMImplementationList

**Source:** `java.xml\org\w3c\dom\DOMImplementationList.html`

### Class Description

```java
public interface
DOMImplementationList
```

The

DOMImplementationList

interface provides the abstraction
of an ordered collection of DOM implementations, without defining or
constraining how this collection is implemented. The items in the

DOMImplementationList

are accessible via an integral index,
starting from 0.

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

#### DOMImplementation
item​(int index)

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMImplementation

s in the list, this returns

null

.

**Parameters:**
- index

- Index into the collection.

**Returns:**
- The

DOMImplementation

at the

index

th position in the

DOMImplementationList

, or

null

if that is not a valid index.

---

#### int getLength()

The number of

DOMImplementation

s in the list. The range
of valid child node indices is 0 to

length-1

inclusive.

---

### Additional Sections

#### Interface DOMImplementationList

```java
public interface
DOMImplementationList
```

The

DOMImplementationList

interface provides the abstraction
of an ordered collection of DOM implementations, without defining or
constraining how this collection is implemented. The items in the

DOMImplementationList

are accessible via an integral index,
starting from 0.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

public interface

DOMImplementationList

The

DOMImplementationList

interface provides the abstraction
of an ordered collection of DOM implementations, without defining or
constraining how this collection is implemented. The items in the

DOMImplementationList

are accessible via an integral index,
starting from 0.

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

int

getLength

()

The number of

DOMImplementation

s in the list.

DOMImplementation

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

int

getLength

()

The number of

DOMImplementation

s in the list.

DOMImplementation

item

​(int index)

Returns the

index

th item in the collection.

---

#### Method Summary

The number of

DOMImplementation

s in the list.

Returns the

index

th item in the collection.

============ METHOD DETAIL ==========

- Method Detail

- item

```java
DOMImplementation
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMImplementation

s in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

DOMImplementation

at the

index

th position in the

DOMImplementationList

, or

null

if that is not a valid index.

- getLength

```java
int getLength()
```

The number of

DOMImplementation

s in the list. The range
of valid child node indices is 0 to

length-1

inclusive.

Method Detail

- item

```java
DOMImplementation
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMImplementation

s in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

DOMImplementation

at the

index

th position in the

DOMImplementationList

, or

null

if that is not a valid index.

- getLength

```java
int getLength()
```

The number of

DOMImplementation

s in the list. The range
of valid child node indices is 0 to

length-1

inclusive.

---

#### Method Detail

item

```java
DOMImplementation
item​(int index)
```

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMImplementation

s in the list, this returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The

DOMImplementation

at the

index

th position in the

DOMImplementationList

, or

null

if that is not a valid index.

---

#### item

DOMImplementation

item​(int index)

Returns the

index

th item in the collection. If

index

is greater than or equal to the number of

DOMImplementation

s in the list, this returns

null

.

getLength

```java
int getLength()
```

The number of

DOMImplementation

s in the list. The range
of valid child node indices is 0 to

length-1

inclusive.

---

#### getLength

int getLength()

The number of

DOMImplementation

s in the list. The range
of valid child node indices is 0 to

length-1

inclusive.

---

