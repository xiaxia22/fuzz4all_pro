# Class Encoder

**Source:** `java.desktop\java\beans\Encoder.html`

### Class Description

```java
public class
Encoder

extends
Object
```

An

Encoder

is a class which can be used to create
files or streams that encode the state of a collection of
JavaBeans in terms of their public APIs. The

Encoder

,
in conjunction with its persistence delegates, is responsible for
breaking the object graph down into a series of

Statement

s
and

Expression

s which can be used to create it.
A subclass typically provides a syntax for these expressions
using some human readable form - like Java source code or XML.

**Direct Known Subclasses:** XMLEncoder

---

### Field Details

*No entries found.*

### Constructor Details

#### public Encoder()

*No description found.*

---

### Method Details

#### protected void writeObject​(
Object
o)

Write the specified object to the output stream.
The serialized form will denote a series of
expressions, the combined effect of which will create
an equivalent object when the input stream is read.
By default, the object is assumed to be a

JavaBean

with a nullary constructor, whose state is defined by
the matching pairs of "setter" and "getter" methods
returned by the Introspector.

**Parameters:**
- o

- The object to be written to the stream.

**See Also:**
- XMLDecoder.readObject()

---

#### public void setExceptionListener​(
ExceptionListener
exceptionListener)

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

**Parameters:**
- exceptionListener

- The exception handler for this stream;
if

null

the default exception listener will be used.

**See Also:**
- getExceptionListener()

---

#### public
ExceptionListener
getExceptionListener()

Gets the exception handler for this stream.

**Returns:**
- The exception handler for this stream;
Will return the default exception listener if this has not explicitly been set.

**See Also:**
- setExceptionListener(java.beans.ExceptionListener)

---

#### public
PersistenceDelegate
getPersistenceDelegate​(
Class
<?> type)

Returns the persistence delegate for the given type.
The persistence delegate is calculated by applying
the following rules in order:

- If a persistence delegate is associated with the given type
by using the

setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

method
it is returned.

A persistence delegate is then looked up by the name
composed of the fully qualified name of the given type
and the "PersistenceDelegate" postfix.
For example, a persistence delegate for the

Bean

class
should be named

BeanPersistenceDelegate

and located in the same package.

```java
public class Bean { ... }
public class BeanPersistenceDelegate { ... }
```

The instance of the

BeanPersistenceDelegate

class
is returned for the

Bean

class.

If the type is

null

,
a shared internal persistence delegate is returned
that encodes

null

value.

If the type is an

enum

declaration,
a shared internal persistence delegate is returned
that encodes constants of this enumeration
by their names.

If the type is a primitive type or the corresponding wrapper,
a shared internal persistence delegate is returned
that encodes values of the given type.

If the type is an array,
a shared internal persistence delegate is returned
that encodes an array of the appropriate type and length,
and each of its elements as if they are properties.

If the type is a proxy,
a shared internal persistence delegate is returned
that encodes a proxy instance by using
the

Proxy.newProxyInstance(java.lang.ClassLoader, java.lang.Class<?>[], java.lang.reflect.InvocationHandler)

method.

If the

BeanInfo

for this type has a

BeanDescriptor

which defined a "persistenceDelegate" attribute,
the value of this named attribute is returned.

In all other cases the default persistence delegate is returned.
The default persistence delegate assumes the type is a

JavaBean

,
implying that it has a default constructor and that its state
may be characterized by the matching pairs of "setter" and "getter"
methods returned by the

Introspector

class.
The default constructor is the constructor with the greatest number
of parameters that has the

ConstructorProperties

annotation.
If none of the constructors has the

ConstructorProperties

annotation,
then the nullary constructor (constructor with no parameters) will be used.
For example, in the following code fragment, the nullary constructor
for the

Foo

class will be used,
while the two-parameter constructor
for the

Bar

class will be used.

```java
public class Foo {
public Foo() { ... }
public Foo(int x) { ... }
}
public class Bar {
public Bar() { ... }
@ConstructorProperties({"x"})
public Bar(int x) { ... }
@ConstructorProperties({"x", "y"})
public Bar(int x, int y) { ... }
}
```

**Parameters:**
- type

- the class of the objects

**Returns:**
- the persistence delegate for the given type

**See Also:**
- setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

,

Introspector.getBeanInfo(java.lang.Class<?>)

,

BeanInfo.getBeanDescriptor()

---

