# Interface Reporter

**Source:** `jdk.javadoc\jdk\javadoc\doclet\Reporter.html`

### Class Description

```java
public interface
Reporter
```

This interface provides error, warning and notice reporting.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void print​(
Diagnostic.Kind
kind,

String
msg)

Print error message and increment error count.

**Parameters:**
- kind

- specify the diagnostic kind
- msg

- message to print

---

#### void print​(
Diagnostic.Kind
kind,

DocTreePath
path,

String
msg)

Print an error message and increment error count.

**Parameters:**
- kind

- specify the diagnostic kind
- path

- the DocTreePath of item where the error occurs
- msg

- message to print

---

#### void print​(
Diagnostic.Kind
kind,

Element
e,

String
msg)

Print an error message and increment error count.

**Parameters:**
- kind

- specify the diagnostic kind
- e

- the Element for which the error occurs
- msg

- message to print

---

### Additional Sections

#### Interface Reporter

```java
public interface
Reporter
```

This interface provides error, warning and notice reporting.

**Since:** 9

public interface

Reporter

This interface provides error, warning and notice reporting.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

print

​(

Diagnostic.Kind

kind,

DocTreePath

path,

String

msg)

Print an error message and increment error count.

void

print

​(

Diagnostic.Kind

kind,

String

msg)

Print error message and increment error count.

void

print

​(

Diagnostic.Kind

kind,

Element

e,

String

msg)

Print an error message and increment error count.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

print

​(

Diagnostic.Kind

kind,

DocTreePath

path,

String

msg)

Print an error message and increment error count.

void

print

​(

Diagnostic.Kind

kind,

String

msg)

Print error message and increment error count.

void

print

​(

Diagnostic.Kind

kind,

Element

e,

String

msg)

Print an error message and increment error count.

---

#### Method Summary

Print an error message and increment error count.

Print error message and increment error count.

============ METHOD DETAIL ==========

- Method Detail

- print

```java
void print​(
Diagnostic.Kind
kind,

String
msg)
```

Print error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** msg

- message to print

- print

```java
void print​(
Diagnostic.Kind
kind,

DocTreePath
path,

String
msg)
```

Print an error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** path

- the DocTreePath of item where the error occurs
**Parameters:** msg

- message to print

- print

```java
void print​(
Diagnostic.Kind
kind,

Element
e,

String
msg)
```

Print an error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** e

- the Element for which the error occurs
**Parameters:** msg

- message to print

Method Detail

- print

```java
void print​(
Diagnostic.Kind
kind,

String
msg)
```

Print error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** msg

- message to print

- print

```java
void print​(
Diagnostic.Kind
kind,

DocTreePath
path,

String
msg)
```

Print an error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** path

- the DocTreePath of item where the error occurs
**Parameters:** msg

- message to print

- print

```java
void print​(
Diagnostic.Kind
kind,

Element
e,

String
msg)
```

Print an error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** e

- the Element for which the error occurs
**Parameters:** msg

- message to print

---

#### Method Detail

print

```java
void print​(
Diagnostic.Kind
kind,

String
msg)
```

Print error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** msg

- message to print

---

#### print

void print​(

Diagnostic.Kind

kind,

String

msg)

Print error message and increment error count.

print

```java
void print​(
Diagnostic.Kind
kind,

DocTreePath
path,

String
msg)
```

Print an error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** path

- the DocTreePath of item where the error occurs
**Parameters:** msg

- message to print

---

#### print

void print​(

Diagnostic.Kind

kind,

DocTreePath

path,

String

msg)

Print an error message and increment error count.

print

```java
void print​(
Diagnostic.Kind
kind,

Element
e,

String
msg)
```

Print an error message and increment error count.

**Parameters:** kind

- specify the diagnostic kind
**Parameters:** e

- the Element for which the error occurs
**Parameters:** msg

- message to print

---

#### print

void print​(

Diagnostic.Kind

kind,

Element

e,

String

msg)

Print an error message and increment error count.

---

