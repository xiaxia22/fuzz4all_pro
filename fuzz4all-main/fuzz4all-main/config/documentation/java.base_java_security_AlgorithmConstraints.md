# Interface AlgorithmConstraints

**Source:** `java.base\java\security\AlgorithmConstraints.html`

### Class Description

```java
public interface
AlgorithmConstraints
```

This interface specifies constraints for cryptographic algorithms,
keys (key sizes), and other algorithm parameters.

AlgorithmConstraints

objects are immutable. An implementation
of this interface should not provide methods that can change the state
of an instance once it has been created.

Note that

AlgorithmConstraints

can be used to represent the
restrictions described by the security properties

jdk.certpath.disabledAlgorithms

and

jdk.tls.disabledAlgorithms

, or could be used by a
concrete

PKIXCertPathChecker

to check whether a specified
certificate in the certification path contains the required algorithm
constraints.

**Since:** 1.7
**See Also:** SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean permits​(
Set
<
CryptoPrimitive
> primitives,

String
algorithm,

AlgorithmParameters
parameters)

Determines whether an algorithm is granted permission for the
specified cryptographic primitives.

**Parameters:**
- primitives

- a set of cryptographic primitives
- algorithm

- the algorithm name
- parameters

- the algorithm parameters, or null if no additional
parameters

**Returns:**
- true if the algorithm is permitted and can be used for all
of the specified cryptographic primitives

**Throws:**
- IllegalArgumentException

- if primitives or algorithm is null
or empty

---

#### boolean permits​(
Set
<
CryptoPrimitive
> primitives,

Key
key)

Determines whether a key is granted permission for the specified
cryptographic primitives.

This method is usually used to check key size and key usage.

**Parameters:**
- primitives

- a set of cryptographic primitives
- key

- the key

**Returns:**
- true if the key can be used for all of the specified
cryptographic primitives

**Throws:**
- IllegalArgumentException

- if primitives is null or empty,
or the key is null

---

#### boolean permits​(
Set
<
CryptoPrimitive
> primitives,

String
algorithm,

Key
key,

AlgorithmParameters
parameters)

Determines whether an algorithm and the corresponding key are granted
permission for the specified cryptographic primitives.

**Parameters:**
- primitives

- a set of cryptographic primitives
- algorithm

- the algorithm name
- key

- the key
- parameters

- the algorithm parameters, or null if no additional
parameters

**Returns:**
- true if the key and the algorithm can be used for all of the
specified cryptographic primitives

**Throws:**
- IllegalArgumentException

- if primitives or algorithm is null
or empty, or the key is null

---

### Additional Sections

#### Interface AlgorithmConstraints

```java
public interface
AlgorithmConstraints
```

This interface specifies constraints for cryptographic algorithms,
keys (key sizes), and other algorithm parameters.

AlgorithmConstraints

objects are immutable. An implementation
of this interface should not provide methods that can change the state
of an instance once it has been created.

Note that

AlgorithmConstraints

can be used to represent the
restrictions described by the security properties

jdk.certpath.disabledAlgorithms

and

jdk.tls.disabledAlgorithms

, or could be used by a
concrete

PKIXCertPathChecker

to check whether a specified
certificate in the certification path contains the required algorithm
constraints.

**Since:** 1.7
**See Also:** SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

public interface

AlgorithmConstraints

This interface specifies constraints for cryptographic algorithms,
keys (key sizes), and other algorithm parameters.

AlgorithmConstraints

objects are immutable. An implementation
of this interface should not provide methods that can change the state
of an instance once it has been created.

Note that

AlgorithmConstraints

can be used to represent the
restrictions described by the security properties

jdk.certpath.disabledAlgorithms

and

jdk.tls.disabledAlgorithms

, or could be used by a
concrete

PKIXCertPathChecker

to check whether a specified
certificate in the certification path contains the required algorithm
constraints.

AlgorithmConstraints

objects are immutable. An implementation
of this interface should not provide methods that can change the state
of an instance once it has been created.

Note that

AlgorithmConstraints

can be used to represent the
restrictions described by the security properties

jdk.certpath.disabledAlgorithms

and

jdk.tls.disabledAlgorithms

, or could be used by a
concrete

PKIXCertPathChecker

to check whether a specified
certificate in the certification path contains the required algorithm
constraints.

Note that

AlgorithmConstraints

can be used to represent the
restrictions described by the security properties

jdk.certpath.disabledAlgorithms

and

jdk.tls.disabledAlgorithms

, or could be used by a
concrete

PKIXCertPathChecker

to check whether a specified
certificate in the certification path contains the required algorithm
constraints.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

permits

​(

Set

<

CryptoPrimitive

> primitives,

String

algorithm,

AlgorithmParameters

parameters)

Determines whether an algorithm is granted permission for the
specified cryptographic primitives.

boolean

permits

​(

Set

<

CryptoPrimitive

> primitives,

String

algorithm,

Key

key,

AlgorithmParameters

parameters)

Determines whether an algorithm and the corresponding key are granted
permission for the specified cryptographic primitives.

boolean

permits

​(

Set

<

CryptoPrimitive

> primitives,

Key

key)

Determines whether a key is granted permission for the specified
cryptographic primitives.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

