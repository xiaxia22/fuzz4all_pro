# Class PKIXCertPathChecker

**Source:** `java.base\java\security\cert\PKIXCertPathChecker.html`

### Class Description

```java
public abstract class
PKIXCertPathChecker

extends
Object

implements
CertPathChecker
,
Cloneable
```

An abstract class that performs one or more checks on an

X509Certificate

.

A concrete implementation of the

PKIXCertPathChecker

class
can be created to extend the PKIX certification path validation algorithm.
For example, an implementation may check for and process a critical private
extension of each certificate in a certification path.

Instances of

PKIXCertPathChecker

are passed as parameters
using the

setCertPathCheckers

or

addCertPathChecker

methods
of the

PKIXParameters

and

PKIXBuilderParameters

class. Each of the

PKIXCertPathChecker

s

check

methods will be called, in turn, for each certificate processed by a PKIX

CertPathValidator

or

CertPathBuilder

implementation.

A

PKIXCertPathChecker

may be called multiple times on
successive certificates in a certification path. Concrete subclasses
are expected to maintain any internal state that may be necessary to
check successive certificates. The

init

method is used
to initialize the internal state of the checker so that the certificates
of a new certification path may be checked. A stateful implementation

must

override the

clone

method if necessary in
order to allow a PKIX

CertPathBuilder

to efficiently
backtrack and try other paths. In these situations, the

CertPathBuilder

is able to restore prior path validation
states by restoring the cloned

PKIXCertPathChecker

s.

The order in which the certificates are presented to the

PKIXCertPathChecker

may be either in the forward direction
(from target to most-trusted CA) or in the reverse direction (from
most-trusted CA to target). A

PKIXCertPathChecker

implementation

must

support reverse checking (the ability to perform its checks when
it is presented with certificates in the reverse direction) and

may

support forward checking (the ability to perform its checks when it is
presented with certificates in the forward direction). The

isForwardCheckingSupported

method
indicates whether forward checking is supported.

Additional input parameters required for executing the check may be
specified through constructors of concrete implementations of this class.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**All Implemented Interfaces:** Cloneable

,

CertPathChecker

---

### Field Details

*No entries found.*

### Constructor Details

#### protected PKIXCertPathChecker()

Default constructor.

---

### Method Details

#### public abstract void init​(boolean forward)
throws
CertPathValidatorException

Initializes the internal state of this

PKIXCertPathChecker

.

The

forward

flag specifies the order that
certificates will be passed to the

check

method
(forward or reverse). A

PKIXCertPathChecker

must

support reverse checking and

may

support forward checking.

**Specified by:**
- init

in interface

CertPathChecker

**Parameters:**
- forward

- the order that certificates are presented to
the

check

method. If

true

, certificates
are presented from target to most-trusted CA (forward); if

false

, from most-trusted CA to target (reverse).

**Throws:**
- CertPathValidatorException

- if this

PKIXCertPathChecker

is unable to check certificates in
the specified order; it should never be thrown if the forward flag
is false since reverse checking must be supported

---

#### public abstract boolean isForwardCheckingSupported()

Indicates if forward checking is supported. Forward checking refers
to the ability of the

PKIXCertPathChecker

to perform
its checks when certificates are presented to the

check

method in the forward direction (from target to most-trusted CA).

**Specified by:**
- isForwardCheckingSupported

in interface

CertPathChecker

**Returns:**
- true

if forward checking is supported,

false

otherwise

---

#### public abstract
Set
<
String
> getSupportedExtensions()

Returns an immutable

Set

of X.509 certificate extensions
that this

PKIXCertPathChecker

supports (i.e. recognizes, is
able to process), or

null

if no extensions are supported.

Each element of the set is a

String

representing the
Object Identifier (OID) of the X.509 extension that is supported.
The OID is represented by a set of nonnegative integers separated by
periods.

All X.509 certificate extensions that a

PKIXCertPathChecker

might possibly be able to process should be included in the set.

**Returns:**
- an immutable

Set

