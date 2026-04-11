# Class CertPathValidatorSpi

**Source:** `java.base\java\security\cert\CertPathValidatorSpi.html`

### Class Description

```java
public abstract class
CertPathValidatorSpi

extends
Object
```

The

Service Provider Interface

(

SPI

)
for the

CertPathValidator

class. All

CertPathValidator

implementations must include a class (the
SPI class) that extends this class (

CertPathValidatorSpi

)
and implements all of its methods. In general, instances of this class
should only be accessed through the

CertPathValidator

class.
For details, see the Java Cryptography Architecture.

Concurrent Access

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathValidatorSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathValidator

object.

However, implementations of

CertPathValidatorSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathValidatorSpi

instance need not
synchronize.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertPathValidatorSpi()

The default constructor.

---

### Method Details

#### public abstract
CertPathValidatorResult
engineValidate​(
CertPath
certPath,

CertPathParameters
params)
throws
CertPathValidatorException
,

InvalidAlgorithmParameterException

Validates the specified certification path using the specified
algorithm parameter set.

The

CertPath

specified must be of a type that is
supported by the validation algorithm, otherwise an

InvalidAlgorithmParameterException

will be thrown. For
example, a

CertPathValidator

that implements the PKIX
algorithm validates

CertPath

objects of type X.509.

**Parameters:**
- certPath

- the

CertPath

to be validated
- params

- the algorithm parameters

**Returns:**
- the result of the validation algorithm

**Throws:**
- CertPathValidatorException

- if the

CertPath

does not validate
- InvalidAlgorithmParameterException

- if the specified
parameters or the type of the specified

CertPath

are
inappropriate for this

CertPathValidator

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

CertPathValidator

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

#### Class CertPathValidatorSpi

java.lang.Object

- java.security.cert.CertPathValidatorSpi

java.security.cert.CertPathValidatorSpi

```java
public abstract class
CertPathValidatorSpi

extends
Object
```

The

Service Provider Interface

(

SPI

)
for the

CertPathValidator

class. All

CertPathValidator

implementations must include a class (the
SPI class) that extends this class (

CertPathValidatorSpi

)
and implements all of its methods. In general, instances of this class
should only be accessed through the

CertPathValidator

class.
For details, see the Java Cryptography Architecture.

Concurrent Access

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathValidatorSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathValidator

object.

However, implementations of

CertPathValidatorSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathValidatorSpi

instance need not
synchronize.

**Since:** 1.4

public abstract class

CertPathValidatorSpi

extends

Object

The

Service Provider Interface

(

SPI

)
for the

CertPathValidator

class. All

CertPathValidator

implementations must include a class (the
SPI class) that extends this class (

CertPathValidatorSpi

)
and implements all of its methods. In general, instances of this class
should only be accessed through the

CertPathValidator

class.
For details, see the Java Cryptography Architecture.

Concurrent Access

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathValidatorSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathValidator

object.

However, implementations of

CertPathValidatorSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathValidatorSpi

instance need not
synchronize.

Concurrent Access

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathValidatorSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathValidator

object.

However, implementations of

CertPathValidatorSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathValidatorSpi

instance need not
synchronize.

Instances of this class need not be protected against concurrent
access from multiple threads. Threads that need to access a single

CertPathValidatorSpi

instance concurrently should synchronize
amongst themselves and provide the necessary locking before calling the
wrapping

CertPathValidator

object.

However, implementations of

CertPathValidatorSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathValidatorSpi

instance need not
synchronize.

However, implementations of

CertPathValidatorSpi

may still
encounter concurrency issues, since multiple threads each
manipulating a different

CertPathValidatorSpi

instance need not
synchronize.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertPathValidatorSpi

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

CertPathChecker

engineGetRevocationChecker

()

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates.

abstract

CertPathValidatorResult

engineValidate

​(

CertPath

certPath,

CertPathParameters

params)

Validates the specified certification path using the specified
algorithm parameter set.

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

CertPathValidatorSpi

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

CertPathChecker

engineGetRevocationChecker

()

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates.

abstract

CertPathValidatorResult

engineValidate

​(

CertPath

certPath,

CertPathParameters

params)

Validates the specified certification path using the specified
algorithm parameter set.

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

Returns a

CertPathChecker