#### public void setPersistenceDelegate​(
Class
<?> type,

PersistenceDelegate
delegate)

Associates the specified persistence delegate with the given type.

**Parameters:**
- type

- the class of objects that the specified persistence delegate applies to
- delegate

- the persistence delegate for instances of the given type

**See Also:**
- getPersistenceDelegate(java.lang.Class<?>)

,

Introspector.getBeanInfo(java.lang.Class<?>)

,

BeanInfo.getBeanDescriptor()

---

#### public
Object
remove​(
Object
oldInstance)

Removes the entry for this instance, returning the old entry.

**Parameters:**
- oldInstance

- The entry that should be removed.

**Returns:**
- The entry that was removed.

**See Also:**
- get(java.lang.Object)

---

#### public
Object
get​(
Object
oldInstance)

Returns a tentative value for

oldInstance

in
the environment created by this stream. A persistence
delegate can use its

mutatesTo

method to
determine whether this value may be initialized to
form the equivalent object at the output or whether
a new object must be instantiated afresh. If the
stream has not yet seen this value, null is returned.

**Parameters:**
- oldInstance

- The instance to be looked up.

**Returns:**
- The object, null if the object has not been seen before.

---

#### public void writeStatement​(
Statement
oldStm)

Writes statement

oldStm

to the stream.
The

oldStm

should be written entirely
in terms of the callers environment, i.e. the
target and all arguments should be part of the
object graph being written. These expressions
represent a series of "what happened" expressions
which tell the output stream how to produce an
object graph like the original.

The implementation of this method will produce
a second expression to represent the same expression in
an environment that will exist when the stream is read.
This is achieved simply by calling

writeObject

on the target and all the arguments and building a new
expression with the results.

**Parameters:**
- oldStm

- The expression to be written to the stream.

---

#### public void writeExpression​(
Expression
oldExp)

The implementation first checks to see if an
expression with this value has already been written.
If not, the expression is cloned, using
the same procedure as

writeStatement

,
and the value of this expression is reconciled
with the value of the cloned expression
by calling

writeObject

.

**Parameters:**
- oldExp

- The expression to be written to the stream.

---

### Additional Sections

#### Class Encoder

java.lang.Object

- java.beans.Encoder

java.beans.Encoder

**Direct Known Subclasses:** XMLEncoder

```java
public class
Encoder

extends
Object
```

An

Encoder

is a class which can be used to create
files or streams that encode the state of a collection of
JavaBeans in terms of their public APIs. The

Encoder

,
in conjunction with its persistence delegates, is responsible for
breaking the object graph down into a series of

Statement

s
and

Expression

s which can be used to create it.
A subclass typically provides a syntax for these expressions
using some human readable form - like Java source code or XML.

**Since:** 1.4

public class

Encoder

extends

Object

An

Encoder

is a class which can be used to create
files or streams that encode the state of a collection of
JavaBeans in terms of their public APIs. The

Encoder

,
in conjunction with its persistence delegates, is responsible for
breaking the object graph down into a series of

Statement

s
and

Expression

s which can be used to create it.
A subclass typically provides a syntax for these expressions
using some human readable form - like Java source code or XML.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Encoder

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

get

​(

Object

oldInstance)

Returns a tentative value for

oldInstance

in
the environment created by this stream.

ExceptionListener

getExceptionListener

()

Gets the exception handler for this stream.

PersistenceDelegate

getPersistenceDelegate

​(

Class

<?> type)

Returns the persistence delegate for the given type.

Object

remove

​(

Object

oldInstance)

Removes the entry for this instance, returning the old entry.

void

setExceptionListener

​(

ExceptionListener

exceptionListener)

Sets the exception handler for this stream to

exceptionListener

.

void

setPersistenceDelegate

​(

Class

<?> type,

PersistenceDelegate

delegate)

Associates the specified persistence delegate with the given type.

void

writeExpression

​(

Expression

oldExp)

The implementation first checks to see if an
expression with this value has already been written.

protected void

writeObject

​(

Object

o)

Write the specified object to the output stream.

void

writeStatement

​(

Statement

oldStm)

Writes statement

oldStm

to the stream.

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

Encoder

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

get

​(

Object

oldInstance)

Returns a tentative value for

oldInstance

in
the environment created by this stream.

ExceptionListener

getExceptionListener

()

Gets the exception handler for this stream.

PersistenceDelegate

getPersistenceDelegate

​(

Class

<?> type)

