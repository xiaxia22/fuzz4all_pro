# Interface DocErrorReporter

**Source:** `jdk.javadoc\com\sun\javadoc\DocErrorReporter.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
DocErrorReporter
```

This interface provides error, warning and notice printing.

**All Known Subinterfaces:** RootDoc

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void printError​(
String
msg)

Print error message and increment error count.

**Parameters:**
- msg

- message to print

---

#### void printError​(
SourcePosition
pos,

String
msg)

Print an error message and increment error count.

**Parameters:**
- pos

- the position item where the error occurs
- msg

- message to print

**Since:**
- 1.4

---

#### void printWarning​(
String
msg)

Print warning message and increment warning count.

**Parameters:**
- msg

- message to print

---

#### void printWarning​(
SourcePosition
pos,

String
msg)

Print warning message and increment warning count.

**Parameters:**
- pos

- the position item where the warning occurs
- msg

- message to print

**Since:**
- 1.4

---

#### void printNotice​(
String
msg)

Print a message.

**Parameters:**
- msg

- message to print

---

#### void printNotice​(
SourcePosition
pos,

String
msg)

Print a message.

**Parameters:**
- pos

- the position item where the message occurs
- msg

- message to print

**Since:**
- 1.4

---

### Additional Sections

#### Interface DocErrorReporter

**All Known Subinterfaces:** RootDoc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
DocErrorReporter
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

This interface provides error, warning and notice printing.

**Since:** 1.2

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

DocErrorReporter

This interface provides error, warning and notice printing.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

printError

​(

SourcePosition

pos,

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print an error message and increment error count.

void

printError

​(

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print error message and increment error count.

void

printNotice

​(

SourcePosition

pos,

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

void

printNotice

​(

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

void

printWarning

​(

SourcePosition

pos,

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

void

printWarning

​(

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

printError

​(

SourcePosition

pos,

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print an error message and increment error count.

void

printError

​(

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print error message and increment error count.

void

printNotice

​(

SourcePosition

pos,

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

void

printNotice

​(

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

void

printWarning

​(

SourcePosition

pos,

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

void

printWarning

​(

String

msg)

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Print an error message and increment error count.

Print error message and increment error count.

Print a message.

Print warning message and increment warning count.

============ METHOD DETAIL ==========

- Method Detail

- printError

```java
void printError​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print error message and increment error count.

**Parameters:** msg

- message to print

- printError

```java
void printError​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print an error message and increment error count.

**Parameters:** pos

- the position item where the error occurs
**Parameters:** msg

- message to print
**Since:** 1.4

- printWarning

```java
void printWarning​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

**Parameters:** msg

- message to print

- printWarning

```java
void printWarning​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

**Parameters:** pos

- the position item where the warning occurs
**Parameters:** msg

- message to print
**Since:** 1.4

- printNotice

```java
void printNotice​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

**Parameters:** msg

- message to print

- printNotice

```java
void printNotice​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

**Parameters:** pos

- the position item where the message occurs
**Parameters:** msg

- message to print
**Since:** 1.4

Method Detail

- printError

```java
void printError​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print error message and increment error count.

**Parameters:** msg

- message to print

- printError

```java
void printError​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print an error message and increment error count.

**Parameters:** pos

- the position item where the error occurs
**Parameters:** msg

- message to print
**Since:** 1.4

- printWarning

```java
void printWarning​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

**Parameters:** msg

- message to print

- printWarning

```java
void printWarning​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

**Parameters:** pos

- the position item where the warning occurs
**Parameters:** msg

- message to print
**Since:** 1.4

- printNotice

```java
void printNotice​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

**Parameters:** msg

- message to print

- printNotice

```java
void printNotice​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

**Parameters:** pos

- the position item where the message occurs
**Parameters:** msg

- message to print
**Since:** 1.4

---

#### Method Detail

printError

```java
void printError​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print error message and increment error count.

**Parameters:** msg

- message to print

---

#### printError

void printError​(

String

msg)

Print error message and increment error count.

printError

```java
void printError​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print an error message and increment error count.

**Parameters:** pos

- the position item where the error occurs
**Parameters:** msg

- message to print
**Since:** 1.4

---

#### printError

void printError​(

SourcePosition

pos,

String

msg)

Print an error message and increment error count.

printWarning

```java
void printWarning​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

**Parameters:** msg

- message to print

---

#### printWarning

void printWarning​(

String

msg)

Print warning message and increment warning count.

printWarning

```java
void printWarning​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print warning message and increment warning count.

**Parameters:** pos

- the position item where the warning occurs
**Parameters:** msg

- message to print
**Since:** 1.4

---

#### printWarning

void printWarning​(

SourcePosition

pos,

String

msg)

Print warning message and increment warning count.

printNotice

```java
void printNotice​(
String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

**Parameters:** msg

- message to print

---

#### printNotice

void printNotice​(

String

msg)

Print a message.

printNotice

```java
void printNotice​(
SourcePosition
pos,

String
msg)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Print a message.

**Parameters:** pos

- the position item where the message occurs
**Parameters:** msg

- message to print
**Since:** 1.4

---

#### printNotice

void printNotice​(

SourcePosition

pos,

String

msg)

Print a message.

---

