# Class CertPathBuilderSpi

**Source:** `java.base\java\security\cert\CertPathBuilderSpi.html`

### Class Description

```java
public abstract class
CertPathBuilderSpi

extends
Object
```

The

Service Provider Interface

(

SPI

)
for the

CertPathBuilder

class. All

CertPathBuilder

implementations must include a class (the
SPI class) that extends this class (

CertPathBuilderSpi

) and
implements all of its methods. In general, instances of this class should
only be accessed through the

CertPathBuilder

class. For
details, see the Java Cryptography Architecture.

Concurrent Access

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathBuilderSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathBuilder

object.

However, implementations of

CertPathBuilderSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathBuilderSpi

instance need not
synchronize.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertPathBuilderSpi()

The default constructor.

---

### Method Details

#### public abstract
CertPathBuilderResult
engineBuild​(
CertPathParameters
params)
throws
CertPathBuilderException
,

InvalidAlgorithmParameterException

Attempts to build a certification path using the specified
algorithm parameter set.

**Parameters:**
- params

- the algorithm parameters

**Returns:**
- the result of the build algorithm

**Throws:**
- CertPathBuilderException

- if the builder is unable to construct
a certification path that satisfies the specified parameters
- InvalidAlgorithmParameterException

- if the specified parameters
are inappropriate for this

CertPathBuilder

---

#### public
CertPathChecker
engineGetRevocationChecker()

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates. A PKIX implementation
returns objects of type

PKIXRevocationChecker

.

The primary purpose of this method is to allow callers to specify
additional input parameters and options specific to revocation checking.
See the class description of

CertPathBuilder

for an example.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method cannot be abstract and by default throws
an

UnsupportedOperationException

.

**Returns:**
- a

CertPathChecker

that this implementation uses to
check the revocation status of certificates

**Throws:**
- UnsupportedOperationException

- if this method is not supported

**Since:**
- 1.8

---

### Additional Sections

#### Class CertPathBuilderSpi

java.lang.Object

- java.security.cert.CertPathBuilderSpi

java.security.cert.CertPathBuilderSpi

```java
public abstract class
CertPathBuilderSpi

extends
Object
```

The

Service Provider Interface

(

SPI

)
for the

CertPathBuilder

class. All

CertPathBuilder

implementations must include a class (the
SPI class) that extends this class (

CertPathBuilderSpi

) and
implements all of its methods. In general, instances of this class should
only be accessed through the

CertPathBuilder

class. For
details, see the Java Cryptography Architecture.

Concurrent Access

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathBuilderSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathBuilder

object.

However, implementations of

CertPathBuilderSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathBuilderSpi

instance need not
synchronize.

**Since:** 1.4

public abstract class

CertPathBuilderSpi

extends

Object

The

Service Provider Interface

(

SPI

)
for the

CertPathBuilder

class. All

CertPathBuilder

implementations must include a class (the
SPI class) that extends this class (

CertPathBuilderSpi

) and
implements all of its methods. In general, instances of this class should
only be accessed through the

CertPathBuilder

class. For
details, see the Java Cryptography Architecture.

Concurrent Access

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathBuilderSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathBuilder

object.

However, implementations of

CertPathBuilderSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathBuilderSpi

instance need not
synchronize.

Concurrent Access

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathBuilderSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathBuilder

object.

However, implementations of

CertPathBuilderSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathBuilderSpi

instance need not
synchronize.

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathBuilderSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathBuilder

object.

However, implementations of

CertPathBuilderSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathBuilderSpi

instance need not
synchronize.

However, implementations of

CertPathBuilderSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathBuilderSpi

instance need not
synchronize.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertPathBuilderSpi

()

The default constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

CertPathBuilderResult

engineBuild

​(

CertPathParameters

params)

Attempts to build a certification path using the specified
algorithm parameter set.

CertPathChecker

engineGetRevocationChecker

()

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates.

- Methods declared in class java.lang.

Object

clone

,

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

Constructor

Description

CertPathBuilderSpi

()

The default constructor.

---

#### Constructor Summary

The default constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

CertPathBuilderResult

engineBuild

​(

CertPathParameters

params)

Attempts to build a certification path using the specified
algorithm parameter set.

CertPathChecker

engineGetRevocationChecker

()

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates.

- Methods declared in class java.lang.

Object

clone

,

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

Attempts to build a certification path using the specified
algorithm parameter set.

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates.

Methods declared in class java.lang.

Object

clone

,

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

- CertPathBuilderSpi

```java
public CertPathBuilderSpi()
```

The default constructor.

============ METHOD DETAIL ==========