Returns the persistence delegate for the given type.

Object

remove

​(

Object

oldInstance)

Removes the entry for this instance, returning the old entry.

void

setExceptionListener

​(

ExceptionListener

exceptionListener)

Sets the exception handler for this stream to

exceptionListener

.

void

setPersistenceDelegate

​(

Class

<?> type,

PersistenceDelegate

delegate)

Associates the specified persistence delegate with the given type.

void

writeExpression

​(

Expression

oldExp)

The implementation first checks to see if an
expression with this value has already been written.

protected void

writeObject

​(

Object

o)

Write the specified object to the output stream.

void

writeStatement

​(

Statement

oldStm)

Writes statement

oldStm

to the stream.

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

Returns a tentative value for

oldInstance

in
the environment created by this stream.

Gets the exception handler for this stream.

Returns the persistence delegate for the given type.

Removes the entry for this instance, returning the old entry.

Sets the exception handler for this stream to

exceptionListener

.

Associates the specified persistence delegate with the given type.

The implementation first checks to see if an
expression with this value has already been written.

Write the specified object to the output stream.

Writes statement

oldStm

to the stream.

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

- Encoder

```java
public Encoder()
```

============ METHOD DETAIL ==========

- Method Detail

- writeObject

```java
protected void writeObject​(
Object
o)
```

Write the specified object to the output stream.
The serialized form will denote a series of
expressions, the combined effect of which will create
an equivalent object when the input stream is read.
By default, the object is assumed to be a

JavaBean

with a nullary constructor, whose state is defined by
the matching pairs of "setter" and "getter" methods
returned by the Introspector.

**Parameters:** o

- The object to be written to the stream.
**See Also:** XMLDecoder.readObject()

- setExceptionListener

```java
public void setExceptionListener​(
ExceptionListener
exceptionListener)
```

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

**Parameters:** exceptionListener

- The exception handler for this stream;
if

null

the default exception listener will be used.
**See Also:** getExceptionListener()

- getExceptionListener

```java
public
ExceptionListener
getExceptionListener()
```

Gets the exception handler for this stream.

**Returns:** The exception handler for this stream;
Will return the default exception listener if this has not explicitly been set.
**See Also:** setExceptionListener(java.beans.ExceptionListener)

- getPersistenceDelegate

```java
public
PersistenceDelegate
getPersistenceDelegate​(
Class
<?> type)
```

Returns the persistence delegate for the given type.
The persistence delegate is calculated by applying
the following rules in order:

- If a persistence delegate is associated with the given type
by using the

setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

method
it is returned.

A persistence delegate is then looked up by the name
composed of the fully qualified name of the given type
and the "PersistenceDelegate" postfix.
For example, a persistence delegate for the

Bean

class
should be named

BeanPersistenceDelegate

and located in the same package.

```java
public class Bean { ... }
public class BeanPersistenceDelegate { ... }
```

The instance of the

BeanPersistenceDelegate

class
is returned for the

Bean

class.

If the type is

null

,
a shared internal persistence delegate is returned
that encodes

null

value.

If the type is an

enum

declaration,
a shared internal persistence delegate is returned
that encodes constants of this enumeration
by their names.

If the type is a primitive type or the corresponding wrapper,
a shared internal persistence delegate is returned
that encodes values of the given type.

If the type is an array,
a shared internal persistence delegate is returned
that encodes an array of the appropriate type and length,
and each of its elements as if they are properties.

If the type is a proxy,
a shared internal persistence delegate is returned
that encodes a proxy instance by using
the

Proxy.newProxyInstance(java.lang.ClassLoader, java.lang.Class<?>[], java.lang.reflect.InvocationHandler)

method.

If the

BeanInfo

for this type has a

BeanDescriptor

which defined a "persistenceDelegate" attribute,
the value of this named attribute is returned.

In all other cases the default persistence delegate is returned.
The default persistence delegate assumes the type is a

JavaBean

,
implying that it has a default constructor and that its state
may be characterized by the matching pairs of "setter" and "getter"
methods returned by the

Introspector

class.
The default constructor is the constructor with the greatest number
of parameters that has the

ConstructorProperties

annotation.
If none of the constructors has the

ConstructorProperties

annotation,
then the nullary constructor (constructor with no parameters) will be used.
For example, in the following code fragment, the nullary constructor
for the

Foo

class will be used,
while the two-parameter constructor
for the

Bar

class will be used.

