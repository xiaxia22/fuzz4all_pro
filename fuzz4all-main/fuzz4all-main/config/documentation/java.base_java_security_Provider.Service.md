# Class Provider.Service

**Source:** `java.base\java\security\Provider.Service.html`

### Class Description

```java
public static class
Provider.Service

extends
Object
```

The description of a security service. It encapsulates the properties
of a service and contains a factory method to obtain new implementation
instances of this service.

Each service has a provider that offers the service, a type,
an algorithm name, and the name of the class that implements the
service. Optionally, it also includes a list of alternate algorithm
names for this service (aliases) and attributes, which are a map of
(name, value) String pairs.

This class defines the methods

supportsParameter()

and

newInstance()

which are used by the Java security framework when it searches for
suitable services and instantiates them. The valid arguments to those
methods depend on the type of service. For the service types defined
within Java SE, see the

Java Cryptography Architecture (JCA) Reference Guide

for the valid values.
Note that components outside of Java SE can define additional types of
services and their behavior.

Instances of this class are immutable.

**Enclosing class:** Provider

---

### Field Details

*No entries found.*

### Constructor Details

#### public Service​(
Provider
provider,

String
type,

String
algorithm,

String
className,

List
<
String
> aliases,

Map
<
String
,​
String
> attributes)

Construct a new service.

**Parameters:**
- provider

- the provider that offers this service
- type

- the type of this service
- algorithm

- the algorithm name
- className

- the name of the class implementing this service
- aliases

- List of aliases or null if algorithm has no aliases
- attributes

- Map of attributes or null if this implementation
has no attributes

**Throws:**
- NullPointerException

- if provider, type, algorithm, or
className is null

---

### Method Details

#### public final
String
getType()

Get the type of this service. For example,

MessageDigest

.

**Returns:**
- the type of this service

---

#### public final
String
getAlgorithm()

Return the name of the algorithm of this service. For example,

SHA-1

.

**Returns:**
- the algorithm of this service

---

#### public final
Provider
getProvider()

Return the Provider of this service.

**Returns:**
- the Provider of this service

---

#### public final
String
getClassName()

Return the name of the class implementing this service.

**Returns:**
- the name of the class implementing this service

---

#### public final
String
getAttribute​(
String
name)

Return the value of the specified attribute or null if this
attribute is not set for this Service.

**Parameters:**
- name

- the name of the requested attribute

**Returns:**
- the value of the specified attribute or null if the
attribute is not present

**Throws:**
- NullPointerException

- if name is null

---

#### public
Object
newInstance​(
Object
constructorParameter)
throws
NoSuchAlgorithmException

Return a new instance of the implementation described by this
service. The security provider framework uses this method to
construct implementations. Applications will typically not need
to call it.

The default implementation uses reflection to invoke the
standard constructor for this type of service.
Security providers can override this method to implement
instantiation in a different way.
For details and the values of constructorParameter that are
valid for the various types of services see the

Java Cryptography Architecture (JCA) Reference Guide

.

**Parameters:**
- constructorParameter

- the value to pass to the constructor,
or null if this type of service does not use a constructorParameter.

**Returns:**
- a new implementation of this service

**Throws:**
- InvalidParameterException

- if the value of
constructorParameter is invalid for this type of service.
- NoSuchAlgorithmException

- if instantiation failed for
any other reason.

---

#### public boolean supportsParameter​(
Object
parameter)

Test whether this Service can use the specified parameter.
Returns false if this service cannot use the parameter. Returns
true if this service can use the parameter, if a fast test is
infeasible, or if the status is unknown.

The security provider framework uses this method with
some types of services to quickly exclude non-matching
implementations for consideration.
Applications will typically not need to call it.

For details and the values of parameter that are valid for the
various types of services see the top of this class and the

Java Cryptography Architecture (JCA) Reference Guide

.
Security providers can override it to implement their own test.

**Parameters:**
- parameter

- the parameter to test

**Returns:**
- false if this service cannot use the specified
parameter; true if it can possibly use the parameter

**Throws:**
- InvalidParameterException

- if the value of parameter is
invalid for this type of service or if this method cannot be
used with this type of service

---

#### public
String
toString()

Return a String representation of this service.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this service.