- Method Detail

- engineBuild

```java
public abstract
CertPathBuilderResult
engineBuild​(
CertPathParameters
params)
throws
CertPathBuilderException
,

InvalidAlgorithmParameterException
```

Attempts to build a certification path using the specified
algorithm parameter set.

**Parameters:** params

- the algorithm parameters
**Returns:** the result of the build algorithm
**Throws:** CertPathBuilderException

- if the builder is unable to construct
a certification path that satisfies the specified parameters
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are inappropriate for this

CertPathBuilder

- engineGetRevocationChecker

```java
public
CertPathChecker
engineGetRevocationChecker()
```

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates. A PKIX implementation
returns objects of type

PKIXRevocationChecker

.

The primary purpose of this method is to allow callers to specify
additional input parameters and options specific to revocation checking.
See the class description of

CertPathBuilder

for an example.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method cannot be abstract and by default throws
an

UnsupportedOperationException

.

**Returns:** a

CertPathChecker

that this implementation uses to
check the revocation status of certificates
**Throws:** UnsupportedOperationException

- if this method is not supported
**Since:** 1.8

Constructor Detail

- CertPathBuilderSpi

```java
public CertPathBuilderSpi()
```

The default constructor.

---

#### Constructor Detail

CertPathBuilderSpi

```java
public CertPathBuilderSpi()
```

The default constructor.

---

#### CertPathBuilderSpi

public CertPathBuilderSpi()

The default constructor.

Method Detail

- engineBuild

```java
public abstract
CertPathBuilderResult
engineBuild​(
CertPathParameters
params)
throws
CertPathBuilderException
,

InvalidAlgorithmParameterException
```

Attempts to build a certification path using the specified
algorithm parameter set.

**Parameters:** params

- the algorithm parameters
**Returns:** the result of the build algorithm
**Throws:** CertPathBuilderException

- if the builder is unable to construct
a certification path that satisfies the specified parameters
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are inappropriate for this

CertPathBuilder

- engineGetRevocationChecker

```java
public
CertPathChecker
engineGetRevocationChecker()
```

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates. A PKIX implementation
returns objects of type

PKIXRevocationChecker

.

The primary purpose of this method is to allow callers to specify
additional input parameters and options specific to revocation checking.
See the class description of

CertPathBuilder

for an example.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method cannot be abstract and by default throws
an

UnsupportedOperationException

.

**Returns:** a

CertPathChecker

that this implementation uses to
check the revocation status of certificates
**Throws:** UnsupportedOperationException

- if this method is not supported
**Since:** 1.8

---

#### Method Detail

engineBuild

```java
public abstract
CertPathBuilderResult
engineBuild​(
CertPathParameters
params)
throws
CertPathBuilderException
,

InvalidAlgorithmParameterException
```

Attempts to build a certification path using the specified
algorithm parameter set.

**Parameters:** params

- the algorithm parameters
**Returns:** the result of the build algorithm
**Throws:** CertPathBuilderException

- if the builder is unable to construct
a certification path that satisfies the specified parameters
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are inappropriate for this

CertPathBuilder

---

#### engineBuild

public abstract

CertPathBuilderResult

engineBuild​(

CertPathParameters

params)
throws

CertPathBuilderException

,

InvalidAlgorithmParameterException

Attempts to build a certification path using the specified
algorithm parameter set.

engineGetRevocationChecker

```java
public
CertPathChecker
engineGetRevocationChecker()
```

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates. A PKIX implementation
returns objects of type

PKIXRevocationChecker

.

The primary purpose of this method is to allow callers to specify
additional input parameters and options specific to revocation checking.
See the class description of

CertPathBuilder

for an example.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method cannot be abstract and by default throws
an

UnsupportedOperationException

.

**Returns:** a

CertPathChecker

that this implementation uses to
check the revocation status of certificates
**Throws:** UnsupportedOperationException

- if this method is not supported
**Since:** 1.8

---

#### engineGetRevocationChecker

public

CertPathChecker

engineGetRevocationChecker()

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates. A PKIX implementation
returns objects of type

PKIXRevocationChecker

.

The primary purpose of this method is to allow callers to specify
additional input parameters and options specific to revocation checking.
See the class description of

CertPathBuilder

for an example.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method cannot be abstract and by default throws
an

UnsupportedOperationException

.

The primary purpose of this method is to allow callers to specify
additional input parameters and options specific to revocation checking.
See the class description of

CertPathBuilder

for an example.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method cannot be abstract and by default throws
an

UnsupportedOperationException

.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method cannot be abstract and by default throws
an

UnsupportedOperationException

.

---