```java
public class Foo {
public Foo() { ... }
public Foo(int x) { ... }
}
public class Bar {
public Bar() { ... }
@ConstructorProperties({"x"})
public Bar(int x) { ... }
@ConstructorProperties({"x", "y"})
public Bar(int x, int y) { ... }
}
```

**Parameters:** type

- the class of the objects
**Returns:** the persistence delegate for the given type
**See Also:** setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

,

Introspector.getBeanInfo(java.lang.Class<?>)

,

BeanInfo.getBeanDescriptor()

- setPersistenceDelegate

```java
public void setPersistenceDelegate​(
Class
<?> type,

PersistenceDelegate
delegate)
```

Associates the specified persistence delegate with the given type.

**Parameters:** type

- the class of objects that the specified persistence delegate applies to
**Parameters:** delegate

- the persistence delegate for instances of the given type
**See Also:** getPersistenceDelegate(java.lang.Class<?>)

,

Introspector.getBeanInfo(java.lang.Class<?>)

,

BeanInfo.getBeanDescriptor()

- remove

```java
public
Object
remove​(
Object
oldInstance)
```

Removes the entry for this instance, returning the old entry.

**Parameters:** oldInstance

- The entry that should be removed.
**Returns:** The entry that was removed.
**See Also:** get(java.lang.Object)

- get

```java
public
Object
get​(
Object
oldInstance)
```

Returns a tentative value for

oldInstance

in
the environment created by this stream. A persistence
delegate can use its

mutatesTo

method to
determine whether this value may be initialized to
form the equivalent object at the output or whether
a new object must be instantiated afresh. If the
stream has not yet seen this value, null is returned.

**Parameters:** oldInstance

- The instance to be looked up.
**Returns:** The object, null if the object has not been seen before.

- writeStatement

```java
public void writeStatement​(
Statement
oldStm)
```

Writes statement

oldStm

to the stream.
The

oldStm

should be written entirely
in terms of the callers environment, i.e. the
target and all arguments should be part of the
object graph being written. These expressions
represent a series of "what happened" expressions
which tell the output stream how to produce an
object graph like the original.

The implementation of this method will produce
a second expression to represent the same expression in
an environment that will exist when the stream is read.
This is achieved simply by calling

writeObject

on the target and all the arguments and building a new
expression with the results.

**Parameters:** oldStm

- The expression to be written to the stream.

- writeExpression

```java
public void writeExpression​(
Expression
oldExp)
```

The implementation first checks to see if an
expression with this value has already been written.
If not, the expression is cloned, using
the same procedure as

writeStatement

,
and the value of this expression is reconciled
with the value of the cloned expression
by calling

writeObject

.

**Parameters:** oldExp

- The expression to be written to the stream.

Constructor Detail

- Encoder

```java
public Encoder()
```

---

#### Constructor Detail

Encoder

```java
public Encoder()
```

---

#### Encoder

public Encoder()

Method Detail

- writeObject

```java
protected void writeObject​(
Object
o)
```

Write the specified object to the output stream.
The serialized form will denote a series of
expressions, the combined effect of which will create
an equivalent object when the input stream is read.
By default, the object is assumed to be a

JavaBean

with a nullary constructor, whose state is defined by
the matching pairs of "setter" and "getter" methods
returned by the Introspector.

**Parameters:** o

- The object to be written to the stream.
**See Also:** XMLDecoder.readObject()

- setExceptionListener

```java
public void setExceptionListener​(
ExceptionListener
exceptionListener)
```

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

**Parameters:** exceptionListener

- The exception handler for this stream;
if

null

the default exception listener will be used.
**See Also:** getExceptionListener()

- getExceptionListener

```java
public
ExceptionListener
getExceptionListener()
```

Gets the exception handler for this stream.

**Returns:** The exception handler for this stream;
Will return the default exception listener if this has not explicitly been set.
**See Also:** setExceptionListener(java.beans.ExceptionListener)

- getPersistenceDelegate

```java
public
PersistenceDelegate
getPersistenceDelegate​(
Class
<?> type)
```

Returns the persistence delegate for the given type.
The persistence delegate is calculated by applying
the following rules in order:

- If a persistence delegate is associated with the given type
by using the

setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

method
it is returned.

A persistence delegate is then looked up by the name
composed of the fully qualified name of the given type
and the "PersistenceDelegate" postfix.
For example, a persistence delegate for the

Bean

class
should be named

