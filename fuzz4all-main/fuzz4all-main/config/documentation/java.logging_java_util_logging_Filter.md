# Interface Filter

**Source:** `java.logging\java\util\logging\Filter.html`

### Class Description

```java
@FunctionalInterface

public interface
Filter
```

A Filter can be used to provide fine grain control over
what is logged, beyond the control provided by log levels.

Each Logger and each Handler can have a filter associated with it.
The Logger or Handler will call the isLoggable method to check
if a given LogRecord should be published. If isLoggable returns
false, the LogRecord will be discarded.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isLoggable​(
LogRecord
record)

Check if a given log record should be published.

**Parameters:**
- record

- a LogRecord

**Returns:**
- true if the log record should be published.

---

### Additional Sections

#### Interface Filter

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
Filter
```

A Filter can be used to provide fine grain control over
what is logged, beyond the control provided by log levels.

Each Logger and each Handler can have a filter associated with it.
The Logger or Handler will call the isLoggable method to check
if a given LogRecord should be published. If isLoggable returns
false, the LogRecord will be discarded.

**Since:** 1.4

@FunctionalInterface

public interface

Filter

A Filter can be used to provide fine grain control over
what is logged, beyond the control provided by log levels.

Each Logger and each Handler can have a filter associated with it.
The Logger or Handler will call the isLoggable method to check
if a given LogRecord should be published. If isLoggable returns
false, the LogRecord will be discarded.

Each Logger and each Handler can have a filter associated with it.
The Logger or Handler will call the isLoggable method to check
if a given LogRecord should be published. If isLoggable returns
false, the LogRecord will be discarded.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isLoggable

​(

LogRecord

record)

Check if a given log record should be published.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isLoggable

​(

LogRecord

record)

Check if a given log record should be published.

---

#### Method Summary

Check if a given log record should be published.

============ METHOD DETAIL ==========

- Method Detail

- isLoggable

```java
boolean isLoggable​(
LogRecord
record)
```

Check if a given log record should be published.

**Parameters:** record

- a LogRecord
**Returns:** true if the log record should be published.

Method Detail

- isLoggable

```java
boolean isLoggable​(
LogRecord
record)
```

Check if a given log record should be published.

**Parameters:** record

- a LogRecord
**Returns:** true if the log record should be published.

---

#### Method Detail

isLoggable

```java
boolean isLoggable​(
LogRecord
record)
```

Check if a given log record should be published.

**Parameters:** record

- a LogRecord
**Returns:** true if the log record should be published.

---

#### isLoggable

boolean isLoggable​(

LogRecord

record)

Check if a given log record should be published.

---

