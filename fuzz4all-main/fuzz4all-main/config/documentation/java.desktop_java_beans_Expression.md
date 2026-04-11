# Class Expression

**Source:** `java.desktop\java\beans\Expression.html`

### Class Description

```java
public class
Expression

extends
Statement
```

An

Expression

object represents a primitive expression
in which a single method is applied to a target and a set of
arguments to return a result - as in

"a.getFoo()"

.

In addition to the properties of the super class, the

Expression

object provides a

value

which
is the object returned when this expression is evaluated.
The return value is typically not provided by the caller and
is instead computed by dynamically finding the method and invoking
it when the first call to

getValue

is made.

**Since:** 1.4
**See Also:** getValue()

,

setValue(java.lang.Object)

---

### Field Details

*No entries found.*

### Constructor Details

#### @ConstructorProperties
({"target","methodName","arguments"})
public Expression​(
Object
target,

String
methodName,

Object
[] arguments)

Creates a new

Expression

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

**Parameters:**
- target

- the target object of this expression
- methodName

- the name of the method to invoke on the specified target
- arguments

- the array of arguments to invoke the specified method

**See Also:**
- getValue()

---

#### public Expression​(
Object
value,

Object
target,

String
methodName,

Object
[] arguments)

Creates a new

Expression

object with the specified value
for the specified target object to invoke the method
specified by the name and by the array of arguments.
The

value

value is used as the value of the

value

property,
so the

getValue()

method will return it
without executing this

Expression

.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

**Parameters:**
- value

- the value of this expression
- target

- the target object of this expression
- methodName

- the name of the method to invoke on the specified target
- arguments

- the array of arguments to invoke the specified method

**See Also:**
- setValue(java.lang.Object)

---

### Method Details

#### public void execute()
throws
Exception

The

execute

method finds a method whose name is the same
as the

methodName

property, and invokes the method on
the target.

When the target's class defines many methods with the given name
the implementation should choose the most specific method using
the algorithm specified in the Java Language Specification
(15.11). The dynamic class of the target and arguments are used
in place of the compile-time type information and, like the

Method

class itself, conversion between
primitive values and their associated wrapper classes is handled
internally.

The following method types are handled as special cases:

- Static methods may be called by using a class object as the target.

The reserved method name "new" may be used to call a class's constructor
as if all classes defined static "new" methods. Constructor invocations
are typically considered

Expression

s rather than

Statement

s
as they return a value.

The method names "get" and "set" defined in the

List

interface may also be applied to array instances, mapping to
the static methods of the same name in the

Array

class.

If the invoked method completes normally,
the value it returns is copied in the

value

property.
Note that the

value

property is set to

null

,
if the return type of the underlying method is

void

.

**Overrides:**
- execute

in class

Statement

**Throws:**
- NullPointerException

- if the value of the

target

or

methodName

property is

null
- NoSuchMethodException

- if a matching method is not found
- SecurityException

- if a security manager exists and
it denies the method invocation
- Exception

- that is thrown by the invoked method

**See Also:**
- Method

**Since:**
- 1.7

---

#### public
Object
getValue()
throws
Exception

If the value property of this instance is not already set,
this method dynamically finds the method with the specified
methodName on this target with these arguments and calls it.
The result of the method invocation is first copied
into the value property of this expression and then returned
as the result of

getValue

. If the value property
was already set, either by a call to

setValue

or a previous call to

getValue

then the value
property is returned without either looking up or calling the method.

The value property of an

Expression

is set to
a unique private (non-

null

) value by default and
this value is used as an internal indication that the method
has not yet been called. A return value of

null

replaces this default value in the same way that any other value
would, ensuring that expressions are never evaluated more than once.

See the

execute

method for details on how
methods are chosen using the dynamic types of the target
and arguments.

**Returns:**
- The result of applying this method to these arguments.

**Throws:**
- Exception

- if the method with the specified methodName
throws an exception

**See Also:**
- Statement.execute()

,

setValue(java.lang.Object)

---

#### public void setValue​(
Object
value)

Sets the value of this expression to

value

.
This value will be returned by the getValue method
without calling the method associated with this
expression.

**Parameters:**
- value

- The value of this expression.

**See Also:**
- getValue()

---

#### public
String
toString()

Prints the value of this expression using a Java-style syntax.