BeanPersistenceDelegate

and located in the same package.

```java
public class Bean { ... }
public class BeanPersistenceDelegate { ... }
```

The instance of the

BeanPersistenceDelegate

class
is returned for the

Bean

class.

If the type is

null

,
a shared internal persistence delegate is returned
that encodes

null

value.

If the type is an

enum

declaration,
a shared internal persistence delegate is returned
that encodes constants of this enumeration
by their names.

If the type is a primitive type or the corresponding wrapper,
a shared internal persistence delegate is returned
that encodes values of the given type.

If the type is an array,
a shared internal persistence delegate is returned
that encodes an array of the appropriate type and length,
and each of its elements as if they are properties.

If the type is a proxy,
a shared internal persistence delegate is returned
that encodes a proxy instance by using
the

Proxy.newProxyInstance(java.lang.ClassLoader, java.lang.Class<?>[], java.lang.reflect.InvocationHandler)

method.

If the

BeanInfo

for this type has a

BeanDescriptor

which defined a "persistenceDelegate" attribute,
the value of this named attribute is returned.

In all other cases the default persistence delegate is returned.
The default persistence delegate assumes the type is a

JavaBean

,
implying that it has a default constructor and that its state
may be characterized by the matching pairs of "setter" and "getter"
methods returned by the

Introspector

class.
The default constructor is the constructor with the greatest number
of parameters that has the

ConstructorProperties

annotation.
If none of the constructors has the

ConstructorProperties

annotation,
then the nullary constructor (constructor with no parameters) will be used.
For example, in the following code fragment, the nullary constructor
for the

Foo

class will be used,
while the two-parameter constructor
for the

Bar

class will be used.

```java
public class Foo {
public Foo() { ... }
public Foo(int x) { ... }
}
public class Bar {
public Bar() { ... }
@ConstructorProperties({"x"})
public Bar(int x) { ... }
@ConstructorProperties({"x", "y"})
public Bar(int x, int y) { ... }
}
```

**Parameters:** type

- the class of the objects
**Returns:** the persistence delegate for the given type
**See Also:** setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

,

Introspector.getBeanInfo(java.lang.Class<?>)

,

BeanInfo.getBeanDescriptor()

- setPersistenceDelegate

```java
public void setPersistenceDelegate​(
Class
<?> type,

PersistenceDelegate
delegate)
```

Associates the specified persistence delegate with the given type.

**Parameters:** type

- the class of objects that the specified persistence delegate applies to
**Parameters:** delegate

- the persistence delegate for instances of the given type
**See Also:** getPersistenceDelegate(java.lang.Class<?>)

,

Introspector.getBeanInfo(java.lang.Class<?>)

,

BeanInfo.getBeanDescriptor()

- remove

```java
public
Object
remove​(
Object
oldInstance)
```

Removes the entry for this instance, returning the old entry.

**Parameters:** oldInstance

- The entry that should be removed.
**Returns:** The entry that was removed.
**See Also:** get(java.lang.Object)

- get

```java
public
Object
get​(
Object
oldInstance)
```

Returns a tentative value for

oldInstance

in
the environment created by this stream. A persistence
delegate can use its

mutatesTo

method to
determine whether this value may be initialized to
form the equivalent object at the output or whether
a new object must be instantiated afresh. If the
stream has not yet seen this value, null is returned.

**Parameters:** oldInstance

- The instance to be looked up.
**Returns:** The object, null if the object has not been seen before.

- writeStatement

```java
public void writeStatement​(
Statement
oldStm)
```

Writes statement

oldStm

to the stream.
The

oldStm

should be written entirely
in terms of the callers environment, i.e. the
target and all arguments should be part of the
object graph being written. These expressions
represent a series of "what happened" expressions
which tell the output stream how to produce an
object graph like the original.

The implementation of this method will produce
a second expression to represent the same expression in
an environment that will exist when the stream is read.
This is achieved simply by calling

writeObject

on the target and all the arguments and building a new
expression with the results.

**Parameters:** oldStm

- The expression to be written to the stream.

- writeExpression

```java
public void writeExpression​(
Expression
oldExp)
```

The implementation first checks to see if an
expression with this value has already been written.
If not, the expression is cloned, using
the same procedure as

writeStatement

,
and the value of this expression is reconciled
with the value of the cloned expression
by calling

writeObject

.

**Parameters:** oldExp

- The expression to be written to the stream.

---

#### Method Detail

