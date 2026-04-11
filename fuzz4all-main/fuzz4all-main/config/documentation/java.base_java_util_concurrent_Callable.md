# Interface Callable<V>

**Source:** `java.base\java\util\concurrent\Callable.html`

### Class Description

```java
@FunctionalInterface

public interface
Callable<V>
```

A task that returns a result and may throw an exception.
Implementors define a single method with no arguments called

call

.

The

Callable

interface is similar to

Runnable

, in that both are designed for classes whose
instances are potentially executed by another thread. A

Runnable

, however, does not return a result and cannot
throw a checked exception.

The

Executors

class contains utility methods to
convert from other common forms to

Callable

classes.

**Type Parameters:** V

- the result type of method

call

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### V
call()
throws
Exception

Computes a result, or throws an exception if unable to do so.

**Returns:**
- computed result

**Throws:**
- Exception

- if unable to compute a result

---

### Additional Sections

#### Interface Callable<V>

**Type Parameters:** V

- the result type of method

call

**All Known Subinterfaces:** DocumentationTool.DocumentationTask

,

JavaCompiler.CompilationTask

**All Known Implementing Classes:** JavacTask

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
Callable<V>
```

A task that returns a result and may throw an exception.
Implementors define a single method with no arguments called

call

.

The

Callable

interface is similar to

Runnable

, in that both are designed for classes whose
instances are potentially executed by another thread. A

Runnable

, however, does not return a result and cannot
throw a checked exception.

The

Executors

class contains utility methods to
convert from other common forms to

Callable

classes.

**Since:** 1.5
**See Also:** Executor

@FunctionalInterface

public interface

Callable<V>

A task that returns a result and may throw an exception.
Implementors define a single method with no arguments called

call

.

The

Callable

interface is similar to

Runnable

, in that both are designed for classes whose
instances are potentially executed by another thread. A

Runnable

, however, does not return a result and cannot
throw a checked exception.

The

Executors

class contains utility methods to
convert from other common forms to

Callable

classes.

The

Callable

interface is similar to

Runnable

, in that both are designed for classes whose
instances are potentially executed by another thread. A

Runnable

, however, does not return a result and cannot
throw a checked exception.

The

Executors

class contains utility methods to
convert from other common forms to

Callable

classes.

The

Executors

class contains utility methods to
convert from other common forms to

Callable

classes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

V

call

()

Computes a result, or throws an exception if unable to do so.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

V

call

()

Computes a result, or throws an exception if unable to do so.

---

#### Method Summary

Computes a result, or throws an exception if unable to do so.

============ METHOD DETAIL ==========

- Method Detail

- call

```java
V
call()
throws
Exception
```

Computes a result, or throws an exception if unable to do so.

**Returns:** computed result
**Throws:** Exception

- if unable to compute a result

Method Detail

- call

```java
V
call()
throws
Exception
```

Computes a result, or throws an exception if unable to do so.

**Returns:** computed result
**Throws:** Exception

- if unable to compute a result

---

#### Method Detail

call

```java
V
call()
throws
Exception
```

Computes a result, or throws an exception if unable to do so.

**Returns:** computed result
**Throws:** Exception

- if unable to compute a result

---

#### call

V

call()
throws

Exception

Computes a result, or throws an exception if unable to do so.

---