of X.509 extension OIDs (in

String

format) supported by this

PKIXCertPathChecker

, or

null

if no
extensions are supported

---

#### public abstract void check​(
Certificate
cert,

Collection
<
String
> unresolvedCritExts)
throws
CertPathValidatorException

Performs the check(s) on the specified certificate using its internal
state and removes any critical extensions that it processes from the
specified collection of OID strings that represent the unresolved
critical extensions. The certificates are presented in the order
specified by the

init

method.

**Parameters:**
- cert

- the

Certificate

to be checked
- unresolvedCritExts

- a

Collection

of OID strings
representing the current set of unresolved critical extensions

**Throws:**
- CertPathValidatorException

- if the specified certificate does
not pass the check

---

#### public void check​(
Certificate
cert)
throws
CertPathValidatorException

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

This implementation calls

check(cert, java.util.Collections.<String>emptySet())

.

**Specified by:**
- check

in interface

CertPathChecker

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

#### public
Object
clone()

Returns a clone of this object. Calls the

Object.clone()

method.
All subclasses which maintain state must support and
override this method, if necessary.

**Overrides:**
- clone

in class

Object

**Returns:**
- a copy of this

PKIXCertPathChecker

**See Also:**
- Cloneable

---

### Additional Sections

#### Class PKIXCertPathChecker

java.lang.Object

- java.security.cert.PKIXCertPathChecker

java.security.cert.PKIXCertPathChecker

**All Implemented Interfaces:** Cloneable

,

CertPathChecker

**Direct Known Subclasses:** PKIXRevocationChecker

```java
public abstract class
PKIXCertPathChecker

extends
Object

implements
CertPathChecker
,
Cloneable
```

An abstract class that performs one or more checks on an

X509Certificate

.

A concrete implementation of the

PKIXCertPathChecker

class
can be created to extend the PKIX certification path validation algorithm.
For example, an implementation may check for and process a critical private
extension of each certificate in a certification path.

Instances of

PKIXCertPathChecker

are passed as parameters
using the

setCertPathCheckers

or

addCertPathChecker

methods
of the

PKIXParameters

and

PKIXBuilderParameters

class. Each of the

PKIXCertPathChecker

s

check

methods will be called, in turn, for each certificate processed by a PKIX

CertPathValidator

or

CertPathBuilder

implementation.

A

PKIXCertPathChecker

may be called multiple times on
successive certificates in a certification path. Concrete subclasses
are expected to maintain any internal state that may be necessary to
check successive certificates. The

init

method is used
to initialize the internal state of the checker so that the certificates
of a new certification path may be checked. A stateful implementation

must

override the

clone

method if necessary in
order to allow a PKIX

CertPathBuilder

to efficiently
backtrack and try other paths. In these situations, the

CertPathBuilder

is able to restore prior path validation
states by restoring the cloned

PKIXCertPathChecker

s.

The order in which the certificates are presented to the

PKIXCertPathChecker

may be either in the forward direction
(from target to most-trusted CA) or in the reverse direction (from
most-trusted CA to target). A

PKIXCertPathChecker

implementation

must

support reverse checking (the ability to perform its checks when
it is presented with certificates in the reverse direction) and

may

support forward checking (the ability to perform its checks when it is
presented with certificates in the forward direction). The

isForwardCheckingSupported

method
indicates whether forward checking is supported.

Additional input parameters required for executing the check may be
specified through constructors of concrete implementations of this class.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** PKIXParameters

,

PKIXBuilderParameters

public abstract class

PKIXCertPathChecker

extends

Object

implements

CertPathChecker

,

Cloneable

An abstract class that performs one or more checks on an

X509Certificate

.

A concrete implementation of the

PKIXCertPathChecker

class
can be created to extend the PKIX certification path validation algorithm.
For example, an implementation may check for and process a critical private
extension of each certificate in a certification path.

Instances of

PKIXCertPathChecker

are passed as parameters
using the

setCertPathCheckers

or

addCertPathChecker

methods
of the

PKIXParameters

and

