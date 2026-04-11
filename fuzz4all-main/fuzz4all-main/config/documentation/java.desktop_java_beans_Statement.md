# Class Statement

**Source:** `java.desktop\java\beans\Statement.html`

### Class Description

```java
public class
Statement

extends
Object
```

A

Statement

object represents a primitive statement
in which a single method is applied to a target and
a set of arguments - as in

"a.setFoo(b)"

.
Note that where this example uses names
to denote the target and its argument, a statement
object does not require a name space and is constructed with
the values themselves.
The statement object associates the named method
with its environment as a simple set of values:
the target and an array of argument values.

**Direct Known Subclasses:** Expression

---

### Field Details

*No entries found.*

### Constructor Details

#### @ConstructorProperties
({"target","methodName","arguments"})
public Statement​(
Object
target,

String
methodName,

Object
[] arguments)

Creates a new

Statement

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

- the target object of this statement
- methodName

- the name of the method to invoke on the specified target
- arguments

- the array of arguments to invoke the specified method

---

### Method Details

#### public
Object
getTarget()

Returns the target object of this statement.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

**Returns:**
- the target object of this statement

---

#### public
String
getMethodName()

Returns the name of the method to invoke.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

**Returns:**
- the name of the method

---

#### public
Object
[] getArguments()

Returns the arguments for the method to invoke.
The number of arguments and their types
must match the method being called.

null

can be used as a synonym of an empty array.

**Returns:**
- the array of arguments

---

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

---

#### public
String
toString()

Prints the value of this statement using a Java-style syntax.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class Statement

java.lang.Object

- java.beans.Statement

java.beans.Statement

**Direct Known Subclasses:** Expression

```java
public class
Statement

extends
Object
```

A

Statement

object represents a primitive statement
in which a single method is applied to a target and
a set of arguments - as in

"a.setFoo(b)"

.
Note that where this example uses names
to denote the target and its argument, a statement
object does not require a name space and is constructed with
the values themselves.
The statement object associates the named method
with its environment as a simple set of values:
the target and an array of argument values.

**Since:** 1.4

public class

Statement

extends

Object

A

Statement

object represents a primitive statement
in which a single method is applied to a target and
a set of arguments - as in

"a.setFoo(b)"

.
Note that where this example uses names
to denote the target and its argument, a statement
object does not require a name space and is constructed with
the values themselves.
The statement object associates the named method
with its environment as a simple set of values:
the target and an array of argument values.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Statement

​(

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Statement

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

[]

getArguments

()

Returns the arguments for the method to invoke.

String

getMethodName

()

Returns the name of the method to invoke.

Object

getTarget

()

Returns the target object of this statement.

String

toString

()

Prints the value of this statement using a Java-style syntax.

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

Statement

​(

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Statement

object
for the specified target object to invoke the method
specified by the name and by the array of arguments.

---

#### Constructor Summary

Creates a new

Statement

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

[]

getArguments

()

Returns the arguments for the method to invoke.

String

getMethodName

()

Returns the name of the method to invoke.

Object

getTarget

()

Returns the target object of this statement.

String

toString

()

Prints the value of this statement using a Java-style syntax.

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

Returns the arguments for the method to invoke.

Returns the name of the method to invoke.

Returns the target object of this statement.

Prints the value of this statement using a Java-style syntax.

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

- Statement

```java
@ConstructorProperties
({"target","methodName","arguments"})
public Statement​(
Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Statement

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

- the target object of this statement
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method

============ METHOD DETAIL ==========

- Method Detail

- getTarget

```java
public
Object
getTarget()
```

Returns the target object of this statement.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

**Returns:** the target object of this statement

- getMethodName

```java
public
String
getMethodName()
```

Returns the name of the method to invoke.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

**Returns:** the name of the method

- getArguments

```java
public
Object
[] getArguments()
```

Returns the arguments for the method to invoke.
The number of arguments and their types
must match the method being called.

null

can be used as a synonym of an empty array.

**Returns:** the array of arguments

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
**See Also:** Method

- toString

```java
public
String
toString()
```

Prints the value of this statement using a Java-style syntax.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- Statement

```java
@ConstructorProperties
({"target","methodName","arguments"})
public Statement​(
Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Statement

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

- the target object of this statement
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method

---

#### Constructor Detail

Statement

```java
@ConstructorProperties
({"target","methodName","arguments"})
public Statement​(
Object
target,

String
methodName,

Object
[] arguments)
```

Creates a new

Statement

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

- the target object of this statement
**Parameters:** methodName

- the name of the method to invoke on the specified target
**Parameters:** arguments

- the array of arguments to invoke the specified method

---

#### Statement

@ConstructorProperties

({"target","methodName","arguments"})
public Statement​(

Object

target,

String

methodName,

Object

[] arguments)

Creates a new

Statement

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

Method Detail

- getTarget

```java
public
Object
getTarget()
```

Returns the target object of this statement.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

**Returns:** the target object of this statement

- getMethodName

```java
public
String
getMethodName()
```

Returns the name of the method to invoke.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

**Returns:** the name of the method

- getArguments

```java
public
Object
[] getArguments()
```

Returns the arguments for the method to invoke.
The number of arguments and their types
must match the method being called.

null

can be used as a synonym of an empty array.

**Returns:** the array of arguments

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
**See Also:** Method

- toString

```java
public
String
toString()
```

Prints the value of this statement using a Java-style syntax.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getTarget

```java
public
Object
getTarget()
```

Returns the target object of this statement.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

**Returns:** the target object of this statement

---

#### getTarget

public

Object

getTarget()

Returns the target object of this statement.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

getMethodName

```java
public
String
getMethodName()
```

Returns the name of the method to invoke.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

**Returns:** the name of the method

---

#### getMethodName

public

String

getMethodName()

Returns the name of the method to invoke.
If this method returns

null

,
the

execute()

method
throws a

NullPointerException

.

getArguments

```java
public
Object
[] getArguments()
```

Returns the arguments for the method to invoke.
The number of arguments and their types
must match the method being called.

null

can be used as a synonym of an empty array.

**Returns:** the array of arguments

---

#### getArguments

public

Object

[] getArguments()

Returns the arguments for the method to invoke.
The number of arguments and their types
must match the method being called.

null

can be used as a synonym of an empty array.

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

toString

```java
public
String
toString()
```

Prints the value of this statement using a Java-style syntax.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Prints the value of this statement using a Java-style syntax.

---

