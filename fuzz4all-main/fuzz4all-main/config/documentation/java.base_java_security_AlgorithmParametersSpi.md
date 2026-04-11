# Class AlgorithmParametersSpi

**Source:** `java.base\java\security\AlgorithmParametersSpi.html`

### Class Description

```java
public abstract class
AlgorithmParametersSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

AlgorithmParameters

class, which is used to manage
algorithm parameters.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply parameter management
for a particular algorithm.

**Since:** 1.2
**See Also:** AlgorithmParameters

,

AlgorithmParameterSpec

,

DSAParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public AlgorithmParametersSpi()

*No description found.*

---

### Method Details

#### protected abstract void engineInit​(
AlgorithmParameterSpec
paramSpec)
throws
InvalidParameterSpecException

Initializes this parameters object using the parameters
specified in

paramSpec

.

**Parameters:**
- paramSpec

- the parameter specification.

**Throws:**
- InvalidParameterSpecException

- if the given parameter
specification is inappropriate for the initialization of this parameter
object.

---

#### protected abstract void engineInit​(byte[] params)
throws
IOException

Imports the specified parameters and decodes them
according to the primary decoding format for parameters.
The primary decoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Parameters:**
- params

- the encoded parameters.

**Throws:**
- IOException

- on decoding errors

---

#### protected abstract void engineInit​(byte[] params,

String
format)
throws
IOException

Imports the parameters from

params

and
decodes them according to the specified decoding format.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:**
- params

- the encoded parameters.
- format

- the name of the decoding format.

**Throws:**
- IOException

- on decoding errors

---

#### protected abstract <T extends
AlgorithmParameterSpec
> T engineGetParameterSpec​(
Class
<T> paramSpec)
throws
InvalidParameterSpecException

Returns a (transparent) specification of this parameters
object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

**Parameters:**
- paramSpec

- the specification class in which
the parameters should be returned.

**Returns:**
- the parameter specification.

**Throws:**
- InvalidParameterSpecException

- if the requested parameter
specification is inappropriate for this parameter object.

**Type Parameters:**
- T

- the type of the parameter specification to be returned

---

#### protected abstract byte[] engineGetEncoded()
throws
IOException

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Returns:**
- the parameters encoded using their primary encoding format.

**Throws:**
- IOException

- on encoding errors.

---

#### protected abstract byte[] engineGetEncoded​(
String
format)
throws
IOException

Returns the parameters encoded in the specified format.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:**
- format

- the name of the encoding format.

**Returns:**
- the parameters encoded using the specified encoding scheme.

**Throws:**
- IOException

- on encoding errors.

---

#### protected abstract
String
engineToString()

Returns a formatted string describing the parameters.

**Returns:**
- a formatted string describing the parameters.

---

### Additional Sections

#### Class AlgorithmParametersSpi

java.lang.Object

- java.security.AlgorithmParametersSpi

java.security.AlgorithmParametersSpi

```java
public abstract class
AlgorithmParametersSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

AlgorithmParameters

class, which is used to manage
algorithm parameters.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply parameter management
for a particular algorithm.

**Since:** 1.2
**See Also:** AlgorithmParameters

,

AlgorithmParameterSpec

,

DSAParameterSpec

public abstract class

AlgorithmParametersSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

AlgorithmParameters

class, which is used to manage
algorithm parameters.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply parameter management
for a particular algorithm.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply parameter management
for a particular algorithm.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AlgorithmParametersSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract byte[]

engineGetEncoded

()

Returns the parameters in their primary encoding format.

protected abstract byte[]

engineGetEncoded

​(

String

format)

Returns the parameters encoded in the specified format.

protected abstract <T extends

AlgorithmParameterSpec

>

T

engineGetParameterSpec

​(

Class

<T> paramSpec)

Returns a (transparent) specification of this parameters
object.

protected abstract void

engineInit

​(byte[] params)

Imports the specified parameters and decodes them
according to the primary decoding format for parameters.

protected abstract void

engineInit

​(byte[] params,

String

format)

Imports the parameters from

params

and
decodes them according to the specified decoding format.

protected abstract void

engineInit

​(

AlgorithmParameterSpec

paramSpec)

Initializes this parameters object using the parameters
specified in

paramSpec

.

protected abstract

String

engineToString

()

Returns a formatted string describing the parameters.

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

AlgorithmParametersSpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract byte[]

engineGetEncoded

()

Returns the parameters in their primary encoding format.

protected abstract byte[]

engineGetEncoded

​(

String

format)

Returns the parameters encoded in the specified format.

protected abstract <T extends

AlgorithmParameterSpec

>

T

engineGetParameterSpec

​(

Class

<T> paramSpec)