PKIXBuilderParameters

class. Each of the

PKIXCertPathChecker

s

check

methods will be called, in turn, for each certificate processed by a PKIX

CertPathValidator

or

CertPathBuilder

implementation.

A

PKIXCertPathChecker

may be called multiple times on
successive certificates in a certification path. Concrete subclasses
are expected to maintain any internal state that may be necessary to
check successive certificates. The

init

method is used
to initialize the internal state of the checker so that the certificates
of a new certification path may be checked. A stateful implementation

must

override the

clone

method if necessary in
order to allow a PKIX

CertPathBuilder

to efficiently
backtrack and try other paths. In these situations, the

CertPathBuilder

is able to restore prior path validation
states by restoring the cloned

PKIXCertPathChecker

s.

The order in which the certificates are presented to the

PKIXCertPathChecker

may be either in the forward direction
(from target to most-trusted CA) or in the reverse direction (from
most-trusted CA to target). A

PKIXCertPathChecker

implementation

must

support reverse checking (the ability to perform its checks when
it is presented with certificates in the reverse direction) and

may

support forward checking (the ability to perform its checks when it is
presented with certificates in the forward direction). The

isForwardCheckingSupported

method
indicates whether forward checking is supported.

Additional input parameters required for executing the check may be
specified through constructors of concrete implementations of this class.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

A concrete implementation of the

PKIXCertPathChecker

class
can be created to extend the PKIX certification path validation algorithm.
For example, an implementation may check for and process a critical private
extension of each certificate in a certification path.

Instances of

PKIXCertPathChecker

are passed as parameters
using the

setCertPathCheckers

or

addCertPathChecker

methods
of the

PKIXParameters

and

PKIXBuilderParameters

class. Each of the

PKIXCertPathChecker

s

check

methods will be called, in turn, for each certificate processed by a PKIX

CertPathValidator

or

CertPathBuilder

implementation.

A

PKIXCertPathChecker

may be called multiple times on
successive certificates in a certification path. Concrete subclasses
are expected to maintain any internal state that may be necessary to
check successive certificates. The

init

method is used
to initialize the internal state of the checker so that the certificates
of a new certification path may be checked. A stateful implementation

must

override the

clone

method if necessary in
order to allow a PKIX

CertPathBuilder

to efficiently
backtrack and try other paths. In these situations, the

CertPathBuilder

is able to restore prior path validation
states by restoring the cloned

PKIXCertPathChecker

s.

The order in which the certificates are presented to the

PKIXCertPathChecker

may be either in the forward direction
(from target to most-trusted CA) or in the reverse direction (from
most-trusted CA to target). A

PKIXCertPathChecker

implementation

must

support reverse checking (the ability to perform its checks when
it is presented with certificates in the reverse direction) and

may

support forward checking (the ability to perform its checks when it is
presented with certificates in the forward direction). The

isForwardCheckingSupported

method
indicates whether forward checking is supported.

Additional input parameters required for executing the check may be
specified through constructors of concrete implementations of this class.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Instances of

PKIXCertPathChecker

are passed as parameters
using the

setCertPathCheckers

or

addCertPathChecker

methods
of the

PKIXParameters

and

PKIXBuilderParameters

class. Each of the

PKIXCertPathChecker

s

check

methods will be called, in turn, for each certificate processed by a PKIX

CertPathValidator

or

CertPathBuilder

implementation.

A

PKIXCertPathChecker

may be called multiple times on
successive certificates in a certification path. Concrete subclasses
are expected to maintain any internal state that may be necessary to
check successive certificates. The

init

method is used
to initialize the internal state of the checker so that the certificates
of a new certification path may be checked. A stateful implementation

must

override the

clone

method if necessary in
order to allow a PKIX

CertPathBuilder

to efficiently
backtrack and try other paths. In these situations, the

CertPathBuilder

is able to restore prior path validation
states by restoring the cloned

PKIXCertPathChecker

s.

The order in which the certificates are presented to the

PKIXCertPathChecker