permits

​(

Set

<

CryptoPrimitive

> primitives,

String

algorithm,

AlgorithmParameters

parameters)

Determines whether an algorithm is granted permission for the
specified cryptographic primitives.

boolean

permits

​(

Set

<

CryptoPrimitive

> primitives,

String

algorithm,

Key

key,

AlgorithmParameters

parameters)

Determines whether an algorithm and the corresponding key are granted
permission for the specified cryptographic primitives.

boolean

permits

​(

Set

<

CryptoPrimitive

> primitives,

Key

key)

Determines whether a key is granted permission for the specified
cryptographic primitives.

---

#### Method Summary

Determines whether an algorithm is granted permission for the
specified cryptographic primitives.

Determines whether an algorithm and the corresponding key are granted
permission for the specified cryptographic primitives.

Determines whether a key is granted permission for the specified
cryptographic primitives.

============ METHOD DETAIL ==========

- Method Detail

- permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

String
algorithm,

AlgorithmParameters
parameters)
```

Determines whether an algorithm is granted permission for the
specified cryptographic primitives.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** algorithm

- the algorithm name
**Parameters:** parameters

- the algorithm parameters, or null if no additional
parameters
**Returns:** true if the algorithm is permitted and can be used for all
of the specified cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives or algorithm is null
or empty

- permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

Key
key)
```

Determines whether a key is granted permission for the specified
cryptographic primitives.

This method is usually used to check key size and key usage.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** key

- the key
**Returns:** true if the key can be used for all of the specified
cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives is null or empty,
or the key is null

- permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

String
algorithm,

Key
key,

AlgorithmParameters
parameters)
```

Determines whether an algorithm and the corresponding key are granted
permission for the specified cryptographic primitives.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** algorithm

- the algorithm name
**Parameters:** key

- the key
**Parameters:** parameters

- the algorithm parameters, or null if no additional
parameters
**Returns:** true if the key and the algorithm can be used for all of the
specified cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives or algorithm is null
or empty, or the key is null

Method Detail

- permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

String
algorithm,

AlgorithmParameters
parameters)
```

Determines whether an algorithm is granted permission for the
specified cryptographic primitives.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** algorithm

- the algorithm name
**Parameters:** parameters

- the algorithm parameters, or null if no additional
parameters
**Returns:** true if the algorithm is permitted and can be used for all
of the specified cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives or algorithm is null
or empty

- permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

Key
key)
```

Determines whether a key is granted permission for the specified
cryptographic primitives.

This method is usually used to check key size and key usage.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** key

- the key
**Returns:** true if the key can be used for all of the specified
cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives is null or empty,
or the key is null

- permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

String
algorithm,

Key
key,

AlgorithmParameters
parameters)
```

Determines whether an algorithm and the corresponding key are granted
permission for the specified cryptographic primitives.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** algorithm

- the algorithm name
**Parameters:** key

- the key
**Parameters:** parameters

- the algorithm parameters, or null if no additional
parameters
**Returns:** true if the key and the algorithm can be used for all of the
specified cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives or algorithm is null
or empty, or the key is null

---

#### Method Detail

permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

String
algorithm,

AlgorithmParameters
parameters)
```

Determines whether an algorithm is granted permission for the
specified cryptographic primitives.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** algorithm

- the algorithm name
**Parameters:** parameters

- the algorithm parameters, or null if no additional
parameters
**Returns:** true if the algorithm is permitted and can be used for all
of the specified cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives or algorithm is null
or empty

---

#### permits

boolean permits​(

Set

<

CryptoPrimitive

> primitives,

String

algorithm,

AlgorithmParameters

parameters)

Determines whether an algorithm is granted permission for the
specified cryptographic primitives.

permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

Key
key)
```

Determines whether a key is granted permission for the specified
cryptographic primitives.

This method is usually used to check key size and key usage.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** key

- the key
**Returns:** true if the key can be used for all of the specified
cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives is null or empty,
or the key is null

---

#### permits

boolean permits​(

Set

<

CryptoPrimitive

> primitives,

Key

key)

Determines whether a key is granted permission for the specified
cryptographic primitives.

This method is usually used to check key size and key usage.

This method is usually used to check key size and key usage.

permits

```java
boolean permits​(
Set
<
CryptoPrimitive
> primitives,

String
algorithm,

Key
key,

AlgorithmParameters
parameters)
```

Determines whether an algorithm and the corresponding key are granted
permission for the specified cryptographic primitives.

**Parameters:** primitives

- a set of cryptographic primitives
**Parameters:** algorithm

- the algorithm name
**Parameters:** key

- the key
**Parameters:** parameters

- the algorithm parameters, or null if no additional
parameters
**Returns:** true if the key and the algorithm can be used for all of the
specified cryptographic primitives
**Throws:** IllegalArgumentException

- if primitives or algorithm is null
or empty, or the key is null

---

#### permits

boolean permits​(

Set

<

CryptoPrimitive

> primitives,

String

algorithm,

Key

key,

AlgorithmParameters

parameters)

Determines whether an algorithm and the corresponding key are granted
permission for the specified cryptographic primitives.

---

