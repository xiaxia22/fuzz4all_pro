# Interface PrivilegedAction<T>

**Source:** `java.base\java\security\PrivilegedAction.html`

### Class Description

```java
public interface
PrivilegedAction<T>
```

A computation to be performed with privileges enabled. The computation is
performed by invoking

AccessController.doPrivileged

on the

PrivilegedAction

object. This interface is used only for
computations that do not throw checked exceptions; computations that
throw checked exceptions must use

PrivilegedExceptionAction

instead.

**Since:** 1.2
**See Also:** AccessController

,

AccessController.doPrivileged(PrivilegedAction)

,

PrivilegedExceptionAction

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### T
run()

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

**Returns:**
- a class-dependent value that may represent the results of the
computation. Each class that implements

PrivilegedAction

should document what (if anything) this value represents.

**See Also:**
- AccessController.doPrivileged(PrivilegedAction)

,

AccessController.doPrivileged(PrivilegedAction,
AccessControlContext)

---

### Additional Sections

#### Interface PrivilegedAction<T>

```java
public interface
PrivilegedAction<T>
```

A computation to be performed with privileges enabled. The computation is
performed by invoking

AccessController.doPrivileged

on the

PrivilegedAction

object. This interface is used only for
computations that do not throw checked exceptions; computations that
throw checked exceptions must use

PrivilegedExceptionAction

instead.

**Since:** 1.2
**See Also:** AccessController

,

AccessController.doPrivileged(PrivilegedAction)

,

PrivilegedExceptionAction

public interface

PrivilegedAction<T>

A computation to be performed with privileges enabled. The computation is
performed by invoking

AccessController.doPrivileged

on the

PrivilegedAction

object. This interface is used only for
computations that do not throw checked exceptions; computations that
throw checked exceptions must use

PrivilegedExceptionAction

instead.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

T

run

()

Performs the computation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

T

run

()

Performs the computation.

---

#### Method Summary

Performs the computation.

============ METHOD DETAIL ==========

- Method Detail

- run

```java
T
run()
```

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

**Returns:** a class-dependent value that may represent the results of the
computation. Each class that implements

PrivilegedAction

should document what (if anything) this value represents.
**See Also:** AccessController.doPrivileged(PrivilegedAction)

,

AccessController.doPrivileged(PrivilegedAction,
AccessControlContext)

Method Detail

- run

```java
T
run()
```

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

**Returns:** a class-dependent value that may represent the results of the
computation. Each class that implements

PrivilegedAction

should document what (if anything) this value represents.
**See Also:** AccessController.doPrivileged(PrivilegedAction)

,

AccessController.doPrivileged(PrivilegedAction,
AccessControlContext)

---

#### Method Detail

run

```java
T
run()
```

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

**Returns:** a class-dependent value that may represent the results of the
computation. Each class that implements

PrivilegedAction

should document what (if anything) this value represents.
**See Also:** AccessController.doPrivileged(PrivilegedAction)

,

AccessController.doPrivileged(PrivilegedAction,
AccessControlContext)

---

#### run

T

run()

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

---

