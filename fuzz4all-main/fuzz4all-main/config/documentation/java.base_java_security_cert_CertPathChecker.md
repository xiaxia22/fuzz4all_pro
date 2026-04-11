# Interface CertPathChecker

**Source:** `java.base\java\security\cert\CertPathChecker.html`

### Class Description

```java
public interface
CertPathChecker
```

Performs one or more checks on each

Certificate

of a

CertPath

.

A

CertPathChecker

implementation is typically created to extend
a certification path validation algorithm. For example, an implementation
may check for and process a critical private extension of each certificate
in a certification path.

**All Known Implementing Classes:** PKIXCertPathChecker

,

PKIXRevocationChecker

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void init​(boolean forward)
throws
CertPathValidatorException

Initializes the internal state of this

CertPathChecker

.

The

forward

flag specifies the order that certificates will
be passed to the

check

method (forward or reverse).

**Parameters:**
- forward

- the order that certificates are presented to the

check

method. If

true

, certificates are
presented from target to trust anchor (forward); if

false

, from trust anchor to target (reverse).

**Throws:**
- CertPathValidatorException

- if this

CertPathChecker

is
unable to check certificates in the specified order

---

#### boolean isForwardCheckingSupported()

Indicates if forward checking is supported. Forward checking refers
to the ability of the

CertPathChecker

to perform its checks
when certificates are presented to the

check

method in the
forward direction (from target to trust anchor).

**Returns:**
- true

if forward checking is supported,

false

otherwise

---

#### void check​(
Certificate
cert)
throws
CertPathValidatorException

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

**Parameters:**
- cert

- the

Certificate

to be checked

**Throws:**
- CertPathValidatorException

- if the specified certificate does
not pass the check

---

### Additional Sections

#### Interface CertPathChecker

**All Known Implementing Classes:** PKIXCertPathChecker

,

PKIXRevocationChecker

```java
public interface
CertPathChecker
```

Performs one or more checks on each

Certificate

of a

CertPath

.

A

CertPathChecker

implementation is typically created to extend
a certification path validation algorithm. For example, an implementation
may check for and process a critical private extension of each certificate
in a certification path.

**Since:** 1.8

public interface

CertPathChecker

Performs one or more checks on each

Certificate

of a

CertPath

.

A

CertPathChecker

implementation is typically created to extend
a certification path validation algorithm. For example, an implementation
may check for and process a critical private extension of each certificate
in a certification path.

A

CertPathChecker

implementation is typically created to extend
a certification path validation algorithm. For example, an implementation
may check for and process a critical private extension of each certificate
in a certification path.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

check

​(

Certificate

cert)

Performs the check(s) on the specified certificate using its internal
state.

void

init

​(boolean forward)

Initializes the internal state of this

CertPathChecker

.

boolean

isForwardCheckingSupported

()

Indicates if forward checking is supported.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

check

​(

Certificate

cert)

Performs the check(s) on the specified certificate using its internal
state.

void

init

​(boolean forward)

Initializes the internal state of this

CertPathChecker

.

boolean

isForwardCheckingSupported

()

Indicates if forward checking is supported.

---

#### Method Summary

Performs the check(s) on the specified certificate using its internal
state.

Initializes the internal state of this

CertPathChecker

.

Indicates if forward checking is supported.

============ METHOD DETAIL ==========

- Method Detail

- init

```java
void init​(boolean forward)
throws
CertPathValidatorException
```

Initializes the internal state of this

CertPathChecker

.

The

forward

flag specifies the order that certificates will
be passed to the

check

method (forward or reverse).

**Parameters:** forward

- the order that certificates are presented to the

check

method. If

true

, certificates are
presented from target to trust anchor (forward); if

false

, from trust anchor to target (reverse).
**Throws:** CertPathValidatorException

- if this

CertPathChecker

is
unable to check certificates in the specified order

- isForwardCheckingSupported

```java
boolean isForwardCheckingSupported()
```

Indicates if forward checking is supported. Forward checking refers
to the ability of the

CertPathChecker

to perform its checks
when certificates are presented to the

check

method in the
forward direction (from target to trust anchor).

**Returns:** true

if forward checking is supported,

false

otherwise

- check

```java
void check​(
Certificate
cert)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

**Parameters:** cert

- the

Certificate

to be checked
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

Method Detail

- init

```java
void init​(boolean forward)
throws
CertPathValidatorException
```

Initializes the internal state of this

CertPathChecker

.

The

forward

flag specifies the order that certificates will
be passed to the

check

method (forward or reverse).

**Parameters:** forward

- the order that certificates are presented to the

check

method. If

true

, certificates are
presented from target to trust anchor (forward); if

false

, from trust anchor to target (reverse).
**Throws:** CertPathValidatorException

- if this

CertPathChecker

is
unable to check certificates in the specified order

- isForwardCheckingSupported

```java
boolean isForwardCheckingSupported()
```

Indicates if forward checking is supported. Forward checking refers
to the ability of the

CertPathChecker

to perform its checks
when certificates are presented to the

check

method in the
forward direction (from target to trust anchor).

**Returns:** true

if forward checking is supported,

false

otherwise

- check

```java
void check​(
Certificate
cert)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

**Parameters:** cert

- the

Certificate

to be checked
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

---

#### Method Detail

init

```java
void init​(boolean forward)
throws
CertPathValidatorException
```

Initializes the internal state of this

CertPathChecker

.

The

forward

flag specifies the order that certificates will
be passed to the

check

method (forward or reverse).

**Parameters:** forward

- the order that certificates are presented to the

check

method. If

true

, certificates are
presented from target to trust anchor (forward); if

false

, from trust anchor to target (reverse).
**Throws:** CertPathValidatorException

- if this

CertPathChecker

is
unable to check certificates in the specified order

---

#### init

void init​(boolean forward)
throws

CertPathValidatorException

Initializes the internal state of this

CertPathChecker

.

The

forward

flag specifies the order that certificates will
be passed to the

check

method (forward or reverse).

The

forward

flag specifies the order that certificates will
be passed to the

check

method (forward or reverse).

isForwardCheckingSupported

```java
boolean isForwardCheckingSupported()
```

Indicates if forward checking is supported. Forward checking refers
to the ability of the

CertPathChecker

to perform its checks
when certificates are presented to the

check

method in the
forward direction (from target to trust anchor).

**Returns:** true

if forward checking is supported,

false

otherwise

---

#### isForwardCheckingSupported

boolean isForwardCheckingSupported()

Indicates if forward checking is supported. Forward checking refers
to the ability of the

CertPathChecker

to perform its checks
when certificates are presented to the

check

method in the
forward direction (from target to trust anchor).

check

```java
void check​(
Certificate
cert)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

**Parameters:** cert

- the

Certificate

to be checked
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

---

#### check

void check​(

Certificate

cert)
throws

CertPathValidatorException

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

---

