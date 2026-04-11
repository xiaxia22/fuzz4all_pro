# Interface CompletionHandler<V,​A>

**Source:** `java.base\java\nio\channels\CompletionHandler.html`

### Class Description

```java
public interface
CompletionHandler<V,​A>
```

A handler for consuming the result of an asynchronous I/O operation.

The asynchronous channels defined in this package allow a completion
handler to be specified to consume the result of an asynchronous operation.
The

completed

method is invoked when the I/O operation
completes successfully. The

failed

method is invoked if the
I/O operations fails. The implementations of these methods should complete
in a timely manner so as to avoid keeping the invoking thread from dispatching
to other completion handlers.

**Type Parameters:** V

- The result type of the I/O operation
**Type Parameters:** A

- The type of the object attached to the I/O operation

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void completed​(
V
result,

A
attachment)

Invoked when an operation has completed.

**Parameters:**
- result

- The result of the I/O operation.
- attachment

- The object attached to the I/O operation when it was initiated.

---

#### void failed​(
Throwable
exc,

A
attachment)

Invoked when an operation fails.

**Parameters:**
- exc

- The exception to indicate why the I/O operation failed
- attachment

- The object attached to the I/O operation when it was initiated.

---

### Additional Sections

#### Interface CompletionHandler<V,​A>

**Type Parameters:** V

- The result type of the I/O operation
**Type Parameters:** A

- The type of the object attached to the I/O operation

```java
public interface
CompletionHandler<V,​A>
```

A handler for consuming the result of an asynchronous I/O operation.

The asynchronous channels defined in this package allow a completion
handler to be specified to consume the result of an asynchronous operation.
The

completed

method is invoked when the I/O operation
completes successfully. The

failed

method is invoked if the
I/O operations fails. The implementations of these methods should complete
in a timely manner so as to avoid keeping the invoking thread from dispatching
to other completion handlers.

**Since:** 1.7

public interface

CompletionHandler<V,​A>

A handler for consuming the result of an asynchronous I/O operation.

The asynchronous channels defined in this package allow a completion
handler to be specified to consume the result of an asynchronous operation.
The

completed

method is invoked when the I/O operation
completes successfully. The

failed

method is invoked if the
I/O operations fails. The implementations of these methods should complete
in a timely manner so as to avoid keeping the invoking thread from dispatching
to other completion handlers.

The asynchronous channels defined in this package allow a completion
handler to be specified to consume the result of an asynchronous operation.
The

completed

method is invoked when the I/O operation
completes successfully. The

failed

method is invoked if the
I/O operations fails. The implementations of these methods should complete
in a timely manner so as to avoid keeping the invoking thread from dispatching
to other completion handlers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

completed

​(

V

result,

A

attachment)

Invoked when an operation has completed.

void

failed

​(

Throwable

exc,

A

attachment)

Invoked when an operation fails.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

completed

​(

V

result,

A

attachment)

Invoked when an operation has completed.

void

failed

​(

Throwable

exc,

A

attachment)

Invoked when an operation fails.

---

#### Method Summary

Invoked when an operation has completed.

Invoked when an operation fails.

============ METHOD DETAIL ==========

- Method Detail

- completed

```java
void completed​(
V
result,

A
attachment)
```

Invoked when an operation has completed.

**Parameters:** result

- The result of the I/O operation.
**Parameters:** attachment

- The object attached to the I/O operation when it was initiated.

- failed

```java
void failed​(
Throwable
exc,

A
attachment)
```

Invoked when an operation fails.

**Parameters:** exc

- The exception to indicate why the I/O operation failed
**Parameters:** attachment

- The object attached to the I/O operation when it was initiated.

Method Detail

- completed

```java
void completed​(
V
result,

A
attachment)
```

Invoked when an operation has completed.

**Parameters:** result

- The result of the I/O operation.
**Parameters:** attachment

- The object attached to the I/O operation when it was initiated.

- failed

```java
void failed​(
Throwable
exc,

A
attachment)
```

Invoked when an operation fails.

**Parameters:** exc

- The exception to indicate why the I/O operation failed
**Parameters:** attachment

- The object attached to the I/O operation when it was initiated.

---

#### Method Detail

completed

```java
void completed​(
V
result,

A
attachment)
```

Invoked when an operation has completed.

**Parameters:** result

- The result of the I/O operation.
**Parameters:** attachment

- The object attached to the I/O operation when it was initiated.

---

#### completed

void completed​(

V

result,

A

attachment)

Invoked when an operation has completed.

failed

```java
void failed​(
Throwable
exc,

A
attachment)
```

Invoked when an operation fails.

**Parameters:** exc

- The exception to indicate why the I/O operation failed
**Parameters:** attachment

- The object attached to the I/O operation when it was initiated.

---

#### failed

void failed​(

Throwable

exc,

A

attachment)

Invoked when an operation fails.

---

