# Interface NodeSetData<T>

**Source:** `java.xml.crypto\javax\xml\crypto\NodeSetData.html`

### Class Description

```java
public interface
NodeSetData<T>

extends
Data
,
Iterable
<T>
```

An abstract representation of a

Data

type containing a
node-set. The type (class) and ordering of the nodes contained in the set
are not defined by this class; instead that behavior should be
defined by

NodeSetData

subclasses.

**Type Parameters:** T

- the type of nodes maintained by this set

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Iterator
<
T
> iterator()

Returns a read-only iterator over the nodes contained in this

NodeSetData

in

document order

. Attempts to modify the returned iterator
via the

remove

method throw

UnsupportedOperationException

.

**Specified by:**
- iterator

in interface

Iterable

<

T

>

**Returns:**
- an

Iterator

over the nodes in this

NodeSetData

in document order

---

### Additional Sections

#### Interface NodeSetData<T>

**Type Parameters:** T

- the type of nodes maintained by this set

**All Superinterfaces:** Data

,

Iterable

<T>

```java
public interface
NodeSetData<T>

extends
Data
,
Iterable
<T>
```

An abstract representation of a

Data

type containing a
node-set. The type (class) and ordering of the nodes contained in the set
are not defined by this class; instead that behavior should be
defined by

NodeSetData

subclasses.

**Since:** 1.6

public interface

NodeSetData<T>

extends

Data

,

Iterable

<T>

An abstract representation of a

Data

type containing a
node-set. The type (class) and ordering of the nodes contained in the set
are not defined by this class; instead that behavior should be
defined by

NodeSetData

subclasses.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Iterator

<

T

>

iterator

()

Returns a read-only iterator over the nodes contained in this

NodeSetData

in

document order

.

- Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Iterator

<

T

>

iterator

()

Returns a read-only iterator over the nodes contained in this

NodeSetData

in

document order

.

- Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

---

#### Method Summary

Returns a read-only iterator over the nodes contained in this

NodeSetData

in

document order

.

Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

---

#### Methods declared in interface java.lang. Iterable

============ METHOD DETAIL ==========

- Method Detail

- iterator

```java
Iterator
<
T
> iterator()
```

Returns a read-only iterator over the nodes contained in this

NodeSetData

in

document order

. Attempts to modify the returned iterator
via the

remove

method throw

UnsupportedOperationException

.

**Specified by:** iterator

in interface

Iterable

<

T

>
**Returns:** an

Iterator

over the nodes in this

NodeSetData

in document order

Method Detail

- iterator

```java
Iterator
<
T
> iterator()
```

Returns a read-only iterator over the nodes contained in this

NodeSetData

in

document order

. Attempts to modify the returned iterator
via the

remove

method throw

UnsupportedOperationException

.

**Specified by:** iterator

in interface

Iterable

<

T

>
**Returns:** an

Iterator

over the nodes in this

NodeSetData

in document order

---

#### Method Detail

iterator

```java
Iterator
<
T
> iterator()
```

Returns a read-only iterator over the nodes contained in this

NodeSetData

in

document order

. Attempts to modify the returned iterator
via the

remove

method throw

UnsupportedOperationException

.

**Specified by:** iterator

in interface

Iterable

<

T

>
**Returns:** an

Iterator

over the nodes in this

NodeSetData

in document order

---

#### iterator

Iterator

<

T

> iterator()

Returns a read-only iterator over the nodes contained in this

NodeSetData

in

document order

. Attempts to modify the returned iterator
via the

remove

method throw

UnsupportedOperationException

.

---

