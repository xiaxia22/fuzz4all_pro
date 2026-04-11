# Interface PrivilegedExceptionAction<T>

**Source:** `java.base\java\security\PrivilegedExceptionAction.html`

### Class Description

```java
public interface
PrivilegedExceptionAction<T>
```

A computation to be performed with privileges enabled, that throws one or
more checked exceptions. The computation is performed by invoking

AccessController.doPrivileged

on the

PrivilegedExceptionAction

object. This interface is
used only for computations that throw checked exceptions;
computations that do not throw
checked exceptions should use

PrivilegedAction

instead.

**Since:** 1.2
**See Also:** AccessController

,

AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,
AccessControlContext)

,

PrivilegedAction

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### T
run()
throws
Exception

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

**Returns:**
- a class-dependent value that may represent the results of the
computation. Each class that implements

PrivilegedExceptionAction

should document what
(if anything) this value represents.

**Throws:**
- Exception

- an exceptional condition has occurred. Each class
that implements

PrivilegedExceptionAction

should
document the exceptions that its run method can throw.

**See Also:**
- AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,AccessControlContext)

---

### Additional Sections

#### Interface PrivilegedExceptionAction<T>

```java
public interface
PrivilegedExceptionAction<T>
```

A computation to be performed with privileges enabled, that throws one or
more checked exceptions. The computation is performed by invoking

AccessController.doPrivileged

on the

PrivilegedExceptionAction

object. This interface is
used only for computations that throw checked exceptions;
computations that do not throw
checked exceptions should use

PrivilegedAction

instead.

**Since:** 1.2
**See Also:** AccessController

,

AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,
AccessControlContext)

,

PrivilegedAction

public interface

PrivilegedExceptionAction<T>

A computation to be performed with privileges enabled, that throws one or
more checked exceptions. The computation is performed by invoking

AccessController.doPrivileged

on the

PrivilegedExceptionAction

object. This interface is
used only for computations that throw checked exceptions;
computations that do not throw
checked exceptions should use

PrivilegedAction

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
throws
Exception
```

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

**Returns:** a class-dependent value that may represent the results of the
computation. Each class that implements

PrivilegedExceptionAction

should document what
(if anything) this value represents.
**Throws:** Exception

- an exceptional condition has occurred. Each class
that implements

PrivilegedExceptionAction

should
document the exceptions that its run method can throw.
**See Also:** AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,AccessControlContext)

Method Detail

- run

```java
T
run()
throws
Exception
```

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

**Returns:** a class-dependent value that may represent the results of the
computation. Each class that implements

PrivilegedExceptionAction

should document what
(if anything) this value represents.
**Throws:** Exception

- an exceptional condition has occurred. Each class
that implements

PrivilegedExceptionAction

should
document the exceptions that its run method can throw.
**See Also:** AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,AccessControlContext)

---

#### Method Detail

run

```java
T
run()
throws
Exception
```

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

**Returns:** a class-dependent value that may represent the results of the
computation. Each class that implements

PrivilegedExceptionAction

should document what
(if anything) this value represents.
**Throws:** Exception

- an exceptional condition has occurred. Each class
that implements

PrivilegedExceptionAction

should
document the exceptions that its run method can throw.
**See Also:** AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,AccessControlContext)

---

#### run

T

run()
throws

Exception

Performs the computation. This method will be called by

AccessController.doPrivileged

after enabling privileges.

---