writeObject

```java
protected void writeObject​(
Object
o)
```

Write the specified object to the output stream.
The serialized form will denote a series of
expressions, the combined effect of which will create
an equivalent object when the input stream is read.
By default, the object is assumed to be a

JavaBean

with a nullary constructor, whose state is defined by
the matching pairs of "setter" and "getter" methods
returned by the Introspector.

**Parameters:** o

- The object to be written to the stream.
**See Also:** XMLDecoder.readObject()

---

#### writeObject

protected void writeObject​(

Object

o)

Write the specified object to the output stream.
The serialized form will denote a series of
expressions, the combined effect of which will create
an equivalent object when the input stream is read.
By default, the object is assumed to be a

JavaBean

with a nullary constructor, whose state is defined by
the matching pairs of "setter" and "getter" methods
returned by the Introspector.

setExceptionListener

```java
public void setExceptionListener​(
ExceptionListener
exceptionListener)
```

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

**Parameters:** exceptionListener

- The exception handler for this stream;
if

null

the default exception listener will be used.
**See Also:** getExceptionListener()

---

#### setExceptionListener

public void setExceptionListener​(

ExceptionListener

exceptionListener)

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

getExceptionListener

```java
public
ExceptionListener
getExceptionListener()
```

Gets the exception handler for this stream.

**Returns:** The exception handler for this stream;
Will return the default exception listener if this has not explicitly been set.
**See Also:** setExceptionListener(java.beans.ExceptionListener)

---

#### getExceptionListener

public

ExceptionListener

getExceptionListener()

Gets the exception handler for this stream.

getPersistenceDelegate

```java
public
PersistenceDelegate
getPersistenceDelegate​(
Class
<?> type)
```

Returns the persistence delegate for the given type.
The persistence delegate is calculated by applying
the following rules in order:

- If a persistence delegate is associated with the given type
by using the

setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

method
it is returned.

A persistence delegate is then looked up by the name
composed of the fully qualified name of the given type
and the "PersistenceDelegate" postfix.
For example, a persistence delegate for the

Bean

class
should be named

BeanPersistenceDelegate

and located in the same package.

```java
public class Bean { ... }
public class BeanPersistenceDelegate { ... }
```

The instance of the

BeanPersistenceDelegate

class
is returned for the

Bean

class.

If the type is

null

,
a shared internal persistence delegate is returned
that encodes

null

value.

If the type is an

enum

declaration,
a shared internal persistence delegate is returned
that encodes constants of this enumeration
by their names.

If the type is a primitive type or the corresponding wrapper,
a shared internal persistence delegate is returned
that encodes values of the given type.

If the type is an array,
a shared internal persistence delegate is returned
that encodes an array of the appropriate type and length,
and each of its elements as if they are properties.

If the type is a proxy,
a shared internal persistence delegate is returned
that encodes a proxy instance by using
the

Proxy.newProxyInstance(java.lang.ClassLoader, java.lang.Class<?>[], java.lang.reflect.InvocationHandler)

method.

If the

BeanInfo

for this type has a

BeanDescriptor

which defined a "persistenceDelegate" attribute,
the value of this named attribute is returned.

In all other cases the default persistence delegate is returned.
The default persistence delegate assumes the type is a

JavaBean

,
implying that it has a default constructor and that its state
may be characterized by the matching pairs of "setter" and "getter"
methods returned by the

Introspector

class.
The default constructor is the constructor with the greatest number
of parameters that has the

ConstructorProperties

annotation.
If none of the constructors has the

ConstructorProperties

annotation,
then the nullary constructor (constructor with no parameters) will be used.
For example, in the following code fragment, the nullary constructor
for the

Foo

class will be used,
while the two-parameter constructor
for the

Bar

class will be used.

```java
public class Foo {
public Foo() { ... }
public Foo(int x) { ... }
}
public class Bar {
public Bar() { ... }
@ConstructorProperties({"x"})
public Bar(int x) { ... }
@ConstructorProperties({"x", "y"})
public Bar(int x, int y) { ... }
}
```

**Parameters:** type

- the class of the objects
**Returns:** the persistence delegate for the given type
**See Also:** setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

,

Introspector.getBeanInfo(java.lang.Class<?>)

,

BeanInfo.getBeanDescriptor()

---

#### getPersistenceDelegate

public

PersistenceDelegate

getPersistenceDelegate​(

Class

<?> type)

