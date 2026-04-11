# Interface CRLSelector

**Source:** `java.base\java\security\cert\CRLSelector.html`

### Class Description

```java
public interface
CRLSelector

extends
Cloneable
```

A selector that defines a set of criteria for selecting

CRL

s.
Classes that implement this interface are often used to specify
which

CRL

s should be retrieved from a

CertStore

.

Concurrent Access

Unless otherwise specified, the methods defined in this interface are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**All Superinterfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean match​(
CRL
crl)

Decides whether a

CRL

should be selected.

**Parameters:**
- crl

- the

CRL

to be checked

**Returns:**
- true

if the

CRL

should be selected,

false

otherwise

---

#### Object
clone()

Makes a copy of this

CRLSelector

. Changes to the
copy will not affect the original and vice versa.

**Returns:**
- a copy of this

CRLSelector

---

### Additional Sections

#### Interface CRLSelector

**All Superinterfaces:** Cloneable

**All Known Implementing Classes:** X509CRLSelector

```java
public interface
CRLSelector

extends
Cloneable
```

A selector that defines a set of criteria for selecting

CRL

s.
Classes that implement this interface are often used to specify
which

CRL

s should be retrieved from a

CertStore

.

Concurrent Access

Unless otherwise specified, the methods defined in this interface are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** CRL

,

CertStore

,

CertStore.getCRLs(java.security.cert.CRLSelector)

public interface

CRLSelector

extends

Cloneable

A selector that defines a set of criteria for selecting

CRL

s.
Classes that implement this interface are often used to specify
which

CRL

s should be retrieved from a

CertStore

.

Concurrent Access

Unless otherwise specified, the methods defined in this interface are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Concurrent Access

Unless otherwise specified, the methods defined in this interface are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Unless otherwise specified, the methods defined in this interface are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of this

CRLSelector

.

boolean

match

​(

CRL

crl)

Decides whether a

CRL

should be selected.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of this

CRLSelector

.

boolean

match

​(

CRL

crl)

Decides whether a

CRL

should be selected.

---

#### Method Summary

Makes a copy of this

CRLSelector

.

Decides whether a

CRL

should be selected.

============ METHOD DETAIL ==========

- Method Detail

- match

```java
boolean match​(
CRL
crl)
```

Decides whether a

CRL

should be selected.

**Parameters:** crl

- the

CRL

to be checked
**Returns:** true

if the

CRL

should be selected,

false

otherwise

- clone

```java
Object
clone()
```

Makes a copy of this

CRLSelector

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CRLSelector

Method Detail

- match

```java
boolean match​(
CRL
crl)
```

Decides whether a

CRL

should be selected.

**Parameters:** crl

- the

CRL

to be checked
**Returns:** true

if the

CRL

should be selected,

false

otherwise

- clone

```java
Object
clone()
```

Makes a copy of this

CRLSelector

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CRLSelector

---

#### Method Detail

match

```java
boolean match​(
CRL
crl)
```

Decides whether a

CRL

should be selected.

**Parameters:** crl

- the

CRL

to be checked
**Returns:** true

if the

CRL

should be selected,

false

otherwise

---

#### match

boolean match​(

CRL

crl)

Decides whether a

CRL

should be selected.

clone

```java
Object
clone()
```

Makes a copy of this

CRLSelector

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CRLSelector

---

#### clone

Object

clone()

Makes a copy of this

CRLSelector

. Changes to the
copy will not affect the original and vice versa.

---

