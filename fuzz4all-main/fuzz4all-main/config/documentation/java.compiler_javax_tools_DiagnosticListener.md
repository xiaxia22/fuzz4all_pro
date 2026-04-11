# Interface DiagnosticListener<S>

**Source:** `java.compiler\javax\tools\DiagnosticListener.html`

### Class Description

```java
public interface
DiagnosticListener<S>
```

Interface for receiving diagnostics from tools.

**Type Parameters:** S

- the type of source objects used by diagnostics received
by this listener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void report​(
Diagnostic
<? extends
S
> diagnostic)

Invoked when a problem is found.

**Parameters:**
- diagnostic

- a diagnostic representing the problem that
was found

**Throws:**
- NullPointerException

- if the diagnostic argument is

null

and the implementation cannot handle

null

arguments

---

### Additional Sections

#### Interface DiagnosticListener<S>

**Type Parameters:** S

- the type of source objects used by diagnostics received
by this listener

**All Known Implementing Classes:** DiagnosticCollector

```java
public interface
DiagnosticListener<S>
```

Interface for receiving diagnostics from tools.

**Since:** 1.6

public interface

DiagnosticListener<S>

Interface for receiving diagnostics from tools.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

report

​(

Diagnostic

<? extends

S

> diagnostic)

Invoked when a problem is found.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

report

​(

Diagnostic

<? extends

S

> diagnostic)

Invoked when a problem is found.

---

#### Method Summary

Invoked when a problem is found.

============ METHOD DETAIL ==========

- Method Detail

- report

```java
void report​(
Diagnostic
<? extends
S
> diagnostic)
```

Invoked when a problem is found.

**Parameters:** diagnostic

- a diagnostic representing the problem that
was found
**Throws:** NullPointerException

- if the diagnostic argument is

null

and the implementation cannot handle

null

arguments

Method Detail

- report

```java
void report​(
Diagnostic
<? extends
S
> diagnostic)
```

Invoked when a problem is found.

**Parameters:** diagnostic

- a diagnostic representing the problem that
was found
**Throws:** NullPointerException

- if the diagnostic argument is

null

and the implementation cannot handle

null

arguments

---

#### Method Detail

report

```java
void report​(
Diagnostic
<? extends
S
> diagnostic)
```

Invoked when a problem is found.

**Parameters:** diagnostic

- a diagnostic representing the problem that
was found
**Throws:** NullPointerException

- if the diagnostic argument is

null

and the implementation cannot handle

null

arguments

---

#### report

void report​(

Diagnostic

<? extends

S

> diagnostic)

Invoked when a problem is found.

---