Returns the persistence delegate for the given type.
The persistence delegate is calculated by applying
the following rules in order:

- If a persistence delegate is associated with the given type
by using the

setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

method
it is returned.

A persistence delegate is then looked up by the name
composed of the fully qualified name of the given type
and the "PersistenceDelegate" postfix.
For example, a persistence delegate for the

Bean

class
should be named

BeanPersistenceDelegate

and located in the same package.

```java
public class Bean { ... }
public class BeanPersistenceDelegate { ... }
```

The instance of the

BeanPersistenceDelegate

class
is returned for the

Bean

class.

If the type is

null

,
a shared internal persistence delegate is returned
that encodes

null

value.

If the type is an

enum

declaration,
a shared internal persistence delegate is returned
that encodes constants of this enumeration
by their names.

If the type is a primitive type or the corresponding wrapper,
a shared internal persistence delegate is returned
that encodes values of the given type.

If the type is an array,
a shared internal persistence delegate is returned
that encodes an array of the appropriate type and length,
and each of its elements as if they are properties.

If the type is a proxy,
a shared internal persistence delegate is returned
that encodes a proxy instance by using
the

Proxy.newProxyInstance(java.lang.ClassLoader, java.lang.Class<?>[], java.lang.reflect.InvocationHandler)

method.

If the

BeanInfo

for this type has a

BeanDescriptor

which defined a "persistenceDelegate" attribute,
the value of this named attribute is returned.

In all other cases the default persistence delegate is returned.
The default persistence delegate assumes the type is a

JavaBean

,
implying that it has a default constructor and that its state
may be characterized by the matching pairs of "setter" and "getter"
methods returned by the

Introspector

class.
The default constructor is the constructor with the greatest number
of parameters that has the

ConstructorProperties

annotation.
If none of the constructors has the

ConstructorProperties

annotation,
then the nullary constructor (constructor with no parameters) will be used.
For example, in the following code fragment, the nullary constructor
for the

Foo

class will be used,
while the two-parameter constructor
for the

Bar

class will be used.

```java
public class Foo {
public Foo() { ... }
public Foo(int x) { ... }
}
public class Bar {
public Bar() { ... }
@ConstructorProperties({"x"})
public Bar(int x) { ... }
@ConstructorProperties({"x", "y"})
public Bar(int x, int y) { ... }
}
```

If a persistence delegate is associated with the given type
by using the

setPersistenceDelegate(java.lang.Class<?>, java.beans.PersistenceDelegate)

method
it is returned.

A persistence delegate is then looked up by the name
composed of the fully qualified name of the given type
and the "PersistenceDelegate" postfix.
For example, a persistence delegate for the

Bean

class
should be named

BeanPersistenceDelegate

and located in the same package.

```java
public class Bean { ... }
public class BeanPersistenceDelegate { ... }
```

The instance of the

BeanPersistenceDelegate

class
is returned for the

Bean

class.

If the type is

null

,
a shared internal persistence delegate is returned
that encodes

null

value.

If the type is an

enum

declaration,
a shared internal persistence delegate is returned
that encodes constants of this enumeration
by their names.

If the type is a primitive type or the corresponding wrapper,
a shared internal persistence delegate is returned
that encodes values of the given type.

If the type is an array,
a shared internal persistence delegate is returned
that encodes an array of the appropriate type and length,
and each of its elements as if they are properties.

If the type is a proxy,
a shared internal persistence delegate is returned
that encodes a proxy instance by using
the

Proxy.newProxyInstance(java.lang.ClassLoader, java.lang.Class<?>[], java.lang.reflect.InvocationHandler)

method.

If the

BeanInfo

for this type has a

BeanDescriptor

which defined a "persistenceDelegate" attribute,
the value of this named attribute is returned.

In all other cases the default persistence delegate is returned.
The default persistence delegate assumes the type is a

JavaBean

,
implying that it has a default constructor and that its state
may be characterized by the matching pairs of "setter" and "getter"
methods returned by the

Introspector

class.
The default constructor is the constructor with the greatest number
of parameters that has the

ConstructorProperties

annotation.
If none of the constructors has the

ConstructorProperties

annotation,
then the nullary constructor (constructor with no parameters) will be used.
For example, in the following code fragment, the nullary constructor
for the

Foo

class will be used,
while the two-parameter constructor
for the

Bar

class will be used.

