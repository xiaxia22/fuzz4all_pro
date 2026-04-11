# Class SerializedLambda

**Source:** `java.base\java\lang\invoke\SerializedLambda.html`

### Class Description

```java
public final class
SerializedLambda

extends
Object

implements
Serializable
```

Serialized form of a lambda expression. The properties of this class
represent the information that is present at the lambda factory site, including
static metafactory arguments such as the identity of the primary functional
interface method and the identity of the implementation method, as well as
dynamic metafactory arguments such as values captured from the lexical scope
at the time of lambda capture.

Implementors of serializable lambdas, such as compilers or language
runtime libraries, are expected to ensure that instances deserialize properly.
One means to do so is to ensure that the

writeReplace

method returns
an instance of

SerializedLambda

, rather than allowing default
serialization to proceed.

SerializedLambda

has a

readResolve

method that looks for
a (possibly private) static method called

$deserializeLambda$(SerializedLambda)

in the capturing class, invokes
that with itself as the first argument, and returns the result. Lambda classes
implementing

$deserializeLambda$

are responsible for validating
that the properties of the

SerializedLambda

are consistent with a
lambda actually captured by that class.

The identity of a function object produced by deserializing the serialized
form is unpredictable, and therefore identity-sensitive operations (such as
reference equality, object locking, and

System.identityHashCode()

may
produce different results in different implementations, or even upon
different deserializations in the same implementation.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SerializedLambda​(
Class
<?> capturingClass,

String
functionalInterfaceClass,

String
functionalInterfaceMethodName,

String
functionalInterfaceMethodSignature,
int implMethodKind,

String
implClass,

String
implMethodName,

String
implMethodSignature,

String
instantiatedMethodType,

Object
[] capturedArgs)

Create a

SerializedLambda

from the low-level information present
at the lambda factory site.

**Parameters:**
- capturingClass

- The class in which the lambda expression appears
- functionalInterfaceClass

- Name, in slash-delimited form, of static
type of the returned lambda object
- functionalInterfaceMethodName

- Name of the functional interface
method for the present at the
lambda factory site
- functionalInterfaceMethodSignature

- Signature of the functional
interface method present at
the lambda factory site
- implMethodKind

- Method handle kind for the implementation method
- implClass

- Name, in slash-delimited form, for the class holding
the implementation method
- implMethodName

- Name of the implementation method
- implMethodSignature

- Signature of the implementation method
- instantiatedMethodType

- The signature of the primary functional
interface method after type variables
are substituted with their instantiation
from the capture site
- capturedArgs

- The dynamic arguments to the lambda factory site,
which represent variables captured by
the lambda

---

### Method Details

#### public
String
getCapturingClass()

Get the name of the class that captured this lambda.

**Returns:**
- the name of the class that captured this lambda

---

#### public
String
getFunctionalInterfaceClass()

Get the name of the invoked type to which this
lambda has been converted

**Returns:**
- the name of the functional interface class to which
this lambda has been converted

---

#### public
String
getFunctionalInterfaceMethodName()

Get the name of the primary method for the functional interface
to which this lambda has been converted.

**Returns:**
- the name of the primary methods of the functional interface

---

#### public
String
getFunctionalInterfaceMethodSignature()

Get the signature of the primary method for the functional
interface to which this lambda has been converted.

**Returns:**
- the signature of the primary method of the functional
interface

---

#### public
String
getImplClass()

Get the name of the class containing the implementation
method.

**Returns:**
- the name of the class containing the implementation
method

---

#### public
String
getImplMethodName()

Get the name of the implementation method.

**Returns:**
- the name of the implementation method

---

#### public
String
getImplMethodSignature()

Get the signature of the implementation method.

**Returns:**
- the signature of the implementation method

---

#### public int getImplMethodKind()

Get the method handle kind (see

MethodHandleInfo

) of
the implementation method.

**Returns:**
- the method handle kind of the implementation method

---

#### public final
String
getInstantiatedMethodType()

Get the signature of the primary functional interface method
after type variables are substituted with their instantiation
from the capture site.

**Returns:**
- the signature of the primary functional interface method
after type variable processing

---

#### public int getCapturedArgCount()

Get the count of dynamic arguments to the lambda capture site.

**Returns:**
- the count of dynamic arguments to the lambda capture site

---

#### public
Object
getCapturedArg​(int i)

Get a dynamic argument to the lambda capture site.

**Parameters:**
- i

- the argument to capture

**Returns:**
- a dynamic argument to the lambda capture site

---

### Additional Sections

#### Class SerializedLambda

java.lang.Object

- java.lang.invoke.SerializedLambda

java.lang.invoke.SerializedLambda

**All Implemented Interfaces:** Serializable

```java
public final class
SerializedLambda

extends
Object

implements
Serializable
```

Serialized form of a lambda expression. The properties of this class
represent the information that is present at the lambda factory site, including
static metafactory arguments such as the identity of the primary functional
interface method and the identity of the implementation method, as well as
dynamic metafactory arguments such as values captured from the lexical scope
at the time of lambda capture.

Implementors of serializable lambdas, such as compilers or language
runtime libraries, are expected to ensure that instances deserialize properly.
One means to do so is to ensure that the

writeReplace

method returns
an instance of

SerializedLambda

, rather than allowing default
serialization to proceed.

SerializedLambda

has a

readResolve

method that looks for
a (possibly private) static method called

$deserializeLambda$(SerializedLambda)

in the capturing class, invokes
that with itself as the first argument, and returns the result. Lambda classes
implementing

$deserializeLambda$

are responsible for validating
that the properties of the

SerializedLambda

are consistent with a
lambda actually captured by that class.

The identity of a function object produced by deserializing the serialized
form is unpredictable, and therefore identity-sensitive operations (such as
reference equality, object locking, and

System.identityHashCode()

may
produce different results in different implementations, or even upon
different deserializations in the same implementation.

**Since:** 1.8
**See Also:** LambdaMetafactory

,

Serialized Form

public final class

SerializedLambda

extends

Object

implements

Serializable

Serialized form of a lambda expression. The properties of this class
represent the information that is present at the lambda factory site, including
static metafactory arguments such as the identity of the primary functional
interface method and the identity of the implementation method, as well as
dynamic metafactory arguments such as values captured from the lexical scope
at the time of lambda capture.

Implementors of serializable lambdas, such as compilers or language
runtime libraries, are expected to ensure that instances deserialize properly.
One means to do so is to ensure that the

writeReplace

method returns
an instance of

SerializedLambda

, rather than allowing default
serialization to proceed.

SerializedLambda

has a

readResolve

method that looks for
a (possibly private) static method called

$deserializeLambda$(SerializedLambda)

in the capturing class, invokes
that with itself as the first argument, and returns the result. Lambda classes
implementing

$deserializeLambda$

are responsible for validating
that the properties of the

SerializedLambda

are consistent with a
lambda actually captured by that class.

The identity of a function object produced by deserializing the serialized
form is unpredictable, and therefore identity-sensitive operations (such as
reference equality, object locking, and

System.identityHashCode()

may
produce different results in different implementations, or even upon
different deserializations in the same implementation.

Implementors of serializable lambdas, such as compilers or language
runtime libraries, are expected to ensure that instances deserialize properly.
One means to do so is to ensure that the

writeReplace

method returns
an instance of

SerializedLambda

, rather than allowing default
serialization to proceed.

SerializedLambda

has a

readResolve

method that looks for
a (possibly private) static method called

$deserializeLambda$(SerializedLambda)

in the capturing class, invokes
that with itself as the first argument, and returns the result. Lambda classes
implementing

$deserializeLambda$

are responsible for validating
that the properties of the

SerializedLambda

are consistent with a
lambda actually captured by that class.

The identity of a function object produced by deserializing the serialized
form is unpredictable, and therefore identity-sensitive operations (such as
reference equality, object locking, and

System.identityHashCode()

may
produce different results in different implementations, or even upon
different deserializations in the same implementation.

SerializedLambda

has a

readResolve

method that looks for
a (possibly private) static method called

$deserializeLambda$(SerializedLambda)

in the capturing class, invokes
that with itself as the first argument, and returns the result. Lambda classes
implementing

$deserializeLambda$

are responsible for validating
that the properties of the

SerializedLambda

are consistent with a
lambda actually captured by that class.

The identity of a function object produced by deserializing the serialized
form is unpredictable, and therefore identity-sensitive operations (such as
reference equality, object locking, and

System.identityHashCode()

may
produce different results in different implementations, or even upon
different deserializations in the same implementation.

The identity of a function object produced by deserializing the serialized
form is unpredictable, and therefore identity-sensitive operations (such as
reference equality, object locking, and

System.identityHashCode()

may
produce different results in different implementations, or even upon
different deserializations in the same implementation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SerializedLambda

​(

Class

<?> capturingClass,

String

functionalInterfaceClass,

String

functionalInterfaceMethodName,

String

functionalInterfaceMethodSignature,
int implMethodKind,

String

implClass,

String

implMethodName,

String

implMethodSignature,

String

instantiatedMethodType,

Object

[] capturedArgs)

Create a

SerializedLambda

from the low-level information present
at the lambda factory site.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getCapturedArg

​(int i)

Get a dynamic argument to the lambda capture site.

int

getCapturedArgCount

()

Get the count of dynamic arguments to the lambda capture site.

String

getCapturingClass

()

Get the name of the class that captured this lambda.

String

getFunctionalInterfaceClass

()

Get the name of the invoked type to which this
lambda has been converted

String

getFunctionalInterfaceMethodName

()

Get the name of the primary method for the functional interface
to which this lambda has been converted.

String

getFunctionalInterfaceMethodSignature

()

Get the signature of the primary method for the functional
interface to which this lambda has been converted.

String

getImplClass

()

Get the name of the class containing the implementation
method.

int

getImplMethodKind

()

Get the method handle kind (see

MethodHandleInfo

) of
the implementation method.

String

getImplMethodName

()

Get the name of the implementation method.

String

getImplMethodSignature

()

Get the signature of the implementation method.

String

getInstantiatedMethodType

()

Get the signature of the primary functional interface method
after type variables are substituted with their instantiation
from the capture site.

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

SerializedLambda

​(

Class

<?> capturingClass,

String

functionalInterfaceClass,

String

functionalInterfaceMethodName,

String

functionalInterfaceMethodSignature,
int implMethodKind,

String

implClass,

String

implMethodName,

String

implMethodSignature,

String

instantiatedMethodType,

Object

[] capturedArgs)

Create a

SerializedLambda

from the low-level information present
at the lambda factory site.

---

#### Constructor Summary

Create a

SerializedLambda

from the low-level information present
at the lambda factory site.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getCapturedArg

​(int i)

Get a dynamic argument to the lambda capture site.

int

getCapturedArgCount

()

Get the count of dynamic arguments to the lambda capture site.

String

getCapturingClass

()

Get the name of the class that captured this lambda.

String

getFunctionalInterfaceClass

()

Get the name of the invoked type to which this
lambda has been converted

String

getFunctionalInterfaceMethodName

()

Get the name of the primary method for the functional interface
to which this lambda has been converted.

String

getFunctionalInterfaceMethodSignature

()

Get the signature of the primary method for the functional
interface to which this lambda has been converted.

String

getImplClass

()

Get the name of the class containing the implementation
method.

int

getImplMethodKind

()

Get the method handle kind (see

MethodHandleInfo

) of
the implementation method.

String

getImplMethodName

()

Get the name of the implementation method.

String

getImplMethodSignature

()

Get the signature of the implementation method.

String

getInstantiatedMethodType

()

Get the signature of the primary functional interface method
after type variables are substituted with their instantiation
from the capture site.

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

Get a dynamic argument to the lambda capture site.

Get the count of dynamic arguments to the lambda capture site.

Get the name of the class that captured this lambda.

Get the name of the invoked type to which this
lambda has been converted

Get the name of the primary method for the functional interface
to which this lambda has been converted.

Get the signature of the primary method for the functional
interface to which this lambda has been converted.

Get the name of the class containing the implementation
method.

Get the method handle kind (see

MethodHandleInfo

) of
the implementation method.

Get the name of the implementation method.

Get the signature of the implementation method.

Get the signature of the primary functional interface method
after type variables are substituted with their instantiation
from the capture site.

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

- SerializedLambda

```java
public SerializedLambda​(
Class
<?> capturingClass,

String
functionalInterfaceClass,

String
functionalInterfaceMethodName,

String
functionalInterfaceMethodSignature,
int implMethodKind,

String
implClass,

String
implMethodName,

String
implMethodSignature,

String
instantiatedMethodType,

Object
[] capturedArgs)
```

Create a

SerializedLambda

from the low-level information present
at the lambda factory site.

**Parameters:** capturingClass

- The class in which the lambda expression appears
**Parameters:** functionalInterfaceClass

- Name, in slash-delimited form, of static
type of the returned lambda object
**Parameters:** functionalInterfaceMethodName

- Name of the functional interface
method for the present at the
lambda factory site
**Parameters:** functionalInterfaceMethodSignature

- Signature of the functional
interface method present at
the lambda factory site
**Parameters:** implMethodKind

- Method handle kind for the implementation method
**Parameters:** implClass

- Name, in slash-delimited form, for the class holding
the implementation method
**Parameters:** implMethodName

- Name of the implementation method
**Parameters:** implMethodSignature

- Signature of the implementation method
**Parameters:** instantiatedMethodType

- The signature of the primary functional
interface method after type variables
are substituted with their instantiation
from the capture site
**Parameters:** capturedArgs

- The dynamic arguments to the lambda factory site,
which represent variables captured by
the lambda

============ METHOD DETAIL ==========

- Method Detail

- getCapturingClass

```java
public
String
getCapturingClass()
```

Get the name of the class that captured this lambda.

**Returns:** the name of the class that captured this lambda

- getFunctionalInterfaceClass

```java
public
String
getFunctionalInterfaceClass()
```

Get the name of the invoked type to which this
lambda has been converted

**Returns:** the name of the functional interface class to which
this lambda has been converted

- getFunctionalInterfaceMethodName

```java
public
String
getFunctionalInterfaceMethodName()
```

Get the name of the primary method for the functional interface
to which this lambda has been converted.

**Returns:** the name of the primary methods of the functional interface

- getFunctionalInterfaceMethodSignature

```java
public
String
getFunctionalInterfaceMethodSignature()
```

Get the signature of the primary method for the functional
interface to which this lambda has been converted.

**Returns:** the signature of the primary method of the functional
interface

- getImplClass

```java
public
String
getImplClass()
```

Get the name of the class containing the implementation
method.

**Returns:** the name of the class containing the implementation
method

- getImplMethodName

```java
public
String
getImplMethodName()
```

Get the name of the implementation method.

**Returns:** the name of the implementation method

- getImplMethodSignature

```java
public
String
getImplMethodSignature()
```

Get the signature of the implementation method.

**Returns:** the signature of the implementation method

- getImplMethodKind

```java
public int getImplMethodKind()
```

Get the method handle kind (see

MethodHandleInfo

) of
the implementation method.

**Returns:** the method handle kind of the implementation method

- getInstantiatedMethodType

```java
public final
String
getInstantiatedMethodType()
```

Get the signature of the primary functional interface method
after type variables are substituted with their instantiation
from the capture site.

**Returns:** the signature of the primary functional interface method
after type variable processing

- getCapturedArgCount

```java
public int getCapturedArgCount()
```

Get the count of dynamic arguments to the lambda capture site.

**Returns:** the count of dynamic arguments to the lambda capture site

- getCapturedArg

```java
public
Object
getCapturedArg​(int i)
```

Get a dynamic argument to the lambda capture site.

**Parameters:** i

- the argument to capture
**Returns:** a dynamic argument to the lambda capture site

Constructor Detail

- SerializedLambda

```java
public SerializedLambda​(
Class
<?> capturingClass,

String
functionalInterfaceClass,

String
functionalInterfaceMethodName,

String
functionalInterfaceMethodSignature,
int implMethodKind,

String
implClass,

String
implMethodName,

String
implMethodSignature,

String
instantiatedMethodType,

Object
[] capturedArgs)
```

Create a

SerializedLambda

from the low-level information present
at the lambda factory site.

**Parameters:** capturingClass

- The class in which the lambda expression appears
**Parameters:** functionalInterfaceClass

- Name, in slash-delimited form, of static
type of the returned lambda object
**Parameters:** functionalInterfaceMethodName

- Name of the functional interface
method for the present at the
lambda factory site
**Parameters:** functionalInterfaceMethodSignature

- Signature of the functional
interface method present at
the lambda factory site
**Parameters:** implMethodKind

- Method handle kind for the implementation method
**Parameters:** implClass

- Name, in slash-delimited form, for the class holding
the implementation method
**Parameters:** implMethodName

- Name of the implementation method
**Parameters:** implMethodSignature

- Signature of the implementation method
**Parameters:** instantiatedMethodType

- The signature of the primary functional
interface method after type variables
are substituted with their instantiation
from the capture site
**Parameters:** capturedArgs

- The dynamic arguments to the lambda factory site,
which represent variables captured by
the lambda

---

#### Constructor Detail

SerializedLambda

```java
public SerializedLambda​(
Class
<?> capturingClass,

String
functionalInterfaceClass,

String
functionalInterfaceMethodName,

String
functionalInterfaceMethodSignature,
int implMethodKind,

String
implClass,

String
implMethodName,

String
implMethodSignature,

String
instantiatedMethodType,

Object
[] capturedArgs)
```

Create a

SerializedLambda

from the low-level information present
at the lambda factory site.

**Parameters:** capturingClass

- The class in which the lambda expression appears
**Parameters:** functionalInterfaceClass

- Name, in slash-delimited form, of static
type of the returned lambda object
**Parameters:** functionalInterfaceMethodName

- Name of the functional interface
method for the present at the
lambda factory site
**Parameters:** functionalInterfaceMethodSignature

- Signature of the functional
interface method present at
the lambda factory site
**Parameters:** implMethodKind

- Method handle kind for the implementation method
**Parameters:** implClass

- Name, in slash-delimited form, for the class holding
the implementation method
**Parameters:** implMethodName

- Name of the implementation method
**Parameters:** implMethodSignature

- Signature of the implementation method
**Parameters:** instantiatedMethodType

- The signature of the primary functional
interface method after type variables
are substituted with their instantiation
from the capture site
**Parameters:** capturedArgs

- The dynamic arguments to the lambda factory site,
which represent variables captured by
the lambda

---

#### SerializedLambda

public SerializedLambda​(

Class

<?> capturingClass,

String

functionalInterfaceClass,

String

functionalInterfaceMethodName,

String

functionalInterfaceMethodSignature,
int implMethodKind,

String

implClass,

String

implMethodName,

String

implMethodSignature,

String

instantiatedMethodType,

Object

[] capturedArgs)

Create a

SerializedLambda

from the low-level information present
at the lambda factory site.

Method Detail

- getCapturingClass

```java
public
String
getCapturingClass()
```

Get the name of the class that captured this lambda.

**Returns:** the name of the class that captured this lambda

- getFunctionalInterfaceClass

```java
public
String
getFunctionalInterfaceClass()
```

Get the name of the invoked type to which this
lambda has been converted

**Returns:** the name of the functional interface class to which
this lambda has been converted

- getFunctionalInterfaceMethodName

```java
public
String
getFunctionalInterfaceMethodName()
```

Get the name of the primary method for the functional interface
to which this lambda has been converted.

**Returns:** the name of the primary methods of the functional interface

- getFunctionalInterfaceMethodSignature

```java
public
String
getFunctionalInterfaceMethodSignature()
```

Get the signature of the primary method for the functional
interface to which this lambda has been converted.

**Returns:** the signature of the primary method of the functional
interface

- getImplClass

```java
public
String
getImplClass()
```

Get the name of the class containing the implementation
method.

**Returns:** the name of the class containing the implementation
method

- getImplMethodName

```java
public
String
getImplMethodName()
```

Get the name of the implementation method.

**Returns:** the name of the implementation method

- getImplMethodSignature

```java
public
String
getImplMethodSignature()
```

Get the signature of the implementation method.

**Returns:** the signature of the implementation method

- getImplMethodKind

```java
public int getImplMethodKind()
```

Get the method handle kind (see

MethodHandleInfo

) of
the implementation method.

**Returns:** the method handle kind of the implementation method

- getInstantiatedMethodType

```java
public final
String
getInstantiatedMethodType()
```

Get the signature of the primary functional interface method
after type variables are substituted with their instantiation
from the capture site.

**Returns:** the signature of the primary functional interface method
after type variable processing

- getCapturedArgCount

```java
public int getCapturedArgCount()
```

Get the count of dynamic arguments to the lambda capture site.

**Returns:** the count of dynamic arguments to the lambda capture site

- getCapturedArg

```java
public
Object
getCapturedArg​(int i)
```

Get a dynamic argument to the lambda capture site.

**Parameters:** i

- the argument to capture
**Returns:** a dynamic argument to the lambda capture site

---

#### Method Detail

getCapturingClass

```java
public
String
getCapturingClass()
```

Get the name of the class that captured this lambda.

**Returns:** the name of the class that captured this lambda

---

#### getCapturingClass

public

String

getCapturingClass()

Get the name of the class that captured this lambda.

getFunctionalInterfaceClass

```java
public
String
getFunctionalInterfaceClass()
```

Get the name of the invoked type to which this
lambda has been converted

**Returns:** the name of the functional interface class to which
this lambda has been converted

---

#### getFunctionalInterfaceClass

public

String

getFunctionalInterfaceClass()

Get the name of the invoked type to which this
lambda has been converted

getFunctionalInterfaceMethodName

```java
public
String
getFunctionalInterfaceMethodName()
```

Get the name of the primary method for the functional interface
to which this lambda has been converted.

**Returns:** the name of the primary methods of the functional interface

---

#### getFunctionalInterfaceMethodName

public

String

getFunctionalInterfaceMethodName()

Get the name of the primary method for the functional interface
to which this lambda has been converted.

getFunctionalInterfaceMethodSignature

```java
public
String
getFunctionalInterfaceMethodSignature()
```

Get the signature of the primary method for the functional
interface to which this lambda has been converted.

**Returns:** the signature of the primary method of the functional
interface

---

#### getFunctionalInterfaceMethodSignature

public

String

getFunctionalInterfaceMethodSignature()

Get the signature of the primary method for the functional
interface to which this lambda has been converted.

getImplClass

```java
public
String
getImplClass()
```

Get the name of the class containing the implementation
method.

**Returns:** the name of the class containing the implementation
method

---

#### getImplClass

public

String

getImplClass()

Get the name of the class containing the implementation
method.

getImplMethodName

```java
public
String
getImplMethodName()
```

Get the name of the implementation method.

**Returns:** the name of the implementation method

---

#### getImplMethodName

public

String

getImplMethodName()

Get the name of the implementation method.

getImplMethodSignature

```java
public
String
getImplMethodSignature()
```

Get the signature of the implementation method.

**Returns:** the signature of the implementation method

---

#### getImplMethodSignature

public

String

getImplMethodSignature()

Get the signature of the implementation method.

getImplMethodKind

```java
public int getImplMethodKind()
```

Get the method handle kind (see

MethodHandleInfo

) of
the implementation method.

**Returns:** the method handle kind of the implementation method

---

#### getImplMethodKind

public int getImplMethodKind()

Get the method handle kind (see

MethodHandleInfo

) of
the implementation method.

getInstantiatedMethodType

```java
public final
String
getInstantiatedMethodType()
```

Get the signature of the primary functional interface method
after type variables are substituted with their instantiation
from the capture site.

**Returns:** the signature of the primary functional interface method
after type variable processing

---

#### getInstantiatedMethodType

public final

String

getInstantiatedMethodType()

Get the signature of the primary functional interface method
after type variables are substituted with their instantiation
from the capture site.

getCapturedArgCount

```java
public int getCapturedArgCount()
```

Get the count of dynamic arguments to the lambda capture site.

**Returns:** the count of dynamic arguments to the lambda capture site

---

#### getCapturedArgCount

public int getCapturedArgCount()

Get the count of dynamic arguments to the lambda capture site.

getCapturedArg

```java
public
Object
getCapturedArg​(int i)
```

Get a dynamic argument to the lambda capture site.

**Parameters:** i

- the argument to capture
**Returns:** a dynamic argument to the lambda capture site

---

#### getCapturedArg

public

Object

getCapturedArg​(int i)

Get a dynamic argument to the lambda capture site.

---

