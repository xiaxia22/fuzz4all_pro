# Interface CertPathBuilderResult

**Source:** `java.base\java\security\cert\CertPathBuilderResult.html`

### Class Description

```java
public interface
CertPathBuilderResult

extends
Cloneable
```

A specification of the result of a certification path builder algorithm.
All results returned by the

CertPathBuilder.build

method must implement this interface.

At a minimum, a

CertPathBuilderResult

contains the

CertPath

built by the

CertPathBuilder

instance.
Implementations of this interface may add methods to return implementation
or algorithm specific information, such as debugging information or
certification path validation results.

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

#### CertPath
getCertPath()

Returns the built certification path.

**Returns:**
- the certification path (never

null

)

---

#### Object
clone()

Makes a copy of this

CertPathBuilderResult

. Changes to the
copy will not affect the original and vice versa.

**Returns:**
- a copy of this

CertPathBuilderResult

---

### Additional Sections

#### Interface CertPathBuilderResult

**All Superinterfaces:** Cloneable

**All Known Implementing Classes:** PKIXCertPathBuilderResult

```java
public interface
CertPathBuilderResult

extends
Cloneable
```

A specification of the result of a certification path builder algorithm.
All results returned by the

CertPathBuilder.build

method must implement this interface.

At a minimum, a

CertPathBuilderResult

contains the

CertPath

built by the

CertPathBuilder

instance.
Implementations of this interface may add methods to return implementation
or algorithm specific information, such as debugging information or
certification path validation results.

Concurrent Access

Unless otherwise specified, the methods defined in this interface are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** CertPathBuilder

public interface

CertPathBuilderResult

extends

Cloneable

A specification of the result of a certification path builder algorithm.
All results returned by the

CertPathBuilder.build

method must implement this interface.

At a minimum, a

CertPathBuilderResult

contains the

CertPath

built by the

CertPathBuilder

instance.
Implementations of this interface may add methods to return implementation
or algorithm specific information, such as debugging information or
certification path validation results.

Concurrent Access

Unless otherwise specified, the methods defined in this interface are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

At a minimum, a

CertPathBuilderResult

contains the

CertPath

built by the

CertPathBuilder

instance.
Implementations of this interface may add methods to return implementation
or algorithm specific information, such as debugging information or
certification path validation results.

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

CertPathBuilderResult

.

CertPath

getCertPath

()

Returns the built certification path.

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

CertPathBuilderResult

.

CertPath

getCertPath

()

Returns the built certification path.

---

#### Method Summary

Makes a copy of this

CertPathBuilderResult

.

Returns the built certification path.

============ METHOD DETAIL ==========

- Method Detail

- getCertPath

```java
CertPath
getCertPath()
```

Returns the built certification path.

**Returns:** the certification path (never

null

)

- clone

```java
Object
clone()
```

Makes a copy of this

CertPathBuilderResult

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathBuilderResult

Method Detail

- getCertPath

```java
CertPath
getCertPath()
```

Returns the built certification path.

**Returns:** the certification path (never

null

)

- clone

```java
Object
clone()
```

Makes a copy of this

CertPathBuilderResult

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathBuilderResult

---

#### Method Detail

getCertPath

```java
CertPath
getCertPath()
```

Returns the built certification path.

**Returns:** the certification path (never

null

)

---

#### getCertPath

CertPath

getCertPath()

Returns the built certification path.

clone

```java
Object
clone()
```

Makes a copy of this

CertPathBuilderResult

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathBuilderResult

---

#### clone

Object

clone()

Makes a copy of this

CertPathBuilderResult

. Changes to the
copy will not affect the original and vice versa.

---