```java
public class Foo {
public Foo() { ... }
public Foo(int x) { ... }
}
public class Bar {
public Bar() { ... }
@ConstructorProperties({"x"})
public Bar(int x) { ... }
@ConstructorProperties({"x", "y"})
public Bar(int x, int y) { ... }
}
```

public class Bean { ... }
public class BeanPersistenceDelegate { ... }

public class Foo {
public Foo() { ... }
public Foo(int x) { ... }
}
public class Bar {
public Bar() { ... }
@ConstructorProperties({"x"})
public Bar(int x) { ... }
@ConstructorProperties({"x", "y"})
public Bar(int x, int y) { ... }
}

setPersistenceDelegate

```java
public void setPersistenceDelegate​(
Class
<?> type,

PersistenceDelegate
delegate)
```

Associates the specified persistence delegate with the given type.

**Parameters:** type

- the class of objects that the specified persistence delegate applies to
**Parameters:** delegate

- the persistence delegate for instances of the given type
**See Also:** getPersistenceDelegate(java.lang.Class<?>)

,

Introspector.getBeanInfo(java.lang.Class<?>)

,

BeanInfo.getBeanDescriptor()

---

#### setPersistenceDelegate

public void setPersistenceDelegate​(

Class

<?> type,

PersistenceDelegate

delegate)

Associates the specified persistence delegate with the given type.

remove

```java
public
Object
remove​(
Object
oldInstance)
```

Removes the entry for this instance, returning the old entry.

**Parameters:** oldInstance

- The entry that should be removed.
**Returns:** The entry that was removed.
**See Also:** get(java.lang.Object)

---

#### remove

public

Object

remove​(

Object

oldInstance)

Removes the entry for this instance, returning the old entry.

get

```java
public
Object
get​(
Object
oldInstance)
```

Returns a tentative value for

oldInstance

in
the environment created by this stream. A persistence
delegate can use its

mutatesTo

method to
determine whether this value may be initialized to
form the equivalent object at the output or whether
a new object must be instantiated afresh. If the
stream has not yet seen this value, null is returned.

**Parameters:** oldInstance

- The instance to be looked up.
**Returns:** The object, null if the object has not been seen before.

---

#### get

public

Object

get​(

Object

oldInstance)

Returns a tentative value for

oldInstance

in
the environment created by this stream. A persistence
delegate can use its

mutatesTo

method to
determine whether this value may be initialized to
form the equivalent object at the output or whether
a new object must be instantiated afresh. If the
stream has not yet seen this value, null is returned.

writeStatement

```java
public void writeStatement​(
Statement
oldStm)
```

Writes statement

oldStm

to the stream.
The

oldStm

should be written entirely
in terms of the callers environment, i.e. the
target and all arguments should be part of the
object graph being written. These expressions
represent a series of "what happened" expressions
which tell the output stream how to produce an
object graph like the original.

The implementation of this method will produce
a second expression to represent the same expression in
an environment that will exist when the stream is read.
This is achieved simply by calling

writeObject

on the target and all the arguments and building a new
expression with the results.

**Parameters:** oldStm

- The expression to be written to the stream.

---

#### writeStatement

public void writeStatement​(

Statement

oldStm)

Writes statement

oldStm

to the stream.
The

oldStm

should be written entirely
in terms of the callers environment, i.e. the
target and all arguments should be part of the
object graph being written. These expressions
represent a series of "what happened" expressions
which tell the output stream how to produce an
object graph like the original.

The implementation of this method will produce
a second expression to represent the same expression in
an environment that will exist when the stream is read.
This is achieved simply by calling

writeObject

on the target and all the arguments and building a new
expression with the results.

The implementation of this method will produce
a second expression to represent the same expression in
an environment that will exist when the stream is read.
This is achieved simply by calling

writeObject

on the target and all the arguments and building a new
expression with the results.

writeExpression

```java
public void writeExpression​(
Expression
oldExp)
```

The implementation first checks to see if an
expression with this value has already been written.
If not, the expression is cloned, using
the same procedure as

writeStatement

,
and the value of this expression is reconciled
with the value of the cloned expression
by calling

writeObject

.

**Parameters:** oldExp

- The expression to be written to the stream.

---

#### writeExpression

public void writeExpression​(

Expression

oldExp)

The implementation first checks to see if an
expression with this value has already been written.
If not, the expression is cloned, using
the same procedure as

writeStatement

,
and the value of this expression is reconciled
with the value of the cloned expression
by calling

writeObject

.

---