**Overrides:**
- toString

in class

Statement

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class Expression

java.lang.Object

- java.beans.Statement
- - java.beans.Expression

java.beans.Statement

- java.beans.Expression

java.beans.Expression

```java
public class
Expression

extends
Statement
```

An

Expression

object represents a primitive expression
in which a single method is applied to a target and a set of
arguments to return a result - as in

"a.getFoo()"

.

In addition to the properties of the super class, the

Expression

object provides a

value

which
is the object returned when this expression is evaluated.
The return value is typically not provided by the caller and
is instead computed by dynamically finding the method and invoking
it when the first call to

getValue

is made.

**Since:** 1.4
**See Also:** getValue()

,

setValue(java.lang.Object)

public class

Expression

extends

Statement

An

Expression

object represents a primitive expression
in which a single method is applied to a target and a set of
arguments to return a result - as in

"a.getFoo()"

.

In addition to the properties of the super class, the

Expression

object provides a

value

which
is the object returned when this expression is evaluated.
The return value is typically not provided by the caller and
is instead computed by dynamically finding the method and invoking
it when the first call to

getValue

is made.

In addition to the properties of the super class, the

Expression

object provides a

value

which
is the object returned when this expression is evaluated.
The return value is typically not provided by the caller and
is instead computed by dynamically finding the method and invoking
it when the first call to

getValue

is made.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Expression