may be either in the forward direction
(from target to most-trusted CA) or in the reverse direction (from
most-trusted CA to target). A

PKIXCertPathChecker

implementation

must

support reverse checking (the ability to perform its checks when
it is presented with certificates in the reverse direction) and

may

support forward checking (the ability to perform its checks when it is
presented with certificates in the forward direction). The

isForwardCheckingSupported

method
indicates whether forward checking is supported.

Additional input parameters required for executing the check may be
specified through constructors of concrete implementations of this class.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

A

PKIXCertPathChecker

may be called multiple times on
successive certificates in a certification path. Concrete subclasses
are expected to maintain any internal state that may be necessary to
check successive certificates. The

init

method is used
to initialize the internal state of the checker so that the certificates
of a new certification path may be checked. A stateful implementation

must

override the

clone

method if necessary in
order to allow a PKIX

CertPathBuilder

to efficiently
backtrack and try other paths. In these situations, the

CertPathBuilder

is able to restore prior path validation
states by restoring the cloned

PKIXCertPathChecker

s.

The order in which the certificates are presented to the

PKIXCertPathChecker

may be either in the forward direction
(from target to most-trusted CA) or in the reverse direction (from
most-trusted CA to target). A

PKIXCertPathChecker

implementation

must

support reverse checking (the ability to perform its checks when
it is presented with certificates in the reverse direction) and

may

support forward checking (the ability to perform its checks when it is
presented with certificates in the forward direction). The

isForwardCheckingSupported

method
indicates whether forward checking is supported.

Additional input parameters required for executing the check may be
specified through constructors of concrete implementations of this class.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

The order in which the certificates are presented to the

PKIXCertPathChecker

may be either in the forward direction
(from target to most-trusted CA) or in the reverse direction (from
most-trusted CA to target). A

PKIXCertPathChecker

implementation

must

support reverse checking (the ability to perform its checks when
it is presented with certificates in the reverse direction) and

may

support forward checking (the ability to perform its checks when it is
presented with certificates in the forward direction). The

isForwardCheckingSupported

method
indicates whether forward checking is supported.

Additional input parameters required for executing the check may be
specified through constructors of concrete implementations of this class.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Additional input parameters required for executing the check may be
specified through constructors of concrete implementations of this class.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PKIXCertPathChecker

()

Default constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

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

abstract void

check

​(

Certificate

cert,

Collection

<

String

> unresolvedCritExts)

Performs the check(s) on the specified certificate using its internal
state and removes any critical extensions that it processes from the
specified collection of OID strings that represent the unresolved
critical extensions.

Object

clone

()

Returns a clone of this object.

abstract

Set

<

String

>

getSupportedExtensions

()

Returns an immutable

Set

of X.509 certificate extensions
that this

PKIXCertPathChecker

supports (i.e. recognizes, is
able to process), or

null

if no extensions are supported.

abstract void

init

​(boolean forward)

Initializes the internal state of this

PKIXCertPathChecker

.

abstract boolean

isForwardCheckingSupported

()

Indicates if forward checking is supported.

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PKIXCertPathChecker

()

Default constructor.

---

#### Constructor Summary

Default constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

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

abstract void

check

​(

Certificate

cert,

Collection

<

String

> unresolvedCritExts)

Performs the check(s) on the specified certificate using its internal
state and removes any critical extensions that it processes from the
specified collection of OID strings that represent the unresolved
critical extensions.

Object

clone

()

Returns a clone of this object.

abstract

Set

<

String

>

getSupportedExtensions

()

Returns an immutable

Set

of X.509 certificate extensions
that this

PKIXCertPathChecker

supports (i.e. recognizes, is
able to process), or

null

if no extensions are supported.

abstract void

init

​(boolean forward)

Initializes the internal state of this

PKIXCertPathChecker

.

abstract boolean

isForwardCheckingSupported

()

Indicates if forward checking is supported.

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Performs the check(s) on the specified certificate using its internal
state.