---

### Additional Sections

#### Class Provider.Service

java.lang.Object

- java.security.Provider.Service

java.security.Provider.Service

**Enclosing class:** Provider

```java
public static class
Provider.Service

extends
Object
```

The description of a security service. It encapsulates the properties
of a service and contains a factory method to obtain new implementation
instances of this service.

Each service has a provider that offers the service, a type,
an algorithm name, and the name of the class that implements the
service. Optionally, it also includes a list of alternate algorithm
names for this service (aliases) and attributes, which are a map of
(name, value) String pairs.

This class defines the methods

supportsParameter()

and

newInstance()

which are used by the Java security framework when it searches for
suitable services and instantiates them. The valid arguments to those
methods depend on the type of service. For the service types defined
within Java SE, see the

Java Cryptography Architecture (JCA) Reference Guide

for the valid values.
Note that components outside of Java SE can define additional types of
services and their behavior.

Instances of this class are immutable.

**Since:** 1.5

public static class

Provider.Service

extends

Object

The description of a security service. It encapsulates the properties
of a service and contains a factory method to obtain new implementation
instances of this service.

Each service has a provider that offers the service, a type,
an algorithm name, and the name of the class that implements the
service. Optionally, it also includes a list of alternate algorithm
names for this service (aliases) and attributes, which are a map of
(name, value) String pairs.

This class defines the methods

supportsParameter()

and

newInstance()

which are used by the Java security framework when it searches for
suitable services and instantiates them. The valid arguments to those
methods depend on the type of service. For the service types defined
within Java SE, see the

Java Cryptography Architecture (JCA) Reference Guide

for the valid values.
Note that components outside of Java SE can define additional types of
services and their behavior.

Instances of this class are immutable.

Each service has a provider that offers the service, a type,
an algorithm name, and the name of the class that implements the
service. Optionally, it also includes a list of alternate algorithm
names for this service (aliases) and attributes, which are a map of
(name, value) String pairs.

This class defines the methods

supportsParameter()

and

newInstance()

which are used by the Java security framework when it searches for
suitable services and instantiates them. The valid arguments to those
methods depend on the type of service. For the service types defined
within Java SE, see the

Java Cryptography Architecture (JCA) Reference Guide

for the valid values.
Note that components outside of Java SE can define additional types of
services and their behavior.

Instances of this class are immutable.

This class defines the methods

supportsParameter()

and

newInstance()

which are used by the Java security framework when it searches for
suitable services and instantiates them. The valid arguments to those
methods depend on the type of service. For the service types defined
within Java SE, see the

Java Cryptography Architecture (JCA) Reference Guide

for the valid values.
Note that components outside of Java SE can define additional types of
services and their behavior.

Instances of this class are immutable.

Instances of this class are immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Service

​(

Provider

provider,

String

type,

String

algorithm,

String

className,

List

<

String

> aliases,

Map

<

String

,​

String

> attributes)

Construct a new service.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Return the name of the algorithm of this service.

String

getAttribute

​(

String

name)

Return the value of the specified attribute or null if this
attribute is not set for this Service.

String

getClassName

()

Return the name of the class implementing this service.

Provider

getProvider

()

Return the Provider of this service.

String

getType

()

Get the type of this service.

Object

newInstance

​(

Object

constructorParameter)

Return a new instance of the implementation described by this
service.

boolean

supportsParameter

​(

Object

parameter)

Test whether this Service can use the specified parameter.

String

toString

()

Return a String representation of this service.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

Service

​(

Provider

provider,

String

type,

String

algorithm,

String

className,

List

<

String

> aliases,

Map

<

String

,​

String

> attributes)

Construct a new service.

---

#### Constructor Summary

Construct a new service.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Return the name of the algorithm of this service.

String

getAttribute

​(

String

name)

Return the value of the specified attribute or null if this
attribute is not set for this Service.

String

getClassName

()

Return the name of the class implementing this service.

Provider

getProvider

()

Return the Provider of this service.

String

getType

()

Get the type of this service.

Object

newInstance

​(

Object

constructorParameter)

Return a new instance of the implementation described by this
service.

boolean

supportsParameter

​(

Object

parameter)

Test whether this Service can use the specified parameter.

String

toString