that this implementation uses to
check the revocation status of certificates.

Validates the specified certification path using the specified
algorithm parameter set.

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

- CertPathValidatorSpi

```java
public CertPathValidatorSpi()
```

The default constructor.

============ METHOD DETAIL ==========

- Method Detail

- engineValidate

```java
public abstract
CertPathValidatorResult
engineValidate​(
CertPath
certPath,

CertPathParameters
params)
throws
CertPathValidatorException
,

InvalidAlgorithmParameterException
```

Validates the specified certification path using the specified
algorithm parameter set.

The

CertPath

specified must be of a type that is
supported by the validation algorithm, otherwise an

InvalidAlgorithmParameterException

will be thrown. For
example, a

CertPathValidator

that implements the PKIX
algorithm validates

CertPath

objects of type X.509.

**Parameters:** certPath

- the

CertPath

to be validated
**Parameters:** params

- the algorithm parameters
**Returns:** the result of the validation algorithm
**Throws:** CertPathValidatorException

- if the

CertPath

does not validate
**Throws:** InvalidAlgorithmParameterException

- if the specified
parameters or the type of the specified

CertPath

are
inappropriate for this

CertPathValidator

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

CertPathValidator

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

- CertPathValidatorSpi

```java
public CertPathValidatorSpi()
```

The default constructor.

---

#### Constructor Detail

CertPathValidatorSpi

```java
public CertPathValidatorSpi()
```

The default constructor.

---

#### CertPathValidatorSpi

public CertPathValidatorSpi()

The default constructor.

Method Detail

- engineValidate

```java
public abstract
CertPathValidatorResult
engineValidate​(
CertPath
certPath,

CertPathParameters
params)
throws
CertPathValidatorException
,

InvalidAlgorithmParameterException
```

Validates the specified certification path using the specified
algorithm parameter set.

The

CertPath

specified must be of a type that is
supported by the validation algorithm, otherwise an

InvalidAlgorithmParameterException

will be thrown. For
example, a

CertPathValidator

that implements the PKIX
algorithm validates

CertPath

objects of type X.509.

**Parameters:** certPath

- the

CertPath

to be validated
**Parameters:** params

- the algorithm parameters
**Returns:** the result of the validation algorithm
**Throws:** CertPathValidatorException

- if the

CertPath

does not validate
**Throws:** InvalidAlgorithmParameterException

- if the specified
parameters or the type of the specified

CertPath

are
inappropriate for this

CertPathValidator

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

CertPathValidator

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

engineValidate

```java
public abstract
CertPathValidatorResult
engineValidate​(
CertPath
certPath,

CertPathParameters
params)
throws
CertPathValidatorException
,

InvalidAlgorithmParameterException
```

Validates the specified certification path using the specified
algorithm parameter set.

The

CertPath

specified must be of a type that is
supported by the validation algorithm, otherwise an

InvalidAlgorithmParameterException

will be thrown. For
example, a

CertPathValidator

that implements the PKIX
algorithm validates

CertPath

objects of type X.509.

**Parameters:** certPath

- the

CertPath

to be validated
**Parameters:** params

- the algorithm parameters
**Returns:** the result of the validation algorithm
**Throws:** CertPathValidatorException

- if the

CertPath

does not validate
**Throws:** InvalidAlgorithmParameterException

- if the specified
parameters or the type of the specified

CertPath

are
inappropriate for this

CertPathValidator

---

#### engineValidate

public abstract

CertPathValidatorResult

engineValidate​(

CertPath

certPath,

CertPathParameters

params)
throws

CertPathValidatorException

,

InvalidAlgorithmParameterException

Validates the specified certification path using the specified
algorithm parameter set.

The

CertPath

specified must be of a type that is
supported by the validation algorithm, otherwise an

InvalidAlgorithmParameterException

will be thrown. For
example, a

CertPathValidator

that implements the PKIX
algorithm validates

CertPath

objects of type X.509.

The

CertPath

specified must be of a type that is
supported by the validation algorithm, otherwise an

InvalidAlgorithmParameterException

will be thrown. For
example, a

CertPathValidator

that implements the PKIX
algorithm validates

CertPath

objects of type X.509.

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

CertPathValidator

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

CertPathValidator

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

CertPathValidator

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