Performs the check(s) on the specified certificate using its internal
state and removes any critical extensions that it processes from the
specified collection of OID strings that represent the unresolved
critical extensions.

Returns a clone of this object.

Returns an immutable

Set

of X.509 certificate extensions
that this

PKIXCertPathChecker

supports (i.e. recognizes, is
able to process), or

null

if no extensions are supported.

Initializes the internal state of this

PKIXCertPathChecker

.

Indicates if forward checking is supported.

Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PKIXCertPathChecker

```java
protected PKIXCertPathChecker()
```

Default constructor.

============ METHOD DETAIL ==========

- Method Detail

- init

```java
public abstract void init​(boolean forward)
throws
CertPathValidatorException
```

Initializes the internal state of this

PKIXCertPathChecker

.

The

forward

flag specifies the order that
certificates will be passed to the

check

method
(forward or reverse). A

PKIXCertPathChecker

must

support reverse checking and

may

support forward checking.

**Specified by:** init

in interface

CertPathChecker
**Parameters:** forward

- the order that certificates are presented to
the

check

method. If

true

, certificates
are presented from target to most-trusted CA (forward); if

false

, from most-trusted CA to target (reverse).
**Throws:** CertPathValidatorException

- if this

PKIXCertPathChecker

is unable to check certificates in
the specified order; it should never be thrown if the forward flag
is false since reverse checking must be supported

- isForwardCheckingSupported

```java
public abstract boolean isForwardCheckingSupported()
```

Indicates if forward checking is supported. Forward checking refers
to the ability of the

PKIXCertPathChecker

to perform
its checks when certificates are presented to the

check

method in the forward direction (from target to most-trusted CA).

**Specified by:** isForwardCheckingSupported

in interface

CertPathChecker
**Returns:** true

if forward checking is supported,

false

otherwise

- getSupportedExtensions

```java
public abstract
Set
<
String
> getSupportedExtensions()
```

Returns an immutable

Set

of X.509 certificate extensions
that this

PKIXCertPathChecker

supports (i.e. recognizes, is
able to process), or

null

if no extensions are supported.

Each element of the set is a

String

representing the
Object Identifier (OID) of the X.509 extension that is supported.
The OID is represented by a set of nonnegative integers separated by
periods.

All X.509 certificate extensions that a

PKIXCertPathChecker

might possibly be able to process should be included in the set.

**Returns:** an immutable

Set

of X.509 extension OIDs (in

String

format) supported by this

PKIXCertPathChecker

, or

null

if no
extensions are supported

- check

```java
public abstract void check​(
Certificate
cert,

Collection
<
String
> unresolvedCritExts)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state and removes any critical extensions that it processes from the
specified collection of OID strings that represent the unresolved
critical extensions. The certificates are presented in the order
specified by the

init

method.

**Parameters:** cert

- the

Certificate

to be checked
**Parameters:** unresolvedCritExts

- a

Collection

of OID strings
representing the current set of unresolved critical extensions
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

- check

```java
public void check​(
Certificate
cert)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

This implementation calls

check(cert, java.util.Collections.<String>emptySet())

.

**Specified by:** check

in interface

CertPathChecker
**Parameters:** cert

- the

Certificate

to be checked
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

- clone

```java
public
Object
clone()
```

Returns a clone of this object. Calls the

Object.clone()

method.
All subclasses which maintain state must support and
override this method, if necessary.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

PKIXCertPathChecker
**See Also:** Cloneable

Constructor Detail

- PKIXCertPathChecker

```java
protected PKIXCertPathChecker()
```

Default constructor.

---

#### Constructor Detail

PKIXCertPathChecker

```java
protected PKIXCertPathChecker()
```

Default constructor.

---

#### PKIXCertPathChecker

protected PKIXCertPathChecker()

Default constructor.

Method Detail

- init

```java
public abstract void init​(boolean forward)
throws
CertPathValidatorException
```

Initializes the internal state of this

PKIXCertPathChecker

.

The

forward

flag specifies the order that
certificates will be passed to the

check

method
(forward or reverse). A

PKIXCertPathChecker