()

Return a String representation of this service.

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

wait

,

wait

,

wait

---

#### Method Summary

Return the name of the algorithm of this service.

Return the value of the specified attribute or null if this
attribute is not set for this Service.

Return the name of the class implementing this service.

Return the Provider of this service.

Get the type of this service.

Return a new instance of the implementation described by this
service.

Test whether this Service can use the specified parameter.

Return a String representation of this service.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Service

```java
public Service​(
Provider
provider,

String
type,

String
algorithm,

String
className,

List
<
String
> aliases,

Map
<
String
,​
String
> attributes)
```

Construct a new service.

**Parameters:** provider

- the provider that offers this service
**Parameters:** type

- the type of this service
**Parameters:** algorithm

- the algorithm name
**Parameters:** className

- the name of the class implementing this service
**Parameters:** aliases

- List of aliases or null if algorithm has no aliases
**Parameters:** attributes

- Map of attributes or null if this implementation
has no attributes
**Throws:** NullPointerException

- if provider, type, algorithm, or
className is null

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public final
String
getType()
```

Get the type of this service. For example,

MessageDigest

.

**Returns:** the type of this service

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Return the name of the algorithm of this service. For example,

SHA-1

.

**Returns:** the algorithm of this service

- getProvider

```java
public final
Provider
getProvider()
```

Return the Provider of this service.

**Returns:** the Provider of this service

- getClassName

```java
public final
String
getClassName()
```

Return the name of the class implementing this service.

**Returns:** the name of the class implementing this service

- getAttribute

```java
public final
String
getAttribute​(
String
name)
```

Return the value of the specified attribute or null if this
attribute is not set for this Service.

**Parameters:** name

- the name of the requested attribute
**Returns:** the value of the specified attribute or null if the
attribute is not present
**Throws:** NullPointerException

- if name is null

- newInstance

```java
public
Object
newInstance​(
Object
constructorParameter)
throws
NoSuchAlgorithmException
```

Return a new instance of the implementation described by this
service. The security provider framework uses this method to
construct implementations. Applications will typically not need
to call it.

The default implementation uses reflection to invoke the
standard constructor for this type of service.
Security providers can override this method to implement
instantiation in a different way.
For details and the values of constructorParameter that are
valid for the various types of services see the

Java Cryptography Architecture (JCA) Reference Guide

.

**Parameters:** constructorParameter

- the value to pass to the constructor,
or null if this type of service does not use a constructorParameter.
**Returns:** a new implementation of this service
**Throws:** InvalidParameterException

- if the value of
constructorParameter is invalid for this type of service.
**Throws:** NoSuchAlgorithmException

- if instantiation failed for
any other reason.

- supportsParameter

```java
public boolean supportsParameter​(
Object
parameter)
```

Test whether this Service can use the specified parameter.
Returns false if this service cannot use the parameter. Returns
true if this service can use the parameter, if a fast test is
infeasible, or if the status is unknown.

The security provider framework uses this method with
some types of services to quickly exclude non-matching
implementations for consideration.
Applications will typically not need to call it.

For details and the values of parameter that are valid for the
various types of services see the top of this class and the

Java Cryptography Architecture (JCA) Reference Guide

.
Security providers can override it to implement their own test.

**Parameters:** parameter

- the parameter to test
**Returns:** false if this service cannot use the specified
parameter; true if it can possibly use the parameter
**Throws:** InvalidParameterException

- if the value of parameter is
invalid for this type of service or if this method cannot be
used with this type of service

- toString

```java
public
String
toString()
```

Return a String representation of this service.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this service.

Constructor Detail

- Service

```java
public Service​(
Provider
provider,

String
type,

String
algorithm,

String
className,

List
<
String
> aliases,

Map
<
String
,​
String
> attributes)
```

Construct a new service.

**Parameters:** provider

- the provider that offers this service
**Parameters:** type

- the type of this service
**Parameters:** algorithm

- the algorithm name
**Parameters:** className

- the name of the class implementing this service
**Parameters:** aliases

- List of aliases or null if algorithm has no aliases
**Parameters:** attributes

- Map of attributes or null if this implementation
has no attributes
**Throws:** NullPointerException

- if provider, type, algorithm, or
className is null

---

#### Constructor Detail

Service

```java
public Service​(
Provider
provider,

String
type,

String
algorithm,

String
className,

List
<
String
> aliases,

Map
<
String
,​
String
> attributes)
```

Construct a new service.

**Parameters:** provider

- the provider that offers this service
**Parameters:** type

- the type of this service
**Parameters:** algorithm

- the algorithm name
**Parameters:** className

- the name of the class implementing this service
**Parameters:** aliases

- List of aliases or null if algorithm has no aliases
**Parameters:** attributes

- Map of attributes or null if this implementation
has no attributes
**Throws:** NullPointerException

- if provider, type, algorithm, or
className is null

---

#### Service

public Service​(

Provider

provider,

String

type,

String

algorithm,

String

className,

List

<

String

> aliases,

Map

<

String

,​

String

> attributes)

Construct a new service.

Method Detail

- getType

```java
public final
String
getType()
```

Get the type of this service. For example,

MessageDigest

.

**Returns:** the type of this service

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Return the name of the algorithm of this service. For example,

SHA-1

.

**Returns:** the algorithm of this service

- getProvider

```java
public final
Provider
getProvider()
```

Return the Provider of this service.

**Returns:** the Provider of this service

- getClassName

```java
public final
String
getClassName()
```

Return the name of the class implementing this service.

**Returns:** the name of the class implementing this service

- getAttribute

```java
public final
String
getAttribute​(
String
name)
```

Return the value of the specified attribute or null if this
attribute is not set for this Service.

**Parameters:** name

- the name of the requested attribute
**Returns:** the value of the specified attribute or null if the
attribute is not present
**Throws:** NullPointerException

- if name is null

- newInstance

```java
public
Object
newInstance​(
Object
constructorParameter)
throws
NoSuchAlgorithmException
```

Return a new instance of the implementation described by this
service. The security provider framework uses this method to
construct implementations. Applications will typically not need
to call it.

The default implementation uses reflection to invoke the
standard constructor for this type of service.
Security providers can override this method to implement
instantiation in a different way.
For details and the values of constructorParameter that are
valid for the various types of services see the

Java Cryptography Architecture (JCA) Reference Guide

.

**Parameters:** constructorParameter

- the value to pass to the constructor,
or null if this type of service does not use a constructorParameter.
**Returns:** a new implementation of this service
**Throws:** InvalidParameterException

- if the value of
constructorParameter is invalid for this type of service.
**Throws:** NoSuchAlgorithmException

- if instantiation failed for
any other reason.

- supportsParameter

```java
public boolean supportsParameter​(
Object
parameter)
```

Test whether this Service can use the specified parameter.
Returns false if this service cannot use the parameter. Returns
true if this service can use the parameter, if a fast test is
infeasible, or if the status is unknown.

The security provider framework uses this method with
some types of services to quickly exclude non-matching
implementations for consideration.
Applications will typically not need to call it.

For details and the values of parameter that are valid for the
various types of services see the top of this class and the

Java Cryptography Architecture (JCA) Reference Guide

.
Security providers can override it to implement their own test.

**Parameters:** parameter

- the parameter to test
**Returns:** false if this service cannot use the specified
parameter; true if it can possibly use the parameter
**Throws:** InvalidParameterException

- if the value of parameter is
invalid for this type of service or if this method cannot be
used with this type of service

- toString

```java
public
String
toString()
```

Return a String representation of this service.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this service.

---

#### Method Detail

getType

```java
public final
String
getType()
```

Get the type of this service. For example,

MessageDigest

.

**Returns:** the type of this service

---

#### getType

public final

String

getType()

Get the type of this service. For example,

MessageDigest

.

getAlgorithm

```java
public final
String
getAlgorithm()
```

Return the name of the algorithm of this service. For example,

SHA-1

.

**Returns:** the algorithm of this service

---

#### getAlgorithm

public final

String

getAlgorithm()

Return the name of the algorithm of this service. For example,

SHA-1

.

getProvider

```java
public final
Provider
getProvider()
```

Return the Provider of this service.

**Returns:** the Provider of this service

---

#### getProvider

public final

Provider

getProvider()

Return the Provider of this service.

getClassName

```java
public final
String
getClassName()
```

Return the name of the class implementing this service.

**Returns:** the name of the class implementing this service

---

#### getClassName

public final

String

getClassName()

Return the name of the class implementing this service.

getAttribute

```java
public final
String
getAttribute​(
String
name)
```

Return the value of the specified attribute or null if this
attribute is not set for this Service.

**Parameters:** name

- the name of the requested attribute
**Returns:** the value of the specified attribute or null if the
attribute is not present
**Throws:** NullPointerException

- if name is null

---

#### getAttribute

public final

String

getAttribute​(

String

name)

Return the value of the specified attribute or null if this
attribute is not set for this Service.

newInstance

```java
public
Object
newInstance​(
Object
constructorParameter)
throws
NoSuchAlgorithmException
```

Return a new instance of the implementation described by this
service. The security provider framework uses this method to
construct implementations. Applications will typically not need
to call it.

The default implementation uses reflection to invoke the
standard constructor for this type of service.
Security providers can override this method to implement
instantiation in a different way.
For details and the values of constructorParameter that are
valid for the various types of services see the

Java Cryptography Architecture (JCA) Reference Guide

.

**Parameters:** constructorParameter

- the value to pass to the constructor,
or null if this type of service does not use a constructorParameter.
**Returns:** a new implementation of this service
**Throws:** InvalidParameterException

- if the value of
constructorParameter is invalid for this type of service.
**Throws:** NoSuchAlgorithmException

- if instantiation failed for
any other reason.

---

#### newInstance

public

Object

newInstance​(

Object

constructorParameter)
throws

NoSuchAlgorithmException

Return a new instance of the implementation described by this
service. The security provider framework uses this method to
construct implementations. Applications will typically not need
to call it.

The default implementation uses reflection to invoke the
standard constructor for this type of service.
Security providers can override this method to implement
instantiation in a different way.
For details and the values of constructorParameter that are
valid for the various types of services see the

Java Cryptography Architecture (JCA) Reference Guide

.

The default implementation uses reflection to invoke the
standard constructor for this type of service.
Security providers can override this method to implement
instantiation in a different way.
For details and the values of constructorParameter that are
valid for the various types of services see the

Java Cryptography Architecture (JCA) Reference Guide

.

supportsParameter

```java
public boolean supportsParameter​(
Object
parameter)
```

Test whether this Service can use the specified parameter.
Returns false if this service cannot use the parameter. Returns
true if this service can use the parameter, if a fast test is
infeasible, or if the status is unknown.

The security provider framework uses this method with
some types of services to quickly exclude non-matching
implementations for consideration.
Applications will typically not need to call it.

For details and the values of parameter that are valid for the
various types of services see the top of this class and the

Java Cryptography Architecture (JCA) Reference Guide

.
Security providers can override it to implement their own test.

**Parameters:** parameter

- the parameter to test
**Returns:** false if this service cannot use the specified
parameter; true if it can possibly use the parameter
**Throws:** InvalidParameterException

- if the value of parameter is
invalid for this type of service or if this method cannot be
used with this type of service

---

#### supportsParameter

public boolean supportsParameter​(

Object

parameter)

Test whether this Service can use the specified parameter.
Returns false if this service cannot use the parameter. Returns
true if this service can use the parameter, if a fast test is
infeasible, or if the status is unknown.

The security provider framework uses this method with
some types of services to quickly exclude non-matching
implementations for consideration.
Applications will typically not need to call it.

For details and the values of parameter that are valid for the
various types of services see the top of this class and the

Java Cryptography Architecture (JCA) Reference Guide

.
Security providers can override it to implement their own test.

The security provider framework uses this method with
some types of services to quickly exclude non-matching
implementations for consideration.
Applications will typically not need to call it.

For details and the values of parameter that are valid for the
various types of services see the top of this class and the

Java Cryptography Architecture (JCA) Reference Guide

.
Security providers can override it to implement their own test.

For details and the values of parameter that are valid for the
various types of services see the top of this class and the

Java Cryptography Architecture (JCA) Reference Guide

.
Security providers can override it to implement their own test.

toString

```java
public
String
toString()
```

Return a String representation of this service.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this service.

---

#### toString

public

String

toString()

Return a String representation of this service.

---