​(

Object

value,

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Expression

object with the specified value
for the specified target object to invoke the method
specified by the name and by the array of arguments.

Expression

​(

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Expression

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

execute

()

The

execute

method finds a method whose name is the same
as the

methodName

property, and invokes the method on
the target.

Object

getValue

()

If the value property of this instance is not already set,
this method dynamically finds the method with the specified
methodName on this target with these arguments and calls it.

void

setValue

​(

Object

value)

Sets the value of this expression to

value

.

String

toString

()

Prints the value of this expression using a Java-style syntax.

- Methods declared in class java.beans.

Statement

getArguments

,

getMethodName

,

getTarget

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

Expression

​(

Object

value,

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Expression

object with the specified value
for the specified target object to invoke the method
specified by the name and by the array of arguments.

Expression

​(

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Expression

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

---

#### Constructor Summary

Creates a new

Expression

object with the specified value
for the specified target object to invoke the method
specified by the name and by the array of arguments.

Creates a new

Expression

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

execute

()

The

execute

method finds a method whose name is the same
as the

methodName

property, and invokes the method on
the target.

Object

getValue

()

If the value property of this instance is not already set,
this method dynamically finds the method with the specified
methodName on this target with these arguments and calls it.

void

setValue

​(

Object

value)

Sets the value of this expression to

value

.

String

toString

()

Prints the value of this expression using a Java-style syntax.

- Methods declared in class java.beans.

Statement

getArguments

,

getMethodName

,

getTarget

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

The

execute

method finds a method whose name is the same
as the

methodName

property, and invokes the method on
the target.

If the value property of this instance is not already set,
this method dynamically finds the method with the specified
methodName on this target with these arguments and calls it.

Sets the value of this expression to

value

.

Prints the value of this expression using a Java-style syntax.

Methods declared in class java.beans.

Statement

getArguments

,

getMethodName

,

getTarget

---

#### Methods declared in class java.beans. Statement

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

- Expression

```java
@ConstructorProperties
({"target","methodName","arguments"})
public Expression​(
Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Expression

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

**Parameters:** target

- the target object of this expression
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method
**See Also:** getValue()

- Expression

```java
public Expression​(
Object
value,

Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Expression

object with the specified value
for the specified target object to invoke the method
specified by the name and by the array of arguments.
The

value

value is used as the value of the

value

property,
so the

getValue()

method will return it
without executing this

Expression

.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

**Parameters:** value

- the value of this expression
**Parameters:** target

- the target object of this expression
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method
**See Also:** setValue(java.lang.Object)

============ METHOD DETAIL ==========

- Method Detail

- execute

```java
public void execute()
throws
Exception
```

The

execute

method finds a method whose name is the same
as the

methodName

property, and invokes the method on
the target.

When the target's class defines many methods with the given name
the implementation should choose the most specific method using
the algorithm specified in the Java Language Specification
(15.11). The dynamic class of the target and arguments are used
in place of the compile-time type information and, like the

Method

class itself, conversion between
primitive values and their associated wrapper classes is handled
internally.

The following method types are handled as special cases:

- Static methods may be called by using a class object as the target.

The reserved method name "new" may be used to call a class's constructor
as if all classes defined static "new" methods. Constructor invocations
are typically considered

Expression

s rather than

Statement

s
as they return a value.

The method names "get" and "set" defined in the

List

interface may also be applied to array instances, mapping to
the static methods of the same name in the

Array

class.

If the invoked method completes normally,
the value it returns is copied in the

value

property.
Note that the

value

property is set to

null

,
if the return type of the underlying method is

void

.

**Overrides:** execute

in class

Statement
**Throws:** NullPointerException

- if the value of the

target

or

methodName

property is

null
**Throws:** NoSuchMethodException

- if a matching method is not found
**Throws:** SecurityException

- if a security manager exists and
it denies the method invocation
**Throws:** Exception

- that is thrown by the invoked method
**Since:** 1.7
**See Also:** Method

- getValue

```java
public
Object
getValue()
throws
Exception
```

If the value property of this instance is not already set,
this method dynamically finds the method with the specified
methodName on this target with these arguments and calls it.
The result of the method invocation is first copied
into the value property of this expression and then returned
as the result of

getValue

. If the value property
was already set, either by a call to

setValue

or a previous call to

getValue

then the value
property is returned without either looking up or calling the method.

The value property of an

Expression

is set to
a unique private (non-

null

) value by default and
this value is used as an internal indication that the method
has not yet been called. A return value of

null

replaces this default value in the same way that any other value
would, ensuring that expressions are never evaluated more than once.

See the

execute

method for details on how
methods are chosen using the dynamic types of the target
and arguments.

**Returns:** The result of applying this method to these arguments.
**Throws:** Exception

- if the method with the specified methodName
throws an exception
**See Also:** Statement.execute()

,

setValue(java.lang.Object)

- setValue

```java
public void setValue​(
Object
value)
```

Sets the value of this expression to

value

.
This value will be returned by the getValue method
without calling the method associated with this
expression.

**Parameters:** value

- The value of this expression.
**See Also:** getValue()

- toString

```java
public
String
toString()
```

Prints the value of this expression using a Java-style syntax.

**Overrides:** toString

in class

Statement
**Returns:** a string representation of the object.

Constructor Detail

- Expression

```java
@ConstructorProperties
({"target","methodName","arguments"})
public Expression​(
Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Expression

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

**Parameters:** target

- the target object of this expression
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method
**See Also:** getValue()

- Expression

```java
public Expression​(
Object
value,

Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Expression

object with the specified value
for the specified target object to invoke the method
specified by the name and by the array of arguments.
The

value

value is used as the value of the

value

property,
so the

getValue()

method will return it
without executing this

Expression

.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

**Parameters:** value

- the value of this expression
**Parameters:** target

- the target object of this expression
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method
**See Also:** setValue(java.lang.Object)

---

#### Constructor Detail

Expression

```java
@ConstructorProperties
({"target","methodName","arguments"})
public Expression​(
Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Expression

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

**Parameters:** target

- the target object of this expression
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method
**See Also:** getValue()

---

#### Expression

@ConstructorProperties

({"target","methodName","arguments"})
public Expression​(

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Expression

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

Expression

```java
public Expression​(
Object
value,

Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Expression

object with the specified value
for the specified target object to invoke the method
specified by the name and by the array of arguments.
The

value

value is used as the value of the

value

property,
so the

getValue()

method will return it
without executing this

Expression

.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

**Parameters:** value

- the value of this expression
**Parameters:** target

- the target object of this expression
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method
**See Also:** setValue(java.lang.Object)

---

#### Expression

public Expression​(

Object

value,

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Expression

object with the specified value
for the specified target object to invoke the method
specified by the name and by the array of arguments.
The

value

value is used as the value of the

value

property,
so the

getValue()

method will return it
without executing this

Expression

.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

The

target

and the

methodName

values should not be

null

.
Otherwise an attempt to execute this

Expression

will result in a

NullPointerException

.
If the

arguments

value is

null

,
an empty array is used as the value of the

arguments

property.

Method Detail

- execute

```java
public void execute()
throws
Exception
```

The

execute

method finds a method whose name is the same
as the

methodName

property, and invokes the method on
the target.

When the target's class defines many methods with the given name
the implementation should choose the most specific method using
the algorithm specified in the Java Language Specification
(15.11). The dynamic class of the target and arguments are used
in place of the compile-time type information and, like the

Method

class itself, conversion between
primitive values and their associated wrapper classes is handled
internally.

The following method types are handled as special cases:

- Static methods may be called by using a class object as the target.

The reserved method name "new" may be used to call a class's constructor
as if all classes defined static "new" methods. Constructor invocations
are typically considered

Expression

s rather than

Statement

s
as they return a value.

The method names "get" and "set" defined in the

List

interface may also be applied to array instances, mapping to
the static methods of the same name in the

Array

class.

If the invoked method completes normally,
the value it returns is copied in the

value

property.
Note that the

value

property is set to

null

,
if the return type of the underlying method is

void

.

**Overrides:** execute

in class

Statement
**Throws:** NullPointerException

- if the value of the

target

or

methodName

property is

null
**Throws:** NoSuchMethodException

- if a matching method is not found
**Throws:** SecurityException

- if a security manager exists and
it denies the method invocation
**Throws:** Exception

- that is thrown by the invoked method
**Since:** 1.7
**See Also:** Method

- getValue

```java
public
Object
getValue()
throws
Exception
```

If the value property of this instance is not already set,
this method dynamically finds the method with the specified
methodName on this target with these arguments and calls it.
The result of the method invocation is first copied
into the value property of this expression and then returned
as the result of

getValue

. If the value property
was already set, either by a call to

setValue

or a previous call to

getValue

then the value
property is returned without either looking up or calling the method.

The value property of an

Expression

is set to
a unique private (non-

null

) value by default and
this value is used as an internal indication that the method
has not yet been called. A return value of

null

replaces this default value in the same way that any other value
would, ensuring that expressions are never evaluated more than once.

See the

execute

method for details on how
methods are chosen using the dynamic types of the target
and arguments.

**Returns:** The result of applying this method to these arguments.
**Throws:** Exception

- if the method with the specified methodName
throws an exception
**See Also:** Statement.execute()

,

setValue(java.lang.Object)

- setValue

```java
public void setValue​(
Object
value)
```

Sets the value of this expression to

value

.
This value will be returned by the getValue method
without calling the method associated with this
expression.

**Parameters:** value

- The value of this expression.
**See Also:** getValue()

- toString

```java
public
String
toString()
```

Prints the value of this expression using a Java-style syntax.

**Overrides:** toString

in class

Statement
**Returns:** a string representation of the object.

---

#### Method Detail

execute

```java
public void execute()
throws
Exception
```

The

execute

method finds a method whose name is the same
as the

methodName

property, and invokes the method on
the target.

When the target's class defines many methods with the given name
the implementation should choose the most specific method using
the algorithm specified in the Java Language Specification
(15.11). The dynamic class of the target and arguments are used
in place of the compile-time type information and, like the

Method

class itself, conversion between
primitive values and their associated wrapper classes is handled
internally.

The following method types are handled as special cases:

- Static methods may be called by using a class object as the target.

The reserved method name "new" may be used to call a class's constructor
as if all classes defined static "new" methods. Constructor invocations
are typically considered

Expression

s rather than

Statement

s
as they return a value.

The method names "get" and "set" defined in the

List

interface may also be applied to array instances, mapping to
the static methods of the same name in the

Array

class.

If the invoked method completes normally,
the value it returns is copied in the

value

property.
Note that the

value

property is set to

null

,
if the return type of the underlying method is

void

.

**Overrides:** execute

in class

Statement
**Throws:** NullPointerException

- if the value of the

target

or

methodName

property is

null
**Throws:** NoSuchMethodException

- if a matching method is not found
**Throws:** SecurityException

- if a security manager exists and
it denies the method invocation
**Throws:** Exception

- that is thrown by the invoked method
**Since:** 1.7
**See Also:** Method

---

#### execute

public void execute()
throws

Exception

The

execute

method finds a method whose name is the same
as the

methodName

property, and invokes the method on
the target.

When the target's class defines many methods with the given name
the implementation should choose the most specific method using
the algorithm specified in the Java Language Specification
(15.11). The dynamic class of the target and arguments are used
in place of the compile-time type information and, like the

Method

class itself, conversion between
primitive values and their associated wrapper classes is handled
internally.

The following method types are handled as special cases:

- Static methods may be called by using a class object as the target.

The reserved method name "new" may be used to call a class's constructor
as if all classes defined static "new" methods. Constructor invocations
are typically considered

Expression

s rather than

Statement

s
as they return a value.

The method names "get" and "set" defined in the

List

interface may also be applied to array instances, mapping to
the static methods of the same name in the

Array

class.

If the invoked method completes normally,
the value it returns is copied in the

value

property.
Note that the

value

property is set to

null

,
if the return type of the underlying method is

void

.

The following method types are handled as special cases:

- Static methods may be called by using a class object as the target.

The reserved method name "new" may be used to call a class's constructor
as if all classes defined static "new" methods. Constructor invocations
are typically considered

Expression

s rather than

Statement

s
as they return a value.

The method names "get" and "set" defined in the

List

interface may also be applied to array instances, mapping to
the static methods of the same name in the

Array

class.

If the invoked method completes normally,
the value it returns is copied in the

value

property.
Note that the

value

property is set to

null

,
if the return type of the underlying method is

void

.

Static methods may be called by using a class object as the target.

The reserved method name "new" may be used to call a class's constructor
as if all classes defined static "new" methods. Constructor invocations
are typically considered

Expression

s rather than

Statement

s
as they return a value.

The method names "get" and "set" defined in the

List

interface may also be applied to array instances, mapping to
the static methods of the same name in the

Array

class.

If the invoked method completes normally,
the value it returns is copied in the

value

property.
Note that the

value

property is set to

null

,
if the return type of the underlying method is

void

.

getValue

```java
public
Object
getValue()
throws
Exception
```

If the value property of this instance is not already set,
this method dynamically finds the method with the specified
methodName on this target with these arguments and calls it.
The result of the method invocation is first copied
into the value property of this expression and then returned
as the result of

getValue

. If the value property
was already set, either by a call to

setValue

or a previous call to

getValue

then the value
property is returned without either looking up or calling the method.

The value property of an

Expression

is set to
a unique private (non-

null

) value by default and
this value is used as an internal indication that the method
has not yet been called. A return value of

null

replaces this default value in the same way that any other value
would, ensuring that expressions are never evaluated more than once.

See the

execute

method for details on how
methods are chosen using the dynamic types of the target
and arguments.

**Returns:** The result of applying this method to these arguments.
**Throws:** Exception

- if the method with the specified methodName
throws an exception
**See Also:** Statement.execute()

,

setValue(java.lang.Object)

---

#### getValue

public

Object

getValue()
throws

Exception

If the value property of this instance is not already set,
this method dynamically finds the method with the specified
methodName on this target with these arguments and calls it.
The result of the method invocation is first copied
into the value property of this expression and then returned
as the result of

getValue

. If the value property
was already set, either by a call to

setValue

or a previous call to

getValue

then the value
property is returned without either looking up or calling the method.

The value property of an

Expression

is set to
a unique private (non-

null

) value by default and
this value is used as an internal indication that the method
has not yet been called. A return value of

null

replaces this default value in the same way that any other value
would, ensuring that expressions are never evaluated more than once.

See the

execute

method for details on how
methods are chosen using the dynamic types of the target
and arguments.

The value property of an

Expression

is set to
a unique private (non-

null

) value by default and
this value is used as an internal indication that the method
has not yet been called. A return value of

null

replaces this default value in the same way that any other value
would, ensuring that expressions are never evaluated more than once.

See the

execute

method for details on how
methods are chosen using the dynamic types of the target
and arguments.

See the

execute

method for details on how
methods are chosen using the dynamic types of the target
and arguments.

setValue

```java
public void setValue​(
Object
value)
```

Sets the value of this expression to

value

.
This value will be returned by the getValue method
without calling the method associated with this
expression.

**Parameters:** value

- The value of this expression.
**See Also:** getValue()

---

#### setValue

public void setValue​(

Object

value)

Sets the value of this expression to

value

.
This value will be returned by the getValue method
without calling the method associated with this
expression.

toString

```java
public
String
toString()
```

Prints the value of this expression using a Java-style syntax.

**Overrides:** toString

in class

Statement
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Prints the value of this expression using a Java-style syntax.

---