must

support reverse checking and

may

support forward checking.

**Specified by:** init

in interface

CertPathChecker
**Parameters:** forward

- the order that certificates are presented to
the

check

method. If

true

, certificates
are presented from target to most-trusted CA (forward); if

false

, from most-trusted CA to target (reverse).
**Throws:** CertPathValidatorException

- if this

PKIXCertPathChecker

is unable to check certificates in
the specified order; it should never be thrown if the forward flag
is false since reverse checking must be supported

- isForwardCheckingSupported

```java
public abstract boolean isForwardCheckingSupported()
```

Indicates if forward checking is supported. Forward checking refers
to the ability of the

PKIXCertPathChecker

to perform
its checks when certificates are presented to the

check

method in the forward direction (from target to most-trusted CA).

**Specified by:** isForwardCheckingSupported

in interface

CertPathChecker
**Returns:** true

if forward checking is supported,

false

otherwise

- getSupportedExtensions

```java
public abstract
Set
<
String
> getSupportedExtensions()
```

Returns an immutable

Set

of X.509 certificate extensions
that this

PKIXCertPathChecker

supports (i.e. recognizes, is
able to process), or

null

if no extensions are supported.

Each element of the set is a

String

representing the
Object Identifier (OID) of the X.509 extension that is supported.
The OID is represented by a set of nonnegative integers separated by
periods.

All X.509 certificate extensions that a

PKIXCertPathChecker

might possibly be able to process should be included in the set.

**Returns:** an immutable

Set

of X.509 extension OIDs (in

String

format) supported by this

PKIXCertPathChecker

, or

null

if no
extensions are supported

- check

```java
public abstract void check​(
Certificate
cert,

Collection
<
String
> unresolvedCritExts)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state and removes any critical extensions that it processes from the
specified collection of OID strings that represent the unresolved
critical extensions. The certificates are presented in the order
specified by the

init

method.

**Parameters:** cert

- the

Certificate

to be checked
**Parameters:** unresolvedCritExts

- a

Collection

of OID strings
representing the current set of unresolved critical extensions
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

- check

```java
public void check​(
Certificate
cert)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

This implementation calls

check(cert, java.util.Collections.<String>emptySet())

.

**Specified by:** check

in interface

CertPathChecker
**Parameters:** cert

- the

Certificate

to be checked
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

- clone

```java
public
Object
clone()
```

Returns a clone of this object. Calls the

Object.clone()

method.
All subclasses which maintain state must support and
override this method, if necessary.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

PKIXCertPathChecker
**See Also:** Cloneable

---

#### Method Detail

init

```java
public abstract void init​(boolean forward)
throws
CertPathValidatorException
```

Initializes the internal state of this

PKIXCertPathChecker

.

The

forward

flag specifies the order that
certificates will be passed to the

check

method
(forward or reverse). A

PKIXCertPathChecker

must

support reverse checking and

may

support forward checking.

**Specified by:** init

in interface

CertPathChecker
**Parameters:** forward

- the order that certificates are presented to
the

check

method. If

true

, certificates
are presented from target to most-trusted CA (forward); if

false

, from most-trusted CA to target (reverse).
**Throws:** CertPathValidatorException

- if this

PKIXCertPathChecker

is unable to check certificates in
the specified order; it should never be thrown if the forward flag
is false since reverse checking must be supported

---

#### init

public abstract void init​(boolean forward)
throws

CertPathValidatorException

Initializes the internal state of this

PKIXCertPathChecker

.

The

forward

flag specifies the order that
certificates will be passed to the

check

method
(forward or reverse). A

PKIXCertPathChecker

must

support reverse checking and

may

support forward checking.

The

forward

flag specifies the order that
certificates will be passed to the

check

method
(forward or reverse). A

PKIXCertPathChecker

must

support reverse checking and

may

support forward checking.

isForwardCheckingSupported

```java
public abstract boolean isForwardCheckingSupported()
```

Indicates if forward checking is supported. Forward checking refers
to the ability of the

