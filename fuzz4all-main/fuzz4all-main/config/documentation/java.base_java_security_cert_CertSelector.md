# Interface CertSelector

**Source:** `java.base\java\security\cert\CertSelector.html`

### Class Description

```java
public interface
CertSelector

extends
Cloneable
```

A selector that defines a set of criteria for selecting

Certificate

s. Classes that implement this interface
are often used to specify which

Certificate

s should
be retrieved from a

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
Certificate
cert)

Decides whether a

Certificate

should be selected.

**Parameters:**
- cert

- the

Certificate

to be checked

**Returns:**
- true

if the

Certificate

should be selected,

false

otherwise

---

#### Object
clone()

Makes a copy of this

CertSelector

. Changes to the
copy will not affect the original and vice versa.

**Returns:**
- a copy of this

CertSelector

---

### Additional Sections

#### Interface CertSelector

**All Superinterfaces:** Cloneable

**All Known Implementing Classes:** X509CertSelector

```java
public interface
CertSelector

extends
Cloneable
```

A selector that defines a set of criteria for selecting

Certificate

s. Classes that implement this interface
are often used to specify which

Certificate

s should
be retrieved from a

CertStore

.

Concurrent Access

Unless otherwise specified, the methods defined in this interface are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** Certificate

,

CertStore

,

CertStore.getCertificates(java.security.cert.CertSelector)

public interface

CertSelector

extends

Cloneable

A selector that defines a set of criteria for selecting

Certificate

s. Classes that implement this interface
are often used to specify which

Certificate

s should
be retrieved from a

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

CertSelector

.

boolean

match

​(

Certificate

cert)

Decides whether a

Certificate

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

CertSelector

.

boolean

match

​(

Certificate

cert)

Decides whether a

Certificate

should be selected.

---

#### Method Summary

Makes a copy of this

CertSelector

.

Decides whether a

Certificate

should be selected.

============ METHOD DETAIL ==========

- Method Detail

- match

```java
boolean match​(
Certificate
cert)
```

Decides whether a

Certificate

should be selected.

**Parameters:** cert

- the

Certificate

to be checked
**Returns:** true

if the

Certificate

should be selected,

false

otherwise

- clone

```java
Object
clone()
```

Makes a copy of this

CertSelector

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertSelector

Method Detail

- match

```java
boolean match​(
Certificate
cert)
```

Decides whether a

Certificate

should be selected.

**Parameters:** cert

- the

Certificate

to be checked
**Returns:** true

if the

Certificate

should be selected,

false

otherwise

- clone

```java
Object
clone()
```

Makes a copy of this

CertSelector

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertSelector

---

#### Method Detail

match

```java
boolean match​(
Certificate
cert)
```

Decides whether a

Certificate

should be selected.

**Parameters:** cert

- the

Certificate

to be checked
**Returns:** true

if the

Certificate

should be selected,

false

otherwise

---

#### match

boolean match​(

Certificate

cert)

Decides whether a

Certificate

should be selected.

clone

```java
Object
clone()
```

Makes a copy of this

CertSelector

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertSelector

---

#### clone

Object

clone()

Makes a copy of this

CertSelector

. Changes to the
copy will not affect the original and vice versa.

---