Returns a (transparent) specification of this parameters
object.

protected abstract void

engineInit

​(byte[] params)

Imports the specified parameters and decodes them
according to the primary decoding format for parameters.

protected abstract void

engineInit

​(byte[] params,

String

format)

Imports the parameters from

params

and
decodes them according to the specified decoding format.

protected abstract void

engineInit

​(

AlgorithmParameterSpec

paramSpec)

Initializes this parameters object using the parameters
specified in

paramSpec

.

protected abstract

String

engineToString

()

Returns a formatted string describing the parameters.

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

Returns the parameters in their primary encoding format.

Returns the parameters encoded in the specified format.

Returns a (transparent) specification of this parameters
object.

Imports the specified parameters and decodes them
according to the primary decoding format for parameters.

Imports the parameters from

params

and
decodes them according to the specified decoding format.

Initializes this parameters object using the parameters
specified in

paramSpec

.

Returns a formatted string describing the parameters.

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

- AlgorithmParametersSpi

```java
public AlgorithmParametersSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
paramSpec)
throws
InvalidParameterSpecException
```

Initializes this parameters object using the parameters
specified in

paramSpec

.

**Parameters:** paramSpec

- the parameter specification.
**Throws:** InvalidParameterSpecException

- if the given parameter
specification is inappropriate for the initialization of this parameter
object.

- engineInit

```java
protected abstract void engineInit​(byte[] params)
throws
IOException
```

Imports the specified parameters and decodes them
according to the primary decoding format for parameters.
The primary decoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Parameters:** params

- the encoded parameters.
**Throws:** IOException

- on decoding errors

- engineInit

```java
protected abstract void engineInit​(byte[] params,

String
format)
throws
IOException
```

Imports the parameters from

params

and
decodes them according to the specified decoding format.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** params

- the encoded parameters.
**Parameters:** format

- the name of the decoding format.
**Throws:** IOException

- on decoding errors

- engineGetParameterSpec

```java
protected abstract <T extends
AlgorithmParameterSpec
> T engineGetParameterSpec​(
Class
<T> paramSpec)
throws
InvalidParameterSpecException
```

Returns a (transparent) specification of this parameters
object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

**Type Parameters:** T

- the type of the parameter specification to be returned
**Parameters:** paramSpec

- the specification class in which
the parameters should be returned.
**Returns:** the parameter specification.
**Throws:** InvalidParameterSpecException

- if the requested parameter
specification is inappropriate for this parameter object.

- engineGetEncoded

```java
protected abstract byte[] engineGetEncoded()
throws
IOException
```

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Returns:** the parameters encoded using their primary encoding format.
**Throws:** IOException

- on encoding errors.

- engineGetEncoded

```java
protected abstract byte[] engineGetEncoded​(
String
format)
throws
IOException
```

Returns the parameters encoded in the specified format.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** format

- the name of the encoding format.
**Returns:** the parameters encoded using the specified encoding scheme.
**Throws:** IOException

- on encoding errors.

- engineToString

```java
protected abstract
String
engineToString()
```

Returns a formatted string describing the parameters.

**Returns:** a formatted string describing the parameters.

Constructor Detail

- AlgorithmParametersSpi

```java
public AlgorithmParametersSpi()
```

---

#### Constructor Detail

AlgorithmParametersSpi

```java
public AlgorithmParametersSpi()
```

---

#### AlgorithmParametersSpi

public AlgorithmParametersSpi()

Method Detail

- engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
paramSpec)
throws
InvalidParameterSpecException
```

Initializes this parameters object using the parameters
specified in

paramSpec

.

**Parameters:** paramSpec

- the parameter specification.
**Throws:** InvalidParameterSpecException

- if the given parameter
specification is inappropriate for the initialization of this parameter
object.

- engineInit

```java
protected abstract void engineInit​(byte[] params)
throws
IOException
```

Imports the specified parameters and decodes them
according to the primary decoding format for parameters.
The primary decoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Parameters:** params

- the encoded parameters.
**Throws:** IOException

- on decoding errors

- engineInit

```java
protected abstract void engineInit​(byte[] params,

String
format)
throws
IOException
```

Imports the parameters from

params

and
decodes them according to the specified decoding format.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** params

- the encoded parameters.
**Parameters:** format

- the name of the decoding format.
**Throws:** IOException

- on decoding errors

- engineGetParameterSpec

```java
protected abstract <T extends
AlgorithmParameterSpec
> T engineGetParameterSpec​(
Class
<T> paramSpec)
throws
InvalidParameterSpecException
```

Returns a (transparent) specification of this parameters
object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

**Type Parameters:** T

- the type of the parameter specification to be returned
**Parameters:** paramSpec

- the specification class in which
the parameters should be returned.
**Returns:** the parameter specification.
**Throws:** InvalidParameterSpecException

- if the requested parameter
specification is inappropriate for this parameter object.

- engineGetEncoded

```java
protected abstract byte[] engineGetEncoded()
throws
IOException
```

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Returns:** the parameters encoded using their primary encoding format.
**Throws:** IOException

- on encoding errors.

- engineGetEncoded

```java
protected abstract byte[] engineGetEncoded​(
String
format)
throws
IOException
```

Returns the parameters encoded in the specified format.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** format

- the name of the encoding format.
**Returns:** the parameters encoded using the specified encoding scheme.
**Throws:** IOException

- on encoding errors.

- engineToString

```java
protected abstract
String
engineToString()
```

Returns a formatted string describing the parameters.

**Returns:** a formatted string describing the parameters.

---

#### Method Detail

engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
paramSpec)
throws
InvalidParameterSpecException
```