PKIXCertPathChecker

to perform
its checks when certificates are presented to the

check

method in the forward direction (from target to most-trusted CA).

**Specified by:** isForwardCheckingSupported

in interface

CertPathChecker
**Returns:** true

if forward checking is supported,

false

otherwise

---

#### isForwardCheckingSupported

public abstract boolean isForwardCheckingSupported()

Indicates if forward checking is supported. Forward checking refers
to the ability of the

PKIXCertPathChecker

to perform
its checks when certificates are presented to the

check

method in the forward direction (from target to most-trusted CA).

getSupportedExtensions

```java
public abstract
Set
<
String
> getSupportedExtensions()
```

Returns an immutable

Set

of X.509 certificate extensions
that this

PKIXCertPathChecker

supports (i.e. recognizes, is
able to process), or

null

if no extensions are supported.

Each element of the set is a

String

representing the
Object Identifier (OID) of the X.509 extension that is supported.
The OID is represented by a set of nonnegative integers separated by
periods.

All X.509 certificate extensions that a

PKIXCertPathChecker

might possibly be able to process should be included in the set.

**Returns:** an immutable

Set

of X.509 extension OIDs (in

String

format) supported by this

PKIXCertPathChecker

, or

null

if no
extensions are supported

---

#### getSupportedExtensions

public abstract

Set

<

String

> getSupportedExtensions()

Returns an immutable

Set

of X.509 certificate extensions
that this

PKIXCertPathChecker

supports (i.e. recognizes, is
able to process), or

null

if no extensions are supported.

Each element of the set is a

String

representing the
Object Identifier (OID) of the X.509 extension that is supported.
The OID is represented by a set of nonnegative integers separated by
periods.

All X.509 certificate extensions that a

PKIXCertPathChecker

might possibly be able to process should be included in the set.

Each element of the set is a

String

representing the
Object Identifier (OID) of the X.509 extension that is supported.
The OID is represented by a set of nonnegative integers separated by
periods.

All X.509 certificate extensions that a

PKIXCertPathChecker

might possibly be able to process should be included in the set.

All X.509 certificate extensions that a

PKIXCertPathChecker

might possibly be able to process should be included in the set.

check

```java
public abstract void check​(
Certificate
cert,

Collection
<
String
> unresolvedCritExts)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state and removes any critical extensions that it processes from the
specified collection of OID strings that represent the unresolved
critical extensions. The certificates are presented in the order
specified by the

init

method.

**Parameters:** cert

- the

Certificate

to be checked
**Parameters:** unresolvedCritExts

- a

Collection

of OID strings
representing the current set of unresolved critical extensions
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

---

#### check

public abstract void check​(

Certificate

cert,

Collection

<

String

> unresolvedCritExts)
throws

CertPathValidatorException

Performs the check(s) on the specified certificate using its internal
state and removes any critical extensions that it processes from the
specified collection of OID strings that represent the unresolved
critical extensions. The certificates are presented in the order
specified by the

init

method.

check

```java
public void check​(
Certificate
cert)
throws
CertPathValidatorException
```

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

This implementation calls

check(cert, java.util.Collections.<String>emptySet())

.

**Specified by:** check

in interface

CertPathChecker
**Parameters:** cert

- the

Certificate

to be checked
**Throws:** CertPathValidatorException

- if the specified certificate does
not pass the check

---

#### check

public void check​(

Certificate

cert)
throws

CertPathValidatorException

Performs the check(s) on the specified certificate using its internal
state. The certificates are presented in the order specified by the

init

method.

This implementation calls

check(cert, java.util.Collections.<String>emptySet())

.

This implementation calls

check(cert, java.util.Collections.<String>emptySet())

.

clone

```java
public
Object
clone()
```

Returns a clone of this object. Calls the

Object.clone()

method.
All subclasses which maintain state must support and
override this method, if necessary.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

PKIXCertPathChecker
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a clone of this object. Calls the

Object.clone()

method.
All subclasses which maintain state must support and
override this method, if necessary.

---