Initializes this parameters object using the parameters
specified in

paramSpec

.

**Parameters:** paramSpec

- the parameter specification.
**Throws:** InvalidParameterSpecException

- if the given parameter
specification is inappropriate for the initialization of this parameter
object.

---

#### engineInit

protected abstract void engineInit​(

AlgorithmParameterSpec

paramSpec)
throws

InvalidParameterSpecException

Initializes this parameters object using the parameters
specified in

paramSpec

.

engineInit

```java
protected abstract void engineInit​(byte[] params)
throws
IOException
```

Imports the specified parameters and decodes them
according to the primary decoding format for parameters.
The primary decoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Parameters:** params

- the encoded parameters.
**Throws:** IOException

- on decoding errors

---

#### engineInit

protected abstract void engineInit​(byte[] params)
throws

IOException

Imports the specified parameters and decodes them
according to the primary decoding format for parameters.
The primary decoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

engineInit

```java
protected abstract void engineInit​(byte[] params,

String
format)
throws
IOException
```

Imports the parameters from

params

and
decodes them according to the specified decoding format.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** params

- the encoded parameters.
**Parameters:** format

- the name of the decoding format.
**Throws:** IOException

- on decoding errors

---

#### engineInit

protected abstract void engineInit​(byte[] params,

String

format)
throws

IOException

Imports the parameters from

params

and
decodes them according to the specified decoding format.
If

format

is null, the
primary decoding format for parameters is used. The primary decoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

engineGetParameterSpec

```java
protected abstract <T extends
AlgorithmParameterSpec
> T engineGetParameterSpec​(
Class
<T> paramSpec)
throws
InvalidParameterSpecException
```

Returns a (transparent) specification of this parameters
object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

**Type Parameters:** T

- the type of the parameter specification to be returned
**Parameters:** paramSpec

- the specification class in which
the parameters should be returned.
**Returns:** the parameter specification.
**Throws:** InvalidParameterSpecException

- if the requested parameter
specification is inappropriate for this parameter object.

---

#### engineGetParameterSpec

protected abstract <T extends

AlgorithmParameterSpec

> T engineGetParameterSpec​(

Class

<T> paramSpec)
throws

InvalidParameterSpecException

Returns a (transparent) specification of this parameters
object.

paramSpec

identifies the specification class in which
the parameters should be returned. It could, for example, be

DSAParameterSpec.class

, to indicate that the
parameters should be returned in an instance of the

DSAParameterSpec

class.

engineGetEncoded

```java
protected abstract byte[] engineGetEncoded()
throws
IOException
```

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

**Returns:** the parameters encoded using their primary encoding format.
**Throws:** IOException

- on encoding errors.

---

#### engineGetEncoded

protected abstract byte[] engineGetEncoded()
throws

IOException

Returns the parameters in their primary encoding format.
The primary encoding format for parameters is ASN.1, if an ASN.1
specification for this type of parameters exists.

engineGetEncoded

```java
protected abstract byte[] engineGetEncoded​(
String
format)
throws
IOException
```

Returns the parameters encoded in the specified format.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

**Parameters:** format

- the name of the encoding format.
**Returns:** the parameters encoded using the specified encoding scheme.
**Throws:** IOException

- on encoding errors.

---

#### engineGetEncoded

protected abstract byte[] engineGetEncoded​(

String

format)
throws

IOException

Returns the parameters encoded in the specified format.
If

format

is null, the
primary encoding format for parameters is used. The primary encoding
format is ASN.1, if an ASN.1 specification for these parameters
exists.

engineToString

```java
protected abstract
String
engineToString()
```

Returns a formatted string describing the parameters.

**Returns:** a formatted string describing the parameters.

---

#### engineToString

protected abstract

String

engineToString()

Returns a formatted string describing the parameters.

---

